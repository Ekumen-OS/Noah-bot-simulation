cmake_minimum_required(VERSION 2.8.3)

project(noah_description)

find_package(catkin REQUIRED COMPONENTS
  roslaunch
)

catkin_package()

roslaunch_add_file_check(launch)

install(DIRECTORY launch urdf meshes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
