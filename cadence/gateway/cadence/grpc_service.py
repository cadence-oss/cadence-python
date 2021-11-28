from typing import Tuple
import grpc
import uber.cadence.api.v1.service_domain_pb2_grpc as service_domain_pb2_grpc
import uber.cadence.api.v1.service_workflow_pb2_grpc as service_workflow_pb2_grpc
from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse
from cadence.gateway.cadence.interface import CadenceServiceInterface
from cadence.mapping.grpc.domain import \
    proto_list_domains_response_to_dataclass, list_domains_request_dataclass_to_proto
from cadence.mapping.grpc.service_workflow import start_workflow_execution_request_dataclass_to_proto, start_workflow_execution_response_to_dataclass


class CadenceGrpcService(CadenceServiceInterface):
    """
    Client for gRPC functionality
    """
    metadata = [('rpc-caller', 'python-client'), ('rpc-service', 'cadence-frontend'), ('rpc-encoding', 'proto')]

    def __init__(self, host: str = 'localhost', port: int = 7833, timeout: int = 300):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(host, port))

        # stubs
        self.domain = service_domain_pb2_grpc.DomainAPIStub(self.channel)
        self.service_workflow = service_workflow_pb2_grpc.WorkflowAPIStub(self.channel)

    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        grpc_request = list_domains_request_dataclass_to_proto(request)
        response = self.domain.ListDomains.with_call(
            grpc_request,
            metadata=self.metadata,
            timeout=self.timeout
        )
        return (proto_list_domains_response_to_dataclass(response[0]), None) #TODO check how errors are process via tchannel

    def start_workflow(self, request: StartWorkflowExecutionRequest) -> Tuple[StartWorkflowExecutionResponse, object]:
        grpc_request = start_workflow_execution_request_dataclass_to_proto(request)
        response = self.service_workflow.StartWorkflowExecution.with_call(
            grpc_request,
            metadata=self.metadata,
            timeout=self.timeout
        )
        return (start_workflow_execution_response_to_dataclass(response[0]), None) #TODO check how errors are process via tchannel