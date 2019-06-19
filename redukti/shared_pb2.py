# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/shared.proto

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
  name='redukti/shared.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\x14redukti/shared.proto\x12\x07redukti\x1a\x13redukti/enums.proto\"x\n\x0bReplyHeader\x12\x34\n\rresponse_code\x18\x01 \x01(\x0e\x32\x1d.redukti.StandardResponseCode\x12\x18\n\x10response_message\x18\x02 \x01(\t\x12\x19\n\x11response_sub_code\x18\x03 \x01(\x05\x42/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,])




_REPLYHEADER = _descriptor.Descriptor(
  name='ReplyHeader',
  full_name='redukti.ReplyHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_code', full_name='redukti.ReplyHeader.response_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_message', full_name='redukti.ReplyHeader.response_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_sub_code', full_name='redukti.ReplyHeader.response_sub_code', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=54,
  serialized_end=174,
)

_REPLYHEADER.fields_by_name['response_code'].enum_type = redukti_dot_enums__pb2._STANDARDRESPONSECODE
DESCRIPTOR.message_types_by_name['ReplyHeader'] = _REPLYHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReplyHeader = _reflection.GeneratedProtocolMessageType('ReplyHeader', (_message.Message,), dict(
  DESCRIPTOR = _REPLYHEADER,
  __module__ = 'redukti.shared_pb2'
  # @@protoc_insertion_point(class_scope:redukti.ReplyHeader)
  ))
_sym_db.RegisterMessage(ReplyHeader)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)