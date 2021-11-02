from typing import List, Tuple
import grpc
import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
import uber.cadence.api.v1.service_domain_pb2_grpc as service_domain_pb2_grpc


class WorkflowClient(object):
    """
    Client for gRPC functionality
    """
    host = 'localhost'
    server_port = 7833
    timeout = 300  # 5 minutes

    def __init__(self):
        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.domain = service_domain_pb2_grpc.DomainAPIStub(self.channel)

    @staticmethod
    def get_metadata() -> List[Tuple[str, str]]:
        return [('rpc-caller', 'python-client'), ('rpc-service', 'cadence-frontend'), ('rpc-encoding', 'proto')]

    def list_domains(self, request: service_domain_pb2.ListDomainsRequest) -> service_domain_pb2.ListDomainsResponse:
        response = self.domain.ListDomains.with_call(
            request,
            metadata=self.get_metadata(),
            timeout=self.timeout
        )
        return response[0]
