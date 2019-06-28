# DO NOT REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#
# Contributor(s):
#
# The Original Software is OpenRedukti (https://github.com/redukti/OpenRedukti).
# The Initial Developer of the Original Software is REDUKTI LIMITED (http://redukti.com).
# Authors: Dibyendu Majumdar
#
# Copyright 2019 REDUKTI LIMITED. All Rights Reserved.
#
# The contents of this file are subject to the the GNU General Public License
# Version 3 (https://www.gnu.org/licenses/gpl.txt).

import grpc

from redukti import services_pb2
from redukti import services_pb2_grpc
from redukti import enums_pb2 as enums
from redukti import common_pb2 as common
from redukti import curve_pb2 as curve
from redukti import bootstrap_pb2 as bootstrap
from redukti import valuation_pb2 as valuation
from redukti import cashflow_pb2 as cashflows
from redukti import schedule_pb2 as schedule
import redukti

import csv

index_mappings = {
    'EUR-EURIBOR-Reuters': enums.EUR_EURIBOR_Reuters,
    'EUR-EONIA-OIS-COMPOUND': enums.EUR_EONIA_OIS_COMPOUND
    # FIXME add all 
}
interpolator_types = {
    'Linear': enums.LINEAR,
    'MonotoneConvex': enums.MONOTONE_CONVEX,
    'LogCubicSplineNatural': enums.LOG_CUBIC_SPLINE_NATURAL
}
rate_types = {
    'ZeroRate': enums.ZERO_RATE,
    'DiscountFactor': enums.DISCOUNT_FACTOR
}
maturity_rules = {
    'DeriveFromInstruments': enums.MATURITY_GENERATION_RULE_DERIVE_FROM_INSTRUMENTS,
    'FixedTenors': enums.MATURITY_GENERATION_RULE_FIXED_TENORS
}

swap_templates = {
    'EUR_EONIA_1D': {
        'currency': enums.EUR,
        'start_delay': 2,
        'payment_calendar': [enums.EUTA],
        'fixed_payment_frequency': enums.TENOR_12M,
        'floating_payment_frequency': enums.TENOR_12M,
        'fixed_day_fraction': enums.ACT_360,
        'floating_day_fraction': enums.ACT_360,
        'payment_day_convention': enums.MODIFIED_FOLLOWING,
        'floating_index': enums.EUR_EONIA_OIS_COMPOUND,
        'floating_tenor': enums.ISDA_INDEX_UNSPECIFIED
    },
    'EUR_EURIBOR_3M': {
        'currency': enums.EUR,
        'start_delay': 2,
        'payment_calendar': [enums.EUTA],
        'fixed_payment_frequency': enums.TENOR_3M,
        'floating_payment_frequency': enums.TENOR_3M,
        'fixed_day_fraction': enums.ACT_360,
        'floating_day_fraction': enums.ACT_360,
        'payment_day_convention': enums.MODIFIED_FOLLOWING,
        'floating_index': enums.EUR_EURIBOR_Reuters,
        'floating_tenor': enums.TENOR_3M
    },
    'EUR_EURIBOR_6M': {
        'currency': enums.EUR,
        'start_delay': 2,
        'payment_calendar': [enums.EUTA],
        'fixed_payment_frequency': enums.TENOR_6M,
        'floating_payment_frequency': enums.TENOR_6M,
        'fixed_day_fraction': enums.ACT_360,
        'floating_day_fraction': enums.ACT_360,
        'payment_day_convention': enums.MODIFIED_FOLLOWING,
        'floating_index': enums.EUR_EURIBOR_Reuters,
        'floating_tenor': enums.TENOR_6M
    }
}

def build_vanilla_swap(notional, effective_date, termination_date, template_name, fixed_rate, fixed_leg_sign):
    template = swap_templates[template_name]
    if not template:
        raise Exception('No template found with name: ' + template_name)
    ccy = template['currency']
    floating_schedule_params = schedule.ScheduleParameters()
    floating_schedule_params.effective_date = effective_date.serial()
    floating_schedule_params.termination_date = termination_date.serial()
    floating_schedule_params.payment_frequency = template['floating_payment_frequency']
    floating_schedule_params.payment_calendars.extend(template['payment_calendar'])
    floating_schedule_params.payment_convention = template['payment_day_convention']
    floating_schedule = redukti.generate_schedule(floating_schedule_params)

    fixed_schedule_params = schedule.ScheduleParameters()
    fixed_schedule_params.effective_date = effective_date.serial()
    fixed_schedule_params.termination_date = termination_date.serial()
    fixed_schedule_params.payment_frequency = template['fixed_payment_frequency']
    fixed_schedule_params.payment_calendars.extend(template['payment_calendar'])
    fixed_schedule_params.payment_convention = template['payment_day_convention']
    fixed_schedule = redukti.generate_schedule(fixed_schedule_params)
  
    fixed_daycount = redukti.DayFraction(template['fixed_day_fraction'])
    if not fixed_daycount:
        raise Exception('Unable to find day count fraction ' + str(template['fixed_day_fraction']))

    fixed_leg_scalars = []
    for i in range(0, len(fixed_schedule.adjusted_start_dates)):
        fixed_leg_scalars.append(notional * fixed_rate * 
            fixed_daycount.year_fraction(redukti.Date(fixed_schedule.adjusted_start_dates[i]), 
                redukti.Date(fixed_schedule.adjusted_end_dates[i])))

    cfcollection = cashflows.CFCollection()
    fixed_stream = cfcollection.streams.add()
    fixed_stream.factor = fixed_leg_sign
    for i in range(0, len(fixed_leg_scalars)):
        single = fixed_stream.cashflows.add()
        single.simple.currency = ccy
        single.simple.amount = fixed_leg_scalars[i]
        single.simple.payment_date = fixed_schedule.adjusted_payment_dates[i]

    float_stream = cfcollection.streams.add()
    float_stream.factor = -fixed_leg_sign
    for i in range(0, len(floating_schedule.adjusted_start_dates)):
        single = float_stream.cashflows.add()
        single.floating.currency = ccy
        single.floating.day_count_fraction = template['floating_day_fraction']
        single.floating.payment_date = floating_schedule.adjusted_payment_dates[i]
        floating_period = single.floating.floating_periods.add()
        floating_period.notional = notional
        floating_period.accrual_start_date = floating_schedule.adjusted_start_dates[i]
        floating_period.accrual_end_date = floating_schedule.adjusted_end_dates[i]
        floating_period.index = template['floating_index']
        floating_period.tenor = template['floating_tenor']
        floating_period.spread = 0.0

    return cfcollection

class MarketData:

    def __init__(self, date):
        if not isinstance(date, redukti.Date):
            raise ValueError('A business date must be supplied')
        self._curve_definitions = None
        self._par_curve_set = None
        self._fixings = None
        self._business_date = date
        self._yield_curves = None # Redukti YieldCurve instances 
        self._zero_curves_by_id = {} # Bootstrapped raw curves

    def read_curvedefinitions(self, filename):
        defs = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'group':
                    continue
                definition = curve.IRCurveDefinition()
                definition.curve_group = enums.CurveGroup.Value('CURVE_GROUP_' + row[0])
                definition.id = int(row[1])
                definition.currency = enums.Currency.Value(row[2])
                definition.index_family = enums.IndexFamily.Value(row[3])
                if len(row[4]) == 0:
                    definition.tenor = enums.TENOR_UNSPECIFIED
                else:
                    definition.tenor = enums.Tenor.Value('TENOR_' + row[4])
                definition.interpolator_type = interpolator_types[row[5]]
                definition.interpolated_on = rate_types[row[6]]
                definition.maturity_generation_rule = maturity_rules[row[7]]
                if len(row[8].strip()) > 0:
                    tenors = row[8].split(':')
                    for item in tenors:
                        if item == 'ON':
                            item = '1D'
                        definition.tenors.append(enums.Tenor.Value('TENOR_' + item))
                defs.append(definition)
        self._curve_definitions = defs

    def read_parcurves(self, filename):
        par_curve_set = bootstrap.ParCurveSet()
        curve = None
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            current_curve_id = -1
            for row in csv_reader:
                if row[0] == 'curve_id':
                    continue
                id = int(row[0])
                instrument_type = row[1]
                instrument_key = row[2]
                floating_tenor = row[3]
                par_rate = row[4]
                forward_curve_id = row[5]
                discount_curve_id = row[6]
                if id != current_curve_id:
                    curve = par_curve_set.par_curves.add()
                    curve.curve_definition_id = id
                    current_curve_id = id
                inst = curve.instruments.add()
                inst.instrument_key = instrument_key
                inst.instrument_type = instrument_type
                if len(floating_tenor) == 0:
                    inst.floating_tenor = enums.TENOR_UNSPECIFIED
                else:
                    inst.floating_tenor = enums.Tenor.Value('TENOR_' + floating_tenor)
                inst.forward_curve_definition_id = int(forward_curve_id)
                inst.discount_curve_definition_id = int(discount_curve_id)
                curve.par_rates.values.append(float(par_rate))
        self._par_curve_set = par_curve_set

    def read_fixings(self, filename):
        fixings = {}
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'index':
                    continue
                isda_index = index_mappings[row[0]]
                tenor = enums.Tenor.Value('TENOR_' + row[1])
                fixing_date = redukti.parse_date(row[2])
                fixing = float(row[3])
                fixings_by_index = None
                if isda_index not in fixings:
                    fixings_by_index = valuation.FixingsByIndexTenor()
                    fixings_by_index.index = isda_index
                    fixings_by_index.tenor = tenor
                    fixings[isda_index] = fixings_by_index
                else:
                    fixings_by_index = fixings[isda_index]
                fixings_by_index.fixings[fixing_date.serial()] = fixing 
        self._fixings = fixings

    def find_curve_definition(self, id):
        for defn in self._curve_definitions:
            if defn.id == id:
                return defn
        return None

    def init_zero_curves(self, bootstrap_curves_reply):
        zero_curves = bootstrap_curves_reply.curves
        self._yield_curves = []
        for zc in zero_curves:
            definition_id = zc.curve_definition_id
            defn = self.find_curve_definition(definition_id)
            if defn is None:
                raise ValueError('Curve Definition not found for ' + str(definition_id))
            yc = redukti.YieldCurve(self._business_date, defn, zc)
            self._yield_curves.append(yc)
            self._zero_curves_by_id[definition_id] = zc
            print('Curve ' + str(definition_id) + ' created')

    def curve_definitions(self):
        return self._curve_definitions
    
    def yield_curves(self):
        return self._yield_curves
    
    def find_zero_curve_by_id(self, definition_id):
        return self._zero_curves_by_id[definition_id]

    def has_fixings(self):
        return self._fixings is not None

    def fixings(self):
        return self._fixings

    def business_date(self):
        return self._business_date

def load_market_data(business_date, curve_definitions_filename, par_rates_filename, fixings_filename=None):
    market_data = MarketData(business_date)
    market_data.read_curvedefinitions(curve_definitions_filename)
    market_data.read_parcurves(par_rates_filename)
    if fixings_filename:
        market_data.read_fixings(fixings_filename)
    return market_data

class ServerCommand:

    def __init__(self, address):
        self._address = address
    
    def reset_valuation_service(self):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)        
            request = services_pb2.Request()
            request.reset_valuation_service_request.SetInParent()
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)
            return None

    def hello(self, name):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)        
            request = services_pb2.Request()
            request.hello_request.name = name
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)
            return response.hello_reply.message

    def shutdown_valuation_service(self):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)        
            request = services_pb2.Request()
            request.shutdown_request.password = "password"
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)
            return response.hello_reply.message

    def build_curves(self, market_data):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)        
            request = services_pb2.Request()
            request.bootstrap_curves_request.business_date = market_data._business_date.serial()
            request.bootstrap_curves_request.curve_definitions.extend(market_data._curve_definitions)
            request.bootstrap_curves_request.par_curve_set.CopyFrom(market_data._par_curve_set)
            print('Building curves, please wait.')
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)
            return market_data.init_zero_curves(response.bootstrap_curves_reply)

    def register_curve_mappings(self, curve_group, curve_mappings):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)
            print('Registering curve mappings')
            request = services_pb2.Request()
            request.set_curve_mappings_request.curve_group = curve_group
            request.set_curve_mappings_request.mappings.extend(curve_mappings)
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)

    def register_curve_definitions(self, stub, market_data):
        print('Registering curve definitions')
        request = services_pb2.Request()
        request.register_curve_definitions_request.curve_definitions.extend(market_data.curve_definitions())
        response = stub.serve(request)
        if response.header.response_code != 0:
            raise Exception(response.header.response_message)

    def register_zero_curves(self, stub, curve_group, market_data, forward_curves_list, discount_curve_list):
        print('Registering zero curves')
        request = services_pb2.Request()
        for id in forward_curves_list:
            zc = market_data.find_zero_curve_by_id(id)
            if zc is None:
                raise ValueError('Could not find zero curve ' + str(id))
            request.set_zero_curves_request.forward_curves.append(zc)
        for id in discount_curve_list:
            zc = market_data.find_zero_curve_by_id(id)
            if zc is None:
                raise ValueError('Could not find zero curve ' + str(id))
            request.set_zero_curves_request.discount_curves.append(zc)
        request.set_zero_curves_request.as_of_date = market_data.business_date().serial()
        request.set_zero_curves_request.cycle = 0
        request.set_zero_curves_request.qualifier = enums.MDQ_NORMAL
        request.set_zero_curves_request.scenario = 0
        request.set_zero_curves_request.curve_group = curve_group
        response = stub.serve(request)
        if response.header.response_code != 0:
            raise Exception(response.header.response_message)

    def register_fixings(self, stub, market_data):
        print('Registering fixings')
        fixings_by_index = market_data.fixings()
        for entry in fixings_by_index.values():
            request = services_pb2.Request()
            request.set_fixings_request.fixings_by_index_tenor.CopyFrom(entry)
            response = stub.serve(request)
            if response.header.response_code != 0:
                raise Exception(response.header.response_message)

    def register_market_data(self, curve_group, market_data, forward_curves_list, discount_curve_list):
        with grpc.insecure_channel(self._address) as channel:
            stub = services_pb2_grpc.OpenReduktiServicesStub(channel)        
            self.register_curve_definitions(stub, market_data)
            self.register_zero_curves(stub, curve_group, market_data, forward_curves_list, discount_curve_list)            
            if market_data.has_fixings():
                self.register_fixings(stub, market_data)               
