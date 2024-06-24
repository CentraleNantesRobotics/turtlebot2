cmake_minimum_required(VERSION 3.5)
project(turtlebot2_description)

find_package(ament_cmake REQUIRED)


set(TURTLEBOT2_SHARE "${CMAKE_INSTALL_PREFIX}/share")
message(${TURTLEBOT2_SHARE})
string(REPLACE "turtlebot2_description" "kobuki_description" KOBUKI_SHARE ${TURTLEBOT2_SHARE})
message(${KOBUKI_SHARE})
ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY meshes urdf launch DESTINATION share/${PROJECT_NAME})

ament_package()
