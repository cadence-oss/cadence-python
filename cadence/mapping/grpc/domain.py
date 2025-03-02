from typing import Optional

from google.protobuf import timestamp_pb2

import uber.cadence.api.v1.service_domain_pb2 as service_domain_pb2
from cadence.cadence_types import ListDomainsResponse, DescribeDomainResponse, DomainStatus, ArchivalStatus, \
    BadBinaryInfo, BadBinaries, ClusterReplicationConfiguration, ListDomainsRequest, DomainInfo, \
    DomainConfiguration, DomainReplicationConfiguration, RegisterDomainRequest, DescribeDomainRequest, \
    UpdateDomainRequest, UpdateDomainResponse
from cadence.mapping.grpc.common import duration_or_none
from uber.cadence.api.v1 import domain_pb2


def ms_to_days(milliseconds: int) -> int:
    return int(milliseconds / (1000 * 60 * 60 * 24))


def days_to_seconds(days: int) -> int:
    return days * 24 * 60 * 60 if days else 0


def list_domains_request_dataclass_to_proto(list_domains: ListDomainsRequest) -> service_domain_pb2.ListDomainsRequest:
    return service_domain_pb2.ListDomainsRequest(
        page_size=list_domains.page_size,
        next_page_token=list_domains.next_page_token
    )


def proto_list_domains_response_to_dataclass(
        list_domains: service_domain_pb2.ListDomainsResponse) -> ListDomainsResponse:
    return ListDomainsResponse(
        domains=[proto_domain_to_describe_domain_response_dataclass(domain) for domain in list_domains.domains],
        next_page_token=list_domains.next_page_token
    ) if list_domains else None


def describe_domain_request_dataclass_to_proto(
        describe_domain_request: DescribeDomainRequest) -> service_domain_pb2.DescribeDomainRequest:
    return service_domain_pb2.DescribeDomainRequest(
        id=describe_domain_request.uuid,
        name=describe_domain_request.name,
    )


DomainUpdateDescriptionField = "description"
DomainUpdateOwnerEmailField = "owner_email"
DomainUpdateDataField = "data"
DomainUpdateRetentionPeriodField = "workflow_execution_retention_period"
DomainUpdateBadBinariesField = "bad_binaries"
DomainUpdateHistoryArchivalStatusField = "history_archival_status"
DomainUpdateHistoryArchivalURIField = "history_archival_uri"
DomainUpdateVisibilityArchivalStatusField = "visibility_archival_status"
DomainUpdateVisibilityArchivalURIField = "visibility_archival_uri"
DomainUpdateActiveClusterNameField = "active_cluster_name"
DomainUpdateClustersField = "clusters"
DomainUpdateDeleteBadBinaryField = "delete_bad_binary"
DomainUpdateFailoverTimeoutField = "failover_timeout"


def update_domain_request_dataclass_to_proto(
        update_domain_request: UpdateDomainRequest) -> service_domain_pb2.UpdateDomainRequest:
    proto = service_domain_pb2.UpdateDomainRequest(
        security_token=update_domain_request.security_token,
        name=update_domain_request.name
    )

    if update_domain_request.updated_info is not None:
        if update_domain_request.updated_info.description:
            proto.update_mask.paths.append(DomainUpdateDescriptionField)
            proto.description = update_domain_request.updated_info.description

        if update_domain_request.updated_info.owner_email:
            proto.update_mask.paths.append(DomainUpdateOwnerEmailField)
            proto.owner_email = update_domain_request.updated_info.owner_email

        if update_domain_request.updated_info.data:
            proto.update_mask.paths.append(DomainUpdateDataField)
            proto.data.update({key: value for key, value in update_domain_request.updated_info.data.items()})

    if update_domain_request.configuration is not None:
        if update_domain_request.configuration.workflow_execution_retention_period_in_days:
            proto.update_mask.paths.append(DomainUpdateRetentionPeriodField)
            proto.workflow_execution_retention_period.CopyFrom(duration_or_none(
                days_to_seconds(update_domain_request.configuration.workflow_execution_retention_period_in_days)))

        if update_domain_request.configuration.bad_binaries is not None:
            proto.update_mask.paths.append(DomainUpdateBadBinariesField)
            proto.bad_binaries.CopyFrom(bad_binaries_dataclass_to_proto(update_domain_request.configuration.bad_binaries))

        if update_domain_request.configuration.archival_status is not None:
            proto.update_mask.paths.append(DomainUpdateHistoryArchivalStatusField)
            proto.history_archival_status = archival_status_dataclass_to_proto(update_domain_request.configuration.archival_status)

        if update_domain_request.configuration.archival_bucket_name:
            proto.update_mask.paths.append(DomainUpdateHistoryArchivalURIField)
            proto.history_archival_uri = update_domain_request.configuration.archival_bucket_name

        if update_domain_request.configuration.visibility_archival_status is not None:
            proto.update_mask.paths.append(DomainUpdateVisibilityArchivalStatusField)
            proto.visibility_archival_status = archival_status_dataclass_to_proto(update_domain_request.configuration.visibility_archival_status)

        if update_domain_request.configuration.visibility_archival_uri:
            proto.update_mask.paths.append(DomainUpdateVisibilityArchivalURIField)
            proto.visibility_archival_uri = update_domain_request.configuration.visibility_archival_uri

    if update_domain_request.replication_configuration is not None:
        if update_domain_request.replication_configuration.active_cluster_name:
            proto.update_mask.paths.append(DomainUpdateActiveClusterNameField)
            proto.active_cluster_name = update_domain_request.replication_configuration.active_cluster_name

        if update_domain_request.replication_configuration.clusters is not None and len(update_domain_request.replication_configuration.clusters):
            proto.update_mask.paths.append(DomainUpdateClustersField)
            proto.clusters.MergeFrom([cluster_replication_configuration_metadata_to_proto(cluster) for cluster in
                                      update_domain_request.replication_configuration.clusters])

    if update_domain_request.delete_bad_binary:
        proto.update_mask.paths.append(DomainUpdateDeleteBadBinaryField)
        proto.delete_bad_binary = update_domain_request.delete_bad_binary

    if update_domain_request.failover_timeout:
        proto.update_mask.paths.append(DomainUpdateFailoverTimeoutField)
        proto.failover_timeout.CopyFrom(duration_or_none(update_domain_request.failover_timeout))

    return proto


def proto_update_domain_response_to_dataclass(
        update_domain_response: service_domain_pb2.UpdateDomainResponse) -> UpdateDomainResponse:
    domain = update_domain_response.domain
    return UpdateDomainResponse(
        domain_info=proto_domain_to_domain_info_dataclass(domain),
        configuration=proto_domain_to_domain_configuration_dataclass(domain),
        replication_configuration=proto_domain_to_replication_configuration_dataclass(domain),
        failover_version=domain.failover_version,
        is_global_domain=domain.is_global_domain,
    ) if domain else None


def proto_describe_domain_response_to_describe_domain_response_dataclass(
        describe_domain_response: service_domain_pb2.DescribeDomainResponse) -> DescribeDomainResponse:
    return proto_domain_to_describe_domain_response_dataclass(
        describe_domain_response.domain) if describe_domain_response else None


def proto_domain_to_describe_domain_response_dataclass(domain: domain_pb2.Domain) -> DescribeDomainResponse:
    return DescribeDomainResponse(
        domain_info=proto_domain_to_domain_info_dataclass(domain),
        configuration=proto_domain_to_domain_configuration_dataclass(domain),
        replication_configuration=proto_domain_to_replication_configuration_dataclass(domain),
        failover_version=domain.failover_version,
        is_global_domain=domain.is_global_domain,
    ) if domain else None


def proto_domain_to_domain_info_dataclass(domain: domain_pb2.Domain) -> DomainInfo:
    return DomainInfo(
        name=domain.name,
        status=proto_domain_status_to_dataclass(domain.status),
        description=domain.description,
        owner_email=domain.owner_email,
        data={key: value for key, value in domain.data.items()},
        uuid=domain.id,
    ) if domain else None


def proto_domain_to_replication_configuration_dataclass(domain: domain_pb2.Domain) -> DomainReplicationConfiguration:
    return DomainReplicationConfiguration(
        active_cluster_name=domain.active_cluster_name,
        clusters=[proto_cluster_replication_configuration_to_metadata(cluster) for cluster in domain.clusters]
    ) if domain else None


def proto_domain_status_to_dataclass(domain_status: Optional[domain_pb2.DomainStatus.__class__]) -> DomainStatus:
    if domain_status == domain_pb2.DOMAIN_STATUS_REGISTERED:
        return DomainStatus(DomainStatus.REGISTERED)
    elif domain_status == domain_pb2.DOMAIN_STATUS_DELETED:
        return DomainStatus(DomainStatus.DELETED)
    elif domain_status == domain_pb2.DOMAIN_STATUS_DEPRECATED:
        return DomainStatus(DomainStatus.DEPRECATED)
    else:
        return DomainStatus(DomainStatus.INVALID)


def proto_domain_to_domain_configuration_dataclass(domain: domain_pb2.Domain) -> DomainConfiguration:
    return DomainConfiguration(
        workflow_execution_retention_period_in_days=ms_to_days(
            domain.workflow_execution_retention_period.ToMilliseconds()),  # is this milliseconds?
        workflow_execution_retention_period=domain.workflow_execution_retention_period.ToMilliseconds(),
        emit_metric=True,
        archival_status=proto_archival_status_to_dataclass(domain.history_archival_status),
        archival_bucket_name=domain.history_archival_uri,
        history_archival_status=proto_archival_status_to_dataclass(domain.history_archival_status),
        history_archival_uri=domain.history_archival_uri,
        visibility_archival_status=proto_archival_status_to_dataclass(domain.visibility_archival_status),
        visibility_archival_uri=domain.visibility_archival_uri,
        bad_binaries=proto_bad_binaries_to_dataclass(domain.bad_binaries),
    ) if domain else None


def proto_archival_status_to_dataclass(
        archival_status: Optional[domain_pb2.ArchivalStatus.__class__]) -> ArchivalStatus:
    if archival_status == domain_pb2.ARCHIVAL_STATUS_ENABLED:
        return ArchivalStatus(ArchivalStatus.ENABLED)
    elif archival_status == domain_pb2.ARCHIVAL_STATUS_DISABLED:
        return ArchivalStatus(ArchivalStatus.DISABLED)
    else:
        return ArchivalStatus(ArchivalStatus.INVALID)


def archival_status_dataclass_to_proto(archival_status: Optional[ArchivalStatus]) -> domain_pb2.ArchivalStatus:
    if archival_status == ArchivalStatus.ENABLED:
        return domain_pb2.ARCHIVAL_STATUS_ENABLED
    elif archival_status == ArchivalStatus.DISABLED:
        return domain_pb2.ARCHIVAL_STATUS_DISABLED
    else:
        return domain_pb2.ARCHIVAL_STATUS_INVALID


def proto_bad_binaries_to_dataclass(bad_binaries: domain_pb2.BadBinaries) -> BadBinaries:
    return BadBinaries(
        binaries={key: proto_bad_binary_info_to_dataclass(value) for key, value in bad_binaries.binaries.items()}
    ) if bad_binaries else None


def bad_binaries_dataclass_to_proto(bad_binaries: BadBinaries) -> domain_pb2.BadBinaries:
    return domain_pb2.BadBinaries(
        binaries={key: bad_binary_info_dataclass_to_proto(value) for key, value in bad_binaries.binaries.items()}
    ) if bad_binaries else None


def proto_bad_binary_info_to_dataclass(bad_binary_info: domain_pb2.BadBinaryInfo) -> BadBinaryInfo:
    return BadBinaryInfo(
        reason=bad_binary_info.reason,
        operator=bad_binary_info.operator,
        created_time_nano=bad_binary_info.created_time.ToNanoseconds(),
    ) if bad_binary_info else None


def bad_binary_info_dataclass_to_proto(bad_binary_info: BadBinaryInfo) -> domain_pb2.BadBinaryInfo:
    return domain_pb2.BadBinaryInfo(
        reason=bad_binary_info.reason,
        operator=bad_binary_info.operator,
        created_time=timestamp_pb2.Timestamp(nanos=bad_binary_info.created_time_nano),
    ) if bad_binary_info else None


def proto_cluster_replication_configuration_to_metadata(
        cluster_replication_config: domain_pb2.ClusterReplicationConfiguration) -> ClusterReplicationConfiguration:
    return ClusterReplicationConfiguration(
        cluster_name=cluster_replication_config.cluster_name
    ) if cluster_replication_config else None


def cluster_replication_configuration_metadata_to_proto(
        cluster_replication_config: ClusterReplicationConfiguration) -> domain_pb2.ClusterReplicationConfiguration:
    return domain_pb2.ClusterReplicationConfiguration(
        cluster_name=cluster_replication_config.cluster_name
    ) if cluster_replication_config else None


def register_domain_request_dataclass_to_proto(
        register_domain: RegisterDomainRequest) -> service_domain_pb2.RegisterDomainRequest:
    return service_domain_pb2.RegisterDomainRequest(
        security_token=register_domain.security_token,
        name=register_domain.name,
        description=register_domain.description,
        owner_email=register_domain.owner_email,
        workflow_execution_retention_period=duration_or_none(
            days_to_seconds(register_domain.workflow_execution_retention_period_in_days)),
        clusters=[cluster_replication_configuration_metadata_to_proto(cluster) for cluster in register_domain.clusters],
        active_cluster_name=register_domain.active_cluster_name,
        data={key: value for key, value in register_domain.data.items()},
        is_global_domain=register_domain.is_global_domain,
        history_archival_status=archival_status_dataclass_to_proto(register_domain.archival_status),
        history_archival_uri=register_domain.archival_bucket_name,
        visibility_archival_status=archival_status_dataclass_to_proto(register_domain.visibility_archival_status),
        visibility_archival_uri=register_domain.visibility_archival_uri
    ) if register_domain else None
