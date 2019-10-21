#!/usr/bin/env bash

PREFIX=ros1_melodic_to_ros2_dashing_with_custom_messages
DOCKERFILE=dockerfile/context_build/Dockerfile
IMAGE_NAME=${PREFIX}_build
CONTEXT=.

docker build -t ${IMAGE_NAME} -f ${DOCKERFILE} ${CONTEXT}

exit ${?}
