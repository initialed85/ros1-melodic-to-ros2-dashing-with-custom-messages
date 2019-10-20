# spike-ros-interface-gateways

This spike demonstrates the following:

- a custom ROS2 interfaces package `ros2_ws/src/gateway_interfaces` 
- a custom ROS1 interfaces package `ros1_ws/src/gateway_msgs`
- building a custom `ros1_bridge` package referencing the above two packages
- some tests

## How do I set up my environment?

### Assumptions

- MacOS
- CLion
- ROS2 already installed

### Steps

- in a terminal, before you've opened CLion
    - (change directory to the root of this repo)
    - `cd ros2_ws/src`
    - `source ~/ros2_install/ros2-osx/setup.bash`
        - this adjusts your environment for building ROS2 packages
    - `colcon build --symlink-install`
        - this generates `build` and `install` folders with headers / libraries etc for the messages
    - `source install/setup.bash`
        - this adjusts your environment for this ROS2 workspace
    -  `/Applications/CLion.app/Contents/MacOS/clion`
        - open this repo, point at the base `CMakeLists.txt`
    - you should now have header / library code completion

## How do I build it?

- `./build.sh`
    - builds the `gateway_msgs` package for ROS1
    - builds the `gateway_interfaces` package for ROS2
    - builds the `ros1_gateway` for ROS2 (which references the two above)
    - builds the `gateway_pub_sub` for ROS1 (which references the `gateway_msgs` package)
    - builds the `gateway_pub_sub` for ROS2 (which references the `gateway_interfaces` package)

## How to I test it?

- `./test.sh`
    - for `gateway_pub_sub` for ROS1
        - runs a ROS1 container, including:
            - the `roscore` daemon
            - the `some_request_to_some_response.py` node
        - runs the integration tests inside that container against that node
    - for `gateway_pub_sub` for ROS2
        - runs a ROS1 container, including:
            - the ROS daemon (optional for ROS2)
            - the `some_request_to_some_response.py` node
        - runs the integration tests inside that container against that node

## Folder breakdown (in logical order)

- `ros1_ws` - ROS1 workspace for `gateway_msgs` (ROS1 interface package) and `gateway_pub_sub` (example ROS1 implementation)
    - notable files for `gateway_msgs`:
        - `gateway_msgs/package.xml` - package definition for catalogue purposes 
        - `gateway_msgs/CMakeLists.xml` - package definition for build purposes
        - `gateway_msgs/msg/SomeRequest.msg`
        - `gateway_msgs/msg/SomeRequest.msg`
    - notable files for `gateway_pub_sub`:
        - `gateway_pub_sub/package.xml` - package definition for catalogue purposes 
        - `gateway_pub_sub/CMakeLists.xml` - package definition for build purposes
        - `gateway_pub_sub/scripts/some_request_to_some_response.py` - ROS node that subscribes to `some_request : SomeRequest` and publishes to `some_response : SomeResponse` per each subscription callback
        - `gateway_pub_sub/tests/some_request_to_some_response_test.py` - integration test using `rospy` to communicate with the node above (assumes it's already running) 
- `ros2_ws` - ROS1 workspace for `gateway_interfaces` (ROS2 interface package) and `gateway_pub_sub` (example ROS1 implementation)
    - notable files for `gateway_interfaces`:
        - `gateway_interfaces/package.xml` - package definition for catalogue purposes 
        - `gateway_interfaces/CMakeLists.xml` - package definition for build purposes
        - `gateway_interfaces/msg/SomeRequest.msg`
        - `gateway_interfaces/msg/SomeRequest.msg`
    - notable files for `gateway_pub_sub`:
        - `gateway_pub_sub/package.xml` - package definition for catalogue purposes 
        - `gateway_pub_sub/CMakeLists.xml` - package definition for build purposes
        - `gateway_pub_sub/scripts/some_request_to_some_response.py` - ROS node that subscribes to `some_request : SomeRequest` and publishes to `some_response : SomeResponse` per each subscription callback
        - `gateway_pub_sub/tests/some_request_to_some_response_test.py` - integration test using `rclpy` to communicate with the node above (assumes it's already running) 

## Takeaways

- if you want to generate messages externally...
    - you'll need to generate them in both ROS1 and ROS2 formats and place them in the following locations:
        - `ros1_ws/src/gateway_msg/msg`  
        - `ros2_ws/src/gateway_interfaces/msg`
    - you'll also need to update `CMakeLists.txt` for each package to reference the new messages files
    - finally you'll need to recompile the `ros1_gateway` package (so just re-run `build.sh`)
- adjacent ROS1 nodes need to be made aware of a `roscore` via the `ROS_MASTER_URI` environment variable (default `http://localhost:11311`)
    - if you want to do multi-container testing, you'll need to handle hostnames and adjust the `ROS_MASTER_URI` environment variable as applicable
