from unittest import TestCase
from uuid import uuid4
import time

from cadence.gateway.cadence.enums import DefaultPort, ConnectionProtocol
from cadence.cadence_types import RegisterDomainRequest, DescribeDomainRequest, \
    UpdateDomainRequest, DomainConfiguration, DomainReplicationConfiguration
from cadence.workflowservice import WorkflowService


class TestStartWorkflow(TestCase):

    def setUp(self) -> None:
        self.service = WorkflowService.create("localhost", port=DefaultPort.GRPC, protocol=ConnectionProtocol.GRPC, timeout=1000)
        time.sleep(0.5)


    def test_describe_domain(self):
        register_request = RegisterDomainRequest()
        register_request.name = str(uuid4())
        register_request.workflow_execution_retention_period_in_days = 1
        self.service.register_domain(register_request)
        request = DescribeDomainRequest()
        request.name = register_request.name
        response, err = self.service.describe_domain(request)
        self.assertIsNone(err)
        self.assertIsNotNone(response)

    def test_update_domain(self):
        register_request = RegisterDomainRequest()
        register_request.name = str(uuid4())
        register_request.replication_configuration = DomainReplicationConfiguration()
        register_request.workflow_execution_retention_period_in_days = 1
        self.service.register_domain(register_request)
        request = UpdateDomainRequest()
        request.failover_timeout = 10000
        request.name = register_request.name
        request.configuration = DomainConfiguration()
        request.configuration.workflow_execution_retention_period_in_days = 10
        request.replication_configuration = DomainReplicationConfiguration()
        response, err = self.service.update_domain(request)
        self.assertIsNone(err)
        self.assertIsNotNone(response)
        self.assertEqual(10, response.configuration.workflow_execution_retention_period_in_days)


    def tearDown(self) -> None:
        self.service.close()
