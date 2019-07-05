export PATH=$HOME/Software/protobuf/bin:$PATH
SOURCEDIR=$HOME/Software/redukti/proto
DESTDIR=.
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/enums.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/calendar.proto
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/index.proto
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/schedule.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/cashflow.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/curve.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/shared.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/bootstrap.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/valuation.proto 
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR $SOURCEDIR/redukti/instrument_templates.proto
python -m grpc_tools.protoc -I$SOURCEDIR --python_out=$DESTDIR --grpc_python_out=$DESTDIR $SOURCEDIR/redukti/services.proto
