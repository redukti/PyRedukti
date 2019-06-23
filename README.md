# PyRedukti - A Python interface to OpenRedukti

This is work in progress.
The Python interface is being developed using Cython.

## Pre-requisites

* Python grpcio package must be installed

```
python -m pip install grpcio
python -m pip install grpcio-tools
```

## Build notes

* First build [OpenRedukti](https://github.com/redukti/OpenRedukti/blob/master/docs/openredukti-building.rst) with support for [gRPC](https://grpc.io/).
* We assume that Protobuf is installed under `$HOME/Software/protobuf`.
* We assume that OpenRedukti is installed under `$HOME/Software/redukti`.
* We assume that gRPC C++ library is installed under `$HOME/Software/grpc`.

## Build and install Python module

* Set `LD_LIBRARY_PATH` as follows:

```
export LD_LIBRARY_PATH=$HOME/Software/protobuf/lib:$HOME/Software/redukti/lib:$HOME/Software/grpc/lib:$LD_LIBRARY_PATH
```

* Setup Python virtual; environment if necessary
* Execute following steps:

```
python setup.py bdist_wheel
pip install dist/pyredukti-0.1-cp36-cp36m-linux_x86_64.whl
```


