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
from setuptools import setup, Extension
from Cython.Build import cythonize

basepath=os.path.expanduser('~/Software')

sourcefiles = ['_redukti.pyx']
extensions = [Extension("_redukti", sourcefiles,
    libraries=["openredukti"],
    library_dirs=[os.path.join(basepath, 'redukti', 'lib')],
    include_dirs = [os.path.join(basepath, 'redukti', 'include', 'redukti'),
        os.path.join(basepath, 'redukti', 'include'), 
        os.path.join(basepath, 'protobuf', 'include')],
    language="c++",             # generate C++ code
    )]

setup(name='pyredukti',
    version="0.1",
    author='Dibyendu Majumdar',
    author_email='mobile at majumdar.org.uk',
    url='',
    packages=['redukti'],
    ext_modules=cythonize(extensions, language_level = "3")
    )