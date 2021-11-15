from typing import Type

import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsResponse, DescribeDomainResponse, DomainStatus, ArchivalStatus, \
    FailoverInfo, BadBinaryInfo, BadBinaries, ClusterReplicationConfiguration, ListDomainsRequest, DomainInfo, \
    DomainConfiguration
from uber.cadence.api.v1 import domain_pb2


def list_domains_request_to_proto(request: ListDomainsRequest) -> service_domain_pb2.ListDomainsRequest:
    return service_domain_pb2.ListDomainsRequest(page_size=20, next_page_token=bytes(0))

def proto_list_domains_response_to_dataclass(response: service_domain_pb2.ListDomainsResponse) -> Type[ListDomainsResponse]:
    list_domains = ListDomainsResponse
    list_domains.domains = [describe_domain_to_dataclass(domain) for domain in response.domains]
    list_domains.next_page_token = response.next_page_token

    return list_domains


def proto_describe_domain_to_dataclass(domain_response: service_domain_pb2.DescribeDomainResponse) -> Type[
    DescribeDomainResponse]:
    domain = DescribeDomainResponse(
        domain_info = proto_domain_info_to_dataclass(domain_response),
        configuration = proto_domain_configuration_do_dataclass(domain_response),
        replication_configuration = proto_replication_configuration_to_dataclass(domain_response),
        failover_version = domain_response.failover_version,
        is_global_domain = domain_response.is_global_domain,
    )

    return domain


def proto_domain_info_to_dataclass(domain_response: service_domain_pb2.DescribeDomainResponse) -> DomainInfo:
    domain_info = DomainInfo(
        name = domain_response.name,
        status = proto_domain_status_to_dataclass(domain_response.status),
        description = domain_response.description,
        owner_email = domain_response.owner_email,
        data = {key:value for key, value in domain_response.data.values()},
        uuid = domain_response.id,
    )

    return domain_info


def proto_domain_status_to_dataclass(ds: domain_pb2.DomainStatus) -> Type[DomainStatus]:
    if ds == domain_pb2.DOMAIN_STATUS_REGISTERED:
        return DomainStatus(DomainStatus.REGISTERED)
    elif ds == domain_pb2.DOMAIN_STATUS_DELETED:
        return DomainStatus(DomainStatus.DELETED)
    elif ds == domain_pb2.DOMAIN_STATUS_DEPRECATED:
        return DomainStatus(DomainStatus.DEPRECATED)
    else:
        return DomainStatus(DomainStatus.INVALID)


def proto_domain_configuration_do_dataclass(domain_response: service_domain_pb2.DescribeDomainResponse) -> DomainInfo:
    domain_configuration = DomainConfiguration(
        workflow_execution_retention_period_in_days=workflow_execution_retention_period
        workflow_execution_retention_period=domain_response.workflow_execution_retention_period.ToMilliseconds(),
        emit_metric=None,
        archival_bucket_name=None,
    archival_status: ArchivalStatus = None
    bad_binaries: BadBinaries = None
    )

    return domain_configuration


def proto_archival_status_to_dataclass(bb: domain_pb2.BadBinaries) -> BadBinaries:
    bad_binaries = BadBinaries(
        binaries = {key: bad_binary_info_to_dataclass(bad_binary_info) for key, bad_binary_info in bb.binaries}
    )

    return bad_binaries


def proto_bad_binaries_to_dataclass(bb: domain_pb2.BadBinaries) -> BadBinaries:
    bad_binaries = BadBinaries(
        binaries = {key: bad_binary_info_to_dataclass(bad_binary_info) for key, bad_binary_info in bb.binaries}
    )

    return bad_binaries


def bad_binary_info_to_dataclass(bb: domain_pb2.BadBinaryInfo) -> Type[BadBinaryInfo]:
    bad_binary_info = BadBinaryInfo
    bad_binary_info.reason = bb.readon
    bad_binary_info.operator = bb.operator
    bad_binary_info.created_time = bb.created_time.ToMilliseconds()

    return bad_binary_info


def cluster_replication_configuration_to_metadata(
        d: domain_pb2.ClusterReplicationConfiguration) -> ClusterReplicationConfiguration:
    cluster_replication_configuration = ClusterReplicationConfiguration()
    cluster_replication_configuration.cluster_name = d.cluster_name

    return cluster_replication_configuration