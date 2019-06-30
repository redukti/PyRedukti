An Introduction to PyRedukti
============================

PyRedukti is a Python binding for `OpenRedukti <https://github.com/redukti/OpenRedukti>`_.

OpenRedukti is a C++ library that has following features:

* Ability to express an interest rate product as a set of cashflows
* Bootstrap continuously compounded zero coupon interest rate curves using Linear, CubicSpline, and MonotoneConvex interpolators
* Interpolate curves in the discount factor space using LogLinear and LogCubicSpline interpolators
* Compute present value of cashflows
* Compute first and second order derivatives using `Automatic/algorithmic Differentiation <http://www.autodiff.org/>`_.

These features are available as a library, but additionally OpenRedukti provides a server implementation
based upon `gRPC <https://grpc.io/>`_ technology.

The Python bindings operate at two levels.

At the low level, the Python bindings provide wrappers for a number of OpenRedukti classes such as:

* ``Date`` - Date value
* ``ADVar`` - automatically differentiated variable
* ``Calendar`` - business day calendars
* ``DayFraction`` - Day Count Fraction calculators
* ``InterestRateIndex`` - Various functions related to indices
* ``Interpolators`` - Various 2-d interpolation schemes
* ``YieldCurve`` - including two subtypes: InterpolatedYieldCurve, and SvenssonCurve
* ``ScheduleGenerator`` - generates cashflow schedules

Associated with these are a bunch of types and enum values that are generated from Google Protocol Buffer descriptions.

At a higher level, PyRedukti offers the ability to communicate with the OpenRedukti server.
Using this model, you get following additional capabilities:

* Build Zero Curves from market quotes (PAR rates)
* Prime the server with market data such as Zero Curves and Fixings
* Get NPV and Zero/PAR Sensitivities calculated for trades that can be represented as cashflows 

The following classes and utilities provide the core functions:

* ``MarketData`` - This class encapsulates reading raw market data from CSV formatted files
* ``ServerCommand`` - This class encapsulates the functions for interacting with the OpenRedukti server 

Building PyRedukti
------------------

Pre-requisites
++++++++++++++

* Python grpcio package must be installed

::

    python -m pip install grpcio
    python -m pip install grpcio-tools

Build steps
+++++++++++

* First build `OpenRedukti <https://github.com/redukti/OpenRedukti/blob/master/docs/openredukti-building.rst>`_ with support for gRPC.
* We assume that Protobuf is installed under ``$HOME/Software/protobuf``.
* We assume that OpenRedukti is installed under ``$HOME/Software/redukti``.
* We assume that gRPC C++ library is installed under ``$HOME/Software/grpc``.

Build and install Python module
+++++++++++++++++++++++++++++++

* Set ``LD_LIBRARY_PATH`` as follows:

::

    export LD_LIBRARY_PATH=$HOME/Software/protobuf/lib:$HOME/Software/redukti/lib:$HOME/Software/grpc/lib:$LD_LIBRARY_PATH

* Setup Python virtual; environment if necessary
* Execute following steps:

::
    python setup.py bdist_wheel
    pip install dist/pyredukti-0.1-cp36-cp36m-linux_x86_64.whl