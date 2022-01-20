import grpc
from grpc_status import rpc_status

from cadence.errors import WorkflowExecutionAlreadyStartedError, ServiceBusyError, QueryFailedError, LimitExceededError, \
    CancellationAlreadyRequestedError, ClientVersionNotSupportedError, DomainAlreadyExistsError, DomainNotActiveError, \
    EntityNotExistsError, WorkflowExecutionAlreadyCompletedError, FeatureNotEnabledError
from uber.cadence.api.v1 import error_pb2


def process_error(e: grpc.RpcError) -> Exception:
    status = rpc_status.from_call(e)
    for detail in status.details:
        if detail.Is(error_pb2.CancellationAlreadyRequestedError.DESCRIPTOR):
            return CancellationAlreadyRequestedError()
        elif detail.Is(error_pb2.ClientVersionNotSupportedError.DESCRIPTOR):
            error = error_pb2.ClientVersionNotSupportedError()
            detail.Unpack(error)
            return ClientVersionNotSupportedError(feature_version=error.feature_version, client_impl=error.client_impl, supported_versions=error.supported_versions)
        elif detail.Is(error_pb2.DomainAlreadyExistsError.DESCRIPTOR):
            return DomainAlreadyExistsError()
        elif detail.Is(error_pb2.DomainNotActiveError.DESCRIPTOR):
            error = error_pb2.DomainNotActiveError()
            detail.Unpack(error)
            return DomainNotActiveError(domainName=error.domain, currentCluster=error.current_cluster, activeCluster=error.active_cluster)
        elif detail.Is(error_pb2.EntityNotExistsError.DESCRIPTOR):
            error = error_pb2.EntityNotExistsError()
            detail.Unpack(error)
            return EntityNotExistsError(currentCluster=error.current_cluster, activeCluster=error.active_cluster)
        elif detail.Is(error_pb2.FeatureNotEnabledError.DESCRIPTOR):
            error = error_pb2.FeatureNotEnabledError()
            detail.Unpack(error)
            return FeatureNotEnabledError(featureFlag=error.feature_flag)
        elif detail.Is(error_pb2.LimitExceededError.DESCRIPTOR):
            return LimitExceededError()
        elif detail.Is(error_pb2.QueryFailedError.DESCRIPTOR):
            return QueryFailedError()
        elif detail.Is(error_pb2.ServiceBusyError.DESCRIPTOR):
            return ServiceBusyError(message=status.message)
        elif detail.Is(error_pb2.WorkflowExecutionAlreadyCompletedError.DESCRIPTOR):
            return WorkflowExecutionAlreadyCompletedError()
        elif detail.Is(error_pb2.WorkflowExecutionAlreadyStartedError.DESCRIPTOR):
            error = error_pb2.WorkflowExecutionAlreadyStartedError()
            detail.Unpack(error)
            return WorkflowExecutionAlreadyStartedError(startRequestId=error.start_request_id, runId=error.run_id)
        else:
            raise RuntimeError('Unexpected failure: %s' % detail)