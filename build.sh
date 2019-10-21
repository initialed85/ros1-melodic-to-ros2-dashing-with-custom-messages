#!/usr/bin/env bash

./scripts/build_build_container.sh && \
  ./scripts/build_ros2_ros1_bridge_container.sh && \
  ./scripts/build_ros1_gateway_pub_sub_container.sh && \
  ./scripts/build_ros2_gateway_pub_sub_container.sh

exit ${?}
