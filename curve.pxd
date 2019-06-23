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

from libcpp.memory cimport unique_ptr
cimport enums, autodiff, allocator
from autodiff cimport redukti_adouble_t
cdef extern from "curve.h" namespace "redukti":

    ctypedef struct CurveSensitivitiesPointerType:
        redukti_adouble_t *get()

    cdef cppclass YieldCurve:
        double time_from_reference(int d)
        double discount(double time)
        double discount(int d)
        double zero_rate(int d)
        double zero_rate(double t)
        double forward_rate(int d1, int d2)
        double forward_rate(double t1, double t2)
        double forward(double t)
        CurveSensitivitiesPointerType get_sensitivities(double x, allocator.FixedRegionAllocator *A)

    ctypedef struct YieldCurvePointerType:
        YieldCurve *get()
        void reset(void *)

    YieldCurvePointerType make_curve(allocator.Allocator *A, long long id, int as_of_date, int* maturities, double *values, size_t n, enums.InterpolatorType interpolator, enums.IRRateType type, int deriv_order, enums.DayCountFraction fraction)

    long long make_curve_id(enums.PricingCurveType type, enums.Currency ccy, enums.IndexFamily index_family, enums.Tenor tenor, int as_of_date, int cycle, enums.MarketDataQualifier qual, int scenario)