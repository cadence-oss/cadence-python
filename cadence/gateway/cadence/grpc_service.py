from typing import Tuple
import grpc
import uber.cadence.api.v1.service_domain_pb2_grpc as service_domain_pb2_grpc
from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse
from cadence.gateway.cadence.interface import CadenceServiceInterface
from cadence.mapping.grpc.domain import \
    proto_list_domains_response_to_dataclass, list_domains_request_dataclass_to_proto


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

    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        grpc_request = list_domains_request_dataclass_to_proto(request)
        response = self.domain.ListDomains.with_call(
            grpc_request,
            metadata=self.metadata,
            timeout=self.timeout
        )
        return (proto_list_domains_response_to_dataclass(response[0]), response[1])