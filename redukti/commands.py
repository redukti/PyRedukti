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

import logging

import grpc

from redukti import services_pb2
from redukti import services_pb2_grpc
from redukti import enums_pb2 as enums
from redukti import common_pb2 as common
from redukti import curve_pb2 as curve
from redukti import bootstrap_pb2 as bootstrap
from redukti import valuation_pb2 as valuation
import redukti

import argparse
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

def do_valuation_service_reset(stub):
    request = services_pb2.Request()
    request.reset_valuation_service_request.SetInParent()
    response = stub.serve(request)
    if response.header.response_code != 0:
        raise Exception(response.header.response_message)
    return None


def do_hello(stub, name):
    request = services_pb2.Request()
    request.hello_request.name = name
    response = stub.serve(request)
    if response.header.response_code != 0:
        raise Exception(response.header.response_message)
    return response.hello_reply.message


def do_shutdown(stub):
    request = services_pb2.Request()
    request.shutdown_request.password = "password"
    response = stub.serve(request)
    if response.header.response_code != 0:
        raise Exception(response.header.response_message)
    return response.hello_reply.message

class MarketData:
    business_date = redukti.dmy(11,12,2012).serial()     # FIXME date must be set via constructor
    curve_definitions = None
    par_curve_set = None
    fixings = None

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
        self.curve_definitions = defs

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
        self.par_curve_set = par_curve_set

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
        self.fixings = fixings

def load_market_data(curve_definitions_filename, par_rates_filename, fixings_filename=None):
    market_data = MarketData()
    market_data.read_curvedefinitions(curve_definitions_filename)
    # print(definitions)
    market_data.read_parcurves(par_rates_filename)
    # print(par_curve_set)
    if fixings_filename:
        market_data.read_fixings(fixings_filename)
    return market_data

def do_build_curves(stub, market_data):
    request = services_pb2.Request()
    request.bootstrap_curves_request.business_date = market_data.business_date
    request.bootstrap_curves_request.curve_definitions.extend(market_data.curve_definitions)
    request.bootstrap_curves_request.par_curve_set.CopyFrom(market_data.par_curve_set)
    response = stub.serve(request)
    if response.header.response_code != 0:
        raise Exception(response.header.response_message)
    print(response.bootstrap_curves_reply)
    return response.bootstrap_curves_reply

def run(args):
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = services_pb2_grpc.OpenReduktiServicesStub(channel)
        if args.command == 'hello':
            print(do_hello(stub, "Hello"))
        elif args.command == 'reset':
            do_reset_all(stub)
        elif args.command == 'shutdown':
            do_shutdown(stub)
        elif args.command == 'bootstrap':
            do_build_curves(stub, load_market_data(args.input1, args.input2))
        else:
            raise Exception('Command not yet implemented')

if __name__ == '__main__':
    logging.basicConfig()
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('command', help='Command to run: reset, hello, shutdown, bootstrap')
    arg_parser.add_argument('-1', '--input1', help='Full path name of first input file', required=False)
    arg_parser.add_argument('-2', '--input2', help='Full path name of second input file', required=False)
    arg_parser.add_argument('-3', '--input3', help='Full path name of third input file', required=False)
    args = arg_parser.parse_args()
    run(args)
