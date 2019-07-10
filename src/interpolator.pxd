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
cdef extern from "interpolators.h" namespace "redukti":
    
    ctypedef struct SensitivitiesPointerType:
        redukti_adouble_t *get()

    cdef cppclass Interpolator:
        double interpolate(double x)
        SensitivitiesPointerType interpolate_with_sensitivities(double x, allocator.FixedRegionAllocator *A)
        SensitivitiesPointerType interpolate_with_numeric_sensitivities(double x, allocator.FixedRegionAllocator *A)

    cdef struct InterpolationOptions:
        bint monotoneconvex_inputs_are_forwards
        double cubic_left_condition_value
        double cubic_right_condition_value
        bint extrapolate
        int differentiation_order
        InterpolationOptions()

    ctypedef struct InterpolatorPointerType:
        void reset(void *)
        Interpolator *get()

    InterpolatorPointerType make_interpolator(enums.InterpolatorType type, double *x, double *y, unsigned int size, allocator.Allocator *A, const InterpolationOptions& options)
