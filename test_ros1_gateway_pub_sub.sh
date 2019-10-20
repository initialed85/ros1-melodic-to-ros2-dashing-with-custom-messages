#!/usr/bin/env bash

PREFIX=spike_ros_interface_gateways
PACKAGE=gateway_pub_sub
ROS_VERSION=ros1
IMAGE_NAME=${PREFIX}_${ROS_VERSION}_${PACKAGE}
CONTAINER_NAME=${IMAGE_NAME}

docker run --rm -d --name ${CONTAINER_NAME} ${IMAGE_NAME}

sleep 1

docker exec -d ${CONTAINER_NAME} /srv/services.sh

sleep 1

docker exec -t ${CONTAINER_NAME} /srv/test.sh
RETVAL=${?}

docker cp ${CONTAINER_NAME}:/srv/test_results/test_results.xml test_results/${ROS_VERSION}_${PACKAGE}.xml

docker rm -f ${CONTAINER_NAME}

exit ${RETVAL}