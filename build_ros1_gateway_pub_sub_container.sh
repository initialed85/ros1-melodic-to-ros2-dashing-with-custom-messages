#!/usr/bin/env bash

PREFIX=spike_ros_interface_gateways
PACKAGE=gateway_pub_sub
DOCKERFILE=context_ros1_${PACKAGE}/Dockerfile
IMAGE_NAME=${PREFIX}_ros1_${PACKAGE}
CONTEXT=.

docker build -t ${IMAGE_NAME} -f ${DOCKERFILE} ${CONTEXT}

exit ${?}
