cmake_minimum_required(VERSION 2.8.3)

project(noah_2dnav)

find_package(catkin REQUIRED COMPONENTS
  map_server
  amcl
  noah_control_utils
)

catkin_package()

roslaunch_add_file_check(launch)

install(DIRECTORY launch configs
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
