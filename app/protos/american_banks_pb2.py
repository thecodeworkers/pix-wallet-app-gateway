# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: american_banks.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='american_banks.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61merican_banks.proto\"\x13\n\x11\x41mericanBankEmpty\"#\n\x15\x41mericanBankIdRequest\x12\n\n\x02id\x18\x01 \x02(\t\"\xdc\x01\n\x18\x41mericanBankNotIdRequest\x12\x15\n\rroutingNumber\x18\x01 \x02(\t\x12\x10\n\x08\x62\x61nkName\x18\x02 \x02(\t\x12\x10\n\x08\x66ullName\x18\x03 \x02(\t\x12\r\n\x05swift\x18\x04 \x02(\t\x12\x15\n\rnumberAccount\x18\x05 \x02(\t\x12,\n\x04type\x18\x06 \x02(\x0e\x32\x1e.AmericanBankNotIdRequest.Type\x12\x10\n\x08\x63urrency\x18\x07 \x02(\t\"\x1f\n\x04Type\x12\n\n\x06saving\x10\x00\x12\x0b\n\x07\x63urrent\x10\x01\"\xde\x01\n\x13\x41mericanBankRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x15\n\rroutingNumber\x18\x02 \x02(\t\x12\x10\n\x08\x62\x61nkName\x18\x03 \x02(\t\x12\x10\n\x08\x66ullName\x18\x04 \x02(\t\x12\r\n\x05swift\x18\x05 \x02(\t\x12\x15\n\rnumberAccount\x18\x06 \x02(\t\x12\'\n\x04type\x18\x07 \x02(\x0e\x32\x19.AmericanBankRequest.Type\x12\x10\n\x08\x63urrency\x18\x08 \x02(\t\"\x1f\n\x04Type\x12\n\n\x06saving\x10\x00\x12\x0b\n\x07\x63urrent\x10\x01\"O\n\x19\x41mericanBanksTableRequest\x12\x0c\n\x04page\x18\x01 \x02(\x05\x12\x14\n\x08per_page\x18\x02 \x01(\x05:\x02\x31\x35\x12\x0e\n\x06search\x18\x03 \x01(\t\"?\n\x15\x41mericanBanksResponse\x12&\n\x08\x61merican\x18\x01 \x02(\x0b\x32\x14.AmericanBankRequest\"G\n\x1d\x41mericanBanksMultipleResponse\x12&\n\x08\x61merican\x18\x01 \x03(\x0b\x32\x14.AmericanBankRequest\"\x89\x01\n\x1a\x41mericanBanksTableResponse\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.AmericanBankRequest\x12\x0c\n\x04page\x18\x02 \x02(\x05\x12\x10\n\x08per_page\x18\x03 \x02(\x05\x12\x13\n\x0btotal_items\x18\x04 \x02(\x05\x12\x11\n\tnum_pages\x18\x05 \x02(\x05\x32\xf4\x02\n\rAmericanBanks\x12@\n\x05table\x12\x1a.AmericanBanksTableRequest\x1a\x1b.AmericanBanksTableResponse\x12=\n\x07get_all\x12\x12.AmericanBankEmpty\x1a\x1e.AmericanBanksMultipleResponse\x12\x35\n\x03get\x12\x16.AmericanBankIdRequest\x1a\x16.AmericanBanksResponse\x12\x39\n\x04save\x12\x19.AmericanBankNotIdRequest\x1a\x16.AmericanBanksResponse\x12\x36\n\x06update\x12\x14.AmericanBankRequest\x1a\x16.AmericanBanksResponse\x12\x38\n\x06\x64\x65lete\x12\x16.AmericanBankIdRequest\x1a\x16.AmericanBanksResponse'
)



_AMERICANBANKNOTIDREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='AmericanBankNotIdRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='saving', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='current', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=272,
  serialized_end=303,
)
_sym_db.RegisterEnumDescriptor(_AMERICANBANKNOTIDREQUEST_TYPE)

_AMERICANBANKREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='AmericanBankRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='saving', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='current', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=272,
  serialized_end=303,
)
_sym_db.RegisterEnumDescriptor(_AMERICANBANKREQUEST_TYPE)


_AMERICANBANKEMPTY = _descriptor.Descriptor(
  name='AmericanBankEmpty',
  full_name='AmericanBankEmpty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=43,
)


_AMERICANBANKIDREQUEST = _descriptor.Descriptor(
  name='AmericanBankIdRequest',
  full_name='AmericanBankIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AmericanBankIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=80,
)


_AMERICANBANKNOTIDREQUEST = _descriptor.Descriptor(
  name='AmericanBankNotIdRequest',
  full_name='AmericanBankNotIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='routingNumber', full_name='AmericanBankNotIdRequest.routingNumber', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bankName', full_name='AmericanBankNotIdRequest.bankName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fullName', full_name='AmericanBankNotIdRequest.fullName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swift', full_name='AmericanBankNotIdRequest.swift', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numberAccount', full_name='AmericanBankNotIdRequest.numberAccount', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='AmericanBankNotIdRequest.type', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='AmericanBankNotIdRequest.currency', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AMERICANBANKNOTIDREQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=303,
)


_AMERICANBANKREQUEST = _descriptor.Descriptor(
  name='AmericanBankRequest',
  full_name='AmericanBankRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AmericanBankRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routingNumber', full_name='AmericanBankRequest.routingNumber', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bankName', full_name='AmericanBankRequest.bankName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fullName', full_name='AmericanBankRequest.fullName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swift', full_name='AmericanBankRequest.swift', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numberAccount', full_name='AmericanBankRequest.numberAccount', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='AmericanBankRequest.type', index=6,
      number=7, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='AmericanBankRequest.currency', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AMERICANBANKREQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=528,
)


_AMERICANBANKSTABLEREQUEST = _descriptor.Descriptor(
  name='AmericanBanksTableRequest',
  full_name='AmericanBanksTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='AmericanBanksTableRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='AmericanBanksTableRequest.per_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='AmericanBanksTableRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=609,
)


_AMERICANBANKSRESPONSE = _descriptor.Descriptor(
  name='AmericanBanksResponse',
  full_name='AmericanBanksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='american', full_name='AmericanBanksResponse.american', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=674,
)


_AMERICANBANKSMULTIPLERESPONSE = _descriptor.Descriptor(
  name='AmericanBanksMultipleResponse',
  full_name='AmericanBanksMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='american', full_name='AmericanBanksMultipleResponse.american', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=676,
  serialized_end=747,
)


_AMERICANBANKSTABLERESPONSE = _descriptor.Descriptor(
  name='AmericanBanksTableResponse',
  full_name='AmericanBanksTableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='AmericanBanksTableResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='AmericanBanksTableResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='AmericanBanksTableResponse.per_page', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_items', full_name='AmericanBanksTableResponse.total_items', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_pages', full_name='AmericanBanksTableResponse.num_pages', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=887,
)

_AMERICANBANKNOTIDREQUEST.fields_by_name['type'].enum_type = _AMERICANBANKNOTIDREQUEST_TYPE
_AMERICANBANKNOTIDREQUEST_TYPE.containing_type = _AMERICANBANKNOTIDREQUEST
_AMERICANBANKREQUEST.fields_by_name['type'].enum_type = _AMERICANBANKREQUEST_TYPE
_AMERICANBANKREQUEST_TYPE.containing_type = _AMERICANBANKREQUEST
_AMERICANBANKSRESPONSE.fields_by_name['american'].message_type = _AMERICANBANKREQUEST
_AMERICANBANKSMULTIPLERESPONSE.fields_by_name['american'].message_type = _AMERICANBANKREQUEST
_AMERICANBANKSTABLERESPONSE.fields_by_name['items'].message_type = _AMERICANBANKREQUEST
DESCRIPTOR.message_types_by_name['AmericanBankEmpty'] = _AMERICANBANKEMPTY
DESCRIPTOR.message_types_by_name['AmericanBankIdRequest'] = _AMERICANBANKIDREQUEST
DESCRIPTOR.message_types_by_name['AmericanBankNotIdRequest'] = _AMERICANBANKNOTIDREQUEST
DESCRIPTOR.message_types_by_name['AmericanBankRequest'] = _AMERICANBANKREQUEST
DESCRIPTOR.message_types_by_name['AmericanBanksTableRequest'] = _AMERICANBANKSTABLEREQUEST
DESCRIPTOR.message_types_by_name['AmericanBanksResponse'] = _AMERICANBANKSRESPONSE
DESCRIPTOR.message_types_by_name['AmericanBanksMultipleResponse'] = _AMERICANBANKSMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['AmericanBanksTableResponse'] = _AMERICANBANKSTABLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AmericanBankEmpty = _reflection.GeneratedProtocolMessageType('AmericanBankEmpty', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKEMPTY,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBankEmpty)
  })
_sym_db.RegisterMessage(AmericanBankEmpty)

AmericanBankIdRequest = _reflection.GeneratedProtocolMessageType('AmericanBankIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKIDREQUEST,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBankIdRequest)
  })
_sym_db.RegisterMessage(AmericanBankIdRequest)

AmericanBankNotIdRequest = _reflection.GeneratedProtocolMessageType('AmericanBankNotIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKNOTIDREQUEST,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBankNotIdRequest)
  })
_sym_db.RegisterMessage(AmericanBankNotIdRequest)

AmericanBankRequest = _reflection.GeneratedProtocolMessageType('AmericanBankRequest', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKREQUEST,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBankRequest)
  })
_sym_db.RegisterMessage(AmericanBankRequest)

AmericanBanksTableRequest = _reflection.GeneratedProtocolMessageType('AmericanBanksTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKSTABLEREQUEST,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBanksTableRequest)
  })
_sym_db.RegisterMessage(AmericanBanksTableRequest)

AmericanBanksResponse = _reflection.GeneratedProtocolMessageType('AmericanBanksResponse', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKSRESPONSE,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBanksResponse)
  })
_sym_db.RegisterMessage(AmericanBanksResponse)

AmericanBanksMultipleResponse = _reflection.GeneratedProtocolMessageType('AmericanBanksMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKSMULTIPLERESPONSE,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBanksMultipleResponse)
  })
_sym_db.RegisterMessage(AmericanBanksMultipleResponse)

AmericanBanksTableResponse = _reflection.GeneratedProtocolMessageType('AmericanBanksTableResponse', (_message.Message,), {
  'DESCRIPTOR' : _AMERICANBANKSTABLERESPONSE,
  '__module__' : 'american_banks_pb2'
  # @@protoc_insertion_point(class_scope:AmericanBanksTableResponse)
  })
_sym_db.RegisterMessage(AmericanBanksTableResponse)



_AMERICANBANKS = _descriptor.ServiceDescriptor(
  name='AmericanBanks',
  full_name='AmericanBanks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=890,
  serialized_end=1262,
  methods=[
  _descriptor.MethodDescriptor(
    name='table',
    full_name='AmericanBanks.table',
    index=0,
    containing_service=None,
    input_type=_AMERICANBANKSTABLEREQUEST,
    output_type=_AMERICANBANKSTABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='AmericanBanks.get_all',
    index=1,
    containing_service=None,
    input_type=_AMERICANBANKEMPTY,
    output_type=_AMERICANBANKSMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='AmericanBanks.get',
    index=2,
    containing_service=None,
    input_type=_AMERICANBANKIDREQUEST,
    output_type=_AMERICANBANKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='save',
    full_name='AmericanBanks.save',
    index=3,
    containing_service=None,
    input_type=_AMERICANBANKNOTIDREQUEST,
    output_type=_AMERICANBANKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='AmericanBanks.update',
    index=4,
    containing_service=None,
    input_type=_AMERICANBANKREQUEST,
    output_type=_AMERICANBANKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='AmericanBanks.delete',
    index=5,
    containing_service=None,
    input_type=_AMERICANBANKIDREQUEST,
    output_type=_AMERICANBANKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AMERICANBANKS)

DESCRIPTOR.services_by_name['AmericanBanks'] = _AMERICANBANKS

# @@protoc_insertion_point(module_scope)
