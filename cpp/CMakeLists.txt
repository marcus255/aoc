cmake_minimum_required(VERSION 3.10)

# Set the project name
project(AdventOfCode)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files
file(GLOB SOURCES "framework/src/*.cpp" "2024/src/*.cpp")

# Include main.cpp explicitly
list(APPEND SOURCES "main.cpp")

# Include directories
include_directories(framework/inc)
include_directories(2024/inc)

# Set compiler flags for GCC
if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")
endif()

# Add the executable
add_executable(AdventOfCode ${SOURCES})