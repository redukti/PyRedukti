# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redukti/instrument_templates.proto

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
  name='redukti/instrument_templates.proto',
  package='redukti',
  syntax='proto3',
  serialized_options=_b('\n\021com.redukti.typesB\005TypesP\001\370\001\001\252\002\rRedukti.Types'),
  serialized_pb=_b('\n\"redukti/instrument_templates.proto\x12\x07redukti\x1a\x13redukti/enums.proto\"\xf6\x06\n\x12InstrumentTemplate\x12\x31\n\x10product_sub_type\x18\x01 \x01(\x0e\x32\x17.redukti.ProductSubType\x12#\n\x08\x63urrency\x18\x02 \x01(\x0e\x32\x11.redukti.Currency\x12\x32\n\x11payment_calendars\x18\x03 \x03(\x0e\x32\x17.redukti.BusinessCenter\x12*\n\x12payment_frequency1\x18\x04 \x01(\x0e\x32\x0e.redukti.Tenor\x12*\n\x12payment_frequency2\x18\x05 \x01(\x0e\x32\x0e.redukti.Tenor\x12\x36\n\x13\x64\x61y_count_fraction1\x18\x06 \x01(\x0e\x32\x19.redukti.DayCountFraction\x12\x36\n\x13\x64\x61y_count_fraction2\x18\x07 \x01(\x0e\x32\x19.redukti.DayCountFraction\x12>\n\x16payment_day_convention\x18\x08 \x01(\x0e\x32\x1e.redukti.BusinessDayConvention\x12+\n\x0f\x66loating_index1\x18\t \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\'\n\x0f\x66loating_tenor1\x18\n \x01(\x0e\x32\x0e.redukti.Tenor\x12+\n\x0f\x66loating_index2\x18\x0b \x01(\x0e\x32\x12.redukti.IsdaIndex\x12\'\n\x0f\x66loating_tenor2\x18\x0c \x01(\x0e\x32\x0e.redukti.Tenor\x12<\n\x1e\x66ixed_discounting_index_family\x18\r \x01(\x0e\x32\x14.redukti.IndexFamily\x12\x37\n\x13\x63ompounding_method1\x18\x0e \x01(\x0e\x32\x1a.redukti.CompoundingMethod\x12\x37\n\x13\x63ompounding_method2\x18\x0f \x01(\x0e\x32\x1a.redukti.CompoundingMethod\x12\x37\n\x1freset_frequency_if_compounding1\x18\x10 \x01(\x0e\x32\x0e.redukti.Tenor\x12\x37\n\x1freset_frequency_if_compounding2\x18\x11 \x01(\x0e\x32\x0e.redukti.TenorB/\n\x11\x63om.redukti.typesB\x05TypesP\x01\xf8\x01\x01\xaa\x02\rRedukti.Typesb\x06proto3')
  ,
  dependencies=[redukti_dot_enums__pb2.DESCRIPTOR,])




_INSTRUMENTTEMPLATE = _descriptor.Descriptor(
  name='InstrumentTemplate',
  full_name='redukti.InstrumentTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_sub_type', full_name='redukti.InstrumentTemplate.product_sub_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='redukti.InstrumentTemplate.currency', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_calendars', full_name='redukti.InstrumentTemplate.payment_calendars', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_frequency1', full_name='redukti.InstrumentTemplate.payment_frequency1', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_frequency2', full_name='redukti.InstrumentTemplate.payment_frequency2', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction1', full_name='redukti.InstrumentTemplate.day_count_fraction1', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_count_fraction2', full_name='redukti.InstrumentTemplate.day_count_fraction2', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_day_convention', full_name='redukti.InstrumentTemplate.payment_day_convention', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_index1', full_name='redukti.InstrumentTemplate.floating_index1', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_tenor1', full_name='redukti.InstrumentTemplate.floating_tenor1', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_index2', full_name='redukti.InstrumentTemplate.floating_index2', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floating_tenor2', full_name='redukti.InstrumentTemplate.floating_tenor2', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_discounting_index_family', full_name='redukti.InstrumentTemplate.fixed_discounting_index_family', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compounding_method1', full_name='redukti.InstrumentTemplate.compounding_method1', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compounding_method2', full_name='redukti.InstrumentTemplate.compounding_method2', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_frequency_if_compounding1', full_name='redukti.InstrumentTemplate.reset_frequency_if_compounding1', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_frequency_if_compounding2', full_name='redukti.InstrumentTemplate.reset_frequency_if_compounding2', index=16,
      number=17, type=14, cpp_type=8, label=1,
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
  serialized_start=69,
  serialized_end=955,
)

_INSTRUMENTTEMPLATE.fields_by_name['product_sub_type'].enum_type = redukti_dot_enums__pb2._PRODUCTSUBTYPE
_INSTRUMENTTEMPLATE.fields_by_name['currency'].enum_type = redukti_dot_enums__pb2._CURRENCY
_INSTRUMENTTEMPLATE.fields_by_name['payment_calendars'].enum_type = redukti_dot_enums__pb2._BUSINESSCENTER
_INSTRUMENTTEMPLATE.fields_by_name['payment_frequency1'].enum_type = redukti_dot_enums__pb2._TENOR
_INSTRUMENTTEMPLATE.fields_by_name['payment_frequency2'].enum_type = redukti_dot_enums__pb2._TENOR
_INSTRUMENTTEMPLATE.fields_by_name['day_count_fraction1'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_INSTRUMENTTEMPLATE.fields_by_name['day_count_fraction2'].enum_type = redukti_dot_enums__pb2._DAYCOUNTFRACTION
_INSTRUMENTTEMPLATE.fields_by_name['payment_day_convention'].enum_type = redukti_dot_enums__pb2._BUSINESSDAYCONVENTION
_INSTRUMENTTEMPLATE.fields_by_name['floating_index1'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_INSTRUMENTTEMPLATE.fields_by_name['floating_tenor1'].enum_type = redukti_dot_enums__pb2._TENOR
_INSTRUMENTTEMPLATE.fields_by_name['floating_index2'].enum_type = redukti_dot_enums__pb2._ISDAINDEX
_INSTRUMENTTEMPLATE.fields_by_name['floating_tenor2'].enum_type = redukti_dot_enums__pb2._TENOR
_INSTRUMENTTEMPLATE.fields_by_name['fixed_discounting_index_family'].enum_type = redukti_dot_enums__pb2._INDEXFAMILY
_INSTRUMENTTEMPLATE.fields_by_name['compounding_method1'].enum_type = redukti_dot_enums__pb2._COMPOUNDINGMETHOD
_INSTRUMENTTEMPLATE.fields_by_name['compounding_method2'].enum_type = redukti_dot_enums__pb2._COMPOUNDINGMETHOD
_INSTRUMENTTEMPLATE.fields_by_name['reset_frequency_if_compounding1'].enum_type = redukti_dot_enums__pb2._TENOR
_INSTRUMENTTEMPLATE.fields_by_name['reset_frequency_if_compounding2'].enum_type = redukti_dot_enums__pb2._TENOR
DESCRIPTOR.message_types_by_name['InstrumentTemplate'] = _INSTRUMENTTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstrumentTemplate = _reflection.GeneratedProtocolMessageType('InstrumentTemplate', (_message.Message,), dict(
  DESCRIPTOR = _INSTRUMENTTEMPLATE,
  __module__ = 'redukti.instrument_templates_pb2'
  # @@protoc_insertion_point(class_scope:redukti.InstrumentTemplate)
  ))
_sym_db.RegisterMessage(InstrumentTemplate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
