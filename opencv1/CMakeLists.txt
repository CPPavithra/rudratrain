cmake_minimum_required(VERSION 3.10)

project(rotateimage)

find_package(OpenCV REQUIRED)
INCLUDE_DIRECTORIES( ${OpenCV_INCLUDE_DIRS})
add_executable(rotateimage flip_camera_image.cpp)

target_link_libraries(rotateimage ${OpenCV_LIBS})
