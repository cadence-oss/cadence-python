# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uber/cadence/api/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uber.cadence.api.v1 import common_pb2 as uber_dot_cadence_dot_api_dot_v1_dot_common__pb2
from uber.cadence.api.v1 import workflow_pb2 as uber_dot_cadence_dot_api_dot_v1_dot_workflow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uber/cadence/api/v1/query.proto',
  package='uber.cadence.api.v1',
  syntax='proto3',
  serialized_options=b'\n\027com.uber.cadence.api.v1B\010ApiProtoP\001Z/github.com/uber/cadence/.gen/proto/api/v1;apiv1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fuber/cadence/api/v1/query.proto\x12\x13uber.cadence.api.v1\x1a uber/cadence/api/v1/common.proto\x1a\"uber/cadence/api/v1/workflow.proto\"U\n\rWorkflowQuery\x12\x12\n\nquery_type\x18\x01 \x01(\t\x12\x30\n\nquery_args\x18\x02 \x01(\x0b\x32\x1c.uber.cadence.api.v1.Payload\"\x95\x01\n\x13WorkflowQueryResult\x12\x39\n\x0bresult_type\x18\x01 \x01(\x0e\x32$.uber.cadence.api.v1.QueryResultType\x12,\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x1c.uber.cadence.api.v1.Payload\x12\x15\n\rerror_message\x18\x03 \x01(\t\"X\n\rQueryRejected\x12G\n\x0c\x63lose_status\x18\x01 \x01(\x0e\x32\x31.uber.cadence.api.v1.WorkflowExecutionCloseStatus*n\n\x0fQueryResultType\x12\x1d\n\x19QUERY_RESULT_TYPE_INVALID\x10\x00\x12\x1e\n\x1aQUERY_RESULT_TYPE_ANSWERED\x10\x01\x12\x1c\n\x18QUERY_RESULT_TYPE_FAILED\x10\x02*\x91\x01\n\x14QueryRejectCondition\x12\"\n\x1eQUERY_REJECT_CONDITION_INVALID\x10\x00\x12#\n\x1fQUERY_REJECT_CONDITION_NOT_OPEN\x10\x01\x12\x30\n,QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY\x10\x02*\x86\x01\n\x15QueryConsistencyLevel\x12#\n\x1fQUERY_CONSISTENCY_LEVEL_INVALID\x10\x00\x12$\n QUERY_CONSISTENCY_LEVEL_EVENTUAL\x10\x01\x12\"\n\x1eQUERY_CONSISTENCY_LEVEL_STRONG\x10\x02\x42V\n\x17\x63om.uber.cadence.api.v1B\x08\x41piProtoP\x01Z/github.com/uber/cadence/.gen/proto/api/v1;apiv1b\x06proto3'
  ,
  dependencies=[uber_dot_cadence_dot_api_dot_v1_dot_common__pb2.DESCRIPTOR,uber_dot_cadence_dot_api_dot_v1_dot_workflow__pb2.DESCRIPTOR,])

_QUERYRESULTTYPE = _descriptor.EnumDescriptor(
  name='QueryResultType',
  full_name='uber.cadence.api.v1.QueryResultType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_ANSWERED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=455,
  serialized_end=565,
)
_sym_db.RegisterEnumDescriptor(_QUERYRESULTTYPE)

QueryResultType = enum_type_wrapper.EnumTypeWrapper(_QUERYRESULTTYPE)
_QUERYREJECTCONDITION = _descriptor.EnumDescriptor(
  name='QueryRejectCondition',
  full_name='uber.cadence.api.v1.QueryRejectCondition',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_NOT_OPEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=568,
  serialized_end=713,
)
_sym_db.RegisterEnumDescriptor(_QUERYREJECTCONDITION)

QueryRejectCondition = enum_type_wrapper.EnumTypeWrapper(_QUERYREJECTCONDITION)
_QUERYCONSISTENCYLEVEL = _descriptor.EnumDescriptor(
  name='QueryConsistencyLevel',
  full_name='uber.cadence.api.v1.QueryConsistencyLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_EVENTUAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_STRONG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=716,
  serialized_end=850,
)
_sym_db.RegisterEnumDescriptor(_QUERYCONSISTENCYLEVEL)

QueryConsistencyLevel = enum_type_wrapper.EnumTypeWrapper(_QUERYCONSISTENCYLEVEL)
QUERY_RESULT_TYPE_INVALID = 0
QUERY_RESULT_TYPE_ANSWERED = 1
QUERY_RESULT_TYPE_FAILED = 2
QUERY_REJECT_CONDITION_INVALID = 0
QUERY_REJECT_CONDITION_NOT_OPEN = 1
QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY = 2
QUERY_CONSISTENCY_LEVEL_INVALID = 0
QUERY_CONSISTENCY_LEVEL_EVENTUAL = 1
QUERY_CONSISTENCY_LEVEL_STRONG = 2



_WORKFLOWQUERY = _descriptor.Descriptor(
  name='WorkflowQuery',
  full_name='uber.cadence.api.v1.WorkflowQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_type', full_name='uber.cadence.api.v1.WorkflowQuery.query_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_args', full_name='uber.cadence.api.v1.WorkflowQuery.query_args', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=211,
)


_WORKFLOWQUERYRESULT = _descriptor.Descriptor(
  name='WorkflowQueryResult',
  full_name='uber.cadence.api.v1.WorkflowQueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_type', full_name='uber.cadence.api.v1.WorkflowQueryResult.result_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer', full_name='uber.cadence.api.v1.WorkflowQueryResult.answer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='uber.cadence.api.v1.WorkflowQueryResult.error_message', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=363,
)


_QUERYREJECTED = _descriptor.Descriptor(
  name='QueryRejected',
  full_name='uber.cadence.api.v1.QueryRejected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='close_status', full_name='uber.cadence.api.v1.QueryRejected.close_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=365,
  serialized_end=453,
)

_WORKFLOWQUERY.fields_by_name['query_args'].message_type = uber_dot_cadence_dot_api_dot_v1_dot_common__pb2._PAYLOAD
_WORKFLOWQUERYRESULT.fields_by_name['result_type'].enum_type = _QUERYRESULTTYPE
_WORKFLOWQUERYRESULT.fields_by_name['answer'].message_type = uber_dot_cadence_dot_api_dot_v1_dot_common__pb2._PAYLOAD
_QUERYREJECTED.fields_by_name['close_status'].enum_type = uber_dot_cadence_dot_api_dot_v1_dot_workflow__pb2._WORKFLOWEXECUTIONCLOSESTATUS
DESCRIPTOR.message_types_by_name['WorkflowQuery'] = _WORKFLOWQUERY
DESCRIPTOR.message_types_by_name['WorkflowQueryResult'] = _WORKFLOWQUERYRESULT
DESCRIPTOR.message_types_by_name['QueryRejected'] = _QUERYREJECTED
DESCRIPTOR.enum_types_by_name['QueryResultType'] = _QUERYRESULTTYPE
DESCRIPTOR.enum_types_by_name['QueryRejectCondition'] = _QUERYREJECTCONDITION
DESCRIPTOR.enum_types_by_name['QueryConsistencyLevel'] = _QUERYCONSISTENCYLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkflowQuery = _reflection.GeneratedProtocolMessageType('WorkflowQuery', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWQUERY,
  '__module__' : 'uber.cadence.api.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.WorkflowQuery)
  })
_sym_db.RegisterMessage(WorkflowQuery)

WorkflowQueryResult = _reflection.GeneratedProtocolMessageType('WorkflowQueryResult', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWQUERYRESULT,
  '__module__' : 'uber.cadence.api.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.WorkflowQueryResult)
  })
_sym_db.RegisterMessage(WorkflowQueryResult)

QueryRejected = _reflection.GeneratedProtocolMessageType('QueryRejected', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREJECTED,
  '__module__' : 'uber.cadence.api.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:uber.cadence.api.v1.QueryRejected)
  })
_sym_db.RegisterMessage(QueryRejected)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
