from enum import IntEnum


class ConnectionProtocol(IntEnum):
    GRPC = 0
    TCHANNEL = 1


class DefaultPort(IntEnum):
    GRPC = 7833
    TCHANNEL = 7933