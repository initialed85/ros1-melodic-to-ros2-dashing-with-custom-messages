FROM ros1_melodic_to_ros2_dashing_with_custom_messages_build AS build

# build gateway_pub_sub (ROS2)
RUN mkdir -p /srv/ros2_ws/
COPY ros2_ws/src/gateway_interfaces /srv/ros2_ws/src/gateway_interfaces
COPY ros2_ws/src/gateway_pub_sub /srv/ros2_ws/src/gateway_pub_sub
WORKDIR /srv/ros2_ws/
RUN . /opt/ros/dashing/setup.sh && colcon build

FROM ros:dashing-ros-base

RUN apt-get update && apt-get install -y python3 python3-pip

RUN python3 -m pip install pytest

RUN apt-get install -y inetutils-ping nano

# copy in everything required to run the package
COPY --from=build /srv/ros2_ws/install /srv/ros2_ws/install
COPY dockerfile/context_ros2_gateway_pub_sub/required_environments.sh /srv/
COPY dockerfile/context_ros2_gateway_pub_sub/entrypoint.sh /srv/
COPY dockerfile/context_ros2_gateway_pub_sub/services.sh /srv/
COPY dockerfile/context_ros2_gateway_pub_sub/test.sh /srv/

WORKDIR /srv/

CMD /srv/entrypoint.sh
