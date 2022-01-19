from google.protobuf import duration_pb2, timestamp_pb2

from cadence.cadence_types import RegisterDomainRequest, ArchivalStatus, ListDomainsRequest, DomainStatus, \
    ClusterReplicationConfiguration, DescribeDomainRequest
from cadence.mapping.grpc.domain import register_domain_request_dataclass_to_proto, days_to_seconds, ms_to_days, \
    list_domains_request_dataclass_to_proto, proto_list_domains_response_to_dataclass, \
    proto_domain_to_describe_domain_response_dataclass, proto_domain_to_domain_info_dataclass, \
    proto_domain_to_replication_configuration_dataclass, cluster_replication_configuration_metadata_to_proto, \
    proto_domain_status_to_dataclass, proto_domain_to_domain_configuration_dataclass, \
    proto_archival_status_to_dataclass, archival_status_dataclass_to_proto, proto_bad_binaries_to_dataclass, \
    proto_bad_binary_info_to_dataclass, proto_cluster_replication_configuration_to_metadata, \
    proto_describe_domain_response_to_describe_domain_response_dataclass, describe_domain_request_dataclass_to_proto
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


def test_proto_describe_domain_response_to_describe_domain_response_dataclass():
    ddr = service_domain_pb2.DescribeDomainResponse(
        domain=domain_pb2.Domain(
            name="the_domain",
            history_archival_uri="the-uri",
            active_cluster_name="cluster_test",
            failover_version=12,
            is_global_domain=True,
        )
    )

    describe_domain_response = proto_describe_domain_response_to_describe_domain_response_dataclass(ddr)

    assert describe_domain_response.domain_info.name == ddr.domain.name
    assert describe_domain_response.is_global_domain == ddr.domain.is_global_domain
    assert describe_domain_response.failover_version == ddr.domain.failover_version
    assert describe_domain_response.replication_configuration.active_cluster_name == ddr.domain.active_cluster_name
    assert describe_domain_response.configuration.history_archival_uri == ddr.domain.history_archival_uri


def test_describe_domain_request_dataclass_to_proto():
    ddr = DescribeDomainRequest(name="", uuid="uuid")
    describe_domain_request = describe_domain_request_dataclass_to_proto(ddr)

    assert describe_domain_request.name == ""
    assert describe_domain_request.id == describe_domain_request.id

    ddr = DescribeDomainRequest(name="name", uuid="")
    describe_domain_request = describe_domain_request_dataclass_to_proto(ddr)

    assert describe_domain_request.name == ddr.name
    assert describe_domain_request.id == ""

    ddr = DescribeDomainRequest(name="name", uuid="uuid")
    describe_domain_request = describe_domain_request_dataclass_to_proto(ddr)

    assert describe_domain_request.name == ddr.name
    assert describe_domain_request.id == ""


def test_proto_domain_to_domain_info_dataclass():
    domain = domain_pb2.Domain(
        name="the_domain",
        description="the description",
        owner_email="rodrigo@test.com",
        data={"a": "a", "b": "b"},
        id="123-456-789",
    )

    domain_info = proto_domain_to_domain_info_dataclass(domain)

    assert domain_info.name == domain.name
    assert domain_info.description == domain.description
    assert domain_info.owner_email == domain.owner_email
    assert domain_info.data == domain.data
    assert domain_info.uuid == domain.id
    assert domain_info.status == DomainStatus.INVALID


def test_proto_domain_to_domain_info_dataclass_empty_data():
    domain = domain_pb2.Domain(
        data={},
    )

    domain_info = proto_domain_to_domain_info_dataclass(domain)
    assert domain_info.data == domain.data


def test_proto_domain_to_replication_configuration_dataclass_empty_clusters():
    domain = domain_pb2.Domain(
        active_cluster_name="The cluster",
        clusters=[],
    )

    rc = proto_domain_to_replication_configuration_dataclass(domain)

    assert rc.active_cluster_name == domain.active_cluster_name
    assert len(rc.clusters) == len(domain.clusters)


def test_proto_domain_to_replication_configuration_dataclass_():
    domain = domain_pb2.Domain(
        active_cluster_name="The cluster",
        clusters=[domain_pb2.ClusterReplicationConfiguration(
            cluster_name="cluster_a"
        ), domain_pb2.ClusterReplicationConfiguration(
            cluster_name="cluster_b"
        )]
    )

    rc = proto_domain_to_replication_configuration_dataclass(domain)

    assert rc.active_cluster_name == domain.active_cluster_name
    assert len(rc.clusters) == len(domain.clusters)
    assert rc.clusters[0].cluster_name == domain.clusters[0].cluster_name
    assert rc.clusters[1].cluster_name == domain.clusters[1].cluster_name


def test_cluster_replication_configuration_metadata_to_proto():
    crr = domain_pb2.ClusterReplicationConfiguration(
        cluster_name="cluster_b"
    )

    rc = cluster_replication_configuration_metadata_to_proto(crr)

    assert rc.cluster_name == crr.cluster_name


def test_proto_domain_status_to_dataclass():
    assert proto_domain_status_to_dataclass(domain_pb2.DOMAIN_STATUS_DELETED) == DomainStatus.DELETED
    assert proto_domain_status_to_dataclass(domain_pb2.DOMAIN_STATUS_REGISTERED) == DomainStatus.REGISTERED
    assert proto_domain_status_to_dataclass(domain_pb2.DOMAIN_STATUS_DEPRECATED) == DomainStatus.DEPRECATED
    assert proto_domain_status_to_dataclass(None) == DomainStatus.INVALID


def test_proto_domain_to_domain_configuration_dataclass_all_populated():
    domain = domain_pb2.Domain(
        workflow_execution_retention_period=duration_pb2.Duration(seconds=604800),
        history_archival_status=domain_pb2.ARCHIVAL_STATUS_ENABLED,
        history_archival_uri="thehistoryuri",
        visibility_archival_status=domain_pb2.ARCHIVAL_STATUS_DISABLED,
        visibility_archival_uri="visibilityuri",
        bad_binaries=domain_pb2.BadBinaries(
            binaries={"key": domain_pb2.BadBinaryInfo(reason="thereason")}
        )
    )

    domain_configuration = proto_domain_to_domain_configuration_dataclass(domain)

    assert domain_configuration.workflow_execution_retention_period_in_days == 7
    assert domain_configuration.workflow_execution_retention_period == domain.workflow_execution_retention_period.ToMilliseconds()
    assert domain_configuration.emit_metric == True
    assert domain_configuration.archival_status == ArchivalStatus.ENABLED
    assert domain_configuration.archival_bucket_name == domain.history_archival_uri
    assert domain_configuration.visibility_archival_uri == domain.visibility_archival_uri
    assert domain_configuration.visibility_archival_status == ArchivalStatus.DISABLED
    assert domain_configuration.bad_binaries.binaries["key"].reason == domain.bad_binaries.binaries["key"].reason


def test_proto_domain_to_domain_configuration_dataclass_min_values():
    domain = domain_pb2.Domain()

    domain_configuration = proto_domain_to_domain_configuration_dataclass(domain)

    assert domain_configuration.workflow_execution_retention_period_in_days == 0
    assert domain_configuration.workflow_execution_retention_period == domain.workflow_execution_retention_period.ToMilliseconds()
    assert domain_configuration.emit_metric == True
    assert domain_configuration.archival_status == ArchivalStatus.INVALID
    assert domain_configuration.archival_bucket_name == domain.history_archival_uri
    assert domain_configuration.visibility_archival_uri == domain.visibility_archival_uri
    assert domain_configuration.visibility_archival_status == ArchivalStatus.INVALID
    assert len(domain_configuration.bad_binaries.binaries) == len(domain.bad_binaries.binaries)


def test_proto_archival_status_to_dataclass():
    assert proto_archival_status_to_dataclass(domain_pb2.ARCHIVAL_STATUS_ENABLED) == ArchivalStatus.ENABLED
    assert proto_archival_status_to_dataclass(domain_pb2.ARCHIVAL_STATUS_INVALID) == ArchivalStatus.INVALID
    assert proto_archival_status_to_dataclass(domain_pb2.ARCHIVAL_STATUS_DISABLED) == ArchivalStatus.DISABLED
    assert proto_archival_status_to_dataclass(None) == ArchivalStatus.INVALID


def test_archival_status_dataclass_to_proto():
    assert archival_status_dataclass_to_proto(ArchivalStatus.ENABLED) == domain_pb2.ARCHIVAL_STATUS_ENABLED
    assert archival_status_dataclass_to_proto(ArchivalStatus.INVALID) == domain_pb2.ARCHIVAL_STATUS_INVALID
    assert archival_status_dataclass_to_proto(ArchivalStatus.DISABLED) == domain_pb2.ARCHIVAL_STATUS_DISABLED
    assert archival_status_dataclass_to_proto(None) == domain_pb2.ARCHIVAL_STATUS_INVALID


def test_proto_bad_binaries_to_dataclass():
    bad_binaries=domain_pb2.BadBinaries(
        binaries={"key": domain_pb2.BadBinaryInfo(
            reason="thereason",
        ), "key_two": domain_pb2.BadBinaryInfo(
            reason="thereason_2")
        }
    )

    bad_binaries_dataclass = proto_bad_binaries_to_dataclass(bad_binaries)

    assert len(bad_binaries_dataclass.binaries) == 2
    assert bad_binaries.binaries["key"].reason == bad_binaries.binaries["key"].reason
    assert bad_binaries.binaries["key_two"].reason == bad_binaries.binaries["key_two"].reason


def test_proto_bad_binary_info_to_dataclass_all_populated():
    bad_binary_info=domain_pb2.BadBinaryInfo(
        reason="Thereason",
        operator="theoperator",
        created_time=timestamp_pb2.Timestamp(seconds=1)
    )

    bbi = proto_bad_binary_info_to_dataclass(bad_binary_info)

    assert bbi.reason == bad_binary_info.reason
    assert bbi.operator == bad_binary_info.operator
    assert bbi.created_time_nano == 1000000000


def test_proto_bad_binary_info_to_dataclass_min():
    bad_binary_info=domain_pb2.BadBinaryInfo()

    bbi = proto_bad_binary_info_to_dataclass(bad_binary_info)

    assert bbi.reason == bad_binary_info.reason
    assert bbi.operator == bad_binary_info.operator
    assert bbi.created_time_nano == 0


def test_proto_cluster_replication_configuration_to_metadata():
    cluster_replication_configuration = domain_pb2.ClusterReplicationConfiguration(
        cluster_name="cluster_name"
    )

    crc = proto_cluster_replication_configuration_to_metadata(cluster_replication_configuration)
    assert crc.cluster_name == cluster_replication_configuration.cluster_name


def test_cluster_replication_configuration_metadata_to_proto():
    cluster_replication_configuration = ClusterReplicationConfiguration(
        cluster_name="cluster_name"
    )

    crc = cluster_replication_configuration_metadata_to_proto(cluster_replication_configuration)
    assert crc.cluster_name == cluster_replication_configuration.cluster_name


def test_register_domain_request_dataclass_to_proto_all_populated():
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
    assert proto.visibility_archival_status == domain_pb2.ARCHIVAL_STATUS_INVALID
    assert proto.visibility_archival_uri == register_domain.visibility_archival_uri


def test_register_domain_request_dataclass_to_proto_min():
    register_domain = RegisterDomainRequest()

    proto = register_domain_request_dataclass_to_proto(register_domain)

    assert proto.workflow_execution_retention_period.ToSeconds() == 0
    assert proto.data == register_domain.data
    assert proto.history_archival_status == domain_pb2.ARCHIVAL_STATUS_INVALID
    assert proto.visibility_archival_status == domain_pb2.ARCHIVAL_STATUS_INVALID
