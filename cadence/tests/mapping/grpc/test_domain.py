from cadence.cadence_types import RegisterDomainRequest, ArchivalStatus, ListDomainsRequest
from cadence.mapping.grpc.domain import register_domain_request_dataclass_to_proto, days_to_seconds, ms_to_days, \
    list_domains_request_dataclass_to_proto, proto_list_domains_response_to_dataclass, \
    proto_domain_to_describe_domain_response_dataclass
from uber.cadence.api.v1 import domain_pb2, service_domain_pb2


def test_ms_to_days():
    seven_days_in_ms = 604800000
    days = ms_to_days(seven_days_in_ms)
    assert days == 7


def test_days_to_seconds():
    seconds = days_to_seconds(7)
    assert seconds == 604800


def test_list_domains_request_dataclass_to_proto():
    list_domains_request = ListDomainsRequest(
        page_size=100,
        next_page_token=bytes("thetoken", "utf-8"),
    )

    list_domains_request_proto = list_domains_request_dataclass_to_proto(list_domains_request)
    assert list_domains_request_proto.next_page_token == b'thetoken'
    assert list_domains_request_proto.page_size == 100


def test_proto_list_domains_response_to_dataclass():
    domain_response = service_domain_pb2.ListDomainsResponse(
        domains=[domain_pb2.Domain(
            name="the_domain"
        )],
        next_page_token=bytes("thetoken", "utf-8"),
    )
    dataclass = proto_list_domains_response_to_dataclass(domain_response)
    assert dataclass.next_page_token == b'thetoken'
    assert dataclass.domains[0].domain_info.name == domain_response.domains[0].name


def test_proto_domain_to_describe_domain_dataclass():
    domain = domain_pb2.Domain(
        name="the_domain",
        history_archival_uri="the-uri",
        active_cluster_name="cluster_test",
        failover_version=12,
        is_global_domain=True,
    )

    describe_domain_response = proto_domain_to_describe_domain_response_dataclass(domain)

    assert describe_domain_response.domain_info.name == domain.name
    assert describe_domain_response.is_global_domain == domain.is_global_domain
    assert describe_domain_response.failover_version == domain.failover_version
    assert describe_domain_response.replication_configuration.active_cluster_name == domain.active_cluster_name
    assert describe_domain_response.configuration.history_archival_uri == domain.history_archival_uri


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
    assert proto.workflow_execution_retention_period.ToSeconds() == 604800
    assert proto.active_cluster_name == register_domain.active_cluster_name
    assert proto.data == register_domain.data
    assert proto.security_token == register_domain.security_token
    assert proto.history_archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED
    assert proto.history_archival_uri == register_domain.archival_bucket_name
    assert proto.visibility_archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED
    assert proto.visibility_archival_uri == register_domain.visibility_archival_uri
