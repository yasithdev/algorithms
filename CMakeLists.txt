cmake_minimum_required(VERSION 3.8)
project(ieeextreme11)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp knin.cpp runningupstairs.cpp)
add_executable(ieeextreme11 ${SOURCE_FILES})