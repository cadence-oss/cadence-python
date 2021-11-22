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
from cadence.cadence_types import StartWorkflowExecutionRequest, WorkflowType, TaskList, TaskListKind
from uber.cadence.api.v1 import service_workflow_pb2, common_pb2, tasklist_pb2


def start_workflow_execution_request_dataclass_to_proto(request: StartWorkflowExecutionRequest) -> service_workflow_pb2.StartWorkflowExecutionRequest:
    return service_workflow_pb2.StartWorkflowExecutionRequest(
        domain = request.domain,
        workflow_id = request.workflow_id,
        workflow_type = workflow_type_dataclass_to_proto(request.workflow_type),
        task_list = task_list_to_proto(request.task_list)
    )

def workflow_type_dataclass_to_proto(request: WorkflowType) -> common_pb2.WorkflowType:
    return common_pb2.WorkflowType(
        name = request.name
    )

def task_list_to_proto(request: TaskList) -> tasklist_pb2:
    return tasklist_pb2.TaskList(
        name = request.name,
        kind = task_list_kind_to_proto(request.kind)
    )

def task_list_kind_to_proto(request: TaskListKind) -> tasklist_pb2.TaskListKind:
    if request == TaskListKind.STICKY:
        return tasklist_pb2.TASK_LIST_KIND_STICKY
    elif request == TaskListKind.NORMAL:
        return tasklist_pb2.TASK_LIST_KIND_NORMAL
    else:
        return tasklist_pb2.TASK_LIST_KIND_INVALID