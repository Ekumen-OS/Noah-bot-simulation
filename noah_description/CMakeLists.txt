cmake_minimum_required(VERSION 2.8.3)

project(noah_description)

find_package(catkin REQUIRED COMPONENTS
  roslaunch
)

catkin_package()

install(DIRECTORY urdf meshes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
