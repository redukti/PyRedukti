# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/index.proto

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
  name='redukti/index.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\x13redukti/index.proto\x12\x07redukti\x1a\x13redukti/enums.proto\x1a\x14redukti/shared.proto\"\xb0\x06\n\x0fIndexDefinition\x12&\n\nisda_index\x18\x01 \x01(\x0e\x32\x12.redukti.IsdaIndex\x12*\n\x0cindex_family\x18\x02 \x01(\x0e\x32\x14.redukti.IndexFamily\x12#\n\x08\x63urrency\x18\x03 \x01(\x0e\x32\x11.redukti.Currency\x12\x1d\n\x05tenor\x18\x04 \x01(\x0e\x32\x0e.redukti.Tenor\x12\x12\n\nfixing_lag\x18\x05 \x01(\x05\x12-\n\x15short_tenor_threshold\x18\x06 \x01(\x0e\x32\x0e.redukti.Tenor\x12>\n\x16short_tenor_convention\x18\x07 \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12=\n\x15long_tenor_convention\x18\x08 \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12\x0b\n\x03\x65om\x18\t \x01(\x08\x12\x31\n\x10\x66ixing_calendars\x18\n \x03(\x0e\x32\x17.redukti.BusinessCenter\x12>\n\x1a\x66ixing_calendars_join_rule\x18\x0b \x01(\x0e\x32\x1a.redukti.JointCalendarRule\x12\x35\n\x14value_date_calendars\x18\x0c \x03(\x0e\x32\x17.redukti.BusinessCenter\x12\x42\n\x1evalue_date_calendars_join_rule\x18\r \x01(\x0e\x32\x1a.redukti.JointCalendarRule\x12\x30\n\x0findex_calendars\x18\x0e \x03(\x0e\x32\x17.redukti.BusinessCenter\x12=\n\x19index_calendars_join_rule\x18\x0f \x01(\x0e\x32\x1a.redukti.JointCalendarRule\x12\x35\n\x12\x64\x61y_count_fraction\x18\x10 \x01(\x0e\x32\x19.redukti.DayCountFraction\x12 \n\x18\x64\x65\x66\x61ult_for_index_family\x18\x11 \x01(\x08\"T\n\x1eRegisterIndexDefinitionRequest\x12\x32\n\x10index_definition\x18\x01 \x01(\x0b\x32\x18.redukti.IndexDefinition\"D\n\x1cRegisterIndexDefinitionReply\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.redukti.ReplyHeaderB/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,redukti_dot_shared__pb2.DESCRIPTOR,])




_INDEXDEFINITION = _descriptor.Descriptor(
  name='IndexDefinition',
  full_name='redukti.IndexDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isda_index', full_name='redukti.IndexDefinition.isda_index', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_family', full_name='redukti.IndexDefinition.index_family', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='redukti.IndexDefinition.currency', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenor', full_name='redukti.IndexDefinition.tenor', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixing_lag', full_name='redukti.IndexDefinition.fixing_lag', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_tenor_threshold', full_name='redukti.IndexDefinition.short_tenor_threshold', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_tenor_convention', full_name='redukti.IndexDefinition.short_tenor_convention', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_tenor_convention', full_name='redukti.IndexDefinition.long_tenor_convention', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eom', full_name='redukti.IndexDefinition.eom', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixing_calendars', full_name='redukti.IndexDefinition.fixing_calendars', index=9,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixing_calendars_join_rule', full_name='redukti.IndexDefinition.fixing_calendars_join_rule', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_date_calendars', full_name='redukti.IndexDefinition.value_date_calendars', index=11,
      number=12, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_date_calendars_join_rule', full_name='redukti.IndexDefinition.value_date_calendars_join_rule', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_calendars', full_name='redukti.IndexDefinition.index_calendars', index=13,
      number=14, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_calendars_join_rule', full_name='redukti.IndexDefinition.index_calendars_join_rule', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction', full_name='redukti.IndexDefinition.day_count_fraction', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_for_index_family', full_name='redukti.IndexDefinition.default_for_index_family', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=76,
  serialized_end=892,
)


_REGISTERINDEXDEFINITIONREQUEST = _descriptor.Descriptor(
  name='RegisterIndexDefinitionRequest',
  full_name='redukti.RegisterIndexDefinitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index_definition', full_name='redukti.RegisterIndexDefinitionRequest.index_definition', index=0,
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
  serialized_start=894,
  serialized_end=978,
)


_REGISTERINDEXDEFINITIONREPLY = _descriptor.Descriptor(
  name='RegisterIndexDefinitionReply',
  full_name='redukti.RegisterIndexDefinitionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='redukti.RegisterIndexDefinitionReply.header', index=0,
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
  serialized_start=980,
  serialized_end=1048,
)

_INDEXDEFINITION.fields_by_name['isda_index'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_INDEXDEFINITION.fields_by_name['index_family'].enum_type = redukti_dot_enums__pb2._INDEXFAMILY
_INDEXDEFINITION.fields_by_name['currency'].enum_type = redukti_dot_enums__pb2._CURRENCY
_INDEXDEFINITION.fields_by_name['tenor'].enum_type = redukti_dot_enums__pb2._TENOR
_INDEXDEFINITION.fields_by_name['short_tenor_threshold'].enum_type = redukti_dot_enums__pb2._TENOR
_INDEXDEFINITION.fields_by_name['short_tenor_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_INDEXDEFINITION.fields_by_name['long_tenor_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_INDEXDEFINITION.fields_by_name['fixing_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_INDEXDEFINITION.fields_by_name['fixing_calendars_join_rule'].enum_type = redukti_dot_enums__pb2._JOINTCALENDARRULE
_INDEXDEFINITION.fields_by_name['value_date_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_INDEXDEFINITION.fields_by_name['value_date_calendars_join_rule'].enum_type = redukti_dot_enums__pb2._JOINTCALENDARRULE
_INDEXDEFINITION.fields_by_name['index_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_INDEXDEFINITION.fields_by_name['index_calendars_join_rule'].enum_type = redukti_dot_enums__pb2._JOINTCALENDARRULE
_INDEXDEFINITION.fields_by_name['day_count_fraction'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_REGISTERINDEXDEFINITIONREQUEST.fields_by_name['index_definition'].message_type = _INDEXDEFINITION
_REGISTERINDEXDEFINITIONREPLY.fields_by_name['header'].message_type = redukti_dot_shared__pb2._REPLYHEADER
DESCRIPTOR.message_types_by_name['IndexDefinition'] = _INDEXDEFINITION
DESCRIPTOR.message_types_by_name['RegisterIndexDefinitionRequest'] = _REGISTERINDEXDEFINITIONREQUEST
DESCRIPTOR.message_types_by_name['RegisterIndexDefinitionReply'] = _REGISTERINDEXDEFINITIONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndexDefinition = _reflection.GeneratedProtocolMessageType('IndexDefinition', (_message.Message,), dict(
  DESCRIPTOR = _INDEXDEFINITION,
  __module__ = 'redukti.index_pb2'
  # @@protoc_insertion_point(class_scope:redukti.IndexDefinition)
  ))
_sym_db.RegisterMessage(IndexDefinition)

RegisterIndexDefinitionRequest = _reflection.GeneratedProtocolMessageType('RegisterIndexDefinitionRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERINDEXDEFINITIONREQUEST,
  __module__ = 'redukti.index_pb2'
  # @@protoc_insertion_point(class_scope:redukti.RegisterIndexDefinitionRequest)
  ))
_sym_db.RegisterMessage(RegisterIndexDefinitionRequest)

RegisterIndexDefinitionReply = _reflection.GeneratedProtocolMessageType('RegisterIndexDefinitionReply', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERINDEXDEFINITIONREPLY,
  __module__ = 'redukti.index_pb2'
  # @@protoc_insertion_point(class_scope:redukti.RegisterIndexDefinitionReply)
  ))
_sym_db.RegisterMessage(RegisterIndexDefinitionReply)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
