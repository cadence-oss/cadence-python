"""
Will delete after modeling all the fields

message StartWorkflowExecutionRequest {
  string domain = 1;
  string workflow_id = 2;
  WorkflowType workflow_type = 3;
  TaskList task_list = 4;
  Payload input = 5;
  google.protobuf.Duration execution_start_to_close_timeout = 6;
  google.protobuf.Duration task_start_to_close_timeout = 7;
  string identity = 8;
  string request_id = 9;
  WorkflowIdReusePolicy workflow_id_reuse_policy = 10;
  RetryPolicy retry_policy = 11;
  string cron_schedule = 12;
  Memo memo = 13;
  SearchAttributes search_attributes = 14;
  Header header = 15;
  google.protobuf.Duration delay_start = 16;
}
"""
from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind, \
    WorkflowIdReusePolicy, RetryPolicy, Memo, SearchAttributes, Header
from google.protobuf import duration_pb2
from uber.cadence.api.v1 import service_workflow_pb2, common_pb2, tasklist_pb2, workflow_pb2


def start_workflow_execution_request_dataclass_to_proto(
        request: StartWorkflowExecutionRequest) -> service_workflow_pb2.StartWorkflowExecutionRequest:
    return service_workflow_pb2.StartWorkflowExecutionRequest(
        domain=request.domain,
        workflow_id=request.workflow_id,
        workflow_type=workflow_type_dataclass_to_proto(request.workflow_type),
        task_list=task_list_to_proto(request.task_list),
        input=payload_to_proto(request.input),
        execution_start_to_close_timeout=duration_pb2.Duration(seconds=request.execution_start_to_close_timeout_seconds),
        task_start_to_close_timeout=duration_pb2.Duration(seconds=request.task_start_to_close_timeout_seconds),
        identity=request.identity,
        request_id=request.request_id,
        workflow_id_reuse_policy=workflow_id_reuse_policy_to_proto(request.workflow_id_reuse_policy),
        retry_policy=retry_policy_to_proto(request.retry_policy),
        cron_schedule=request.cron_schedule,
        memo=memo_to_proto(request.memo),
        search_attributes=search_attributes_to_proto(request.search_attributes),
        header=header_to_proto(request.header),
        delay_start=duration_pb2.Duration(seconds=request.delay_start),
    )


def workflow_type_dataclass_to_proto(request: WorkflowType) -> common_pb2.WorkflowType:
    return common_pb2.WorkflowType(
        name=request.name
    )


def task_list_to_proto(request: TaskList) -> tasklist_pb2:
    return tasklist_pb2.TaskList(
        name=request.name,
        kind=task_list_kind_to_proto(request.kind)
    )


def task_list_kind_to_proto(request: TaskListKind) -> tasklist_pb2.TaskListKind:
    if request == TaskListKind.STICKY:
        return tasklist_pb2.TASK_LIST_KIND_STICKY
    elif request == TaskListKind.NORMAL:
        return tasklist_pb2.TASK_LIST_KIND_NORMAL
    else:
        return tasklist_pb2.TASK_LIST_KIND_INVALID


def payload_to_proto(request: bytes) -> common_pb2.Payload:
    return common_pb2.Payload(
        data=request
    )


def workflow_id_reuse_policy_to_proto(request: WorkflowIdReusePolicy) -> workflow_pb2.WorkflowIdReusePolicy:
    if request == WorkflowIdReusePolicy.TerminateIfRunning:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING
    elif request == WorkflowIdReusePolicy.AllowDuplicate:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE
    elif request == WorkflowIdReusePolicy.AllowDuplicateFailedOnly:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY
    elif request == WorkflowIdReusePolicy.RejectDuplicate:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE
    else:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_INVALID


def retry_policy_to_proto(request: RetryPolicy) -> common_pb2.RetryPolicy:
    return common_pb2.RetryPolicy(
        initial_interval=duration_pb2.Duration(seconds=request.initial_interval_in_seconds),
        backoff_coefficient=request.backoff_coefficient,
        maximum_interval=duration_pb2.Duration(seconds=request.maximum_interval_in_seconds),
        maximum_attempts=request.maximum_attempts,
        non_retryable_error_reasons=[reason for reason in request.non_retriable_error_reasons],
        expiration_interval=duration_pb2.Duration(seconds=request.expiration_interval_in_seconds),
    )


def memo_to_proto(request: Memo) -> common_pb2.Memo:
    return common_pb2.Memo(
        fields={key: payload_to_proto(value) for key, value in request.fields}
    )


def search_attributes_to_proto(request: SearchAttributes) -> common_pb2.SearchAttributes:
    return common_pb2.SearchAttributes(
        indexed_fields={key: payload_to_proto(value) for key, value in request.indexed_fields}
    )


def header_to_proto(request: Header) -> common_pb2.Header:
    return common_pb2.Header(
        fields={key: payload_to_proto(value) for key, value in request.fields}
    )
