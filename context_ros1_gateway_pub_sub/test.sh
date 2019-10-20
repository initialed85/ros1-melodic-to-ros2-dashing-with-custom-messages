#!/usr/bin/env bash

source /srv/required_environments.sh

mkdir -p /srv/test_results

python -m pytest -v -s --junit-xml=/srv/test_results/test_results.xml /srv/ros1_ws/install_isolated/tests
