FROM spike_ros_interface_gateways_build AS build

# build gateway_pub_sub (ROS1)
RUN mkdir -p /srv/ros1_ws/
COPY ros1_ws/src/gateway_msgs /srv/ros1_ws/src/gateway_msgs
COPY ros1_ws/src/gateway_pub_sub /srv/ros1_ws/src/gateway_pub_sub
WORKDIR /srv/ros1_ws/
RUN . /opt/ros/melodic/setup.sh && catkin_make_isolated --install

FROM ros:melodic-ros-base

RUN apt-get update && apt-get install -y python python-pip

RUN python -m pip install pytest

# copy in everything required to run the package
COPY --from=build /srv/ros1_ws/install_isolated /srv/ros1_ws/install_isolated
COPY context_ros1_gateway_pub_sub/required_environments.sh /srv/
COPY context_ros1_gateway_pub_sub/entrypoint.sh /srv/
COPY context_ros1_gateway_pub_sub/services.sh /srv/
COPY context_ros1_gateway_pub_sub/test.sh /srv/

WORKDIR /srv

CMD /srv/entrypoint.sh
