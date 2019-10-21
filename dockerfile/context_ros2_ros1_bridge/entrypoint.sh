#!/usr/bin/env bash

source /srv/required_environments.sh

ros2 run ros1_bridge dynamic_bridge --print-pairs

ros2 run ros1_bridge dynamic_bridge --bridge-all-topics --show-introspection
