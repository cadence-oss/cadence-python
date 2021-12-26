from cadence.cadence_types import RegisterDomainRequest, ArchivalStatus
from cadence.mapping.grpc.domain import register_domain_request_dataclass_to_proto, days_to_seconds
from uber.cadence.api.v1 import domain_pb2


def test_register_domain_request_dataclass_to_proto():
    register_domain = RegisterDomainRequest()
    register_domain.description = "a"
    register_domain.owner_email = "b"
    register_domain.workflow_execution_retention_period_in_days = 7
    register_domain.active_cluster_name = "my_name"
    register_domain.data = {"a": "a", "b": "b"}
    register_domain.security_token = "security"
    register_domain.archival_status = ArchivalStatus.ENABLED
    register_domain.archival_bucket_name = "/a/b/c"
    register_domain.is_global_domain = True

    proto = register_domain_request_dataclass_to_proto(register_domain)

    assert proto.description == register_domain.description
    assert proto.owner_email == register_domain.owner_email
    assert proto.workflow_execution_retention_period.ToSeconds() == days_to_seconds(register_domain.workflow_execution_retention_period_in_days)
    assert proto.active_cluster_name == register_domain.active_cluster_name
    assert proto.data == register_domain.data
    assert proto.security_token == register_domain.security_token
    assert proto.history_archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED
    assert proto.history_archival_uri == register_domain.archival_bucket_name
    assert proto.visibility_archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED
    assert proto.visibility_archival_uri == register_domain.visibility_archival_uri
