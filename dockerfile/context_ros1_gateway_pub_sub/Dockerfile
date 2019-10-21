FROM ros1_melodic_to_ros2_dashing_with_custom_messages_build AS build

# build gateway_pub_sub (ROS1)
RUN mkdir -p /srv/ros1_ws/
COPY ros1_ws/src/gateway_msgs /srv/ros1_ws/src/gateway_msgs
COPY ros1_ws/src/gateway_pub_sub /srv/ros1_ws/src/gateway_pub_sub
WORKDIR /srv/ros1_ws/
RUN . /opt/ros/melodic/setup.sh && catkin_make_isolated --install

FROM ros:melodic-ros-base

RUN apt-get update && apt-get install -y python python-pip

RUN python -m pip install pytest

RUN apt-get install -y inetutils-ping nano

# copy in everything required to run the package
COPY --from=build /srv/ros1_ws/install_isolated /srv/ros1_ws/install_isolated
COPY dockerfile/context_ros1_gateway_pub_sub/required_environments.sh /srv/
COPY dockerfile/context_ros1_gateway_pub_sub/entrypoint.sh /srv/
COPY dockerfile/context_ros1_gateway_pub_sub/services.sh /srv/
COPY dockerfile/context_ros1_gateway_pub_sub/test.sh /srv/

WORKDIR /srv

CMD /srv/entrypoint.sh
