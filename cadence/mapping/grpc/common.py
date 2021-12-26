from google.protobuf import duration_pb2


def duration_or_none(value: int) -> duration_pb2.Duration:
    return duration_pb2.Duration(seconds=value) if value else None
