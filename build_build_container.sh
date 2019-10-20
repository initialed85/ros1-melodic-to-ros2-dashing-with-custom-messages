#!/usr/bin/env bash

PREFIX=spike_ros_interface_gateways
DOCKERFILE=context_build/Dockerfile
IMAGE_NAME=${PREFIX}_build
CONTEXT=.

docker build -t ${IMAGE_NAME} -f ${DOCKERFILE} ${CONTEXT}

exit ${?}
