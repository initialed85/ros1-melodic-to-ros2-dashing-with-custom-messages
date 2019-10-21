#!/usr/bin/env bash

rm -fr test_results

mkdir -p test_results

./scripts/test_ros1_gateway_pub_sub.sh
RETVAL_1=${?}

./scripts/test_ros2_gateway_pub_sub.sh
RETVAL_2=${?}

./scripts/test_ros1_gateway_pub_sub_from_ros2.sh
RETVAL_3=${?}

./scripts/test_ros2_gateway_pub_sub_from_ros1.sh
RETVAL_4=${?}

if [[ ${RETVAL_1} -ne 0 ]]; then
  exit ${RETVAL_1}
fi

if [[ ${RETVAL_2} -ne 0 ]]; then
  exit ${RETVAL_2}
fi

if [[ ${RETVAL_3} -ne 0 ]]; then
  exit ${RETVAL_3}
fi

if [[ ${RETVAL_4} -ne 0 ]]; then
  exit ${RETVAL_4}
fi
