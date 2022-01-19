from typing import Tuple, Callable
import grpc
import uber.cadence.api.v1.service_domain_pb2_grpc as service_domain_pb2_grpc
import uber.cadence.api.v1.service_workflow_pb2_grpc as service_workflow_pb2_grpc
from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse, RegisterDomainRequest, DescribeDomainRequest, DescribeDomainResponse
from cadence.gateway.cadence.interface import CadenceServiceInterface
from cadence.grpc_errors import process_error
from cadence.mapping.grpc.domain import \
    proto_list_domains_response_to_dataclass, list_domains_request_dataclass_to_proto, \
    register_domain_request_dataclass_to_proto, describe_domain_request_dataclass_to_proto, \
    proto_describe_domain_response_to_describe_domain_response_dataclass
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

    def close(self):
        self.channel.close()

    def set_next_timeout_cb(self, cb: Callable):
        raise NotImplementedError

    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        grpc_request = list_domains_request_dataclass_to_proto(request)
        try:
            response = self.domain.ListDomains.with_call(
                grpc_request,
                metadata=self.metadata,
                timeout=self.timeout
            )
            return proto_list_domains_response_to_dataclass(response[0]), None
        except grpc.RpcError as e:
            return None, process_error(e)

    def start_workflow(self, request: StartWorkflowExecutionRequest) -> Tuple[StartWorkflowExecutionResponse, object]:
        grpc_request = start_workflow_execution_request_dataclass_to_proto(request)
        try:
            response = self.service_workflow.StartWorkflowExecution.with_call(
                grpc_request,
                metadata=self.metadata,
                timeout=self.timeout
            )
            return start_workflow_execution_response_to_dataclass(response[0]), None
        except grpc.RpcError as e:
            return None, process_error(e)

    def register_domain(self, request: RegisterDomainRequest) -> Tuple[None, object]:
        grpc_request = register_domain_request_dataclass_to_proto(request)
        try:
            self.domain.RegisterDomain.with_call(
                grpc_request,
                metadata=self.metadata,
                timeout=self.timeout
            )
            return None, None
        except grpc.RpcError as e:
            return None, process_error(e)


    def describe_domain(self, request: DescribeDomainRequest) -> Tuple[DescribeDomainResponse, object]:
        grpc_request = describe_domain_request_dataclass_to_proto(request)
        try:
            response = self.domain.DescribeDomain.with_call(
                grpc_request,
                metadata=self.metadata,
                timeout=self.timeout
            )
            return proto_describe_domain_response_to_describe_domain_response_dataclass(response[0]), None
        except grpc.RpcError as e:
            return None, process_error(e)
