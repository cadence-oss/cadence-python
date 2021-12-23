generate-grpc-code:
	python3 -m grpc_tools.protoc \
    --proto_path=./idls/proto \
    --python_out=. \
    --mypy_out=. \
    --grpc_python_out=. \
    ./idls/proto/uber/cadence/api/v1/*.proto

fetch-idls:
	git submodule init && git submodule update