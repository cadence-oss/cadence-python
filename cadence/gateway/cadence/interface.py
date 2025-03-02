from abc import abstractmethod
from typing import Tuple, Callable

from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse, RegisterDomainRequest, DescribeDomainRequest, DescribeDomainResponse, \
    UpdateDomainRequest, UpdateDomainResponse, GetWorkflowExecutionHistoryRequest, GetWorkflowExecutionHistoryResponse


class CadenceServiceInterface:

    @abstractmethod
    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        pass

    @abstractmethod
    def start_workflow(self, request: StartWorkflowExecutionRequest) -> Tuple[StartWorkflowExecutionResponse, object]:
        pass

    @abstractmethod
    def register_domain(self, request: RegisterDomainRequest) -> Tuple[None, object]:
        pass

    @abstractmethod
    def describe_domain(self, request: DescribeDomainRequest) -> Tuple[DescribeDomainResponse, object]:
        pass

    @abstractmethod
    def update_domain(self, request: UpdateDomainRequest) -> Tuple[UpdateDomainResponse, object]:
        pass

    @abstractmethod
    def get_workflow_execution_history(self, request: GetWorkflowExecutionHistoryRequest) -> \
            Tuple[GetWorkflowExecutionHistoryResponse, object]:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def set_next_timeout_cb(self, cb: Callable):
        pass