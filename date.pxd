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

cdef extern from "date.h" namespace "redukti":
    cdef struct YearMonthDay:
        short y
        unsigned char m
        unsigned char d
    int make_date(unsigned d, unsigned m, int y)
    YearMonthDay date_components(int z)
    int day_of_year(YearMonthDay ymd)
    unsigned char weekday(int z)
    unsigned last_day_of_month_common_year(unsigned m)
    bint is_leap(int y)
    unsigned last_day_of_month(int y, unsigned m)
    int end_of_month(int y, unsigned m)
    bint is_end_of_month(YearMonthDay ymd)
    unsigned weekday_difference(unsigned x, unsigned y)
    unsigned next_weekday(unsigned wd)
    unsigned prev_weekday(unsigned wd)
    bint parse_date(const char *s, int *d)
