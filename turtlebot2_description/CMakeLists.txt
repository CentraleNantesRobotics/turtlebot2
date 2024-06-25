cmake_minimum_required(VERSION 3.5)
project(turtlebot2_description)

find_package(ament_cmake REQUIRED)


# assume this package lies in the same workspace as kobuki_description and expend Gz hooks
set(TURTLEBOT2_SHARE "${CMAKE_INSTALL_PREFIX}/share")
string(REPLACE "turtlebot2_description" "kobuki_description" KOBUKI_SHARE ${TURTLEBOT2_SHARE})
ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY meshes urdf launch DESTINATION share/${PROJECT_NAME})

file(GLOB scripts scripts/*)
install(PROGRAMS ${scripts} DESTINATION lib/${PROJECT_NAME})

ament_package()
