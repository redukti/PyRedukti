# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/cashflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from redukti import enums_pb2 as redukti_dot_enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='redukti/cashflow.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\x16redukti/cashflow.proto\x12\x07redukti\x1a\x13redukti/enums.proto\"\xce\x01\n\x08\x43\x46Simple\x12#\n\x08\x63urrency\x18\x01 \x01(\x0e\x32\x11.redukti.Currency\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x12\x14\n\x0cpayment_date\x18\x03 \x01(\x05\x12\'\n\x0btrade_index\x18\x04 \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\x36\n\x18\x64iscounting_index_family\x18\x05 \x01(\x0e\x32\x14.redukti.IndexFamily\x12\x16\n\x0e\x65x_coupon_date\x18\x06 \x01(\x05\"\xf0\x01\n\x10\x43\x46\x46loatingPeriod\x12\x10\n\x08notional\x18\x01 \x01(\x01\x12\x0e\n\x06spread\x18\x02 \x01(\x01\x12\x1a\n\x12\x61\x63\x63rual_start_date\x18\x03 \x01(\x05\x12\x18\n\x10\x61\x63\x63rual_end_date\x18\x04 \x01(\x05\x12!\n\x05index\x18\x05 \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\x1d\n\x05tenor\x18\x06 \x01(\x0e\x32\x0e.redukti.Tenor\x12\"\n\x06index2\x18\x07 \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\x1e\n\x06tenor2\x18\x08 \x01(\x0e\x32\x0e.redukti.Tenor\"\xbb\x02\n\nCFFloating\x12#\n\x08\x63urrency\x18\x01 \x01(\x0e\x32\x11.redukti.Currency\x12\x33\n\x10\x66loating_periods\x18\x02 \x03(\x0b\x32\x19.redukti.CFFloatingPeriod\x12\x36\n\x12\x63ompounding_method\x18\x03 \x01(\x0e\x32\x1a.redukti.CompoundingMethod\x12\x35\n\x12\x64\x61y_count_fraction\x18\x04 \x01(\x0e\x32\x19.redukti.DayCountFraction\x12\x14\n\x0cpayment_date\x18\x05 \x01(\x05\x12\x36\n\x18\x64iscounting_index_family\x18\x06 \x01(\x0e\x32\x14.redukti.IndexFamily\x12\x16\n\x0e\x65x_coupon_date\x18\x07 \x01(\x05\"\xc1\x01\n\x05\x43\x46\x46ra\x12#\n\x08\x63urrency\x18\x01 \x01(\x0e\x32\x11.redukti.Currency\x12\x12\n\nfixed_rate\x18\x02 \x01(\x01\x12\x14\n\x0cpayment_date\x18\x03 \x01(\x05\x12\x32\n\x0f\x66loating_period\x18\x04 \x01(\x0b\x32\x19.redukti.CFFloatingPeriod\x12\x35\n\x12\x64\x61y_count_fraction\x18\x05 \x01(\x0e\x32\x19.redukti.DayCountFraction\"\xbf\x01\n\x05\x43\x46Ois\x12!\n\x05index\x18\x01 \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\x10\n\x08notional\x18\x02 \x01(\x01\x12\x1a\n\x12\x61\x63\x63rual_start_date\x18\x03 \x01(\x05\x12\x18\n\x10\x61\x63\x63rual_end_date\x18\x04 \x01(\x05\x12\x14\n\x0cpayment_date\x18\x05 \x01(\x05\x12\x35\n\x12\x64\x61y_count_fraction\x18\x06 \x01(\x0e\x32\x19.redukti.DayCountFraction\"\xa2\x01\n\x08\x43\x46Single\x12#\n\x06simple\x18\x01 \x01(\x0b\x32\x11.redukti.CFSimpleH\x00\x12\'\n\x08\x66loating\x18\x02 \x01(\x0b\x32\x13.redukti.CFFloatingH\x00\x12\x1d\n\x03\x66ra\x18\x03 \x01(\x0b\x32\x0e.redukti.CFFraH\x00\x12\x1d\n\x03ois\x18\x04 \x01(\x0b\x32\x0e.redukti.CFOisH\x00\x42\n\n\x08\x63\x61shflow\"@\n\x08\x43\x46Stream\x12$\n\tcashflows\x18\x01 \x03(\x0b\x32\x11.redukti.CFSingle\x12\x0e\n\x06\x66\x61\x63tor\x18\x02 \x01(\x01\"2\n\x0c\x43\x46\x43ollection\x12\"\n\x07streams\x18\x01 \x03(\x0b\x32\x11.redukti.CFStreamB/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,])




_CFSIMPLE = _descriptor.Descriptor(
  name='CFSimple',
  full_name='redukti.CFSimple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='redukti.CFSimple.currency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='redukti.CFSimple.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_date', full_name='redukti.CFSimple.payment_date', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_index', full_name='redukti.CFSimple.trade_index', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discounting_index_family', full_name='redukti.CFSimple.discounting_index_family', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_date', full_name='redukti.CFSimple.ex_coupon_date', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=263,
)


_CFFLOATINGPERIOD = _descriptor.Descriptor(
  name='CFFloatingPeriod',
  full_name='redukti.CFFloatingPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notional', full_name='redukti.CFFloatingPeriod.notional', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spread', full_name='redukti.CFFloatingPeriod.spread', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accrual_start_date', full_name='redukti.CFFloatingPeriod.accrual_start_date', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accrual_end_date', full_name='redukti.CFFloatingPeriod.accrual_end_date', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='redukti.CFFloatingPeriod.index', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenor', full_name='redukti.CFFloatingPeriod.tenor', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index2', full_name='redukti.CFFloatingPeriod.index2', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenor2', full_name='redukti.CFFloatingPeriod.tenor2', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=506,
)


_CFFLOATING = _descriptor.Descriptor(
  name='CFFloating',
  full_name='redukti.CFFloating',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='redukti.CFFloating.currency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_periods', full_name='redukti.CFFloating.floating_periods', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compounding_method', full_name='redukti.CFFloating.compounding_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction', full_name='redukti.CFFloating.day_count_fraction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_date', full_name='redukti.CFFloating.payment_date', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discounting_index_family', full_name='redukti.CFFloating.discounting_index_family', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_date', full_name='redukti.CFFloating.ex_coupon_date', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=824,
)


_CFFRA = _descriptor.Descriptor(
  name='CFFra',
  full_name='redukti.CFFra',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='redukti.CFFra.currency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_rate', full_name='redukti.CFFra.fixed_rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_date', full_name='redukti.CFFra.payment_date', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_period', full_name='redukti.CFFra.floating_period', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction', full_name='redukti.CFFra.day_count_fraction', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=1020,
)


_CFOIS = _descriptor.Descriptor(
  name='CFOis',
  full_name='redukti.CFOis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='redukti.CFOis.index', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notional', full_name='redukti.CFOis.notional', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accrual_start_date', full_name='redukti.CFOis.accrual_start_date', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accrual_end_date', full_name='redukti.CFOis.accrual_end_date', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_date', full_name='redukti.CFOis.payment_date', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction', full_name='redukti.CFOis.day_count_fraction', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1023,
  serialized_end=1214,
)


_CFSINGLE = _descriptor.Descriptor(
  name='CFSingle',
  full_name='redukti.CFSingle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simple', full_name='redukti.CFSingle.simple', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating', full_name='redukti.CFSingle.floating', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fra', full_name='redukti.CFSingle.fra', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ois', full_name='redukti.CFSingle.ois', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='cashflow', full_name='redukti.CFSingle.cashflow',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1217,
  serialized_end=1379,
)


_CFSTREAM = _descriptor.Descriptor(
  name='CFStream',
  full_name='redukti.CFStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cashflows', full_name='redukti.CFStream.cashflows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='factor', full_name='redukti.CFStream.factor', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1381,
  serialized_end=1445,
)


_CFCOLLECTION = _descriptor.Descriptor(
  name='CFCollection',
  full_name='redukti.CFCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streams', full_name='redukti.CFCollection.streams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1447,
  serialized_end=1497,
)

_CFSIMPLE.fields_by_name['currency'].enum_type = redukti_dot_enums__pb2._CURRENCY
_CFSIMPLE.fields_by_name['trade_index'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_CFSIMPLE.fields_by_name['discounting_index_family'].enum_type = redukti_dot_enums__pb2._INDEXFAMILY
_CFFLOATINGPERIOD.fields_by_name['index'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_CFFLOATINGPERIOD.fields_by_name['tenor'].enum_type = redukti_dot_enums__pb2._TENOR
_CFFLOATINGPERIOD.fields_by_name['index2'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_CFFLOATINGPERIOD.fields_by_name['tenor2'].enum_type = redukti_dot_enums__pb2._TENOR
_CFFLOATING.fields_by_name['currency'].enum_type = redukti_dot_enums__pb2._CURRENCY
_CFFLOATING.fields_by_name['floating_periods'].message_type = _CFFLOATINGPERIOD
_CFFLOATING.fields_by_name['compounding_method'].enum_type = redukti_dot_enums__pb2._COMPOUNDINGMETHOD
_CFFLOATING.fields_by_name['day_count_fraction'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_CFFLOATING.fields_by_name['discounting_index_family'].enum_type = redukti_dot_enums__pb2._INDEXFAMILY
_CFFRA.fields_by_name['currency'].enum_type = redukti_dot_enums__pb2._CURRENCY
_CFFRA.fields_by_name['floating_period'].message_type = _CFFLOATINGPERIOD
_CFFRA.fields_by_name['day_count_fraction'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_CFOIS.fields_by_name['index'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_CFOIS.fields_by_name['day_count_fraction'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_CFSINGLE.fields_by_name['simple'].message_type = _CFSIMPLE
_CFSINGLE.fields_by_name['floating'].message_type = _CFFLOATING
_CFSINGLE.fields_by_name['fra'].message_type = _CFFRA
_CFSINGLE.fields_by_name['ois'].message_type = _CFOIS
_CFSINGLE.oneofs_by_name['cashflow'].fields.append(
  _CFSINGLE.fields_by_name['simple'])
_CFSINGLE.fields_by_name['simple'].containing_oneof = _CFSINGLE.oneofs_by_name['cashflow']
_CFSINGLE.oneofs_by_name['cashflow'].fields.append(
  _CFSINGLE.fields_by_name['floating'])
_CFSINGLE.fields_by_name['floating'].containing_oneof = _CFSINGLE.oneofs_by_name['cashflow']
_CFSINGLE.oneofs_by_name['cashflow'].fields.append(
  _CFSINGLE.fields_by_name['fra'])
_CFSINGLE.fields_by_name['fra'].containing_oneof = _CFSINGLE.oneofs_by_name['cashflow']
_CFSINGLE.oneofs_by_name['cashflow'].fields.append(
  _CFSINGLE.fields_by_name['ois'])
_CFSINGLE.fields_by_name['ois'].containing_oneof = _CFSINGLE.oneofs_by_name['cashflow']
_CFSTREAM.fields_by_name['cashflows'].message_type = _CFSINGLE
_CFCOLLECTION.fields_by_name['streams'].message_type = _CFSTREAM
DESCRIPTOR.message_types_by_name['CFSimple'] = _CFSIMPLE
DESCRIPTOR.message_types_by_name['CFFloatingPeriod'] = _CFFLOATINGPERIOD
DESCRIPTOR.message_types_by_name['CFFloating'] = _CFFLOATING
DESCRIPTOR.message_types_by_name['CFFra'] = _CFFRA
DESCRIPTOR.message_types_by_name['CFOis'] = _CFOIS
DESCRIPTOR.message_types_by_name['CFSingle'] = _CFSINGLE
DESCRIPTOR.message_types_by_name['CFStream'] = _CFSTREAM
DESCRIPTOR.message_types_by_name['CFCollection'] = _CFCOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CFSimple = _reflection.GeneratedProtocolMessageType('CFSimple', (_message.Message,), dict(
  DESCRIPTOR = _CFSIMPLE,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFSimple)
  ))
_sym_db.RegisterMessage(CFSimple)

CFFloatingPeriod = _reflection.GeneratedProtocolMessageType('CFFloatingPeriod', (_message.Message,), dict(
  DESCRIPTOR = _CFFLOATINGPERIOD,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFFloatingPeriod)
  ))
_sym_db.RegisterMessage(CFFloatingPeriod)

CFFloating = _reflection.GeneratedProtocolMessageType('CFFloating', (_message.Message,), dict(
  DESCRIPTOR = _CFFLOATING,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFFloating)
  ))
_sym_db.RegisterMessage(CFFloating)

CFFra = _reflection.GeneratedProtocolMessageType('CFFra', (_message.Message,), dict(
  DESCRIPTOR = _CFFRA,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFFra)
  ))
_sym_db.RegisterMessage(CFFra)

CFOis = _reflection.GeneratedProtocolMessageType('CFOis', (_message.Message,), dict(
  DESCRIPTOR = _CFOIS,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFOis)
  ))
_sym_db.RegisterMessage(CFOis)

CFSingle = _reflection.GeneratedProtocolMessageType('CFSingle', (_message.Message,), dict(
  DESCRIPTOR = _CFSINGLE,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFSingle)
  ))
_sym_db.RegisterMessage(CFSingle)

CFStream = _reflection.GeneratedProtocolMessageType('CFStream', (_message.Message,), dict(
  DESCRIPTOR = _CFSTREAM,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFStream)
  ))
_sym_db.RegisterMessage(CFStream)

CFCollection = _reflection.GeneratedProtocolMessageType('CFCollection', (_message.Message,), dict(
  DESCRIPTOR = _CFCOLLECTION,
  __module__ = 'redukti.cashflow_pb2'
  # @@protoc_insertion_point(class_scope:redukti.CFCollection)
  ))
_sym_db.RegisterMessage(CFCollection)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
