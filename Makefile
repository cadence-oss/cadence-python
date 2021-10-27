generate-grpc-code:
	echo "Generating Python code from Proto files"
	python3 -m grpc_tools.protoc \
    --proto_path=./idls/proto \
    --python_out=. \
    --grpc_python_out=. \
    ./idls/proto/uber/cadence/api/v1/*.proto