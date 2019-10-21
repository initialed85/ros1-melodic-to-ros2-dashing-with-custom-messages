#!/usr/bin/env bash

PREFIX=ros1_melodic_to_ros2_dashing_with_custom_messages
PACKAGE=gateway_pub_sub
ROS_VERSION=ros2
IMAGE_NAME=${PREFIX}_${ROS_VERSION}_${PACKAGE}
CONTAINER_NAME=${IMAGE_NAME}

docker run --rm -t --name ${CONTAINER_NAME} ${IMAGE_NAME}

exit ${?}
