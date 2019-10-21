cmake_minimum_required(VERSION 3.5)
project(gateway_pub_sub)

# Default to C++14
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
endif ()

if (CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif ()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(std_msgs REQUIRED)
find_package(gateway_interfaces REQUIRED)

install(PROGRAMS
        scripts/some_request_to_some_response.py
        DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
        tests
        DESTINATION .)

ament_export_dependencies(ament_cmake REQUIRED)
ament_export_dependencies(ament_cmake_python REQUIRED)
ament_export_dependencies(rclcpp REQUIRED)
ament_export_dependencies(rclpy REQUIRED)
ament_export_dependencies(builtin_interfaces REQUIRED)
ament_export_dependencies(std_msgs REQUIRED)
ament_export_dependencies(gateway_interfaces REQUIRED)

ament_package()
