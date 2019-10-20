#!/usr/bin/env bash

source /srv/required_environments.sh

mkdir -p /srv/test_results

python3 -m pytest -v -s --junit-xml=/srv/test_results/test_results.xml /srv/ros2_ws/install/gateway_pub_sub/tests
