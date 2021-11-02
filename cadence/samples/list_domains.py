import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2

from cadence.gateway.cadence.client import WorkflowClient

if __name__ == "__main__":
    request = service_domain_pb2.ListDomainsRequest(page_size=20, next_page_token=bytes(0))
    wfc = WorkflowClient()
    result = wfc.list_domains(request)
    for domain in result.domains:
        print(domain.name)
