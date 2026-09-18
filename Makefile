APP_DIR ?= fastapi-app
IMAGE_NAME ?= bnay14/fastapi
IMAGE_TAG ?= latest

.PHONY: build run push

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) $(APP_DIR)

run:
	docker run --rm -p 8000:8000 $(IMAGE_NAME):$(IMAGE_TAG)

push:
	docker push $(IMAGE_NAME):$(IMAGE_TAG)
