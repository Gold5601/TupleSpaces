# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TupleSpaces_Replica_XuLiskov.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TupleSpaces_Replica_XuLiskov.proto',
  package='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"TupleSpaces_Replica_XuLiskov.proto\x12\x37pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract\"\x1e\n\nPutRequest\x12\x10\n\x08newTuple\x18\x01 \x01(\t\"\r\n\x0bPutResponse\"$\n\x0bReadRequest\x12\x15\n\rsearchPattern\x18\x01 \x01(\t\"\x1e\n\x0cReadResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"<\n\x11TakePhase1Request\x12\x15\n\rsearchPattern\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\",\n\x12TakePhase1Response\x12\x16\n\x0ereservedTuples\x18\x01 \x03(\t\",\n\x18TakePhase1ReleaseRequest\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\"\x1b\n\x19TakePhase1ReleaseResponse\"4\n\x11TakePhase2Request\x12\r\n\x05tuple\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\"\x14\n\x12TakePhase2Response\"\x1c\n\x1agetTupleSpacesStateRequest\",\n\x1bgetTupleSpacesStateResponse\x12\r\n\x05tuple\x18\x01 \x03(\t2\x8d\x08\n\x12TupleSpacesReplica\x12\x90\x01\n\x03put\x12\x43.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutRequest\x1a\x44.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutResponse\x12\x93\x01\n\x04read\x12\x44.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadRequest\x1a\x45.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadResponse\x12\xa5\x01\n\ntakePhase1\x12J.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Request\x1aK.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Response\x12\xba\x01\n\x11takePhase1Release\x12Q.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseRequest\x1aR.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseResponse\x12\xa5\x01\n\ntakePhase2\x12J.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Request\x1aK.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Response\x12\xc0\x01\n\x13getTupleSpacesState\x12S.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateRequest\x1aT.pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateResponseb\x06proto3'
)




_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='newTuple', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutRequest.newTuple', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=125,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutResponse',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=140,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchPattern', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadRequest.searchPattern', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=178,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=210,
)


_TAKEPHASE1REQUEST = _descriptor.Descriptor(
  name='TakePhase1Request',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchPattern', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Request.searchPattern', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Request.clientId', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=272,
)


_TAKEPHASE1RESPONSE = _descriptor.Descriptor(
  name='TakePhase1Response',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reservedTuples', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Response.reservedTuples', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=318,
)


_TAKEPHASE1RELEASEREQUEST = _descriptor.Descriptor(
  name='TakePhase1ReleaseRequest',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseRequest.clientId', index=0,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=364,
)


_TAKEPHASE1RELEASERESPONSE = _descriptor.Descriptor(
  name='TakePhase1ReleaseResponse',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseResponse',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=393,
)


_TAKEPHASE2REQUEST = _descriptor.Descriptor(
  name='TakePhase2Request',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuple', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Request.tuple', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Request.clientId', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=447,
)


_TAKEPHASE2RESPONSE = _descriptor.Descriptor(
  name='TakePhase2Response',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Response',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=469,
)


_GETTUPLESPACESSTATEREQUEST = _descriptor.Descriptor(
  name='getTupleSpacesStateRequest',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateRequest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=499,
)


_GETTUPLESPACESSTATERESPONSE = _descriptor.Descriptor(
  name='getTupleSpacesStateResponse',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuple', full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateResponse.tuple', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=545,
)

DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['TakePhase1Request'] = _TAKEPHASE1REQUEST
DESCRIPTOR.message_types_by_name['TakePhase1Response'] = _TAKEPHASE1RESPONSE
DESCRIPTOR.message_types_by_name['TakePhase1ReleaseRequest'] = _TAKEPHASE1RELEASEREQUEST
DESCRIPTOR.message_types_by_name['TakePhase1ReleaseResponse'] = _TAKEPHASE1RELEASERESPONSE
DESCRIPTOR.message_types_by_name['TakePhase2Request'] = _TAKEPHASE2REQUEST
DESCRIPTOR.message_types_by_name['TakePhase2Response'] = _TAKEPHASE2RESPONSE
DESCRIPTOR.message_types_by_name['getTupleSpacesStateRequest'] = _GETTUPLESPACESSTATEREQUEST
DESCRIPTOR.message_types_by_name['getTupleSpacesStateResponse'] = _GETTUPLESPACESSTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

TakePhase1Request = _reflection.GeneratedProtocolMessageType('TakePhase1Request', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE1REQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Request)
  })
_sym_db.RegisterMessage(TakePhase1Request)

TakePhase1Response = _reflection.GeneratedProtocolMessageType('TakePhase1Response', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE1RESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1Response)
  })
_sym_db.RegisterMessage(TakePhase1Response)

TakePhase1ReleaseRequest = _reflection.GeneratedProtocolMessageType('TakePhase1ReleaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE1RELEASEREQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseRequest)
  })
_sym_db.RegisterMessage(TakePhase1ReleaseRequest)

TakePhase1ReleaseResponse = _reflection.GeneratedProtocolMessageType('TakePhase1ReleaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE1RELEASERESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase1ReleaseResponse)
  })
_sym_db.RegisterMessage(TakePhase1ReleaseResponse)

TakePhase2Request = _reflection.GeneratedProtocolMessageType('TakePhase2Request', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE2REQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Request)
  })
_sym_db.RegisterMessage(TakePhase2Request)

TakePhase2Response = _reflection.GeneratedProtocolMessageType('TakePhase2Response', (_message.Message,), {
  'DESCRIPTOR' : _TAKEPHASE2RESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TakePhase2Response)
  })
_sym_db.RegisterMessage(TakePhase2Response)

getTupleSpacesStateRequest = _reflection.GeneratedProtocolMessageType('getTupleSpacesStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTUPLESPACESSTATEREQUEST,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateRequest)
  })
_sym_db.RegisterMessage(getTupleSpacesStateRequest)

getTupleSpacesStateResponse = _reflection.GeneratedProtocolMessageType('getTupleSpacesStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTUPLESPACESSTATERESPONSE,
  '__module__' : 'TupleSpaces_Replica_XuLiskov_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.getTupleSpacesStateResponse)
  })
_sym_db.RegisterMessage(getTupleSpacesStateResponse)



_TUPLESPACESREPLICA = _descriptor.ServiceDescriptor(
  name='TupleSpacesReplica',
  full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=548,
  serialized_end=1585,
  methods=[
  _descriptor.MethodDescriptor(
    name='put',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.put',
    index=0,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='read',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='takePhase1',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.takePhase1',
    index=2,
    containing_service=None,
    input_type=_TAKEPHASE1REQUEST,
    output_type=_TAKEPHASE1RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='takePhase1Release',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.takePhase1Release',
    index=3,
    containing_service=None,
    input_type=_TAKEPHASE1RELEASEREQUEST,
    output_type=_TAKEPHASE1RELEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='takePhase2',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.takePhase2',
    index=4,
    containing_service=None,
    input_type=_TAKEPHASE2REQUEST,
    output_type=_TAKEPHASE2RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getTupleSpacesState',
    full_name='pt.ulisboa.tecnico.tuplespaces.replicaXuLiskov.contract.TupleSpacesReplica.getTupleSpacesState',
    index=5,
    containing_service=None,
    input_type=_GETTUPLESPACESSTATEREQUEST,
    output_type=_GETTUPLESPACESSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TUPLESPACESREPLICA)

DESCRIPTOR.services_by_name['TupleSpacesReplica'] = _TUPLESPACESREPLICA

# @@protoc_insertion_point(module_scope)
