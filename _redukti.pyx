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
cimport autodiff
cimport date

cdef class ADVar:
    cdef autodiff.redukti_adouble_t* _ad
    cdef int _vars
    cdef int _order

    def __cinit__(self, int n_vars, int order, int variable, double initial_value):
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
    cdef int _date

    def __cinit__(self, int date):
        _date = date

def make(unsigned d, unsigned m, int y):
    return Date(date.make_date(d, m, y))
