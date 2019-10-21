FROM ros:melodic-ros-base-bionic

ENV DEBIAN_FRONTEND noninteractive

RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime

RUN apt-get update && apt-get install -y curl gnupg2 lsb-release tzdata

RUN dpkg-reconfigure --frontend noninteractive tzdata

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

RUN sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'

RUN apt-get update && apt-get install -y ros-dashing-ros-base python3-argcomplete \
    python3-colcon-common-extensions python-rosdep libpython3-dev python-pip python3-pip

RUN python -m pip install pytest && python3 -m pip install pytest

RUN rosdep update && rosdep install --from-paths /opt/ros/dashing/share --ignore-src --rosdistro dashing -y \
    --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 osrf_testing_tools_cpp poco_vendor rmw_connext_cpp rosidl_typesupport_connext_c rosidl_typesupport_connext_cpp rti-connext-dds-5.3.1 tinyxml_vendor tinyxml2_vendor urdfdom urdfdom_headers"
