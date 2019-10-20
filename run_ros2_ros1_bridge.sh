#!/usr/bin/env bash

PREFIX=spike_ros_interface_gateways
PACKAGE=ros1_bridge
ROS_VERSION=ros2
IMAGE_NAME=${PREFIX}_${ROS_VERSION}_${PACKAGE}
CONTAINER_NAME=${IMAGE_NAME}

docker run --rm -t --name ${CONTAINER_NAME} -e ROS_MASTER_URI=http://172.17.0.2:11311 ${IMAGE_NAME}

exit ${?}
