#!/usr/bin/env bash

DOCKER_COMPOSE=docker_compose/test_against_ros1_from_ros2/docker-compose.yml
JUNIT_XML=ros1_gateway_pub_sub_from_ros2.xml

docker-compose -f ${DOCKER_COMPOSE} up -d

docker-compose -f ${DOCKER_COMPOSE} exec -d ros_under_test /srv/services.sh

docker-compose -f ${DOCKER_COMPOSE} logs -f

docker-compose -f ${DOCKER_COMPOSE} down

exit ${RETVAL}
