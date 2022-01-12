import sys

from cadence.cadence_types import RegisterDomainRequest
from cadence.gateway.cadence.enums import DefaultPort, ConnectionProtocol
from cadence.workflowservice import WorkflowService

if __name__ == "__main__":
    service = WorkflowService.create("localhost", DefaultPort.GRPC, 10000, ConnectionProtocol.GRPC)

    domain = "test-domain-grpc"

    register_domain_request = RegisterDomainRequest()
    register_domain_request.name = domain
    register_domain_request.workflow_execution_retention_period_in_days = 1

    _, err = service.register_domain(register_domain_request)
    if err:
        print(f"error type {type(err)}")
    else:
        print(f"Registered domain {domain}")
