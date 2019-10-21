#!/usr/bin/env bash

TEST=test_against_ros2_from_ros1
DOCKER_COMPOSE=docker_compose/${TEST}/docker-compose.yml
JUNIT_XML=ros2_gateway_pub_sub_from_ros1.xml

# docker-compose version of "docker exec -t" (vs -it, which Jenkins doesn't link)
export COMPOSE_INTERACTIVE_NO_CLI=1

docker-compose -f ${DOCKER_COMPOSE} up -d

docker-compose -f ${DOCKER_COMPOSE} exec -d -T ros_under_test /srv/services.sh

docker-compose -f ${DOCKER_COMPOSE} exec -d -T ros_test_harness /srv/services.sh

sleep 5

docker-compose -f ${DOCKER_COMPOSE} exec -T ros_test_harness /srv/test.sh
RETVAL=${?}

# TODO: fix assumed container name
docker cp ${TEST}_ros_test_harness_1:/srv/test_results/test_results.xml test_results/${JUNIT_XML}

docker-compose -f ${DOCKER_COMPOSE} down

exit ${RETVAL}
