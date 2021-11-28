from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind, \
    WorkflowIdReusePolicy, RetryPolicy, Memo, SearchAttributes, Header, StartWorkflowExecutionResponse

from cadence.mapping.grpc.common import duration_or_none
from uber.cadence.api.v1 import service_workflow_pb2, common_pb2, tasklist_pb2, workflow_pb2


def start_workflow_execution_request_dataclass_to_proto(
        request: StartWorkflowExecutionRequest) -> service_workflow_pb2.StartWorkflowExecutionRequest:
    return service_workflow_pb2.StartWorkflowExecutionRequest(
        domain=request.domain,
        workflow_id=request.workflow_id,
        workflow_type=workflow_type_dataclass_to_proto(request.workflow_type),
        task_list=task_list_to_proto(request.task_list),
        input=payload_to_proto(request.input),
        execution_start_to_close_timeout=duration_or_none(request.execution_start_to_close_timeout_seconds),
        task_start_to_close_timeout=duration_or_none(request.task_start_to_close_timeout_seconds),
        identity=request.identity,
        request_id=request.request_id,
        workflow_id_reuse_policy=workflow_id_reuse_policy_to_proto(request.workflow_id_reuse_policy),
        retry_policy=retry_policy_to_proto(request.retry_policy),
        cron_schedule=request.cron_schedule,
        memo=memo_to_proto(request.memo),
        search_attributes=search_attributes_to_proto(request.search_attributes),
        header=header_to_proto(request.header),
        delay_start=duration_or_none(request.delay_start),
    ) if request else None


def start_workflow_execution_response_to_dataclass(response: service_workflow_pb2.StartWorkflowExecutionResponse) -> StartWorkflowExecutionResponse:
    return StartWorkflowExecutionResponse(
        run_id=response.run_id
    ) if response else None


def workflow_type_dataclass_to_proto(request: WorkflowType) -> common_pb2.WorkflowType:
    return common_pb2.WorkflowType(
        name=request.name
    ) if request else None


def task_list_to_proto(request: TaskList) -> tasklist_pb2:
    return tasklist_pb2.TaskList(
        name=request.name,
        kind=task_list_kind_to_proto(request.kind)
    ) if request else None


def task_list_kind_to_proto(request: TaskListKind) -> tasklist_pb2.TaskListKind:
    if request == TaskListKind.STICKY:
        return tasklist_pb2.TASK_LIST_KIND_STICKY
    elif request == TaskListKind.NORMAL:
        return tasklist_pb2.TASK_LIST_KIND_NORMAL
    else:
        return tasklist_pb2.TASK_LIST_KIND_INVALID


def payload_to_proto(request: bytes) -> common_pb2.Payload:
    return common_pb2.Payload(
        data=bytes(request, encoding='utf8')
    ) if request else None


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
        initial_interval=duration_or_none(request.initial_interval_in_seconds),
        backoff_coefficient=request.backoff_coefficient,
        maximum_interval=duration_or_none(request.maximum_interval_in_seconds),
        maximum_attempts=request.maximum_attempts,
        non_retryable_error_reasons=[reason for reason in request.non_retriable_error_reasons],
        expiration_interval=duration_or_none(request.expiration_interval_in_seconds),
    ) if request else None


def memo_to_proto(request: Memo) -> common_pb2.Memo:
    return common_pb2.Memo(
        fields={key: payload_to_proto(value) for key, value in request.fields}
    ) if request else None


def search_attributes_to_proto(request: SearchAttributes) -> common_pb2.SearchAttributes:
    return common_pb2.SearchAttributes(
        indexed_fields={key: payload_to_proto(value) for key, value in request.indexed_fields}
    ) if request else None


def header_to_proto(request: Header) -> common_pb2.Header:
    return common_pb2.Header(
        fields={key: payload_to_proto(value) for key, value in request.fields}
    ) if request else None
