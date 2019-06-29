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

cdef extern from "calendars.h" namespace "redukti":

    cdef cppclass Calendar:
        bint is_holiday(int d)
        bint is_businessday(int d)
        bint is_end_of_month(int d)
        int end_of_month(int d)
        int adjust(int date, enums.BusinessDayConvention convention)
        int adjust(int date)
        int advance(int date, int n, enums.PeriodUnit unit)
        int advance(int date, int n, enums.PeriodUnit unit, enums.BusinessDayConvention convention)
        int advance(int date, int n, enums.PeriodUnit unit, enums.BusinessDayConvention convention, bint endOfMonth)
        int business_days_between(int fr, int to)
        int business_days_between(int fr, int to, bint includeFirst)
        int business_days_between(int fr, int to, bint includeFirst, bint includeLast)

    cdef cppclass JointCalendarParameters:
        JointCalendarParameters()
        JointCalendarParameters(enums.BusinessCenter center1, enums.BusinessCenter center2) 
        JointCalendarParameters(enums.BusinessCenter center1, enums.BusinessCenter center2, enums.BusinessCenter center3) 
        JointCalendarParameters(enums.BusinessCenter center1, enums.BusinessCenter center2, enums.BusinessCenter center3, enums.BusinessCenter center4) 

    cdef cppclass CalendarService:
        const Calendar *get_calendar(enums.BusinessCenter id)
        Calendar *get_calendar(JointCalendarParameters calendars)
        Calendar *get_calendar(JointCalendarParameters calendars, enums.JointCalendarRule rule)
        bint set_calendar(enums.BusinessCenter id, const int *holidays, size_t n)

    cdef CalendarService *get_calendar_factory()