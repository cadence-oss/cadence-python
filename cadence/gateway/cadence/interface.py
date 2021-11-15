from abc import abstractmethod
from typing import Tuple

from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse


class CadenceGatewayInterface:

    @abstractmethod
    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        pass