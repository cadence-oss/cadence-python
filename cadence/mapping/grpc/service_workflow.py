from typing import Optional

from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind, \
    WorkflowIdReusePolicy, RetryPolicy, Memo, SearchAttributes, Header, StartWorkflowExecutionResponse, \
    GetWorkflowExecutionHistoryRequest, WorkflowExecution, HistoryEventFilterType, GetWorkflowExecutionHistoryResponse, \
    History, HistoryEvent, EventType, WorkflowExecutionFailedEventAttributes, DataBlob, EncodingType, \
    WorkflowExecutionStartedEventAttributes, ParentExecutionInfo, Payload, ContinueAsNewInitiator, ResetPoints, \
    ResetPointInfo

from cadence.mapping.grpc.common import duration_or_none
from uber.cadence.api.v1 import service_workflow_pb2, common_pb2, tasklist_pb2, workflow_pb2, history_pb2


def start_workflow_execution_request_dataclass_to_proto(
        start_workflow_execution: StartWorkflowExecutionRequest) -> service_workflow_pb2.StartWorkflowExecutionRequest:
    return service_workflow_pb2.StartWorkflowExecutionRequest(
        domain=start_workflow_execution.domain,
        workflow_id=start_workflow_execution.workflow_id,
        workflow_type=workflow_type_dataclass_to_proto(start_workflow_execution.workflow_type),
        task_list=task_list_to_proto(start_workflow_execution.task_list),
        input=payload_to_proto(start_workflow_execution.input),
        execution_start_to_close_timeout=duration_or_none(
            start_workflow_execution.execution_start_to_close_timeout_seconds),
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


def start_workflow_execution_response_to_dataclass(
        start_workflow_execution: service_workflow_pb2.StartWorkflowExecutionResponse) -> StartWorkflowExecutionResponse:
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


def workflow_id_reuse_policy_to_proto(workflow_id_reuse_policy: Optional[WorkflowIdReusePolicy] = None) \
        -> workflow_pb2.WorkflowIdReusePolicy:
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


def get_workflow_execution_history_request_dataclass_to_proto(gwehr: GetWorkflowExecutionHistoryRequest) \
        -> service_workflow_pb2.GetWorkflowExecutionHistoryRequest:
    return service_workflow_pb2.GetWorkflowExecutionHistoryRequest(
        domain=gwehr.domain,
        workflow_execution=workflow_execution_dataclass_to_proto(gwehr.execution),  # here,
        page_size=gwehr.maximum_page_size,
        next_page_token=gwehr.next_page_token,
        wait_for_new_event=gwehr.wait_for_new_event,
        history_event_filter_type=history_event_filter_type_dataclass_to_proto(gwehr.history_event_filter_type),
        skip_archival=gwehr.skip_archival,
    ) if gwehr else None


def workflow_execution_dataclass_to_proto(workflow_execution: WorkflowExecution) -> common_pb2.WorkflowExecution:
    return common_pb2.WorkflowExecution(
        workflow_id=workflow_execution.workflow_id,
        run_id=workflow_execution.run_id
    ) if workflow_execution else None


def history_event_filter_type_dataclass_to_proto(history_event_filter_type: Optional[HistoryEventFilterType] = None) \
        -> history_pb2.EventFilterType:
    if history_event_filter_type == HistoryEventFilterType.ALL_EVENT:
        return history_pb2.EVENT_FILTER_TYPE_ALL_EVENT
    elif history_event_filter_type == HistoryEventFilterType.CLOSE_EVENT:
        return history_pb2.EVENT_FILTER_TYPE_CLOSE_EVENT
    else:
        return history_pb2.EVENT_FILTER_TYPE_INVALID


def proto_encoding_type_to_dataclass(encoding_type: Optional[common_pb2.EncodingType.__class__] = None) -> EncodingType:
    if encoding_type == common_pb2.ENCODING_TYPE_PROTO3:
        return EncodingType.Proto3
    elif encoding_type == common_pb2.ENCODING_TYPE_JSON:
        return EncodingType.JSON
    elif encoding_type == common_pb2.ENCODING_TYPE_THRIFTRW:
        return EncodingType.ThriftRW
    else:
        return EncodingType.Invalid


def proto_datablob_to_dataclass(raw_history: common_pb2.DataBlob) -> DataBlob:
    return DataBlob(
        encoding_type=proto_encoding_type_to_dataclass(raw_history.encoding_type),
        data=raw_history.data
    )


def proto_get_workflow_execution_history_response_to_dataclass(
        gwehr: service_workflow_pb2.GetWorkflowExecutionHistoryResponse) \
        -> GetWorkflowExecutionHistoryResponse:
    return GetWorkflowExecutionHistoryResponse(
        history=proto_history_to_dataclass(gwehr.history),
        raw_history=[proto_datablob_to_dataclass(raw_history) for raw_history in gwehr.raw_history],
        next_page_token=gwehr.next_page_token,
        archived=gwehr.archived
    ) if gwehr else None


def proto_history_to_dataclass(history: history_pb2.History) -> History:
    return History(
        events=[proto_history_event_to_dataclass(event) for event in history.events]
    ) if history else None


def proto_history_event_to_dataclass(history_event: Optional[history_pb2.HistoryEvent] = None) -> Optional[
    HistoryEvent]:
    if not history_event:
        return None

    he = HistoryEvent(
        event_id=history_event.event_id,
        timestamp=history_event.event_time.ToMilliseconds(),
        version=history_event.version,
        task_id=history_event.task_id
    )

    if history_event.workflow_execution_started_event_attributes is not None:
        he.event_type = EventType.WorkflowExecutionStarted
        he.workflow_execution_started_event_attributes = proto_workflow_execution_started_event_attributes_to_dataclass(
            history_event.workflow_execution_started_event_attributes)

    if history_event.workflow_execution_failed_event_attributes is not None:
        he.event_type = EventType.WorkflowExecutionFailed
        he.workflow_execution_failed_event_attributes = proto_workflow_execution_failed_event_attributes_to_dataclass(
            history_event.workflow_execution_failed_event_attributes)

    return he


def proto_workflow_execution_started_event_attributes_to_dataclass(
        event_attributes: history_pb2.WorkflowExecutionStartedEventAttributes) \
        -> WorkflowExecutionStartedEventAttributes:
    return WorkflowExecutionStartedEventAttributes(
        workflow_type=proto_workflow_type_to_dataclass(event_attributes.workflow_type),
        parent_workflow_domain=event_attributes.parent_execution_info.domain_name,
        parent_initiated_event_id=event_attributes.parent_execution_info.initiated_id,
        # deprecated variable, filling for compatibility
        parent_workflow_execution=WorkflowExecution(
            run_id=event_attributes.parent_execution_info.workflow_execution.run_id,
            workflow_id=event_attributes.parent_execution_info.workflow_execution.run_id,
        ),
        parent_execution_info=proto_parent_execution_info_to_dataclass(event_attributes.parent_execution_info),
        task_list=proto_task_list_to_dataclass(event_attributes.task_list),
        input=event_attributes.data,
        execution_start_to_close_timeout_seconds=event_attributes.execution_start_to_close_timeout.ToSeconds(),
        execution_start_to_close_timeout=event_attributes.execution_start_to_close_timeout.ToMilliseconds(),
        task_start_to_close_timeout_seconds=event_attributes.task_start_to_close_timeout.ToSeconds(),
        task_start_to_close_timeout=event_attributes.task_start_to_close_timeout.ToMilliseconds(),
        continued_execution_run_id=event_attributes.continued_execution_run_id,
        initiator=proto_continue_as_new_initiator_to_dataclass(event_attributes.initiator),
        continued_failure_details=event_attributes.continued_failure.details,
        continued_failure_reason=event_attributes.continued_failure.reason,
        last_completion_result=event_attributes.last_completion_result.data,
        original_execution_run_id=event_attributes.original_execution_run_id,
        identity=event_attributes.identity,
        first_execution_run_id=event_attributes.first_execution_run_id,
        retry_policy=proto_retry_policy_to_dataclass(event_attributes.retry_policy),
        attempt=event_attributes.attempt,
        expiration_timestamp=event_attributes.expiration_time.ToDatetime(),
        cron_schedule=event_attributes.cron_schedule,
        first_decision_task_backoff_seconds=event_attributes.first_decision_task_backoff.ToSeconds(),
        memo=proto_memo_to_dataclass(event_attributes.memo),
        search_attributes=proto_search_attributes_to_dataclass(event_attributes.search_attributes),
        prev_auto_reset_points=proto_reset_points_to_dataclass(event_attributes.prev_auto_reset_points),
        header=proto_header_to_dataclass(event_attributes),
    ) if event_attributes else None


def proto_parent_execution_info_to_dataclass(
        parent_execution_info: workflow_pb2.ParentExecutionInfo) -> Optional[ParentExecutionInfo]:
    return ParentExecutionInfo(
        domain_id=parent_execution_info.domain_id,
        domain_name=parent_execution_info.domain_name,
        workflow_execution=proto_workflow_execution_to_dataclass(parent_execution_info.workflow_execution),
        initiated_id=parent_execution_info.initiated_id,
    ) if parent_execution_info else None


def proto_workflow_execution_to_dataclass(workflow_execution: common_pb2.WorkflowExecution) -> WorkflowExecution:
    return WorkflowExecution(
        workflow_id=workflow_execution.workflow_id,
        run_id=workflow_execution.run_id,
    ) if workflow_execution else None


def proto_task_list_to_dataclass(task_list: tasklist_pb2.TaskList) -> TaskList:
    return TaskList(
        name=task_list.name,
        kind=proto_task_list_kind_to_dataclass(task_list.kind),
    ) if task_list else None


def proto_task_list_kind_to_dataclass(task_list_kind: tasklist_pb2.TaskListKind) -> TaskListKind:
    if task_list_kind == tasklist_pb2.TASK_LIST_KIND_STICKY:
        return TaskListKind.STICKY
    elif task_list_kind == tasklist_pb2.TASK_LIST_KIND_NORMAL:
        return TaskListKind.NORMAL
    else:
        return TaskListKind.INVALID


def proto_workflow_type_to_dataclass(workflow_type: common_pb2.WorkflowType) -> WorkflowType:
    return WorkflowType(
        name=workflow_type.name,
    ) if workflow_type else None


def proto_continue_as_new_initiator_to_dataclass(
        continue_as_new_initiator: workflow_pb2.ContinueAsNewInitiator) -> ContinueAsNewInitiator:
    if continue_as_new_initiator == workflow_pb2.CONTINUE_AS_NEW_INITIATOR_DECIDER:
        return ContinueAsNewInitiator.Decider
    elif continue_as_new_initiator == workflow_pb2.CONTINUE_AS_NEW_INITIATOR_RETRY_POLICY:
        return ContinueAsNewInitiator.RetryPolicy
    elif continue_as_new_initiator == workflow_pb2.CONTINUE_AS_NEW_INITIATOR_CRON_SCHEDULE:
        return ContinueAsNewInitiator.CronSchedule
    else:
        return ContinueAsNewInitiator.Invalid


def proto_retry_policy_to_dataclass(retry_policy: common_pb2.RetryPolicy) -> RetryPolicy:
    return RetryPolicy(
        initial_interval_in_seconds=retry_policy.initial_interval.ToSeconds(),
        initial_interval=retry_policy.initial_interval.ToMilliseconds(),
        maximum_interval_in_seconds=retry_policy.maximum_interval.ToSeconds(),
        maximum_interval=retry_policy.maximum_interval.ToMilliseconds(),
        maximum_attempts=retry_policy.maximum_attempts,
        non_retriable_error_reasons=[reason for reason in retry_policy.non_retriable_error_reasons],
        expiration_interval_in_seconds=retry_policy.expiration_interval.ToSeconds(),
        expiration_interval=retry_policy.expiration_interval.ToMilliseconds(),
    ) if retry_policy else None


def proto_memo_to_dataclass(memo: common_pb2.Memo) -> Memo:
    return Memo(
        fields={key: value.data for key, value in memo.fields.items()},
    ) if memo else None


def proto_search_attributes_to_dataclass(search_attributes: common_pb2.SearchAttributes) -> SearchAttributes:
    return SearchAttributes(
        indexed_fields={key: value.data for key, value in search_attributes.indexed_fields.items()}
    ) if search_attributes else None


def proto_header_to_dataclass(header: common_pb2.Header) -> Header:
    return Header(
        fields={key: value.data for key, value in header.fields.items()}
    ) if header else None


def proto_reset_points_to_dataclass(reset_points: workflow_pb2.ResetPoints) -> ResetPoints:
    return ResetPoints(
        points=[proto_reset_points_info_to_dataclass(point) for point in reset_points.points]
    ) if reset_points else None


def proto_reset_points_info_to_dataclass(reset_points_info: workflow_pb2.ResetPointInfo) -> ResetPointInfo:
    return ResetPointInfo(
        binary_checksum=reset_points_info.binary_checksum,
        first_decision_completed_id=reset_points_info.first_decision_completed_id,
        created_time_nano=reset_points_info.created_time.ToNanoseconds(),
        created_time=reset_points_info.created_time.ToDatetime(),
        expiring_time_nano=reset_points_info.expiring_time.ToNanoseconds(),
        expiring_time=reset_points_info.expiring_time.ToDatetime(),
        resettable=reset_points_info.resettable,
    )


def proto_workflow_execution_failed_event_attributes_to_dataclass(
        event_attributes: history_pb2.WorkflowExecutionFailedEventAttributes) \
        -> WorkflowExecutionFailedEventAttributes:
    return WorkflowExecutionFailedEventAttributes(
        reason=event_attributes.failure.reason,
        details=event_attributes.failure.details,
        decision_task_completed_event_id=event_attributes.decision_task_completed_event_id,
    ) if event_attributes else None
