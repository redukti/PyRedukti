# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/calendar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from redukti import enums_pb2 as redukti_dot_enums__pb2
from redukti import shared_pb2 as redukti_dot_shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='redukti/calendar.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\x16redukti/calendar.proto\x12\x07redukti\x1a\x13redukti/enums.proto\x1a\x14redukti/shared.proto\"s\n\x17RegisterCalendarRequest\x12\x30\n\x0f\x62usiness_center\x18\x01 \x01(\x0e\x32\x17.redukti.BusinessCenter\x12\x14\n\x0cweekend_mask\x18\x02 \x01(\x05\x12\x10\n\x08holidays\x18\x03 \x03(\x05\"=\n\x15RegisterCalendarReply\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.redukti.ReplyHeaderB/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,redukti_dot_shared__pb2.DESCRIPTOR,])




_REGISTERCALENDARREQUEST = _descriptor.Descriptor(
  name='RegisterCalendarRequest',
  full_name='redukti.RegisterCalendarRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_center', full_name='redukti.RegisterCalendarRequest.business_center', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekend_mask', full_name='redukti.RegisterCalendarRequest.weekend_mask', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='holidays', full_name='redukti.RegisterCalendarRequest.holidays', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=78,
  serialized_end=193,
)


_REGISTERCALENDARREPLY = _descriptor.Descriptor(
  name='RegisterCalendarReply',
  full_name='redukti.RegisterCalendarReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='redukti.RegisterCalendarReply.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=195,
  serialized_end=256,
)

_REGISTERCALENDARREQUEST.fields_by_name['business_center'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_REGISTERCALENDARREPLY.fields_by_name['header'].message_type = redukti_dot_shared__pb2._REPLYHEADER
DESCRIPTOR.message_types_by_name['RegisterCalendarRequest'] = _REGISTERCALENDARREQUEST
DESCRIPTOR.message_types_by_name['RegisterCalendarReply'] = _REGISTERCALENDARREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterCalendarRequest = _reflection.GeneratedProtocolMessageType('RegisterCalendarRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERCALENDARREQUEST,
  __module__ = 'redukti.calendar_pb2'
  # @@protoc_insertion_point(class_scope:redukti.RegisterCalendarRequest)
  ))
_sym_db.RegisterMessage(RegisterCalendarRequest)

RegisterCalendarReply = _reflection.GeneratedProtocolMessageType('RegisterCalendarReply', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERCALENDARREPLY,
  __module__ = 'redukti.calendar_pb2'
  # @@protoc_insertion_point(class_scope:redukti.RegisterCalendarReply)
  ))
_sym_db.RegisterMessage(RegisterCalendarReply)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
