# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from uber.cadence.api.v1 import service_worker_pb2 as uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2


class WorkerAPIStub(object):
    """WorkerAPI is exposed to provide support for long running applications.  Such applications are
    expected to have a worker which regularly polls for DecisionTask and ActivityTask from the WorkflowService.  For each
    DecisionTask, application is expected to process the history of events for that session and respond back with next
    decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
    with completion or failure.  Worker is expected to regularly heartbeat while activity task is running.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PollForDecisionTask = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/PollForDecisionTask',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskResponse.FromString,
                )
        self.RespondDecisionTaskCompleted = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondDecisionTaskCompleted',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedResponse.FromString,
                )
        self.RespondDecisionTaskFailed = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondDecisionTaskFailed',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedResponse.FromString,
                )
        self.PollForActivityTask = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/PollForActivityTask',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskResponse.FromString,
                )
        self.RespondActivityTaskCompleted = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCompleted',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedResponse.FromString,
                )
        self.RespondActivityTaskCompletedByID = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCompletedByID',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDResponse.FromString,
                )
        self.RespondActivityTaskFailed = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskFailed',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedResponse.FromString,
                )
        self.RespondActivityTaskFailedByID = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskFailedByID',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDResponse.FromString,
                )
        self.RespondActivityTaskCanceled = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCanceled',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledResponse.FromString,
                )
        self.RespondActivityTaskCanceledByID = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCanceledByID',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDResponse.FromString,
                )
        self.RecordActivityTaskHeartbeat = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RecordActivityTaskHeartbeat',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatResponse.FromString,
                )
        self.RecordActivityTaskHeartbeatByID = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RecordActivityTaskHeartbeatByID',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDResponse.FromString,
                )
        self.RespondQueryTaskCompleted = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/RespondQueryTaskCompleted',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedResponse.FromString,
                )
        self.ResetStickyTaskList = channel.unary_unary(
                '/uber.cadence.api.v1.WorkerAPI/ResetStickyTaskList',
                request_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListRequest.SerializeToString,
                response_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListResponse.FromString,
                )


class WorkerAPIServicer(object):
    """WorkerAPI is exposed to provide support for long running applications.  Such applications are
    expected to have a worker which regularly polls for DecisionTask and ActivityTask from the WorkflowService.  For each
    DecisionTask, application is expected to process the history of events for that session and respond back with next
    decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
    with completion or failure.  Worker is expected to regularly heartbeat while activity task is running.
    """

    def PollForDecisionTask(self, request, context):
        """PollForDecisionTask is called by application worker to process DecisionTask from a specific taskList.
        A DecisionTask is dispatched to callers for active workflow executions, with pending decisions.
        Application is then expected to call 'RespondDecisionTaskCompleted' API when it is done processing the DecisionTask.
        It will also create a 'DecisionTaskStarted' event in the history for that session before handing off DecisionTask to
        application worker.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondDecisionTaskCompleted(self, request, context):
        """RespondDecisionTaskCompleted is called by application worker to complete a DecisionTask handed as a result of
        'PollForDecisionTask' API call.  Completing a DecisionTask will result in new events for the workflow execution and
        potentially new ActivityTask being created for corresponding decisions.  It will also create a DecisionTaskCompleted
        event in the history for that session.  Use the 'taskToken' provided as response of PollForDecisionTask API call
        for completing the DecisionTask.
        The response could contain a new decision task if there is one or if the request asking for one.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondDecisionTaskFailed(self, request, context):
        """RespondDecisionTaskFailed is called by application worker to indicate failure.  This results in
        DecisionTaskFailedEvent written to the history and a new DecisionTask created.  This API can be used by client to
        either clear sticky tasklist or report any panics during DecisionTask processing.  Cadence will only append first
        DecisionTaskFailed event to the history of workflow execution for consecutive failures.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PollForActivityTask(self, request, context):
        """PollForActivityTask is called by application worker to process ActivityTask from a specific taskList.  ActivityTask
        is dispatched to callers whenever a ScheduleTask decision is made for a workflow execution.
        Application is expected to call 'RespondActivityTaskCompleted' or 'RespondActivityTaskFailed' once it is done
        processing the task.
        Application also needs to call 'RecordActivityTaskHeartbeat' API within 'heartbeatTimeoutSeconds' interval to
        prevent the task from getting timed out.  An event 'ActivityTaskStarted' event is also written to workflow execution
        history before the ActivityTask is dispatched to application worker.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskCompleted(self, request, context):
        """RespondActivityTaskCompleted is called by application worker when it is done processing an ActivityTask.  It will
        result in a new 'ActivityTaskCompleted' event being written to the workflow history and a new DecisionTask
        created for the workflow so new decisions could be made.  Use the 'taskToken' provided as response of
        PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
        anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskCompletedByID(self, request, context):
        """RespondActivityTaskCompletedByID is called by application worker when it is done processing an ActivityTask.
        It will result in a new 'ActivityTaskCompleted' event being written to the workflow history and a new DecisionTask
        created for the workflow so new decisions could be made.  Similar to RespondActivityTaskCompleted but use Domain,
        WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
        if the these IDs are not valid anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskFailed(self, request, context):
        """RespondActivityTaskFailed is called by application worker when it is done processing an ActivityTask.  It will
        result in a new 'ActivityTaskFailed' event being written to the workflow history and a new DecisionTask
        created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
        PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
        anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskFailedByID(self, request, context):
        """RespondActivityTaskFailedByID is called by application worker when it is done processing an ActivityTask.
        It will result in a new 'ActivityTaskFailed' event being written to the workflow history and a new DecisionTask
        created for the workflow instance so new decisions could be made.  Similar to RespondActivityTaskFailed but use
        Domain, WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
        if the these IDs are not valid anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskCanceled(self, request, context):
        """RespondActivityTaskCanceled is called by application worker when it is successfully canceled an ActivityTask.
        It will result in a new 'ActivityTaskCanceled' event being written to the workflow history and a new DecisionTask
        created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
        PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
        anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondActivityTaskCanceledByID(self, request, context):
        """RespondActivityTaskCanceledByID is called by application worker when it is successfully canceled an ActivityTask.
        It will result in a new 'ActivityTaskCanceled' event being written to the workflow history and a new DecisionTask
        created for the workflow instance so new decisions could be made.  Similar to RespondActivityTaskCanceled but use
        Domain, WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
        if the these IDs are not valid anymore due to activity timeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordActivityTaskHeartbeat(self, request, context):
        """RecordActivityTaskHeartbeat is called by application worker while it is processing an ActivityTask.  If worker fails
        to heartbeat within 'heartbeatTimeoutSeconds' interval for the ActivityTask, then it will be marked as timedout and
        'ActivityTaskTimedOut' event will be written to the workflow history.  Calling 'RecordActivityTaskHeartbeat' will
        fail with 'EntityNotExistsError' in such situations.  Use the 'taskToken' provided as response of
        PollForActivityTask API call for heartbeating.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordActivityTaskHeartbeatByID(self, request, context):
        """RecordActivityTaskHeartbeatByID is called by application worker while it is processing an ActivityTask.  If worker
        fails to heartbeat within 'heartbeatTimeoutSeconds' interval for the ActivityTask, then it will be marked as
        timed out and 'ActivityTaskTimedOut' event will be written to the workflow history.
        Calling 'RecordActivityTaskHeartbeatByID' will fail with 'EntityNotExistsError' in such situations.  Instead of
        using 'taskToken' like in RecordActivityTaskHeartbeat, use Domain, WorkflowID and ActivityID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondQueryTaskCompleted(self, request, context):
        """RespondQueryTaskCompleted is called by application worker to complete a QueryTask (which is a DecisionTask for query)
        as a result of 'PollForDecisionTask' API call. Completing a QueryTask will unblock the client call to 'QueryWorkflow'
        API and return the query result to client as a response to 'QueryWorkflow' API call.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetStickyTaskList(self, request, context):
        """Reset the sticky tasklist related information in mutable state of a given workflow.
        Things cleared are:
        1. StickyTaskList
        2. StickyScheduleToStartTimeout
        3. ClientLibraryVersion
        4. ClientFeatureVersion
        5. ClientImpl
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PollForDecisionTask': grpc.unary_unary_rpc_method_handler(
                    servicer.PollForDecisionTask,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskResponse.SerializeToString,
            ),
            'RespondDecisionTaskCompleted': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondDecisionTaskCompleted,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedResponse.SerializeToString,
            ),
            'RespondDecisionTaskFailed': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondDecisionTaskFailed,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedResponse.SerializeToString,
            ),
            'PollForActivityTask': grpc.unary_unary_rpc_method_handler(
                    servicer.PollForActivityTask,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskResponse.SerializeToString,
            ),
            'RespondActivityTaskCompleted': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskCompleted,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedResponse.SerializeToString,
            ),
            'RespondActivityTaskCompletedByID': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskCompletedByID,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDResponse.SerializeToString,
            ),
            'RespondActivityTaskFailed': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskFailed,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedResponse.SerializeToString,
            ),
            'RespondActivityTaskFailedByID': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskFailedByID,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDResponse.SerializeToString,
            ),
            'RespondActivityTaskCanceled': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskCanceled,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledResponse.SerializeToString,
            ),
            'RespondActivityTaskCanceledByID': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondActivityTaskCanceledByID,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDResponse.SerializeToString,
            ),
            'RecordActivityTaskHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordActivityTaskHeartbeat,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatResponse.SerializeToString,
            ),
            'RecordActivityTaskHeartbeatByID': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordActivityTaskHeartbeatByID,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDResponse.SerializeToString,
            ),
            'RespondQueryTaskCompleted': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondQueryTaskCompleted,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedResponse.SerializeToString,
            ),
            'ResetStickyTaskList': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetStickyTaskList,
                    request_deserializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListRequest.FromString,
                    response_serializer=uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uber.cadence.api.v1.WorkerAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkerAPI(object):
    """WorkerAPI is exposed to provide support for long running applications.  Such applications are
    expected to have a worker which regularly polls for DecisionTask and ActivityTask from the WorkflowService.  For each
    DecisionTask, application is expected to process the history of events for that session and respond back with next
    decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
    with completion or failure.  Worker is expected to regularly heartbeat while activity task is running.
    """

    @staticmethod
    def PollForDecisionTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/PollForDecisionTask',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForDecisionTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondDecisionTaskCompleted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondDecisionTaskCompleted',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskCompletedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondDecisionTaskFailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondDecisionTaskFailed',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondDecisionTaskFailedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PollForActivityTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/PollForActivityTask',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.PollForActivityTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskCompleted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCompleted',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskCompletedByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCompletedByID',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCompletedByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskFailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskFailed',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskFailedByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskFailedByID',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskFailedByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskCanceled(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCanceled',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondActivityTaskCanceledByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondActivityTaskCanceledByID',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondActivityTaskCanceledByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordActivityTaskHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RecordActivityTaskHeartbeat',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordActivityTaskHeartbeatByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RecordActivityTaskHeartbeatByID',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RecordActivityTaskHeartbeatByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondQueryTaskCompleted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/RespondQueryTaskCompleted',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.RespondQueryTaskCompletedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetStickyTaskList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uber.cadence.api.v1.WorkerAPI/ResetStickyTaskList',
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListRequest.SerializeToString,
            uber_dot_cadence_dot_api_dot_v1_dot_service__worker__pb2.ResetStickyTaskListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
