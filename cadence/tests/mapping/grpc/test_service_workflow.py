from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind, \
    WorkflowIdReusePolicy, ChildPolicy, RetryPolicy, Memo, SearchAttributes, Header
from cadence.mapping.grpc.service_workflow import start_workflow_execution_request_dataclass_to_proto, \
    start_workflow_execution_response_to_dataclass, workflow_type_dataclass_to_proto, task_list_to_proto, \
    task_list_kind_to_proto, payload_to_proto, workflow_id_reuse_policy_to_proto, retry_policy_to_proto, memo_to_proto, \
    search_attributes_to_proto, header_to_proto
from uber.cadence.api.v1 import tasklist_pb2, workflow_pb2, service_workflow_pb2


def test_start_workflow_execution_request_dataclass_to_proto():
    swer = StartWorkflowExecutionRequest(
        domain="test",
        workflow_id="test",
        workflow_type=WorkflowType(name="the_type"),
        task_list=TaskList(
            name="the_task",
            kind=TaskListKind(0)
        ),
        input=bytes("theinput", "utf-8"),
        execution_start_to_close_timeout_seconds=60,
        task_start_to_close_timeout_seconds=60,
        identity="identity",
        request_id="123456",
        workflow_id_reuse_policy=WorkflowIdReusePolicy(0),
        child_policy=ChildPolicy(0),
        retry_policy=RetryPolicy(
            initial_interval_in_seconds=60,
            backoff_coefficient=1.0,
            maximum_interval_in_seconds=60,
            maximum_attempts=10,
            non_retriable_error_reasons=["a", "b"],
            expiration_interval_in_seconds=1000,
        ),
        cron_schedule="* * * * *",
        memo=Memo(fields={"a": bytes("a", "utf-8")}),
        search_attributes=SearchAttributes(indexed_fields={"b": bytes("b", "utf-8")}),
        header=Header(fields={"c": bytes("c", "utf-8")}),
        delay_start=100,
    )

    swerp = start_workflow_execution_request_dataclass_to_proto(swer)
    assert swerp.domain == swer.domain
    assert swerp.workflow_id == swer.workflow_id
    assert swerp.workflow_type.name == swer.workflow_type.name
    assert swerp.task_list.name == swer.task_list.name
    assert swerp.task_list.kind == tasklist_pb2.TASK_LIST_KIND_NORMAL
    assert swerp.input.data == bytes("theinput", "utf-8")
    assert swerp.execution_start_to_close_timeout.ToSeconds() == 60
    assert swerp.task_start_to_close_timeout.ToSeconds() == 60
    assert swerp.identity == swer.identity
    assert swerp.request_id == swer.request_id
    assert swerp.workflow_id_reuse_policy == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY
    assert swerp.retry_policy.initial_interval.ToSeconds() == 60
    assert swerp.retry_policy.backoff_coefficient == 1.0
    assert swerp.retry_policy.maximum_interval.ToSeconds() == 60
    assert swerp.retry_policy.maximum_attempts == 10
    assert swerp.retry_policy.non_retryable_error_reasons == swer.retry_policy.non_retriable_error_reasons
    assert swerp.retry_policy.expiration_interval.ToSeconds() == 1000
    assert swerp.cron_schedule == swer.cron_schedule
    assert len(swerp.memo.fields.keys()) == 1
    assert swerp.memo.fields["a"].data == bytes("a", "utf-8")
    assert len(swerp.search_attributes.indexed_fields.keys()) == 1
    assert swerp.search_attributes.indexed_fields["b"].data == bytes("b", "utf-8")
    assert len(swerp.header.fields.keys()) == 1
    assert swerp.header.fields["c"].data == bytes("c", "utf-8")
    assert swerp.delay_start.ToSeconds() == 100


def test_start_workflow_execution_request_dataclass_to_proto_empty():
    swer = StartWorkflowExecutionRequest()

    swerp = start_workflow_execution_request_dataclass_to_proto(swer)
    assert swerp.task_list.kind == tasklist_pb2.TASK_LIST_KIND_INVALID
    assert swerp.execution_start_to_close_timeout.ToSeconds() == 0
    assert swerp.task_start_to_close_timeout.ToSeconds() == 0
    assert swerp.workflow_id_reuse_policy == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_INVALID
    assert len(swerp.memo.fields.keys()) == 0
    assert len(swerp.search_attributes.indexed_fields.keys()) == 0
    assert len(swerp.header.fields.keys()) == 0
    assert swerp.delay_start.ToSeconds() == 0


def test_start_workflow_execution_response_to_dataclass():
    swer = service_workflow_pb2.StartWorkflowExecutionResponse(run_id="100")
    response = start_workflow_execution_response_to_dataclass(swer)
    assert swer.run_id == response.run_id


def test_workflow_type_dataclass_to_proto():
    wt = WorkflowType(name="name")
    response = workflow_type_dataclass_to_proto(wt)
    assert response.name == wt.name


def test_task_list_to_proto():
    tl = TaskList(
        name="task",
        kind=TaskListKind(1)
    )
    response = task_list_to_proto(tl)
    assert response.name == tl.name
    assert tl.kind == tasklist_pb2.TASK_LIST_KIND_NORMAL


def test_task_list_kind_to_proto():
    assert task_list_kind_to_proto(TaskListKind.STICKY) == tasklist_pb2.TASK_LIST_KIND_STICKY
    assert task_list_kind_to_proto(TaskListKind.NORMAL) == tasklist_pb2.TASK_LIST_KIND_NORMAL
    assert task_list_kind_to_proto(TaskListKind.INVALID) == tasklist_pb2.TASK_LIST_KIND_INVALID
    assert task_list_kind_to_proto() == tasklist_pb2.TASK_LIST_KIND_INVALID


def test_payload_to_proto():
    response = payload_to_proto(bytes(61))
    assert response.data == bytes(61)


def test_workflow_id_reuse_policy_to_proto():
    assert workflow_id_reuse_policy_to_proto(WorkflowIdReusePolicy.AllowDuplicateFailedOnly) == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY
    assert workflow_id_reuse_policy_to_proto(WorkflowIdReusePolicy.TerminateIfRunning) == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING
    assert workflow_id_reuse_policy_to_proto(WorkflowIdReusePolicy.RejectDuplicate) == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE
    assert workflow_id_reuse_policy_to_proto(WorkflowIdReusePolicy.AllowDuplicate) == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE
    assert workflow_id_reuse_policy_to_proto(WorkflowIdReusePolicy.Invalid) == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_INVALID
    assert workflow_id_reuse_policy_to_proto() == workflow_pb2.WORKFLOW_ID_REUSE_POLICY_INVALID


def test_retry_policy_to_proto():
    rp = RetryPolicy(
        initial_interval_in_seconds=60,
        backoff_coefficient=1.0,
        maximum_interval_in_seconds=60,
        maximum_attempts=10,
        non_retriable_error_reasons=["a", "b"],
        expiration_interval_in_seconds=1000,
    )

    response = retry_policy_to_proto(rp)
    assert response.initial_interval.ToSeconds() == rp.initial_interval_in_seconds
    assert response.backoff_coefficient == rp.backoff_coefficient
    assert response.maximum_interval.ToSeconds() == rp.maximum_interval_in_seconds
    assert response.maximum_attempts == rp.maximum_attempts
    assert response.non_retryable_error_reasons == rp.non_retriable_error_reasons
    assert response.expiration_interval.ToSeconds() == rp.expiration_interval_in_seconds


def test_memo_to_proto():
    m = Memo(fields={"a": bytes(61)})

    response = memo_to_proto(m)
    assert len(response.fields) == 1
    assert "a" in response.fields
    assert response.fields["a"].data == bytes(61)


def test_search_attributes_to_proto():
    sa = SearchAttributes(indexed_fields={"a": bytes(61)})

    response = search_attributes_to_proto(sa)
    assert len(response.indexed_fields) == 1
    assert "a" in response.indexed_fields
    assert response.indexed_fields["a"].data == bytes(61)


def test_header_to_proto():
    h = Header(fields={"a": bytes(61)})

    response = header_to_proto(h)
    assert len(response.fields) == 1
    assert "a" in response.fields
    assert response.fields["a"].data == bytes(61)