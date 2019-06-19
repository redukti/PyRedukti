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

cimport enums, calendar, dayfraction
from libcpp.string cimport string

cdef extern from "index.pb.h" namespace "redukti":
    cdef cppclass IndexDefinition:
        bint ParseFromString(const string& data)

cdef extern from "index.h" namespace "redukti":
    cdef cppclass InterestRateIndex:
        enums.Currency currency()
        enums.IndexFamily family()
        enums.Tenor tenor()
        enums.IsdaIndex isda_index()
        int value_date(int fixing_date)
        int fixing_date(int accrual_start_date)
        int maturity_date(int value_date)
        bint is_valid_fixing_date(int date)
        const calendar.Calendar *fixing_calendar()
        const dayfraction.DayFraction *day_fraction()
        enums.BusinessDayConvention day_convention()
    
    cdef cppclass IndexService:
        bint register_index(const IndexDefinition &definition)
        InterestRateIndex *get_index(enums.IsdaIndex isda_index, enums.Tenor tenor)
        InterestRateIndex *get_index(enums.Currency currency, enums.IndexFamily index_family, enums.Tenor tenor) 

    cdef IndexService *get_default_index_service()