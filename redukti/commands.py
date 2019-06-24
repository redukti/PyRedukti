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
import redukti
from redukti.library import MarketData, ServerCommand, load_market_data

import argparse
import csv

def do_bootstrap(server_command, args):
    if args.date is None:
        raise ValueError('A business date is required')
    business_date = redukti.parse_date(args.date)
    if args.input1 is None:
        raise ValueError('INPUT1 is required; please supply path to curve definitons file')
    if args.input2 is None:
        raise ValueError('INPUT2 is required; please supply path to par rates file')
    market_data = load_market_data(business_date, args.input1, args.input2)
    server_command.build_curves(market_data)

def run(args):
    server_command = ServerCommand(args.address)
    if args.command == 'hello':
        print(server_command.hello('Server says Hello'))
    elif args.command == 'reset':
        server_command.reset_valuation_service()
    elif args.command == 'shutdown':
        server_command.shutdown_valuation_service()
    elif args.command == 'bootstrap':
        do_bootstrap(server_command, args)
    else:
        raise Exception('Command not yet implemented')

if __name__ == '__main__':
    logging.basicConfig()
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('command', help='Command to run: reset, hello, shutdown, bootstrap')
    arg_parser.add_argument('-a', '--address', help='Server address:port', required=True)
    arg_parser.add_argument('-d', '--date', help='Business date')
    arg_parser.add_argument('-1', '--input1', help='Full path name of first input file', required=False)
    arg_parser.add_argument('-2', '--input2', help='Full path name of second input file', required=False)
    arg_parser.add_argument('-3', '--input3', help='Full path name of third input file', required=False)
    args = arg_parser.parse_args()
    run(args)
