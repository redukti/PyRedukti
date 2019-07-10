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

cdef extern from "allocators.h" namespace "redukti":

    cdef cppclass Allocator
    cdef cppclass RegionAllocator
    cdef cppclass FixedRegionAllocator:
        size_t pos()
        void pos(size_t i)

    cdef struct AllocatorSet:
        RegionAllocator *cashflow_allocator
        RegionAllocator *sensitivities_allocator
        FixedRegionAllocator *tempspace_allocator

    AllocatorSet *get_threadspecific_allocators()

    Allocator* get_default_allocator()