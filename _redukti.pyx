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
cimport autodiff, date, enums, schedule, calendar, dayfraction, index, allocator, interpolator, curve
from redukti import schedule_pb2
from libcpp.string cimport string
from libcpp.memory cimport unique_ptr
from cpython cimport array
import array

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

    @staticmethod
    cdef dup(autodiff.redukti_adouble_t *value):
        if value is NULL:
            raise ValueError('NULL value supplied')
        cdef int n_vars = autodiff.redukti_adouble_get_nvars(value)
        cdef int order = autodiff.redukti_adouble_get_order(value)
        cdef ADVar copy = ADVar(n_vars, order, 0, 0.0)
        autodiff.redukti_adouble_assign(copy._ad, value)
        return copy

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
    
    @staticmethod
    def from_dmy(unsigned d, unsigned m, int y):
        return Date(date.make_date(d, m, y))

def dmy(unsigned d, unsigned m, int y):
    return Date(date.make_date(d, m, y))

cdef validate_periodunit(enums.PeriodUnit unit):
    if unit < 1 or unit > enums.YEARS:
        raise ValueError('Invalid PeriodUnit specified')

def advance(Date d, int n, enums.PeriodUnit unit):
    validate_periodunit(unit)
    return Date(date.advance(d.serial(), n, unit))

cdef bytes to_bytes(s):
    if type(s) is unicode:
        return s.encode('UTF-8')
    elif isinstance(s, bytes):
        return s
    elif isinstance(s, unicode):
        return bytes(s)
    else:
        raise TypeError("Could not convert to bytes.")

def parse_date(s):
    cdef int d
    byte_s = to_bytes(s)
    cdef const char* c_string = byte_s
    if not date.parse_date(c_string, &d):
        raise ValueError('Invalid date: cannot parse')
    return Date(d)

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

cdef validate_business_centers(list business_centres):
    if len(business_centres) == 0:
        raise ValueError('Business centers must be specified')
    for center in business_centres:
        if center < 1 or center > enums.BRSP:
            raise ValueError('Invalid business center')

cdef class Calendar:
    cdef const calendar.Calendar *_calendar

    def __cinit__(self, list business_centres):
        cdef calendar.JointCalendarParameters joint_calendars
        validate_business_centers(business_centres)
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

    def last_day_of_month(self, Date d):
        return Date(self._calendar.end_of_month(d.serial()))

    def advance(self, Date date, int n, enums.PeriodUnit unit, enums.BusinessDayConvention convention = enums.BusinessDayConvention.FOLLOWING, bint eom = False):
        validate_periodunit(unit)
        return Date(self._calendar.advance(date.serial(), n, unit, convention, eom))

    def adjust(self, Date date, enums.BusinessDayConvention convention = enums.BusinessDayConvention.FOLLOWING):
        return Date(self._calendar.adjust(date.serial(), convention))

cdef validate_daycountfraction(enums.DayCountFraction dfc):
    if dfc < 1 or dfc > enums.BUS_252:
        raise ValueError('Invalid DayCountFraction specified')

cdef class DayFraction:
    cdef const dayfraction.DayFraction *_dayfraction

    def __cinit__(self, enums.DayCountFraction dfc):
        validate_daycountfraction(dfc)
        self._dayfraction = dayfraction.get_day_fraction(dfc)

    cpdef double year_fraction(self, Date d1, Date d2):
        return self._dayfraction.year_fraction(d1.serial(), d2.serial())

    cpdef double year_fraction_with_finalperiod(self, Date d1, Date d2, bint final_period):
        return self._dayfraction.year_fraction(d1.serial(), d2.serial(), final_period)
    
    cpdef double year_fraction_with_refdates(self, Date d1, Date d2, Date ref_date1, Date ref_date2):
        return self._dayfraction.year_fraction(d1.serial(), d2.serial(), ref_date1.serial(), ref_date2.serial())

cdef validate_isda_index(enums.IsdaIndex index):
    if index < 1 or index > enums.ZAR_JIBAR_SAFEX:
        raise ValueError('Invalid IsdaIndex specified')

cdef validate_index_family(enums.IndexFamily family):
    if family < 1 or family > enums.REPO_CURVE:
        raise ValueError('Invalid IndexFamily specified')

cdef validate_tenor(enums.Tenor tenor):
    if tenor < 0 or tenor > enums.TENOR_1T:
        raise ValueError('Invalid Tenor specified')

cdef validate_currency(enums.Currency ccy):
    if ccy < 0 or ccy > enums.PLN:
        raise ValueError('Invalid Currency specified')

cdef validate_interpolator_type(enums.InterpolatorType t):
    if t < 0 or t > enums.CUBIC_SPLINE_CLAMPED:
        raise ValueError('Invalid InterpolatorType specified')

cdef class InterestRateIndex:
    cdef const index.InterestRateIndex *_index

    def __cinit__(self):
        self._index = NULL

    @staticmethod
    def get_index_by_isdaindex(enums.IsdaIndex isda_index, enums.Tenor tenor):
        validate_isda_index(isda_index)
        validate_tenor(tenor)
        cdef const index.InterestRateIndex *idx = index.get_default_index_service().get_index(isda_index, tenor)
        if idx is NULL:
            raise ValueError('Index not defined for given IsdaIndex and Tenor')
        cdef InterestRateIndex obj = InterestRateIndex()
        obj._index = idx
        return obj

    @staticmethod
    def get_index(enums.Currency currency, enums.IndexFamily index_family, enums.Tenor tenor):
        validate_currency(currency)
        validate_index_family(index_family)
        validate_tenor(tenor)
        cdef const index.InterestRateIndex *idx = index.get_default_index_service().get_index(currency, index_family, tenor)
        if idx is NULL:
            raise ValueError('Index not defined for given Currency, IndexFamily and Tenor')
        cdef InterestRateIndex obj = InterestRateIndex()
        obj._index = idx
        return obj

    cpdef Date value_date(self, Date fixing_date):
        if self._index is NULL:
            return Exception('Index object is not initialized')
        return Date(self._index.value_date(fixing_date.serial()))

    cpdef Date fixing_date(self, Date accrual_start_date):
        if self._index is NULL:
            return Exception('Index object is not initialized')
        return Date(self._index.fixing_date(accrual_start_date.serial()))

    cpdef Date maturity_date(self, Date value_date):
        if self._index is NULL:
            return Exception('Index object is not initialized')
        return Date(self._index.maturity_date(value_date.serial()))

    def date_components(self, Date adjusted):
        if self._index is NULL:
            return Exception('Index object is not initialized')
        cdef int fixing = self._index.fixing_date(adjusted.serial())
        cdef int value_dt = self._index.value_date(fixing)
        cdef int maturity_dt = self._index.maturity_date(value_dt)        
        return Date(fixing), Date(value_dt), Date(maturity_dt)

    cpdef Date adjust_date(self, Date unadjusted, int days):
        if self._index is NULL:
            return Exception('Index object is not initialized')
        return Date(self._index.fixing_calendar().advance(unadjusted.serial(), days, enums.DAYS, self._index.day_convention()))

cdef class Interpolator:
    cdef array.array _x
    cdef array.array _y
    cdef interpolator.InterpolatorPointerType _interpolator
    cdef interpolator.Interpolator *_interpolator_ptr

    def __cinit__(self, enums.InterpolatorType interpolator_type, array.array x, array.array y, int order = 0):
        validate_interpolator_type(interpolator_type)
        if x.typecode != 'd' or y.typecode != 'd':
            raise ValueError('Supplied arrays must be of type double')
        if len(x) != len(y) or len(x) < 4 or len(x) > 50:
            raise ValueError('Invalid size of x or y: minimum 4 elements required and len(x) must be == len(y)')
        self._x = x
        self._y = y
        cdef double *xdata = <double *>self._x.data.as_voidptr
        cdef double *ydata = <double *>self._y.data.as_voidptr
        cdef int size = len(x)
        cdef interpolator.InterpolationOptions options;
        options.differentiation_order = order
        self._interpolator = interpolator.make_interpolator(interpolator_type, xdata, ydata, size, allocator.get_default_allocator(), options)
        self._interpolator_ptr = self._interpolator.get()

    def __dealloc__(self):
        self._interpolator.reset(NULL)

    cpdef double interpolate(self, double x):
        return self._interpolator_ptr.interpolate(x)

    cdef ADVar interpolate_with_sensitivities_(self, double x, allocator.FixedRegionAllocator *fixed_region_allocator):
        cdef interpolator.SensitivitiesPointerType sensitivities = self._interpolator_ptr.interpolate_with_sensitivities(x, fixed_region_allocator)
        cdef autodiff.redukti_adouble_t *data = sensitivities.get()
        if data is NULL:
            return None
        return ADVar.dup(sensitivities.get())

    cpdef ADVar interpolate_with_sensitivities(self, double x):
        cdef allocator.FixedRegionAllocator *fixed_region_allocator = allocator.get_threadspecific_allocators().tempspace_allocator
        cdef size_t pos = fixed_region_allocator.pos() # Since we can't use the FixedRegionAllocatorGuard in Cython
        try:
            return self.interpolate_with_sensitivities_(x, fixed_region_allocator)
        finally:
            fixed_region_allocator.pos(pos)

cdef class CurveId:
    cdef long long _id

    def __cinit__(self, enums.PricingCurveType pricing_curve_type, enums.Currency ccy, enums.IndexFamily index_family, enums.Tenor tenor,
        Date as_of_date, int cycle = 0, enums.MarketDataQualifier qual = enums.MDQ_NORMAL, int scenario = 0):
        self._id = curve.make_curve_id(pricing_curve_type, ccy, index_family, tenor, as_of_date.serial(),
            cycle, qual, scenario)

    cpdef long long id(self):
        return self._id

def convert_to_date_array(list values):
    cdef array.array date_array = array.array('i', [])
    for v in values:
        if isinstance(v, Date):
            date_array.append(v.serial())
        else:
            raise ValueError('Expected values of redukti.Date type in list')
    return date_array

cdef class InterpolatedYieldCurve:
    cdef array.array _maturities
    cdef array.array _values
    cdef curve.YieldCurvePointerType _yield_curve
    cdef curve.YieldCurve *_yield_curve_ptr
    
    def __cinit__(self, long long id, Date as_of_date, list maturities, list values, enums.InterpolatorType interpolator_type, enums.IRRateType rate_type, int deriv_order, enums.DayCountFraction fraction):
        validate_interpolator_type(interpolator_type)
        if len(maturities) != len(values) or len(maturities) < 4 or len(maturities) > 50:
            raise ValueError('Invalid size of maturities or values: minimum 4 elements required and len(maturies) must be == len(values)')
        self._maturities = convert_to_date_array(maturities)
        self._values = array.array('d', values)
        cdef int *xdata = <int *>self._maturities.data.as_voidptr
        cdef double *ydata = <double *>self._values.data.as_voidptr
        cdef int size = len(maturities)
        self._yield_curve = curve.make_curve(allocator.get_default_allocator(), id, as_of_date.serial(), xdata, ydata, size, interpolator_type, rate_type, deriv_order, fraction)
        self._yield_curve_ptr = self._yield_curve.get()
        if self._yield_curve_ptr is NULL:
            raise Exception('Failed to create instance of InterpolatedYieldCurve: please check inputs are correct')

    def __dealloc__(self):
        self._yield_curve.reset(NULL)

    cpdef double discount(self, Date d):
        return self._yield_curve_ptr.discount(d.serial())

    cpdef double zero_rate(self, Date d):
        return self._yield_curve_ptr.zero_rate(d.serial())

    cpdef double forward_rate(self, Date d1, Date d2):
        return self._yield_curve_ptr.forward_rate(d1.serial(), d2.serial())

    cpdef double time_from_reference(self, Date d):
        return self._yield_curve_ptr.time_from_reference(d.serial())

    cdef ADVar get_sensitivities_(self, double x, allocator.FixedRegionAllocator *fixed_region_allocator):
        cdef curve.CurveSensitivitiesPointerType sensitivities = self._yield_curve_ptr.get_sensitivities(x, fixed_region_allocator)
        cdef autodiff.redukti_adouble_t *data = sensitivities.get()
        if data is NULL:
            return None
        return ADVar.dup(sensitivities.get())

    cpdef ADVar get_sensitivities(self, double x):
        cdef allocator.FixedRegionAllocator *fixed_region_allocator = allocator.get_threadspecific_allocators().tempspace_allocator
        cdef size_t pos = fixed_region_allocator.pos() # Since we can't use the FixedRegionAllocatorGuard in Cython
        try:
            return self.get_sensitivities_(x, fixed_region_allocator)
        finally:
            fixed_region_allocator.pos(pos)

cdef class SvenssonCurve:
    cdef array.array _parameters
    cdef curve.YieldCurvePointerType _yield_curve
    cdef curve.YieldCurve *_yield_curve_ptr

    def __cinit__(self, long long id, Date as_of_date, list parameters, enums.DayCountFraction fraction):
        if len(parameters) != 6:
            raise ValueError('Invalid size of parameters: six parameters required')
        if parameters[0] < 0.0 or parameters[4] < 0.0 or parameters[5] < 0.0:
            raise ValueError('Beta0, tau1 and tau2 must be positive')
        self._parameters = array.array('d', parameters)
        cdef double *ydata = <double *>self._parameters.data.as_voidptr
        cdef int size = len(parameters)
        self._yield_curve = curve.make_svensson_curve(allocator.get_default_allocator(), id, as_of_date.serial(), ydata, size, fraction)
        self._yield_curve_ptr = self._yield_curve.get()
        if self._yield_curve_ptr is NULL:
            raise Exception('Failed to create instance of SvenssonCurve: please check inputs are correct')

    def __dealloc__(self):
        self._yield_curve.reset(NULL)

    cpdef double discount(self, Date d):
        return self._yield_curve_ptr.discount(d.serial())

    cpdef double zero_rate(self, Date d):
        return self._yield_curve_ptr.zero_rate(d.serial())

    cpdef double forward_rate(self, Date d1, Date d2):
        return self._yield_curve_ptr.forward_rate(d1.serial(), d2.serial())

    cpdef double time_from_reference(self, Date d):
        return self._yield_curve_ptr.time_from_reference(d.serial())

cdef class YieldCurve:
    cdef curve.IRCurveDefinition _definition
    cdef curve.ZeroCurve _underlying_curve
    cdef curve.YieldCurvePointerType _yield_curve
    cdef curve.YieldCurve *_yield_curve_ptr

    def __cinit__(self, Date business_date, curve_defn, zero_curve, int deriv_order = 2, enums.PricingCurveType type = enums.PRICING_CURVE_TYPE_FORWARD, enums.MarketDataQualifier mdq = enums.MDQ_NORMAL, int cycle = 0, int scenario = 0):
        cdef string str = curve_defn.SerializeToString()
        if not self._definition.ParseFromString(str):
            raise ValueError("Cannot parse the IRCurveDefinition")
        str = zero_curve.SerializeToString()
        if not self._underlying_curve.ParseFromString(str):
            raise ValueError("Cannot parse the ZeroCurve")
        self._yield_curve = curve.make_curve(business_date.serial(), &self._definition, self._underlying_curve, deriv_order, type, mdq, cycle, scenario)
        self._yield_curve_ptr = self._yield_curve.get()
        if self._yield_curve_ptr is NULL:
            raise Exception('Failed to create instance of SvenssonCurve: please check inputs are correct')

    def __dealloc__(self):
        self._yield_curve.reset(NULL)

    cpdef double discount(self, Date d):
        return self._yield_curve_ptr.discount(d.serial())

    cpdef double zero_rate(self, Date d):
        return self._yield_curve_ptr.zero_rate(d.serial())

    cpdef double forward_rate(self, Date d1, Date d2):
        return self._yield_curve_ptr.forward_rate(d1.serial(), d2.serial())

    cpdef double time_from_reference(self, Date d):
        return self._yield_curve_ptr.time_from_reference(d.serial())
