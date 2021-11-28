import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsResponse, DescribeDomainResponse, DomainStatus, ArchivalStatus, \
    BadBinaryInfo, BadBinaries, ClusterReplicationConfiguration, ListDomainsRequest, DomainInfo, \
    DomainConfiguration, DomainReplicationConfiguration
from uber.cadence.api.v1 import domain_pb2


def ms_to_days(milliseconds: int) -> int:
    return int(milliseconds / (1000*60*60*24))

def list_domains_request_dataclass_to_proto(request: ListDomainsRequest) -> service_domain_pb2.ListDomainsRequest:
    return service_domain_pb2.ListDomainsRequest(page_size=request.page_size, next_page_token=request.next_page_token)


def proto_list_domains_response_to_dataclass(response: service_domain_pb2.ListDomainsResponse) -> ListDomainsResponse:
    list_domains = ListDomainsResponse(
        domains=[proto_describe_domain_to_dataclass(domain) for domain in response.domains],
        next_page_token=response.next_page_token
    )

    return list_domains


def proto_describe_domain_to_dataclass(
        domain_response: service_domain_pb2.DescribeDomainResponse) -> DescribeDomainResponse:
    domain = DescribeDomainResponse(
        domain_info=proto_domain_info_to_dataclass(domain_response),
        configuration=proto_domain_configuration_do_dataclass(domain_response),
        replication_configuration=proto_replication_configuration_to_dataclass(domain_response),
        failover_version=domain_response.failover_version,
        is_global_domain=domain_response.is_global_domain,
    )

    return domain


def proto_domain_info_to_dataclass(domain_response: service_domain_pb2.DescribeDomainResponse) -> DomainInfo:
    domain_info = DomainInfo(
        name=domain_response.name,
        status=proto_domain_status_to_dataclass(domain_response.status),
        description=domain_response.description,
        owner_email=domain_response.owner_email,
        data={key: value for key, value in domain_response.data.values()},
        uuid=domain_response.id,
    )

    return domain_info


def proto_replication_configuration_to_dataclass(
        domain_response: service_domain_pb2.DescribeDomainResponse) -> DomainReplicationConfiguration:
    replication_configuration = DomainReplicationConfiguration(
        active_cluster_name=domain_response.active_cluster_name,
        clusters=[proto_cluster_replication_configuration_to_metadata(cluster) for cluster in domain_response.clusters]
    )

    return replication_configuration


def proto_domain_status_to_dataclass(ds: domain_pb2.DomainStatus) -> DomainStatus:
    if ds == domain_pb2.DOMAIN_STATUS_REGISTERED:
        return DomainStatus(DomainStatus.REGISTERED)
    elif ds == domain_pb2.DOMAIN_STATUS_DELETED:
        return DomainStatus(DomainStatus.DELETED)
    elif ds == domain_pb2.DOMAIN_STATUS_DEPRECATED:
        return DomainStatus(DomainStatus.DEPRECATED)
    else:
        return DomainStatus(DomainStatus.INVALID)


def proto_domain_configuration_do_dataclass(
        domain_response: service_domain_pb2.DescribeDomainResponse) -> DomainConfiguration:
    domain_configuration = DomainConfiguration(
        workflow_execution_retention_period_in_days=ms_to_days(domain_response.workflow_execution_retention_period.ToMilliseconds()),
        workflow_execution_retention_period=domain_response.workflow_execution_retention_period.ToMilliseconds(),
        emit_metric=True,
        archival_status=proto_archival_status_to_dataclass(domain_response.history_archival_status),
        archival_bucket_name=domain_response.history_archival_uri,
        history_archival_status=proto_archival_status_to_dataclass(domain_response.history_archival_status),
        history_archival_uri=domain_response.history_archival_uri,
        visibility_archival_status=proto_archival_status_to_dataclass(domain_response.visibility_archival_status),
        visibility_archival_uri=domain_response.visibility_archival_uri,
        bad_binaries=proto_bad_binaries_to_dataclass(domain_response.bad_binaries),
    )

    return domain_configuration


def proto_archival_status_to_dataclass(archival_status: domain_pb2.ArchivalStatus) -> ArchivalStatus:
    if archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED:
        return ArchivalStatus(ArchivalStatus.ENABLED)
    elif archival_status == domain_pb2.ARCHIVAL_STATUS_DISABLED:
        return ArchivalStatus(ArchivalStatus.DISABLED)
    else:
        return ArchivalStatus(ArchivalStatus.INVALID)


def proto_bad_binaries_to_dataclass(bb: domain_pb2.BadBinaries) -> BadBinaries:
    bad_binaries = BadBinaries(
        binaries={key: proto_bad_binary_info_to_dataclass(bad_binary_info) for key, bad_binary_info in bb.binaries}
    )

    return bad_binaries


def proto_bad_binary_info_to_dataclass(bb: domain_pb2.BadBinaryInfo) -> BadBinaryInfo:
    bad_binary_info = BadBinaryInfo(
        reason=bb.reason,
        operator=bb.operator,
        created_time_nano=bb.created_time.ToNanoseconds(),
    )

    return bad_binary_info


def proto_cluster_replication_configuration_to_metadata(
        d: domain_pb2.ClusterReplicationConfiguration) -> ClusterReplicationConfiguration:
    cluster_replication_configuration = ClusterReplicationConfiguration(
        cluster_name=d.cluster_name
    )

    return cluster_replication_configuration
