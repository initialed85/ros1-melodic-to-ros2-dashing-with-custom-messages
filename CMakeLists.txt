cmake_minimum_required(VERSION 3.5)
project(ros1-melodic-to-ros2-dashing-with-custom-messages)

# Default to C++14
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
endif ()

if (CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif ()

set_property(GLOBAL PROPERTY ALLOW_DUPLICATE_CUSTOM_TARGETS 1)

add_subdirectory(ros2_ws/src/gateway_interfaces)
add_subdirectory(ros2_ws/src/gateway_pub_sub)
