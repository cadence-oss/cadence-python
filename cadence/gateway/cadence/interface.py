from abc import abstractmethod
from typing import Tuple, Callable

from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse, RegisterDomainRequest


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
    def close(self):
        pass

    @abstractmethod
    def set_next_timeout_cb(self, cb: Callable):
        pass