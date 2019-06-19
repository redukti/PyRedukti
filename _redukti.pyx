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

from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
cimport autodiff, date, enums, schedule, calendar
from redukti import schedule_pb2
from libcpp.string cimport string

cdef class ADVar:
    cdef autodiff.redukti_adouble_t* _ad
    cdef int _vars
    cdef int _order

    def __cinit__(self, int n_vars, int order, int variable, double initial_value):
        if (n_vars <= 0):
            raise ValueError('Number of variables in AdVar must be > 0')
        if order < 0 or order > 2:
            raise ValueError('Order must be between 0 and 2')
        if (variable < 0 or variable >= n_vars):
            raise ValueError('Variable index is out of range')
        cdef size_t size = autodiff.redukti_adouble_alloc_size(n_vars, order)
        self._ad = <autodiff.redukti_adouble_t*> PyMem_Malloc(size)
        self._vars = n_vars
        self._order = order
        autodiff.redukti_adouble_init(self._ad, n_vars, order, variable, initial_value)

    def __dealloc__(self):
        PyMem_Free(self._ad)

    def assign(self, ADVar other):
        is_compatible = self._vars == other._vars and self._order == other._order
        if not is_compatible:
            raise ValueError('Supplied values are not of the same order or size')
        autodiff.redukti_adouble_assign(self._ad, other._ad)

    def value(self):
        return autodiff.redukti_adouble_get_value(self._ad)

    def gradient(self):
        g = []
        if self._order == 0:
            return g
        for i in range(0,self._vars):
            list.append(g, autodiff.redukti_adouble_get_derivative1(self._ad, i))
        return g

cdef class Date:
    cdef int _serial
    cdef date.YearMonthDay _ymd

    def __cinit__(self, int value):
        self._serial = value
        self._ymd = date.date_components(value)

    cpdef int day(self):
        return self._ymd.d
    
    cpdef int month(self):
        return self._ymd.m
    
    cpdef int year(self):
        return self._ymd.y

    cpdef int serial(self):
        return self._serial
    
    
def make_date_from_dmy(unsigned d, unsigned m, int y):
    return Date(date.make_date(d, m, y))

def generate_schedule(schedule_parameters):
    cdef string str = schedule_parameters.SerializeToString()
    cdef schedule.ScheduleParameters _parameters
    if not _parameters.ParseFromString(str):
        raise ValueError("Cannot parse the schedule parameters")
    cdef schedule.Schedule _schedule
    status = schedule.build_schedule(_parameters, _schedule)
    if not status == enums.ResponseSubCode.kOk:
        raise Exception('Failed to generate schedule')
    result = schedule_pb2.Schedule()
    cdef string result_str
    if not _schedule.SerializeToString(&result_str):
        raise Exception('Failed to parse result from api call')
    result.ParseFromString(result_str)
    return result

cdef class Calendar:
    cdef const calendar.Calendar *_calendar

    cdef validate(self, list business_centres):
        if len(business_centres) == 0:
            raise ValueError('Business centers must be specified')
        for center in business_centres:
            if center < 1 or center > enums.BRSP:
                raise ValueError('Invalid business center')

    cdef validate_periodunit(self, enums.PeriodUnit unit):
        if unit < 1 or unit > enums.YEARS:
            raise ValueError('Invalid PeriodUnit specified')

    def __cinit__(self, list business_centres):
        cdef calendar.JointCalendarParameters joint_calendars
        self.validate(business_centres)
        if len(business_centres) == 0:
            raise ValueError('Business centers must be specified')
        if len(business_centres) == 1:
            self._calendar = calendar.get_calendar_factory().get_calendar(<enums.BusinessCenter>business_centres[0])
        elif len(business_centres) == 2:
            joint_calendars = calendar.JointCalendarParameters(business_centres[0], business_centres[1]) 
            self._calendar = calendar.get_calendar_factory().get_calendar(joint_calendars)
        elif len(business_centres) == 3:
            joint_calendars = calendar.JointCalendarParameters(business_centres[0], business_centres[1], business_centres[2]) 
            self._calendar = calendar.get_calendar_factory().get_calendar(joint_calendars)
        elif len(business_centres) == 4:
            joint_calendars = calendar.JointCalendarParameters(business_centres[0], business_centres[1], business_centres[2], business_centres[3]) 
            self._calendar = calendar.get_calendar_factory().get_calendar(joint_calendars)
        else:
            raise ValueError('Incorrect number of values in business centres list, max of 4 allowed')
        if self._calendar is NULL:
            raise ValueError('Unable to construct a calendar from given parameters')
    
    cpdef bint is_holiday(self, Date d):
        return self._calendar.is_holiday(d.serial())

    def advance(self, Date date, int n, enums.PeriodUnit unit):
        self.validate_periodunit(unit)
        return Date(self._calendar.advance(date.serial(), n, unit))

