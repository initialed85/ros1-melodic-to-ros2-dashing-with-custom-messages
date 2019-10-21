cmake_minimum_required(VERSION 2.8.3)
project(gateway_pub_sub)

# Default to C99
if (NOT CMAKE_C_STANDARD)
    set(CMAKE_C_STANDARD 99)
endif ()

# Default to C++11
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 11)
endif ()

find_package(
        catkin REQUIRED COMPONENTS
        std_msgs
        message_generation
        roscpp
        rospy
        gateway_msgs
)

catkin_package(
        CATKIN_DEPENDS std_msgs message_runtime gateway_msgs
)

install(
        PROGRAMS
        scripts/some_request_to_some_response.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
        tests
        DESTINATION .)
