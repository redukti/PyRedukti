# distutils: language = c++

cdef extern from "date.h" namespace "redukti":
    cdef struct YearMonthDay:
        short y
        unsigned char m
        unsigned char d
    int make_date(unsigned d, unsigned m, int y)

