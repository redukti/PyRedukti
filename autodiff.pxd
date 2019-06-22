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

cdef extern from "autodiff.h":
    ctypedef struct redukti_adouble_t
    size_t redukti_adouble_alloc_size(int vars, int order)
    void redukti_adouble_init(redukti_adouble_t *A, int n_vars, int order, int variable, double initial_value)
    bint redukti_adouble_are_compatible(const redukti_adouble_t *A, const redukti_adouble_t *B)
    void redukti_adouble_assign(redukti_adouble_t *A, const redukti_adouble_t *B)
    void redukti_adouble_add(redukti_adouble_t *A, redukti_adouble_t *B, double alpha)
    void redukti_adouble_scalar_multiply(redukti_adouble_t *A, double alpha)
    void redukti_adouble_multiply(redukti_adouble_t *A, redukti_adouble_t *B, redukti_adouble_t *temp)
    void redukti_adouble_divide(redukti_adouble_t *A, redukti_adouble_t *B, redukti_adouble_t *temp1,
			    redukti_adouble_t *temp2)
    void redukti_adouble_exp(redukti_adouble_t *A, redukti_adouble_t *temp)
    void redukti_adouble_log(redukti_adouble_t *A, redukti_adouble_t *temp)
    void redukti_adouble_power(redukti_adouble_t *A, double p, redukti_adouble_t *temp)
    void redukti_adouble_abs(redukti_adouble_t *A)
    void redukti_adouble_sin(redukti_adouble_t *A, redukti_adouble_t *temp)
    void redukti_adouble_cos(redukti_adouble_t *A, redukti_adouble_t *temp)
    void redukti_adouble_tan(redukti_adouble_t *A, redukti_adouble_t *temp)
    void redukti_adouble_scalar_add(redukti_adouble_t *A, double alpha)
    double redukti_adouble_get_value(redukti_adouble_t *x)
    double redukti_adouble_get_derivative1(redukti_adouble_t *x, int parameter)
    double redukti_adouble_get_derivative2(redukti_adouble_t *x, int parameter1, int parameter2)
    void redukti_adouble_set_value(redukti_adouble_t *x, double v)
    void redukti_adouble_set_derivative1(redukti_adouble_t *x, int parameter, double v)
    void redukti_adouble_set_derivative2(redukti_adouble_t *x, int parameter1, int parameter2, double v)
    int redukti_adouble_get_order(const redukti_adouble_t *x)
    int redukti_adouble_get_nvars(const redukti_adouble_t *x)