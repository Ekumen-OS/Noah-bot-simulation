cmake_minimum_required(VERSION 3.0.2)
project(noah_rtabmap)

find_package(catkin REQUIRED COMPONENTS
    rtabmap_ros
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

catkin_package()

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

###########
## Build ##
###########

include_directories()

#############
## Install ##
#############

#############
## Testing ##
#############
