#!/usr/bin/env bash

source /srv/required_environments.sh

# this is an optional for ROS2
ros2 daemon start

tail -F /dev/null
