APP_NAME = infra/kundotay
REPO_NAME = hub.molnet.svt.se
MOLN = ssh cli@sthlm.molnet.svt.se --

TAG := $(shell date +%s)
IMAGE = ${REPO_NAME}/$(APP_NAME):$(TAG)

build:
	docker build -t ${IMAGE} -f Dockerfile .

push: build
	docker push ${IMAGE}

run: build
	docker run -ti \
		-p 8080:8080 \
		${IMAGE}

debug: build
	docker run -ti \
		-p 8080:8080 \
		${IMAGE} \
		bash

deploy: push
	${MOLN} deploy -app ${APP_NAME}

update: push
	${MOLN} update -deploy -app ${APP_NAME} -image ${IMAGE}
