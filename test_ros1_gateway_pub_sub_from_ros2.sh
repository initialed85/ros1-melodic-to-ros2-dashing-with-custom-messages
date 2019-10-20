#!/usr/bin/env bash

docker-compose -f test_against_ros1_from_ros2/docker-compose.yml up -d ros_under_test ros2_ros1_bridge

sleep 5

docker-compose -f test_against_ros1_from_ros2/docker-compose.yml up --exit-code-from ros_test_harness ros_test_harness
RETVAL=${?}

docker cp ros_test_harness_1:/srv/test_results/test_results.xml test_results/ros1_gateway_pub_sub_from_ros2.xml

docker-compose -f test_against_ros1_from_ros2/docker-compose.yml down

exit ${RETVAL}
