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
from redukti import index_pb2 as index
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
        'floating_tenor': enums.TENOR_UNSPECIFIED,
        'fixed_discounting_index_family': enums.EONIA,
        'is_ois': True
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
        'floating_tenor': enums.TENOR_3M,
        'fixed_discounting_index_family': enums.EONIA,
        'is_ois': False
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
        'floating_tenor': enums.TENOR_6M,
        'fixed_discounting_index_family': enums.EONIA,
        'is_ois': False
    }
}


def build_vanilla_swap(notional, effective_date, termination_date, template_name, fixed_rate, fixed_leg_sign):
    """
    Constructs cashflows for a Vanilla Interest Rate Swap with a fixed leg and a floating leg

    Args:
        notional: Notional amount
        effective_date: The unadjusted effective date of the swap
        termination_date: The unadjusted termination date of the swap
        template_name: The template to be used to determine various parameters
        fixed_rate: The fixed rate on the fixed leg
        fixed_leg_sign: The sign of the fixed leg, -1.0 indicates pay fixed rate

    Returns:
        Returns an instance of cashflow_pb2.CFCollection
    """
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
    floating_schedule = redukti.ScheduleGenerator.generate_schedule(floating_schedule_params)

    fixed_schedule_params = schedule.ScheduleParameters()
    fixed_schedule_params.effective_date = effective_date.serial()
    fixed_schedule_params.termination_date = termination_date.serial()
    fixed_schedule_params.payment_frequency = template['fixed_payment_frequency']
    fixed_schedule_params.payment_calendars.extend(template['payment_calendar'])
    fixed_schedule_params.payment_convention = template['payment_day_convention']
    fixed_schedule = redukti.ScheduleGenerator.generate_schedule(fixed_schedule_params)

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
        single.simple.discounting_index_family = template['fixed_discounting_index_family']

    float_stream = cfcollection.streams.add()
    float_stream.factor = -fixed_leg_sign
    for i in range(0, len(floating_schedule.adjusted_start_dates)):
        single = float_stream.cashflows.add()
        is_ois = template['is_ois']
        if not is_ois:
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
        else:
            single.ois.index = template['floating_index']
            single.ois.notional = notional
            single.ois.accrual_start_date = floating_schedule.adjusted_start_dates[i]
            single.ois.accrual_end_date = floating_schedule.adjusted_end_dates[i]
            single.ois.payment_date = floating_schedule.adjusted_payment_dates[i]
            single.ois.day_count_fraction = template['floating_day_fraction']
    return cfcollection


class MarketData:
    """
    The MarketData object encapsulates the market data required for valuation

    The MarketData object provides utilities for loading market data from
    CSV format files.
    """

    def __init__(self, date, curve_group):
        if not isinstance(date, redukti.Date):
            raise ValueError('A business date must be supplied')
        self._curve_definitions = None
        self._par_curve_set = None
        self._fixings = None
        self._business_date = date
        self._curve_group = curve_group
        self._yield_curves = None  # Redukti YieldCurve instances
        self._zero_curves_by_id = {}  # Bootstrapped raw curves

    def read_curvedefinitions(self, filename):
        """
        Reads Curve Definitions from a CSV format file

        For an example file see: `https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/curve_definitions.csv <https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/curve_definitions.csv>`_
        """
        defs = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'group':
                    continue
                curve_group = enums.CurveGroup.Value('CURVE_GROUP_' + row[0])
                if curve_group != self._curve_group:
                    continue
                definition = curve.IRCurveDefinition()
                definition.curve_group = curve_group
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
        """
        Loads market quotes from a CSV format file

        For an example see: `https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/par_rates.csv <https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/par_rates.csv>`_.
        """
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
        """
        Reads Index Fixings from a CSV format file

        For an example of fixings data file see: `https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/fixings.csv <https://github.com/redukti/PyRedukti/blob/master/testdata/20121211/fixings.csv>`_.
        """
        fixings = {}
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'index':
                    continue
                isda_index = index_mappings[row[0]]
                tenor = enums.Tenor.Value('TENOR_' + row[1])
                fixing_date = redukti.Date.parse(row[2])
                fixing = float(row[3])
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
        """
        Finds a curve definition by its id

        Precondition is that curve definitions must have been loaded
        """
        for defn in self._curve_definitions:
            if defn.id == id:
                return defn
        return None

    def init_zero_curves(self, bootstrap_curves_reply):
        """
        Converts the result from a curve building call to YieldCurve instances

        Args:
            bootstrap_curves_reply: reply from the Bootstrap command
        """
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
        return self._yield_curves

    def curve_definitions(self):
        """
        Gives a list of the curve definitions currently loaded
        """
        return self._curve_definitions

    def yield_curves(self):
        """
        Gives a list of the yield curves currently available locally

        Note that the list is in the same order as the curve definitions
        """
        return self._yield_curves

    def find_zero_curve_by_id(self, definition_id):
        """
        Given a curve definition id, locates the corresponding ZeroCurve data object.

        Args:
            definition_id: The curve definition id
        """
        return self._zero_curves_by_id[definition_id]

    def has_fixings(self):
        """
        Checks if fixings are available (i.e. loaded)
        """
        return self._fixings is not None

    def fixings(self):
        """
        Returns the currently loaded fixings
        """
        return self._fixings

    def business_date(self):
        """
        Returns the business date associated with this market data instance
        """
        return self._business_date

    def curve_group(self):
        """
        Returns the CurveGroup associated with this market data instance
        """
        return self._curve_group

    def pricing_context(self):
        """
        Builds a default PricingContext object from the market data information
        """
        pricing_context = valuation.PricingContext()
        pricing_context.curve_group = self._curve_group
        pricing_context.as_of_date = self._business_date.serial()
        pricing_context.qualifier = enums.MDQ_NORMAL
        pricing_context.cycle = 0
        pricing_context.payment_cutoff_date = pricing_context.as_of_date
        pricing_context.derivative_order = 2
        pricing_context.is_todays_fixings_included = False
        pricing_context.from_scenario = 0
        pricing_context.to_scenario = 0
        return pricing_context


def load_market_data(business_date, curve_definitions_filename, par_rates_filename, fixings_filename=None):
    market_data = MarketData(business_date)
    market_data.read_curvedefinitions(curve_definitions_filename)
    market_data.read_parcurves(par_rates_filename)
    if fixings_filename:
        market_data.read_fixings(fixings_filename)
    return market_data

class GRPCAdapter:
    """
    Provides a service invocation adapter that connects to an OpenRedukti server
    over the gRPC protocol
    """
    def __init__(self, address):
        self._channel = grpc.insecure_channel(address)
        self._stub = services_pb2_grpc.OpenReduktiServicesStub(self._channel)

    def serve(self, request):
        return self._stub.serve(request)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._channel.close()

class LocalAdapter:
    """
    Provides a service invocation adapter that uses an internal InMemoryRequestProcessor
    to handle requests
    """
    def __init__(self, pricing_script):
        self._request_processor = redukti.InMemoryRequestProcessor(pricing_script)

    def serve(self, request):
        return self._request_processor.serve(request)

class ServerCommand:
    """The ServerCommand object encapsulates interactions withe OpenRedukti Valuation Server

    It communicates with the OpenRedukti Valuation server using gRPC protocol.
    All requests and responses to/from the server are in Google Protocol Buffers format.
    """

    def __init__(self, adapter):
        """Creates a new ServerCommand object with specified address

        Args:
            address: Must be in host:port format
        """
        self._adapter = adapter

    def reset_valuation_service(self):
        """Resets all data held by the OpenRedukti valuation server

        Returns:
            None

        Raises:
            RuntimeError if there was a problem
        """
        request = services_pb2.Request()
        request.reset_valuation_service_request.SetInParent()
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)
        return None

    def hello(self, echo_string):
        """Invokes the hello service

        Args:
            echo_string: An input string that will be echoed back by the server

        Returns:
            An instance of HelloReply message
        """
        request = services_pb2.Request()
        request.hello_request.name = echo_string
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)
        return response.hello_reply.message

    def shutdown_valuation_service(self):
        """Shuts down the valuation service

        Note that if you invoke this the valuation server will shutdown
        and will need to restarted

        Returns:
            None
        """
        request = services_pb2.Request()
        request.shutdown_request.password = "password"
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)

    def build_curves(self, market_data):
        """Invokes the curve building service and returns the resulting yield curves

        Args:
            market_data: MarketData instance that will be used to source curve definitions and market quotes (par rates)

        Returns:
            A list of yield curves upon success
        """
        if not isinstance(market_data, MarketData):
            raise ValueError('market_data must be of MarketData type')
        request = services_pb2.Request()
        request.bootstrap_curves_request.business_date = market_data._business_date.serial()
        request.bootstrap_curves_request.curve_definitions.extend(market_data._curve_definitions)
        request.bootstrap_curves_request.par_curve_set.CopyFrom(market_data._par_curve_set)
        print('Building curves, please wait.')
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)
        return market_data.init_zero_curves(response.bootstrap_curves_reply)

    def register_curve_mappings(self, curve_group, curve_mappings):
        """Registers the list of curve mappings with the OpenRedukti valuation server

        Args:
            curve_group: Curve group
            curve_mappings: The list of curve mappings, each mapping must be of type valuation_pb2.CurveMapping.

        Returns:
            None
        """
        print('Registering curve mappings')
        request = services_pb2.Request()
        request.set_curve_mappings_request.curve_group = curve_group
        request.set_curve_mappings_request.mappings.extend(curve_mappings)
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)

    def register_curve_definitions(self, market_data):
        if not isinstance(market_data, MarketData):
            raise ValueError('market_data must be of MarketData type')
        print('Registering curve definitions')
        request = services_pb2.Request()
        request.register_curve_definitions_request.curve_definitions.extend(market_data.curve_definitions())
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)

    def register_zero_curves(self, market_data, forward_curves_list, discount_curve_list):
        if not isinstance(market_data, MarketData):
            raise ValueError('market_data must be of MarketData type')
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
        request.set_zero_curves_request.curve_group = market_data.curve_group()
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)

    def register_fixings(self, market_data):
        if not isinstance(market_data, MarketData):
            raise ValueError('market_data must be of MarketData type')
        print('Registering fixings')
        fixings_by_index = market_data.fixings()
        for entry in fixings_by_index.values():
            request = services_pb2.Request()
            request.set_fixings_request.fixings_by_index_tenor.CopyFrom(entry)
            response = self._adapter.serve(request)
            if response.header.response_code != 0:
                raise RuntimeError(response.header.response_message)

    def register_market_data(self, market_data, forward_curves_list, discount_curve_list):
        """Registers a set of market data with the OpenRedukti server

        Args:
            market_data: Instance of MarketData
            forward_curves_list: List of curve ids that should be registered as forward curves
            discount_curve_list: List of curve ids that should be registered as discount curves

        Returns:
            None
        """
        if not isinstance(market_data, MarketData):
            raise ValueError('market_data must be of MarketData type')
        self.register_curve_definitions(market_data)
        self.register_zero_curves(market_data, forward_curves_list, discount_curve_list)
        if market_data.has_fixings():
            self.register_fixings(market_data)

    def get_valuation(self, pricing_context, cfcollection):
        """Request Valuation for a set of cashflows

        Args:
            pricing_context: valuation_pb2.PricingContext instance
            cfcollection: cashflow_pb2.CFCollection instance

        Returns:
            The valuation service reply
        """
        if not isinstance(pricing_context, valuation.PricingContext):
            raise ValueError('pricing_context must of of type valuation_pb2.PricingContext')
        if not isinstance(cfcollection, cashflows.CFCollection):
            raise ValueError('cfcollection must be of type cashflow_pb2.CFCollection')
        print('Requesting valuation')
        request = services_pb2.Request()
        request.valuation_request.pricing_context.CopyFrom(pricing_context)
        request.valuation_request.cashflows.CopyFrom(cfcollection)
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)
        return response.valuation_reply

    def register_calendar(self, business_center_id, holidays_list):
        """Registers a calendar for specified business center id

        Note that a calendar can only be registered at system start
        This is because calendars may be joined with other calendars and therefore
        once a calendar is in use it cannot be safely replaced

        Args:
            business_center_id: Business Center id for which calendar is being registered
            holidays_list: List containing redukti.Date objects

        Returns:
            None
        """
        request = services_pb2.Request()
        for day in holidays_list:
            if not isinstance(day, redukti.Date):
                raise ValueError('Holidays must be a list of redukti.Date objects')
            request.register_calendar_request.holidays.append(day.serial())
        request.register_calendar_request.business_center = business_center_id
        print('Registering calendar ' + str(business_center_id))
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)

    def register_index_definition(self, index_definition):
        """Registers an index definition with the server

        Args:
            index_definition: An instance of index_pb2.IndexDefinition

        Returns:
            None
        """
        if not isinstance(index_definition, index.IndexDefinition):
            raise ValueError('index_definition must be of index.IndexDefinition type')
        request = services_pb2.Request()
        request.register_index_definition_request.index_definition = index_definition
        response = self._adapter.serve(request)
        if response.header.response_code != 0:
            raise RuntimeError(response.header.response_message)
