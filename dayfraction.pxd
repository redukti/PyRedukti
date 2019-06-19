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

cimport enums

cdef extern from "dayfractions.h" namespace "redukti":

    cdef cppclass DayFraction:
        double year_fraction(int d1, int d2)
        double year_fraction(int d1, int d2, bint finalPeriod)
        double year_fraction(int d1, int d2, int refStart, int refEnd)

    cdef const DayFraction *get_day_fraction(enums.DayCountFraction dfc)

