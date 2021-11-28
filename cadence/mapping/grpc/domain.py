import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsResponse, DescribeDomainResponse, DomainStatus, ArchivalStatus, \
    BadBinaryInfo, BadBinaries, ClusterReplicationConfiguration, ListDomainsRequest, DomainInfo, \
    DomainConfiguration, DomainReplicationConfiguration
from uber.cadence.api.v1 import domain_pb2


def ms_to_days(milliseconds: int) -> int:
    return int(milliseconds / (1000*60*60*24))


def list_domains_request_dataclass_to_proto(list_domains: ListDomainsRequest) -> service_domain_pb2.ListDomainsRequest:
    return service_domain_pb2.ListDomainsRequest(
        page_size=list_domains.page_size,
        next_page_token=list_domains.next_page_token
    )


def proto_list_domains_response_to_dataclass(list_domains: service_domain_pb2.ListDomainsResponse) -> ListDomainsResponse:
    return ListDomainsResponse(
        domains=[proto_describe_domain_to_dataclass(domain) for domain in list_domains.domains],
        next_page_token=list_domains.next_page_token
    ) if list_domains else None


def proto_describe_domain_to_dataclass(
        describe_domain: service_domain_pb2.DescribeDomainResponse) -> DescribeDomainResponse:
    return DescribeDomainResponse(
        domain_info=proto_domain_info_to_dataclass(describe_domain),
        configuration=proto_domain_configuration_do_dataclass(describe_domain),
        replication_configuration=proto_replication_configuration_to_dataclass(describe_domain),
        failover_version=describe_domain.failover_version,
        is_global_domain=describe_domain.is_global_domain,
    ) if describe_domain else None


def proto_domain_info_to_dataclass(describe_domain: service_domain_pb2.DescribeDomainResponse) -> DomainInfo:
    return DomainInfo(
        name=describe_domain.name,
        status=proto_domain_status_to_dataclass(describe_domain.status),
        description=describe_domain.description,
        owner_email=describe_domain.owner_email,
        data={key: value for key, value in describe_domain.data.values()},
        uuid=describe_domain.id,
    ) if describe_domain else None


def proto_replication_configuration_to_dataclass(
        describe_domain: service_domain_pb2.DescribeDomainResponse) -> DomainReplicationConfiguration:
    return DomainReplicationConfiguration(
        active_cluster_name=describe_domain.active_cluster_name,
        clusters=[proto_cluster_replication_configuration_to_metadata(cluster) for cluster in describe_domain.clusters]
    ) if describe_domain else None


def proto_domain_status_to_dataclass(domain_status: domain_pb2.DomainStatus) -> DomainStatus:
    if domain_status == domain_pb2.DOMAIN_STATUS_REGISTERED:
        return DomainStatus(DomainStatus.REGISTERED)
    elif domain_status == domain_pb2.DOMAIN_STATUS_DELETED:
        return DomainStatus(DomainStatus.DELETED)
    elif domain_status == domain_pb2.DOMAIN_STATUS_DEPRECATED:
        return DomainStatus(DomainStatus.DEPRECATED)
    else:
        return DomainStatus(DomainStatus.INVALID)


def proto_domain_configuration_do_dataclass(
        domain_configuration: service_domain_pb2.DescribeDomainResponse) -> DomainConfiguration:
    return DomainConfiguration(
        workflow_execution_retention_period_in_days=ms_to_days(domain_configuration.workflow_execution_retention_period.ToMilliseconds()),
        workflow_execution_retention_period=domain_configuration.workflow_execution_retention_period.ToMilliseconds(),
        emit_metric=False,
        archival_bucket_name='',
        archival_status=proto_archival_status_to_dataclass(domain_configuration.history_archival_status),
        bad_binaries=proto_bad_binaries_to_dataclass(domain_configuration.bad_binaries),
    ) if domain_configuration else None


def proto_archival_status_to_dataclass(archival_status: domain_pb2.ArchivalStatus) -> ArchivalStatus:
    if archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED:
        return ArchivalStatus(ArchivalStatus.ENABLED)
    elif archival_status == domain_pb2.ARCHIVAL_STATUS_DISABLED:
        return ArchivalStatus(ArchivalStatus.DISABLED)
    else:
        return ArchivalStatus(ArchivalStatus.INVALID)


def proto_bad_binaries_to_dataclass(bad_binaries: domain_pb2.BadBinaries) -> BadBinaries:
    return BadBinaries(
        binaries={key: proto_bad_binary_info_to_dataclass(value) for key, value in bad_binaries.binaries}
    ) if bad_binaries else None


def proto_bad_binary_info_to_dataclass(bad_binary_info: domain_pb2.BadBinaryInfo) -> BadBinaryInfo:
    return BadBinaryInfo(
        reason=bad_binary_info.reason,
        operator=bad_binary_info.operator,
        created_time_nano=bad_binary_info.created_time.ToNanoseconds(),
    ) if bad_binary_info else None

def proto_cluster_replication_configuration_to_metadata(
        cluster_replication_config: domain_pb2.ClusterReplicationConfiguration) -> ClusterReplicationConfiguration:
    return ClusterReplicationConfiguration(
        cluster_name=cluster_replication_config.cluster_name
    ) if cluster_replication_config else None