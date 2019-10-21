FROM ros1_melodic_to_ros2_dashing_with_custom_messages_build AS build

# build gateway_msgs (ROS1)
RUN mkdir -p /srv/ros1_ws/
COPY ros1_ws/src/gateway_msgs /srv/ros1_ws/src/gateway_msgs
WORKDIR /srv/ros1_ws/
RUN . /opt/ros/melodic/setup.sh && catkin_make_isolated --pkg gateway_msgs --install

# build gateway_interfaces (ROS2)
RUN mkdir -p /srv/ros2_ws/
COPY ros2_ws/src/gateway_interfaces /srv/ros2_ws/src/gateway_interfaces
WORKDIR /srv/ros2_ws/
RUN . /opt/ros/dashing/setup.sh && colcon build --packages-select gateway_interfaces

# build ros1_bridge (ROS2)
RUN mkdir -p /srv/bridge_ws/src
WORKDIR /srv/bridge_ws/src
RUN git clone --single-branch --branch dashing https://github.com/ros2/ros1_bridge.git
WORKDIR /srv/bridge_ws/
RUN . /opt/ros/melodic/setup.sh && . /opt/ros/dashing/setup.sh && . \
    /srv/ros1_ws/install_isolated/setup.sh && . /srv/ros2_ws/install/setup.sh && \
    colcon build --packages-select ros1_bridge --cmake-force-configure

FROM ros1_melodic_to_ros2_dashing_with_custom_messages_build

RUN apt-get install -y inetutils-ping nano

# copy in everything required to run the bridge
COPY --from=build /srv/ros1_ws/install_isolated /srv/ros1_ws/install_isolated
COPY --from=build /srv/ros2_ws/install /srv/ros2_ws/install
COPY --from=build /srv/bridge_ws/install /srv/bridge_ws/install
COPY dockerfile/context_ros2_ros1_bridge/required_environments.sh /srv/
COPY dockerfile/context_ros2_ros1_bridge/entrypoint.sh /srv/

WORKDIR /srv/

CMD /srv/entrypoint.sh
