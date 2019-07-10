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

import os
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.docstrings = True   # ensure doc strings are included
Options.annotate = True     # generate HTML version of sources

redukti_subdir = 'redukti'
protobuf_subdir = 'protobuf'

libraries = []
library_dirs = []
extra_compile_args=[]

if sys.platform != 'win32':
    basepath=os.path.expanduser('~/Software')
    libraries = ["openredukti"]
    library_dirs = [os.path.join(basepath, redukti_subdir, 'lib')]
    extra_compile_args=[]
else:
    basepath='/Software'
    libraries = ["openredukti", "libprotobuf", "libopenblas"]
    library_dirs = [os.path.join(basepath, redukti_subdir, 'lib'),
        os.path.join(basepath, protobuf_subdir, 'lib')]
    extra_compile_args=["/MD"]

sourcefiles = ['src/_redukti.pyx']
extensions = [Extension("_redukti", sourcefiles,
    libraries    = libraries,
    library_dirs = library_dirs,
    include_dirs = [os.path.join(basepath, redukti_subdir, 'include/redukti'),
        os.path.join(basepath, redukti_subdir, 'include'), 
        os.path.join(basepath, protobuf_subdir, 'include')],
    language     = "c++",             # generate C++ code,
    extra_compile_args = extra_compile_args
    )]

setup(name='pyredukti',
    version="0.1",
    author='Dibyendu Majumdar',
    author_email='mobile at majumdar.org.uk',
    url='',
    packages=['redukti'],
    ext_modules=cythonize(extensions, language_level = "3")
    )
