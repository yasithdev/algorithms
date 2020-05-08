cmake_minimum_required(VERSION 3.6)
project(ieee_extreme)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main11.cpp)
add_executable(ieee_extreme ${SOURCE_FILES})