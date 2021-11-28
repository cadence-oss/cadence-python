from abc import abstractmethod
from typing import Tuple

from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse


class CadenceServiceInterface:

    @abstractmethod
    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        pass

    @abstractmethod
    def start_workflow(self, request: StartWorkflowExecutionRequest) -> Tuple[StartWorkflowExecutionResponse, object]:
        pass