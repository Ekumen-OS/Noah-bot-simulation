cmake_minimum_required(VERSION 3.0.2)
project(noah_control_utils)

find_package(catkin REQUIRED COMPONENTS
  roslaunch
  geometry_msgs
  rospy
  std_msgs
  move_base
  move_base_sequence
)

################################################
## Declare ROS messages, services and actions ##
################################################

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

###################################
## catkin specific configuration ##
###################################

catkin_package(

)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

catkin_install_python(PROGRAMS
  nodes/wayposes_publisher.py
  nodes/myrobot_key
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
