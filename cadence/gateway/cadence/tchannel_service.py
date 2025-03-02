from __future__ import annotations

from typing import Tuple, Callable

import os
import socket

from cadence.gateway.cadence.interface import CadenceServiceInterface
from cadence.thrift import cadence_thrift
from cadence.connection import TChannelConnection, ThriftFunctionCall
from cadence.errors import find_error
from cadence.conversions import copy_thrift_to_py, copy_py_to_thrift
from cadence.cadence_types import ListDomainsRequest, ListDomainsResponse, StartWorkflowExecutionRequest, \
    StartWorkflowExecutionResponse, RegisterDomainRequest, DescribeDomainRequest, DescribeDomainResponse, \
    UpdateDomainRequest, UpdateDomainResponse, GetWorkflowExecutionHistoryRequest, GetWorkflowExecutionHistoryResponse

TCHANNEL_SERVICE = "cadence-frontend"


class CadenceTChannelService(CadenceServiceInterface):

    @classmethod
    def create(cls, host: str, port: int, timeout: int = None):
        connection = TChannelConnection.open(host, port, timeout=timeout)
        return cls(connection)

    @classmethod
    def get_identity(cls):
        return "%d@%s" % (os.getpid(), socket.gethostname())

    def __init__(self, connection: TChannelConnection):
        self.connection = connection
        self.execution_start_to_close_timeout_seconds = 86400
        self.task_start_to_close_timeout_seconds = 120

    def thrift_call(self, method_name, request_argument):
        thrift_request_argument = copy_py_to_thrift(request_argument)
        fn = getattr(cadence_thrift.WorkflowService, method_name, None)
        assert fn
        request = fn.request(thrift_request_argument)
        request_payload = cadence_thrift.dumps(request)
        call = ThriftFunctionCall.create(TCHANNEL_SERVICE, "WorkflowService::" + method_name, request_payload)
        response = self.connection.call_function(call)
        start_response = cadence_thrift.loads(fn.response, response.thrift_payload)
        return start_response

    def call_return(self, method_name: str, request: object, expected_return_type: type) -> Tuple[object, object]:
        response = self.thrift_call(method_name, request)
        if not response.success:
            return None, find_error(response)
        return_value = copy_thrift_to_py(response.success)
        assert isinstance(return_value, expected_return_type)
        return return_value, None

    def call_void(self, method_name, request):
        response = self.thrift_call(method_name, request)
        error = find_error(response)
        return None, error

    def list_domains(self, request: ListDomainsRequest) -> Tuple[ListDomainsResponse, object]:
        return self.call_return("ListDomains", request, ListDomainsResponse)

    def start_workflow(self, request: StartWorkflowExecutionRequest) -> Tuple[StartWorkflowExecutionResponse, object]:
        return self.call_return("StartWorkflowExecution", request, StartWorkflowExecutionResponse)

    def register_domain(self, request: RegisterDomainRequest) -> Tuple[None, object]:
        return self.call_void("RegisterDomain", request)

    def describe_domain(self, request: DescribeDomainRequest) -> Tuple[DescribeDomainResponse, object]:
        return self.call_return("DescribeDomain", request, DescribeDomainResponse)

    def update_domain(self, request: UpdateDomainRequest) -> Tuple[UpdateDomainResponse, object]:
        return self.call_return("UpdateDomain", request, UpdateDomainResponse)

    def get_workflow_execution_history(self, request: GetWorkflowExecutionHistoryRequest) -> \
            Tuple[GetWorkflowExecutionHistoryResponse, object]:
        return self.call_return("GetWorkflowExecutionHistory", request, GetWorkflowExecutionHistoryResponse)

    def close(self):
        self.connection.close()

    def set_next_timeout_cb(self, cb: Callable):
        self.connection.set_next_timeout_cb(cb)
