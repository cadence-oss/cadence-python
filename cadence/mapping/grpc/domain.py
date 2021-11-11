from typing import Type

import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsResponse, DescribeDomainResponse, DomainStatus, ArchivalStatus, \
    FailoverInfo, BadBinaryInfo, BadBinaries, ClusterReplicationConfiguration, ListDomainsRequest
from uber.cadence.api.v1 import domain_pb2


def list_domains_request_to_dataclass(request: ListDomainsRequest) -> service_domain_pb2.ListDomainsRequest:
    return service_domain_pb2.ListDomainsRequest(page_size=20, next_page_token=bytes(0))

def list_domains_response_to_dataclass(response: service_domain_pb2.ListDomainsResponse) -> Type[ListDomainsResponse]:
    list_domains = ListDomainsResponse
    list_domains.domains = [describe_domain_to_dataclass(domain) for domain in response.domains]
    list_domains.next_page_token = response.next_page_token

    return list_domains


def describe_domain_to_dataclass(domain_response: service_domain_pb2.DescribeDomainResponse) -> Type[
    DescribeDomainResponse]:
    domain = DescribeDomainResponse(
        id = domain_response.id,
        name = domain_response.name,
        status = DomainStatus(domain_response.status),
        description = domain_response.description,
        owner_email = domain_response.owner_email,
        data = {key:value for key, value in domain_response.data.values()},
        workflow_execution_retention_period = domain_response.workflow_execution_retention_period.ToMilliseconds(),
        bad_binaries = bad_binaries_to_dataclass(domain_response.bad_binaries),
        history_archival_status = ArchivalStatus(domain_response.history_archival_status),
        history_archival_uri = domain_response.history_archival_uri,
        visibility_archival_status = ArchivalStatus(domain_response.visibility_archival_status),
        visibility_archival_uri = domain_response.visibility_archival_uri,
        active_cluster_name = domain_response.active_cluster_name,
        clusters = [cluster_replication_configuration_to_metadata(cluster) for cluster in domain_response.clusters],
        failover_version = domain_response.failover_version,
        is_global_domain = domain_response.is_global_domain,
        failover_info = FailoverInfo(domain_response.failover_info),
    )

    return domain


def bad_binaries_to_dataclass(bb: domain_pb2.BadBinaries) -> Type[BadBinaries]:
    bad_binaries = BadBinaries
    bad_binaries.binaries = {key: bad_binary_info_to_dataclass(bad_binary_info) for key, bad_binary_info in bb.binaries}
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
