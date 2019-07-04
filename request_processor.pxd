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
from libcpp.string cimport string

cdef extern from "services.pb.h" namespace "redukti":
    cdef cppclass Request:
        bint SerializeToString(string*output)
        bint ParseFromString(const string& data)
    cdef cppclass Response:
        bint SerializeToString(string*output)
        bint ParseFromString(const string& data)

cdef extern from "request_processor.h" namespace "redukti":
    cdef cppclass RequestProcessor:
        Response *process(const Request *request, Response *response)

    unique_ptr[RequestProcessor] get_request_processor(const char* pricing_scipt)
