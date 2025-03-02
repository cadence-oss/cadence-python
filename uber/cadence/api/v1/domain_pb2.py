# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uber/cadence/api/v1/domain.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uber/cadence/api/v1/domain.proto',
  package='uber.cadence.api.v1',
  syntax='proto3',
  serialized_options=b'\n\027com.uber.cadence.api.v1B\010ApiProtoP\001Z/github.com/uber/cadence/.gen/proto/api/v1;apiv1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n uber/cadence/api/v1/domain.proto\x12\x13uber.cadence.api.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x82\x06\n\x06\x44omain\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x31\n\x06status\x18\x03 \x01(\x0e\x32!.uber.cadence.api.v1.DomainStatus\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bowner_email\x18\x05 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32%.uber.cadence.api.v1.Domain.DataEntry\x12\x46\n#workflow_execution_retention_period\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x36\n\x0c\x62\x61\x64_binaries\x18\x08 \x01(\x0b\x32 .uber.cadence.api.v1.BadBinaries\x12\x44\n\x17history_archival_status\x18\t \x01(\x0e\x32#.uber.cadence.api.v1.ArchivalStatus\x12\x1c\n\x14history_archival_uri\x18\n \x01(\t\x12G\n\x1avisibility_archival_status\x18\x0b \x01(\x0e\x32#.uber.cadence.api.v1.ArchivalStatus\x12\x1f\n\x17visibility_archival_uri\x18\x0c \x01(\t\x12\x1b\n\x13\x61\x63tive_cluster_name\x18\r \x01(\t\x12\x46\n\x08\x63lusters\x18\x0e \x03(\x0b\x32\x34.uber.cadence.api.v1.ClusterReplicationConfiguration\x12\x18\n\x10\x66\x61ilover_version\x18\x0f \x01(\x03\x12\x18\n\x10is_global_domain\x18\x10 \x01(\x08\x12\x38\n\rfailover_info\x18\x11 \x01(\x0b\x32!.uber.cadence.api.v1.FailoverInfo\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n\x1f\x43lusterReplicationConfiguration\x12\x14\n\x0c\x63luster_name\x18\x01 \x01(\t\"\xa4\x01\n\x0b\x42\x61\x64\x42inaries\x12@\n\x08\x62inaries\x18\x01 \x03(\x0b\x32..uber.cadence.api.v1.BadBinaries.BinariesEntry\x1aS\n\rBinariesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".uber.cadence.api.v1.BadBinaryInfo:\x02\x38\x01\"c\n\rBadBinaryInfo\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\x30\n\x0c\x63reated_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdc\x01\n\x0c\x46\x61iloverInfo\x12\x18\n\x10\x66\x61ilover_version\x18\x01 \x01(\x03\x12<\n\x18\x66\x61ilover_start_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12=\n\x19\x66\x61ilover_expire_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x15\x63ompleted_shard_count\x18\x04 \x01(\x05\x12\x16\n\x0epending_shards\x18\x05 \x03(\x05*\x80\x01\n\x0c\x44omainStatus\x12\x19\n\x15\x44OMAIN_STATUS_INVALID\x10\x00\x12\x1c\n\x18\x44OMAIN_STATUS_REGISTERED\x10\x01\x12\x1c\n\x18\x44OMAIN_STATUS_DEPRECATED\x10\x02\x12\x19\n\x15\x44OMAIN_STATUS_DELETED\x10\x03*h\n\x0e\x41rchivalStatus\x12\x1b\n\x17\x41RCHIVAL_STATUS_INVALID\x10\x00\x12\x1c\n\x18\x41RCHIVAL_STATUS_DISABLED\x10\x01\x12\x1b\n\x17\x41RCHIVAL_STATUS_ENABLED\x10\x02\x42V\n\x17\x63om.uber.cadence.api.v1B\x08\x41piProtoP\x01Z/github.com/uber/cadence/.gen/proto/api/v1;apiv1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DOMAINSTATUS = _descriptor.EnumDescriptor(
  name='DomainStatus',
  full_name='uber.cadence.api.v1.DomainStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOMAIN_STATUS_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOMAIN_STATUS_REGISTERED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOMAIN_STATUS_DEPRECATED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOMAIN_STATUS_DELETED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1444,
  serialized_end=1572,
)
_sym_db.RegisterEnumDescriptor(_DOMAINSTATUS)

DomainStatus = enum_type_wrapper.EnumTypeWrapper(_DOMAINSTATUS)
_ARCHIVALSTATUS = _descriptor.EnumDescriptor(
  name='ArchivalStatus',
  full_name='uber.cadence.api.v1.ArchivalStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARCHIVAL_STATUS_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARCHIVAL_STATUS_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARCHIVAL_STATUS_ENABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1574,
  serialized_end=1678,
)
_sym_db.RegisterEnumDescriptor(_ARCHIVALSTATUS)

ArchivalStatus = enum_type_wrapper.EnumTypeWrapper(_ARCHIVALSTATUS)
DOMAIN_STATUS_INVALID = 0
DOMAIN_STATUS_REGISTERED = 1
DOMAIN_STATUS_DEPRECATED = 2
DOMAIN_STATUS_DELETED = 3
ARCHIVAL_STATUS_INVALID = 0
ARCHIVAL_STATUS_DISABLED = 1
ARCHIVAL_STATUS_ENABLED = 2



_DOMAIN_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='uber.cadence.api.v1.Domain.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='uber.cadence.api.v1.Domain.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='uber.cadence.api.v1.Domain.DataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=893,
)

_DOMAIN = _descriptor.Descriptor(
  name='Domain',
  full_name='uber.cadence.api.v1.Domain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='uber.cadence.api.v1.Domain.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='uber.cadence.api.v1.Domain.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='uber.cadence.api.v1.Domain.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='uber.cadence.api.v1.Domain.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_email', full_name='uber.cadence.api.v1.Domain.owner_email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='uber.cadence.api.v1.Domain.data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow_execution_retention_period', full_name='uber.cadence.api.v1.Domain.workflow_execution_retention_period', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bad_binaries', full_name='uber.cadence.api.v1.Domain.bad_binaries', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='history_archival_status', full_name='uber.cadence.api.v1.Domain.history_archival_status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='history_archival_uri', full_name='uber.cadence.api.v1.Domain.history_archival_uri', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility_archival_status', full_name='uber.cadence.api.v1.Domain.visibility_archival_status', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility_archival_uri', full_name='uber.cadence.api.v1.Domain.visibility_archival_uri', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_cluster_name', full_name='uber.cadence.api.v1.Domain.active_cluster_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clusters', full_name='uber.cadence.api.v1.Domain.clusters', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failover_version', full_name='uber.cadence.api.v1.Domain.failover_version', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_global_domain', full_name='uber.cadence.api.v1.Domain.is_global_domain', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failover_info', full_name='uber.cadence.api.v1.Domain.failover_info', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOMAIN_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=893,
)


_CLUSTERREPLICATIONCONFIGURATION = _descriptor.Descriptor(
  name='ClusterReplicationConfiguration',
  full_name='uber.cadence.api.v1.ClusterReplicationConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='uber.cadence.api.v1.ClusterReplicationConfiguration.cluster_name', index=0,
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
  serialized_start=895,
  serialized_end=950,
)


_BADBINARIES_BINARIESENTRY = _descriptor.Descriptor(
  name='BinariesEntry',
  full_name='uber.cadence.api.v1.BadBinaries.BinariesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='uber.cadence.api.v1.BadBinaries.BinariesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='uber.cadence.api.v1.BadBinaries.BinariesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1034,
  serialized_end=1117,
)

_BADBINARIES = _descriptor.Descriptor(
  name='BadBinaries',
  full_name='uber.cadence.api.v1.BadBinaries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaries', full_name='uber.cadence.api.v1.BadBinaries.binaries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BADBINARIES_BINARIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=1117,
)


_BADBINARYINFO = _descriptor.Descriptor(
  name='BadBinaryInfo',
  full_name='uber.cadence.api.v1.BadBinaryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='uber.cadence.api.v1.BadBinaryInfo.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='uber.cadence.api.v1.BadBinaryInfo.operator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_time', full_name='uber.cadence.api.v1.BadBinaryInfo.created_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1119,
  serialized_end=1218,
)


_FAILOVERINFO = _descriptor.Descriptor(
  name='FailoverInfo',
  full_name='uber.cadence.api.v1.FailoverInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='failover_version', full_name='uber.cadence.api.v1.FailoverInfo.failover_version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failover_start_timestamp', full_name='uber.cadence.api.v1.FailoverInfo.failover_start_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failover_expire_timestamp', full_name='uber.cadence.api.v1.FailoverInfo.failover_expire_timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed_shard_count', full_name='uber.cadence.api.v1.FailoverInfo.completed_shard_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_shards', full_name='uber.cadence.api.v1.FailoverInfo.pending_shards', index=4,
      number=5, type=5, cpp_type=1, label=3,
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
  serialized_start=1221,
  serialized_end=1441,
)

_DOMAIN_DATAENTRY.containing_type = _DOMAIN
_DOMAIN.fields_by_name['status'].enum_type = _DOMAINSTATUS
_DOMAIN.fields_by_name['data'].message_type = _DOMAIN_DATAENTRY
_DOMAIN.fields_by_name['workflow_execution_retention_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_DOMAIN.fields_by_name['bad_binaries'].message_type = _BADBINARIES
_DOMAIN.fields_by_name['history_archival_status'].enum_type = _ARCHIVALSTATUS
_DOMAIN.fields_by_name['visibility_archival_status'].enum_type = _ARCHIVALSTATUS
_DOMAIN.fields_by_name['clusters'].message_type = _CLUSTERREPLICATIONCONFIGURATION
_DOMAIN.fields_by_name['failover_info'].message_type = _FAILOVERINFO
_BADBINARIES_BINARIESENTRY.fields_by_name['value'].message_type = _BADBINARYINFO
_BADBINARIES_BINARIESENTRY.containing_type = _BADBINARIES
_BADBINARIES.fields_by_name['binaries'].message_type = _BADBINARIES_BINARIESENTRY
_BADBINARYINFO.fields_by_name['created_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FAILOVERINFO.fields_by_name['failover_start_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FAILOVERINFO.fields_by_name['failover_expire_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Domain'] = _DOMAIN
DESCRIPTOR.message_types_by_name['ClusterReplicationConfiguration'] = _CLUSTERREPLICATIONCONFIGURATION
DESCRIPTOR.message_types_by_name['BadBinaries'] = _BADBINARIES
DESCRIPTOR.message_types_by_name['BadBinaryInfo'] = _BADBINARYINFO
DESCRIPTOR.message_types_by_name['FailoverInfo'] = _FAILOVERINFO
DESCRIPTOR.enum_types_by_name['DomainStatus'] = _DOMAINSTATUS
DESCRIPTOR.enum_types_by_name['ArchivalStatus'] = _ARCHIVALSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Domain = _reflection.GeneratedProtocolMessageType('Domain', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOMAIN_DATAENTRY,
    '__module__' : 'uber.cadence.api.v1.domain_pb2'
    # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.Domain.DataEntry)
    })
  ,
  'DESCRIPTOR' : _DOMAIN,
  '__module__' : 'uber.cadence.api.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.Domain)
  })
_sym_db.RegisterMessage(Domain)
_sym_db.RegisterMessage(Domain.DataEntry)

ClusterReplicationConfiguration = _reflection.GeneratedProtocolMessageType('ClusterReplicationConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERREPLICATIONCONFIGURATION,
  '__module__' : 'uber.cadence.api.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.ClusterReplicationConfiguration)
  })
_sym_db.RegisterMessage(ClusterReplicationConfiguration)

BadBinaries = _reflection.GeneratedProtocolMessageType('BadBinaries', (_message.Message,), {

  'BinariesEntry' : _reflection.GeneratedProtocolMessageType('BinariesEntry', (_message.Message,), {
    'DESCRIPTOR' : _BADBINARIES_BINARIESENTRY,
    '__module__' : 'uber.cadence.api.v1.domain_pb2'
    # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.BadBinaries.BinariesEntry)
    })
  ,
  'DESCRIPTOR' : _BADBINARIES,
  '__module__' : 'uber.cadence.api.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.BadBinaries)
  })
_sym_db.RegisterMessage(BadBinaries)
_sym_db.RegisterMessage(BadBinaries.BinariesEntry)

BadBinaryInfo = _reflection.GeneratedProtocolMessageType('BadBinaryInfo', (_message.Message,), {
  'DESCRIPTOR' : _BADBINARYINFO,
  '__module__' : 'uber.cadence.api.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.BadBinaryInfo)
  })
_sym_db.RegisterMessage(BadBinaryInfo)

FailoverInfo = _reflection.GeneratedProtocolMessageType('FailoverInfo', (_message.Message,), {
  'DESCRIPTOR' : _FAILOVERINFO,
  '__module__' : 'uber.cadence.api.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.FailoverInfo)
  })
_sym_db.RegisterMessage(FailoverInfo)


DESCRIPTOR._options = None
_DOMAIN_DATAENTRY._options = None
_BADBINARIES_BINARIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
