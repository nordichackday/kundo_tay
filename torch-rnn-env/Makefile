IMAGE=kundo_torch_env

build:
	docker build -t ${IMAGE} .

debug: build
	docker run -tiv ${IMAGE} bash
