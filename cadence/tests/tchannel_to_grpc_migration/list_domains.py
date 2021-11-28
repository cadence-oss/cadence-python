import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsRequest
from cadence.workflowservice import WorkflowService, PROTOCOL_GRPC, PROTOCOL_TCHANNEL

if __name__ == "__main__":
    request = ListDomainsRequest(
        page_size=20,
        next_page_token=bytes(0)
    )
    wfc = WorkflowService.create('localhost', 7833, 300, PROTOCOL_GRPC)
    grpc_result, errorOne = wfc.list_domains(request)
    wfc = WorkflowService.create('localhost', 7933, 300, PROTOCOL_TCHANNEL)
    tchannel_result, errorTwo = wfc.list_domains(request)

    assert errorOne is None
    assert errorTwo is None
    assert len(grpc_result.domains) == len(tchannel_result.domains)
    for i in range(len(grpc_result.domains)):
        assert grpc_result.domains[i].domain_info.uuid == tchannel_result.domains[i].domain_info.uuid
        assert grpc_result.domains[i].domain_info.name == tchannel_result.domains[i].domain_info.name
