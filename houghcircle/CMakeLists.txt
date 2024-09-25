cmake_minimum_required(VERSION 3.10)

project(houghcircle)

find_package(OpenCV REQUIRED)

add_executable(houghcircle houghcircle.cpp)


target_link_libraries(houghcircle ${OpenCV_LIBS})

