cmake_minimum_required(VERSION 2.8.3)
project(gateway_msgs)

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
)

add_message_files(
        FILES
        SomeRequest.msg
        SomeResponse.msg
)

generate_messages(
        DEPENDENCIES
        std_msgs
)

catkin_package(
        CATKIN_DEPENDS std_msgs message_runtime
)
