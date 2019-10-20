#!/usr/bin/env bash

PREFIX=spike_ros_interface_gateways
PACKAGE=ros1_bridge
DOCKERFILE=context_ros2_${PACKAGE}/Dockerfile
IMAGE_NAME=${PREFIX}_ros2_${PACKAGE}
CONTEXT=.

docker build -t ${IMAGE_NAME} -f ${DOCKERFILE} ${CONTEXT}

exit ${?}
