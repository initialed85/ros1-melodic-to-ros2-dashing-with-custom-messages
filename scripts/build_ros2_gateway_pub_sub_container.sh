#!/usr/bin/env bash

PREFIX=ros1_melodic_to_ros2_dashing_with_custom_messages
PACKAGE=gateway_pub_sub
DOCKERFILE=dockerfile/context_ros2_${PACKAGE}/Dockerfile
IMAGE_NAME=${PREFIX}_ros2_${PACKAGE}
CONTEXT=.

docker build -t ${IMAGE_NAME} -f ${DOCKERFILE} ${CONTEXT}

exit ${?}
