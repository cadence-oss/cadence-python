"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import typing
import typing_extensions
import uber.cadence.api.v1.common_pb2
import uber.cadence.api.v1.tasklist_pb2
import uber.cadence.api.v1.workflow_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Decision(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCHEDULE_ACTIVITY_TASK_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    START_TIMER_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    COMPLETE_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    FAIL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    REQUEST_CANCEL_ACTIVITY_TASK_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    CANCEL_TIMER_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    CANCEL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    RECORD_MARKER_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    CONTINUE_AS_NEW_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    START_CHILD_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    UPSERT_WORKFLOW_SEARCH_ATTRIBUTES_DECISION_ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def schedule_activity_task_decision_attributes(self) -> global___ScheduleActivityTaskDecisionAttributes: ...
    @property
    def start_timer_decision_attributes(self) -> global___StartTimerDecisionAttributes: ...
    @property
    def complete_workflow_execution_decision_attributes(self) -> global___CompleteWorkflowExecutionDecisionAttributes: ...
    @property
    def fail_workflow_execution_decision_attributes(self) -> global___FailWorkflowExecutionDecisionAttributes: ...
    @property
    def request_cancel_activity_task_decision_attributes(self) -> global___RequestCancelActivityTaskDecisionAttributes: ...
    @property
    def cancel_timer_decision_attributes(self) -> global___CancelTimerDecisionAttributes: ...
    @property
    def cancel_workflow_execution_decision_attributes(self) -> global___CancelWorkflowExecutionDecisionAttributes: ...
    @property
    def request_cancel_external_workflow_execution_decision_attributes(self) -> global___RequestCancelExternalWorkflowExecutionDecisionAttributes: ...
    @property
    def record_marker_decision_attributes(self) -> global___RecordMarkerDecisionAttributes: ...
    @property
    def continue_as_new_workflow_execution_decision_attributes(self) -> global___ContinueAsNewWorkflowExecutionDecisionAttributes: ...
    @property
    def start_child_workflow_execution_decision_attributes(self) -> global___StartChildWorkflowExecutionDecisionAttributes: ...
    @property
    def signal_external_workflow_execution_decision_attributes(self) -> global___SignalExternalWorkflowExecutionDecisionAttributes: ...
    @property
    def upsert_workflow_search_attributes_decision_attributes(self) -> global___UpsertWorkflowSearchAttributesDecisionAttributes: ...
    def __init__(self,
        *,
        schedule_activity_task_decision_attributes : typing.Optional[global___ScheduleActivityTaskDecisionAttributes] = ...,
        start_timer_decision_attributes : typing.Optional[global___StartTimerDecisionAttributes] = ...,
        complete_workflow_execution_decision_attributes : typing.Optional[global___CompleteWorkflowExecutionDecisionAttributes] = ...,
        fail_workflow_execution_decision_attributes : typing.Optional[global___FailWorkflowExecutionDecisionAttributes] = ...,
        request_cancel_activity_task_decision_attributes : typing.Optional[global___RequestCancelActivityTaskDecisionAttributes] = ...,
        cancel_timer_decision_attributes : typing.Optional[global___CancelTimerDecisionAttributes] = ...,
        cancel_workflow_execution_decision_attributes : typing.Optional[global___CancelWorkflowExecutionDecisionAttributes] = ...,
        request_cancel_external_workflow_execution_decision_attributes : typing.Optional[global___RequestCancelExternalWorkflowExecutionDecisionAttributes] = ...,
        record_marker_decision_attributes : typing.Optional[global___RecordMarkerDecisionAttributes] = ...,
        continue_as_new_workflow_execution_decision_attributes : typing.Optional[global___ContinueAsNewWorkflowExecutionDecisionAttributes] = ...,
        start_child_workflow_execution_decision_attributes : typing.Optional[global___StartChildWorkflowExecutionDecisionAttributes] = ...,
        signal_external_workflow_execution_decision_attributes : typing.Optional[global___SignalExternalWorkflowExecutionDecisionAttributes] = ...,
        upsert_workflow_search_attributes_decision_attributes : typing.Optional[global___UpsertWorkflowSearchAttributesDecisionAttributes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attributes",b"attributes","cancel_timer_decision_attributes",b"cancel_timer_decision_attributes","cancel_workflow_execution_decision_attributes",b"cancel_workflow_execution_decision_attributes","complete_workflow_execution_decision_attributes",b"complete_workflow_execution_decision_attributes","continue_as_new_workflow_execution_decision_attributes",b"continue_as_new_workflow_execution_decision_attributes","fail_workflow_execution_decision_attributes",b"fail_workflow_execution_decision_attributes","record_marker_decision_attributes",b"record_marker_decision_attributes","request_cancel_activity_task_decision_attributes",b"request_cancel_activity_task_decision_attributes","request_cancel_external_workflow_execution_decision_attributes",b"request_cancel_external_workflow_execution_decision_attributes","schedule_activity_task_decision_attributes",b"schedule_activity_task_decision_attributes","signal_external_workflow_execution_decision_attributes",b"signal_external_workflow_execution_decision_attributes","start_child_workflow_execution_decision_attributes",b"start_child_workflow_execution_decision_attributes","start_timer_decision_attributes",b"start_timer_decision_attributes","upsert_workflow_search_attributes_decision_attributes",b"upsert_workflow_search_attributes_decision_attributes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes",b"attributes","cancel_timer_decision_attributes",b"cancel_timer_decision_attributes","cancel_workflow_execution_decision_attributes",b"cancel_workflow_execution_decision_attributes","complete_workflow_execution_decision_attributes",b"complete_workflow_execution_decision_attributes","continue_as_new_workflow_execution_decision_attributes",b"continue_as_new_workflow_execution_decision_attributes","fail_workflow_execution_decision_attributes",b"fail_workflow_execution_decision_attributes","record_marker_decision_attributes",b"record_marker_decision_attributes","request_cancel_activity_task_decision_attributes",b"request_cancel_activity_task_decision_attributes","request_cancel_external_workflow_execution_decision_attributes",b"request_cancel_external_workflow_execution_decision_attributes","schedule_activity_task_decision_attributes",b"schedule_activity_task_decision_attributes","signal_external_workflow_execution_decision_attributes",b"signal_external_workflow_execution_decision_attributes","start_child_workflow_execution_decision_attributes",b"start_child_workflow_execution_decision_attributes","start_timer_decision_attributes",b"start_timer_decision_attributes","upsert_workflow_search_attributes_decision_attributes",b"upsert_workflow_search_attributes_decision_attributes"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["attributes",b"attributes"]) -> typing.Optional[typing_extensions.Literal["schedule_activity_task_decision_attributes","start_timer_decision_attributes","complete_workflow_execution_decision_attributes","fail_workflow_execution_decision_attributes","request_cancel_activity_task_decision_attributes","cancel_timer_decision_attributes","cancel_workflow_execution_decision_attributes","request_cancel_external_workflow_execution_decision_attributes","record_marker_decision_attributes","continue_as_new_workflow_execution_decision_attributes","start_child_workflow_execution_decision_attributes","signal_external_workflow_execution_decision_attributes","upsert_workflow_search_attributes_decision_attributes"]]: ...
global___Decision = Decision

class ScheduleActivityTaskDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACTIVITY_ID_FIELD_NUMBER: builtins.int
    ACTIVITY_TYPE_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    TASK_LIST_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    SCHEDULE_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    SCHEDULE_TO_START_TIMEOUT_FIELD_NUMBER: builtins.int
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    HEARTBEAT_TIMEOUT_FIELD_NUMBER: builtins.int
    RETRY_POLICY_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    REQUEST_LOCAL_DISPATCH_FIELD_NUMBER: builtins.int
    activity_id: typing.Text = ...
    @property
    def activity_type(self) -> uber.cadence.api.v1.common_pb2.ActivityType: ...
    domain: typing.Text = ...
    @property
    def task_list(self) -> uber.cadence.api.v1.tasklist_pb2.TaskList: ...
    @property
    def input(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    @property
    def schedule_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def schedule_to_start_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def start_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def heartbeat_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def retry_policy(self) -> uber.cadence.api.v1.common_pb2.RetryPolicy: ...
    @property
    def header(self) -> uber.cadence.api.v1.common_pb2.Header: ...
    request_local_dispatch: builtins.bool = ...
    def __init__(self,
        *,
        activity_id : typing.Text = ...,
        activity_type : typing.Optional[uber.cadence.api.v1.common_pb2.ActivityType] = ...,
        domain : typing.Text = ...,
        task_list : typing.Optional[uber.cadence.api.v1.tasklist_pb2.TaskList] = ...,
        input : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        schedule_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        schedule_to_start_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        start_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        heartbeat_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        retry_policy : typing.Optional[uber.cadence.api.v1.common_pb2.RetryPolicy] = ...,
        header : typing.Optional[uber.cadence.api.v1.common_pb2.Header] = ...,
        request_local_dispatch : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["activity_type",b"activity_type","header",b"header","heartbeat_timeout",b"heartbeat_timeout","input",b"input","retry_policy",b"retry_policy","schedule_to_close_timeout",b"schedule_to_close_timeout","schedule_to_start_timeout",b"schedule_to_start_timeout","start_to_close_timeout",b"start_to_close_timeout","task_list",b"task_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_id",b"activity_id","activity_type",b"activity_type","domain",b"domain","header",b"header","heartbeat_timeout",b"heartbeat_timeout","input",b"input","request_local_dispatch",b"request_local_dispatch","retry_policy",b"retry_policy","schedule_to_close_timeout",b"schedule_to_close_timeout","schedule_to_start_timeout",b"schedule_to_start_timeout","start_to_close_timeout",b"start_to_close_timeout","task_list",b"task_list"]) -> None: ...
global___ScheduleActivityTaskDecisionAttributes = ScheduleActivityTaskDecisionAttributes

class StartTimerDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIMER_ID_FIELD_NUMBER: builtins.int
    START_TO_FIRE_TIMEOUT_FIELD_NUMBER: builtins.int
    timer_id: typing.Text = ...
    @property
    def start_to_fire_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(self,
        *,
        timer_id : typing.Text = ...,
        start_to_fire_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["start_to_fire_timeout",b"start_to_fire_timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["start_to_fire_timeout",b"start_to_fire_timeout","timer_id",b"timer_id"]) -> None: ...
global___StartTimerDecisionAttributes = StartTimerDecisionAttributes

class CompleteWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    def __init__(self,
        *,
        result : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___CompleteWorkflowExecutionDecisionAttributes = CompleteWorkflowExecutionDecisionAttributes

class FailWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def failure(self) -> uber.cadence.api.v1.common_pb2.Failure: ...
    def __init__(self,
        *,
        failure : typing.Optional[uber.cadence.api.v1.common_pb2.Failure] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["failure",b"failure"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure",b"failure"]) -> None: ...
global___FailWorkflowExecutionDecisionAttributes = FailWorkflowExecutionDecisionAttributes

class RequestCancelActivityTaskDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACTIVITY_ID_FIELD_NUMBER: builtins.int
    activity_id: typing.Text = ...
    def __init__(self,
        *,
        activity_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_id",b"activity_id"]) -> None: ...
global___RequestCancelActivityTaskDecisionAttributes = RequestCancelActivityTaskDecisionAttributes

class CancelTimerDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIMER_ID_FIELD_NUMBER: builtins.int
    timer_id: typing.Text = ...
    def __init__(self,
        *,
        timer_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["timer_id",b"timer_id"]) -> None: ...
global___CancelTimerDecisionAttributes = CancelTimerDecisionAttributes

class CancelWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DETAILS_FIELD_NUMBER: builtins.int
    @property
    def details(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    def __init__(self,
        *,
        details : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["details",b"details"]) -> None: ...
global___CancelWorkflowExecutionDecisionAttributes = CancelWorkflowExecutionDecisionAttributes

class RequestCancelExternalWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DOMAIN_FIELD_NUMBER: builtins.int
    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    CONTROL_FIELD_NUMBER: builtins.int
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: builtins.int
    domain: typing.Text = ...
    @property
    def workflow_execution(self) -> uber.cadence.api.v1.common_pb2.WorkflowExecution: ...
    control: builtins.bytes = ...
    child_workflow_only: builtins.bool = ...
    def __init__(self,
        *,
        domain : typing.Text = ...,
        workflow_execution : typing.Optional[uber.cadence.api.v1.common_pb2.WorkflowExecution] = ...,
        control : builtins.bytes = ...,
        child_workflow_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["workflow_execution",b"workflow_execution"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["child_workflow_only",b"child_workflow_only","control",b"control","domain",b"domain","workflow_execution",b"workflow_execution"]) -> None: ...
global___RequestCancelExternalWorkflowExecutionDecisionAttributes = RequestCancelExternalWorkflowExecutionDecisionAttributes

class RecordMarkerDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MARKER_NAME_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    marker_name: typing.Text = ...
    @property
    def details(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    @property
    def header(self) -> uber.cadence.api.v1.common_pb2.Header: ...
    def __init__(self,
        *,
        marker_name : typing.Text = ...,
        details : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        header : typing.Optional[uber.cadence.api.v1.common_pb2.Header] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["details",b"details","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["details",b"details","header",b"header","marker_name",b"marker_name"]) -> None: ...
global___RecordMarkerDecisionAttributes = RecordMarkerDecisionAttributes

class ContinueAsNewWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORKFLOW_TYPE_FIELD_NUMBER: builtins.int
    TASK_LIST_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    BACKOFF_START_INTERVAL_FIELD_NUMBER: builtins.int
    RETRY_POLICY_FIELD_NUMBER: builtins.int
    INITIATOR_FIELD_NUMBER: builtins.int
    FAILURE_FIELD_NUMBER: builtins.int
    LAST_COMPLETION_RESULT_FIELD_NUMBER: builtins.int
    CRON_SCHEDULE_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def workflow_type(self) -> uber.cadence.api.v1.common_pb2.WorkflowType: ...
    @property
    def task_list(self) -> uber.cadence.api.v1.tasklist_pb2.TaskList: ...
    @property
    def input(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    @property
    def execution_start_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def task_start_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def backoff_start_interval(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def retry_policy(self) -> uber.cadence.api.v1.common_pb2.RetryPolicy: ...
    initiator: uber.cadence.api.v1.workflow_pb2.ContinueAsNewInitiator.V = ...
    @property
    def failure(self) -> uber.cadence.api.v1.common_pb2.Failure: ...
    @property
    def last_completion_result(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    cron_schedule: typing.Text = ...
    @property
    def header(self) -> uber.cadence.api.v1.common_pb2.Header: ...
    @property
    def memo(self) -> uber.cadence.api.v1.common_pb2.Memo: ...
    @property
    def search_attributes(self) -> uber.cadence.api.v1.common_pb2.SearchAttributes: ...
    def __init__(self,
        *,
        workflow_type : typing.Optional[uber.cadence.api.v1.common_pb2.WorkflowType] = ...,
        task_list : typing.Optional[uber.cadence.api.v1.tasklist_pb2.TaskList] = ...,
        input : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        execution_start_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        task_start_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        backoff_start_interval : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        retry_policy : typing.Optional[uber.cadence.api.v1.common_pb2.RetryPolicy] = ...,
        initiator : uber.cadence.api.v1.workflow_pb2.ContinueAsNewInitiator.V = ...,
        failure : typing.Optional[uber.cadence.api.v1.common_pb2.Failure] = ...,
        last_completion_result : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        cron_schedule : typing.Text = ...,
        header : typing.Optional[uber.cadence.api.v1.common_pb2.Header] = ...,
        memo : typing.Optional[uber.cadence.api.v1.common_pb2.Memo] = ...,
        search_attributes : typing.Optional[uber.cadence.api.v1.common_pb2.SearchAttributes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backoff_start_interval",b"backoff_start_interval","execution_start_to_close_timeout",b"execution_start_to_close_timeout","failure",b"failure","header",b"header","input",b"input","last_completion_result",b"last_completion_result","memo",b"memo","retry_policy",b"retry_policy","search_attributes",b"search_attributes","task_list",b"task_list","task_start_to_close_timeout",b"task_start_to_close_timeout","workflow_type",b"workflow_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backoff_start_interval",b"backoff_start_interval","cron_schedule",b"cron_schedule","execution_start_to_close_timeout",b"execution_start_to_close_timeout","failure",b"failure","header",b"header","initiator",b"initiator","input",b"input","last_completion_result",b"last_completion_result","memo",b"memo","retry_policy",b"retry_policy","search_attributes",b"search_attributes","task_list",b"task_list","task_start_to_close_timeout",b"task_start_to_close_timeout","workflow_type",b"workflow_type"]) -> None: ...
global___ContinueAsNewWorkflowExecutionDecisionAttributes = ContinueAsNewWorkflowExecutionDecisionAttributes

class StartChildWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DOMAIN_FIELD_NUMBER: builtins.int
    WORKFLOW_ID_FIELD_NUMBER: builtins.int
    WORKFLOW_TYPE_FIELD_NUMBER: builtins.int
    TASK_LIST_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: builtins.int
    PARENT_CLOSE_POLICY_FIELD_NUMBER: builtins.int
    CONTROL_FIELD_NUMBER: builtins.int
    WORKFLOW_ID_REUSE_POLICY_FIELD_NUMBER: builtins.int
    RETRY_POLICY_FIELD_NUMBER: builtins.int
    CRON_SCHEDULE_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    domain: typing.Text = ...
    workflow_id: typing.Text = ...
    @property
    def workflow_type(self) -> uber.cadence.api.v1.common_pb2.WorkflowType: ...
    @property
    def task_list(self) -> uber.cadence.api.v1.tasklist_pb2.TaskList: ...
    @property
    def input(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    @property
    def execution_start_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def task_start_to_close_timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    parent_close_policy: uber.cadence.api.v1.workflow_pb2.ParentClosePolicy.V = ...
    control: builtins.bytes = ...
    workflow_id_reuse_policy: uber.cadence.api.v1.workflow_pb2.WorkflowIdReusePolicy.V = ...
    @property
    def retry_policy(self) -> uber.cadence.api.v1.common_pb2.RetryPolicy: ...
    cron_schedule: typing.Text = ...
    @property
    def header(self) -> uber.cadence.api.v1.common_pb2.Header: ...
    @property
    def memo(self) -> uber.cadence.api.v1.common_pb2.Memo: ...
    @property
    def search_attributes(self) -> uber.cadence.api.v1.common_pb2.SearchAttributes: ...
    def __init__(self,
        *,
        domain : typing.Text = ...,
        workflow_id : typing.Text = ...,
        workflow_type : typing.Optional[uber.cadence.api.v1.common_pb2.WorkflowType] = ...,
        task_list : typing.Optional[uber.cadence.api.v1.tasklist_pb2.TaskList] = ...,
        input : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        execution_start_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        task_start_to_close_timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        parent_close_policy : uber.cadence.api.v1.workflow_pb2.ParentClosePolicy.V = ...,
        control : builtins.bytes = ...,
        workflow_id_reuse_policy : uber.cadence.api.v1.workflow_pb2.WorkflowIdReusePolicy.V = ...,
        retry_policy : typing.Optional[uber.cadence.api.v1.common_pb2.RetryPolicy] = ...,
        cron_schedule : typing.Text = ...,
        header : typing.Optional[uber.cadence.api.v1.common_pb2.Header] = ...,
        memo : typing.Optional[uber.cadence.api.v1.common_pb2.Memo] = ...,
        search_attributes : typing.Optional[uber.cadence.api.v1.common_pb2.SearchAttributes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["execution_start_to_close_timeout",b"execution_start_to_close_timeout","header",b"header","input",b"input","memo",b"memo","retry_policy",b"retry_policy","search_attributes",b"search_attributes","task_list",b"task_list","task_start_to_close_timeout",b"task_start_to_close_timeout","workflow_type",b"workflow_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["control",b"control","cron_schedule",b"cron_schedule","domain",b"domain","execution_start_to_close_timeout",b"execution_start_to_close_timeout","header",b"header","input",b"input","memo",b"memo","parent_close_policy",b"parent_close_policy","retry_policy",b"retry_policy","search_attributes",b"search_attributes","task_list",b"task_list","task_start_to_close_timeout",b"task_start_to_close_timeout","workflow_id",b"workflow_id","workflow_id_reuse_policy",b"workflow_id_reuse_policy","workflow_type",b"workflow_type"]) -> None: ...
global___StartChildWorkflowExecutionDecisionAttributes = StartChildWorkflowExecutionDecisionAttributes

class SignalExternalWorkflowExecutionDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DOMAIN_FIELD_NUMBER: builtins.int
    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    SIGNAL_NAME_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    CONTROL_FIELD_NUMBER: builtins.int
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: builtins.int
    domain: typing.Text = ...
    @property
    def workflow_execution(self) -> uber.cadence.api.v1.common_pb2.WorkflowExecution: ...
    signal_name: typing.Text = ...
    @property
    def input(self) -> uber.cadence.api.v1.common_pb2.Payload: ...
    control: builtins.bytes = ...
    child_workflow_only: builtins.bool = ...
    def __init__(self,
        *,
        domain : typing.Text = ...,
        workflow_execution : typing.Optional[uber.cadence.api.v1.common_pb2.WorkflowExecution] = ...,
        signal_name : typing.Text = ...,
        input : typing.Optional[uber.cadence.api.v1.common_pb2.Payload] = ...,
        control : builtins.bytes = ...,
        child_workflow_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["input",b"input","workflow_execution",b"workflow_execution"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["child_workflow_only",b"child_workflow_only","control",b"control","domain",b"domain","input",b"input","signal_name",b"signal_name","workflow_execution",b"workflow_execution"]) -> None: ...
global___SignalExternalWorkflowExecutionDecisionAttributes = SignalExternalWorkflowExecutionDecisionAttributes

class UpsertWorkflowSearchAttributesDecisionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def search_attributes(self) -> uber.cadence.api.v1.common_pb2.SearchAttributes: ...
    def __init__(self,
        *,
        search_attributes : typing.Optional[uber.cadence.api.v1.common_pb2.SearchAttributes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["search_attributes",b"search_attributes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["search_attributes",b"search_attributes"]) -> None: ...
global___UpsertWorkflowSearchAttributesDecisionAttributes = UpsertWorkflowSearchAttributesDecisionAttributes
