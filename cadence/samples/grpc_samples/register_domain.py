import sys

from cadence.cadence_types import RegisterDomainRequest
from cadence.workflowservice import WorkflowService, PROTOCOL_GRPC

if __name__ == "__main__":
    service = WorkflowService.create("localhost", 7833, 10000, PROTOCOL_GRPC)

    domain = "test-domain-grpc"

    register_domain_request = RegisterDomainRequest()
    register_domain_request.name = domain
    register_domain_request.workflow_execution_retention_period_in_days = 1

    _, err = service.register_domain(register_domain_request)
    if err:
        print(err)
    else:
        print(f"Registered domain {domain}")
