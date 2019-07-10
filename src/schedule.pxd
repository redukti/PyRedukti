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
from libcpp.string cimport string

cdef extern from "schedule.pb.h" namespace "redukti":
    cdef cppclass ScheduleParameters:
        bint ParseFromString(const string& data)
    cdef cppclass Schedule:
        bint SerializeToString(string* output)

cdef extern from "schedule.h" namespace "redukti":
    enums.ResponseSubCode build_schedule(ScheduleParameters &params, Schedule &schedule)