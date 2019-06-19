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

cdef extern from "enums.pb.h" namespace "redukti":

    cdef enum ResponseSubCode:
        kOk = 0
    cdef enum IsdaIndex:
        pass
    cdef enum IndexFamily:
        pass
    cdef enum DayCountFraction:
        BUS_252 = 9
    cdef enum BusinessCenter:
        BUSINESS_CENTER_UNSPECIFIED = 0
        BRSP = 11
    cdef enum PeriodUnit:
        YEARS = 5
    cdef enum JointCalendarRule:
        pass
    cdef enum BusinessDayConvention:
        pass
