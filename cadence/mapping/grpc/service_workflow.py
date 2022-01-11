from typing import Optional

from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind, \
    WorkflowIdReusePolicy, RetryPolicy, Memo, SearchAttributes, Header, StartWorkflowExecutionResponse

from cadence.mapping.grpc.common import duration_or_none
from uber.cadence.api.v1 import service_workflow_pb2, common_pb2, tasklist_pb2, workflow_pb2


def start_workflow_execution_request_dataclass_to_proto(
        start_workflow_execution: StartWorkflowExecutionRequest) -> service_workflow_pb2.StartWorkflowExecutionRequest:
    return service_workflow_pb2.StartWorkflowExecutionRequest(
        domain=start_workflow_execution.domain,
        workflow_id=start_workflow_execution.workflow_id,
        workflow_type=workflow_type_dataclass_to_proto(start_workflow_execution.workflow_type),
        task_list=task_list_to_proto(start_workflow_execution.task_list),
        input=payload_to_proto(start_workflow_execution.input),
        execution_start_to_close_timeout=duration_or_none(start_workflow_execution.execution_start_to_close_timeout_seconds),
        task_start_to_close_timeout=duration_or_none(start_workflow_execution.task_start_to_close_timeout_seconds),
        identity=start_workflow_execution.identity,
        request_id=start_workflow_execution.request_id,
        workflow_id_reuse_policy=workflow_id_reuse_policy_to_proto(start_workflow_execution.workflow_id_reuse_policy),
        retry_policy=retry_policy_to_proto(start_workflow_execution.retry_policy),
        cron_schedule=start_workflow_execution.cron_schedule,
        memo=memo_to_proto(start_workflow_execution.memo),
        search_attributes=search_attributes_to_proto(start_workflow_execution.search_attributes),
        header=header_to_proto(start_workflow_execution.header),
        delay_start=duration_or_none(start_workflow_execution.delay_start),
    ) if start_workflow_execution else None


def start_workflow_execution_response_to_dataclass(start_workflow_execution: service_workflow_pb2.StartWorkflowExecutionResponse) -> StartWorkflowExecutionResponse:
    return StartWorkflowExecutionResponse(
        run_id=start_workflow_execution.run_id
    ) if start_workflow_execution else None


def workflow_type_dataclass_to_proto(workflow_type: WorkflowType) -> common_pb2.WorkflowType:
    return common_pb2.WorkflowType(
        name=workflow_type.name
    ) if workflow_type else None


def task_list_to_proto(task_list: TaskList) -> tasklist_pb2:
    return tasklist_pb2.TaskList(
        name=task_list.name,
        kind=task_list_kind_to_proto(task_list.kind)
    ) if task_list else None


def task_list_kind_to_proto(task_list_kind: Optional[TaskListKind] = None) -> tasklist_pb2.TaskListKind:
    if task_list_kind == TaskListKind.STICKY:
        return tasklist_pb2.TASK_LIST_KIND_STICKY
    elif task_list_kind == TaskListKind.NORMAL:
        return tasklist_pb2.TASK_LIST_KIND_NORMAL
    else:
        return tasklist_pb2.TASK_LIST_KIND_INVALID


def payload_to_proto(payload: bytes) -> common_pb2.Payload:
    data = bytes(payload, encoding='utf8') if isinstance(payload, str) else payload
    return common_pb2.Payload(
        data=data
    ) if payload else None


def workflow_id_reuse_policy_to_proto(workflow_id_reuse_policy: Optional[WorkflowIdReusePolicy] = None) -> workflow_pb2.WorkflowIdReusePolicy:
    if workflow_id_reuse_policy == WorkflowIdReusePolicy.TerminateIfRunning:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING
    elif workflow_id_reuse_policy == WorkflowIdReusePolicy.AllowDuplicate:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE
    elif workflow_id_reuse_policy == WorkflowIdReusePolicy.AllowDuplicateFailedOnly:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY
    elif workflow_id_reuse_policy == WorkflowIdReusePolicy.RejectDuplicate:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE
    else:
        return workflow_pb2.WORKFLOW_ID_REUSE_POLICY_INVALID


def retry_policy_to_proto(retry_policy: RetryPolicy) -> common_pb2.RetryPolicy:
    return common_pb2.RetryPolicy(
        initial_interval=duration_or_none(retry_policy.initial_interval_in_seconds),
        backoff_coefficient=retry_policy.backoff_coefficient,
        maximum_interval=duration_or_none(retry_policy.maximum_interval_in_seconds),
        maximum_attempts=retry_policy.maximum_attempts,
        non_retryable_error_reasons=[reason for reason in retry_policy.non_retriable_error_reasons],
        expiration_interval=duration_or_none(retry_policy.expiration_interval_in_seconds),
    ) if retry_policy else None


def memo_to_proto(memo: Memo) -> common_pb2.Memo:
    return common_pb2.Memo(
        fields={key: payload_to_proto(value) for key, value in memo.fields.items()}
    ) if memo else None


def search_attributes_to_proto(search_attributes: SearchAttributes) -> common_pb2.SearchAttributes:
    return common_pb2.SearchAttributes(
        indexed_fields={key: payload_to_proto(value) for key, value in search_attributes.indexed_fields.items()}
    ) if search_attributes else None


def header_to_proto(header: Header) -> common_pb2.Header:
    return common_pb2.Header(
        fields={key: payload_to_proto(value) for key, value in header.fields.items()}
    ) if header else None
