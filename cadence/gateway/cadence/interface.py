from abc import abstractmethod
from typing import Tuple

from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse


class CadenceServiceInterface:

    @abstractmethod
    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        pass