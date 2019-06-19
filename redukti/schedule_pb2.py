# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/schedule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from redukti import enums_pb2 as redukti_dot_enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='redukti/schedule.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\x16redukti/schedule.proto\x12\x07redukti\x1a\x13redukti/enums.proto\"\xaa\x06\n\x12ScheduleParameters\x12\x16\n\x0e\x65\x66\x66\x65\x63tive_date\x18\x01 \x01(\x05\x12\x18\n\x10termination_date\x18\x02 \x01(\x05\x12\x30\n\x0froll_convention\x18\x03 \x01(\x0e\x32\x17.redukti.RollConvention\x12\'\n\x1f\x66irst_regular_period_start_date\x18\x04 \x01(\x05\x12$\n\x1clast_regular_period_end_date\x18\x05 \x01(\x05\x12\x1c\n\x04term\x18\x06 \x01(\x0e\x32\x0e.redukti.Tenor\x12-\n\x15\x63\x61lculation_frequency\x18\x07 \x01(\x0e\x32\x0e.redukti.Tenor\x12)\n\x11payment_frequency\x18\x08 \x01(\x0e\x32\x0e.redukti.Tenor\x12,\n\rstub_location\x18\t \x01(\x0e\x32\x15.redukti.StubLocation\x12\x1a\n\x12\x66irst_payment_date\x18\n \x01(\x05\x12!\n\x19last_regular_payment_date\x18\x0b \x01(\x05\x12\x39\n\x11period_convention\x18\x0c \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12:\n\x12payment_convention\x18\r \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12\x13\n\x0bpayment_lag\x18\x0e \x01(\x11\x12\x31\n\x10period_calendars\x18\x0f \x03(\x0e\x32\x17.redukti.BusinessCenter\x12\x32\n\x11payment_calendars\x18\x10 \x03(\x0e\x32\x17.redukti.BusinessCenter\x12\x15\n\rex_coupon_lag\x18\x11 \x01(\x11\x12<\n\x14\x65x_coupon_convention\x18\x12 \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12\x34\n\x13\x65x_coupon_calendars\x18\x13 \x03(\x0e\x32\x17.redukti.BusinessCenter\"\xb3\x01\n\x08Schedule\x12\x16\n\x0ehas_front_stub\x18\x01 \x01(\x08\x12\x15\n\rhas_back_stub\x18\x02 \x01(\x08\x12\x1c\n\x14\x61\x64justed_start_dates\x18\x03 \x03(\x05\x12\x1a\n\x12\x61\x64justed_end_dates\x18\x04 \x03(\x05\x12\x1e\n\x16\x61\x64justed_payment_dates\x18\x05 \x03(\x05\x12\x1e\n\x16\x65x_coupon_date_offsets\x18\x06 \x03(\x11*v\n\x0cStubLocation\x12\x12\n\x0eSTUB_TYPE_AUTO\x10\x00\x12\x14\n\x10SHORT_FRONT_STUB\x10\x01\x12\x13\n\x0fLONG_FRONT_STUB\x10\x02\x12\x13\n\x0fSHORT_BACK_STUB\x10\x03\x12\x12\n\x0eLONG_BACK_STUB\x10\x04\x42/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,])

_STUBLOCATION = _descriptor.EnumDescriptor(
  name='StubLocation',
  full_name='redukti.StubLocation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STUB_TYPE_AUTO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHORT_FRONT_STUB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONG_FRONT_STUB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHORT_BACK_STUB', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONG_BACK_STUB', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1051,
  serialized_end=1169,
)
_sym_db.RegisterEnumDescriptor(_STUBLOCATION)

StubLocation = enum_type_wrapper.EnumTypeWrapper(_STUBLOCATION)
STUB_TYPE_AUTO = 0
SHORT_FRONT_STUB = 1
LONG_FRONT_STUB = 2
SHORT_BACK_STUB = 3
LONG_BACK_STUB = 4



_SCHEDULEPARAMETERS = _descriptor.Descriptor(
  name='ScheduleParameters',
  full_name='redukti.ScheduleParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_date', full_name='redukti.ScheduleParameters.effective_date', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='termination_date', full_name='redukti.ScheduleParameters.termination_date', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll_convention', full_name='redukti.ScheduleParameters.roll_convention', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_regular_period_start_date', full_name='redukti.ScheduleParameters.first_regular_period_start_date', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_regular_period_end_date', full_name='redukti.ScheduleParameters.last_regular_period_end_date', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term', full_name='redukti.ScheduleParameters.term', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculation_frequency', full_name='redukti.ScheduleParameters.calculation_frequency', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_frequency', full_name='redukti.ScheduleParameters.payment_frequency', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stub_location', full_name='redukti.ScheduleParameters.stub_location', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_payment_date', full_name='redukti.ScheduleParameters.first_payment_date', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_regular_payment_date', full_name='redukti.ScheduleParameters.last_regular_payment_date', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_convention', full_name='redukti.ScheduleParameters.period_convention', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_convention', full_name='redukti.ScheduleParameters.payment_convention', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_lag', full_name='redukti.ScheduleParameters.payment_lag', index=13,
      number=14, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_calendars', full_name='redukti.ScheduleParameters.period_calendars', index=14,
      number=15, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_calendars', full_name='redukti.ScheduleParameters.payment_calendars', index=15,
      number=16, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_lag', full_name='redukti.ScheduleParameters.ex_coupon_lag', index=16,
      number=17, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_convention', full_name='redukti.ScheduleParameters.ex_coupon_convention', index=17,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_calendars', full_name='redukti.ScheduleParameters.ex_coupon_calendars', index=18,
      number=19, type=14, cpp_type=8, label=3,
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
  serialized_start=57,
  serialized_end=867,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='redukti.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_front_stub', full_name='redukti.Schedule.has_front_stub', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_back_stub', full_name='redukti.Schedule.has_back_stub', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjusted_start_dates', full_name='redukti.Schedule.adjusted_start_dates', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjusted_end_dates', full_name='redukti.Schedule.adjusted_end_dates', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjusted_payment_dates', full_name='redukti.Schedule.adjusted_payment_dates', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ex_coupon_date_offsets', full_name='redukti.Schedule.ex_coupon_date_offsets', index=5,
      number=6, type=17, cpp_type=1, label=3,
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
  serialized_start=870,
  serialized_end=1049,
)

_SCHEDULEPARAMETERS.fields_by_name['roll_convention'].enum_type = redukti_dot_enums__pb2._ROLLCONVENTION
_SCHEDULEPARAMETERS.fields_by_name['term'].enum_type = redukti_dot_enums__pb2._TENOR
_SCHEDULEPARAMETERS.fields_by_name['calculation_frequency'].enum_type = redukti_dot_enums__pb2._TENOR
_SCHEDULEPARAMETERS.fields_by_name['payment_frequency'].enum_type = redukti_dot_enums__pb2._TENOR
_SCHEDULEPARAMETERS.fields_by_name['stub_location'].enum_type = _STUBLOCATION
_SCHEDULEPARAMETERS.fields_by_name['period_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_SCHEDULEPARAMETERS.fields_by_name['payment_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_SCHEDULEPARAMETERS.fields_by_name['period_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_SCHEDULEPARAMETERS.fields_by_name['payment_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_SCHEDULEPARAMETERS.fields_by_name['ex_coupon_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_SCHEDULEPARAMETERS.fields_by_name['ex_coupon_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
DESCRIPTOR.message_types_by_name['ScheduleParameters'] = _SCHEDULEPARAMETERS
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.enum_types_by_name['StubLocation'] = _STUBLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScheduleParameters = _reflection.GeneratedProtocolMessageType('ScheduleParameters', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULEPARAMETERS,
  __module__ = 'redukti.schedule_pb2'
  # @@protoc_insertion_point(class_scope:redukti.ScheduleParameters)
  ))
_sym_db.RegisterMessage(ScheduleParameters)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'redukti.schedule_pb2'
  # @@protoc_insertion_point(class_scope:redukti.Schedule)
  ))
_sym_db.RegisterMessage(Schedule)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)