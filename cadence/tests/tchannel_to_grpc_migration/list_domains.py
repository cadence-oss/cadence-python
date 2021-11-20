import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsRequest
from cadence.workflowservice import WorkflowService, PROTOCOL_GRPC, PROTOCOL_TCHANNEL

if __name__ == "__main__":
    request = ListDomainsRequest(
        page_size=20,
        next_page_token=bytes(0)
    )
    wfc = WorkflowService.create('localhost', 7833, 300, PROTOCOL_GRPC)
    result = wfc.list_domains(request)
    for domain in result[0].domains:
        print(domain.domain_info.uuid)
        print(domain.domain_info.name)


    wfc = WorkflowService.create('localhost', 7933, 300, PROTOCOL_TCHANNEL)
    result = wfc.list_domains(request)
    for domain in result[0].domains:
        print(domain.domain_info.uuid)
        print(domain.domain_info.name)