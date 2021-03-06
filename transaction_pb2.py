# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='transactions',
  syntax='proto3',
  serialized_pb=_b('\n\x11transaction.proto\x12\x0ctransactions\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\t\")\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x32\xea\x01\n\x0cTransactions\x12?\n\x0eGetTransaction\x12\x10.transactions.Id\x1a\x19.transactions.Transaction\"\x00\x12L\n\x10ListTransactions\x12\x19.transactions.Transaction\x1a\x19.transactions.Transaction\"\x00\x30\x01\x12K\n\x11\x43reateTransaction\x12\x19.transactions.Transaction\x1a\x19.transactions.Transaction\"\x00\x42/\n\x13\x63onnor.transactionsB\x11TransactionsProtoP\x01\xa2\x02\x02TPb\x06proto3')
)




_ID = _descriptor.Descriptor(
  name='Id',
  full_name='transactions.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='transactions.Id.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=51,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='transactions.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='transactions.Transaction.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transactions.Transaction.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transactions.Id)
  ))
_sym_db.RegisterMessage(Id)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transactions.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023connor.transactionsB\021TransactionsProtoP\001\242\002\002TP'))

_TRANSACTIONS = _descriptor.ServiceDescriptor(
  name='Transactions',
  full_name='transactions.Transactions',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=97,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTransaction',
    full_name='transactions.Transactions.GetTransaction',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_TRANSACTION,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTransactions',
    full_name='transactions.Transactions.ListTransactions',
    index=1,
    containing_service=None,
    input_type=_TRANSACTION,
    output_type=_TRANSACTION,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTransaction',
    full_name='transactions.Transactions.CreateTransaction',
    index=2,
    containing_service=None,
    input_type=_TRANSACTION,
    output_type=_TRANSACTION,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTIONS)

DESCRIPTOR.services_by_name['Transactions'] = _TRANSACTIONS

# @@protoc_insertion_point(module_scope)
