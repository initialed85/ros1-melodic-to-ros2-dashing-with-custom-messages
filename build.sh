#!/usr/bin/env bash

./build_build_container.sh && \
  ./build_ros2_ros1_bridge_container.sh && \
  ./build_ros1_gateway_pub_sub_container.sh && \
  ./build_ros2_gateway_pub_sub_container.sh

exit ${?}
