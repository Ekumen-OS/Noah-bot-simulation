cmake_minimum_required(VERSION 2.8.3)

project(noah_gazebo)

find_package(catkin REQUIRED COMPONENTS
	gazebo_ros
	gazebo_plugins
	noah_description
	noah_2dnav
	noah_rtabmap
	noah_rviz
	noah_control_utils
	roslaunch
)

catkin_package()

roslaunch_add_file_check(launch)

install(DIRECTORY launch worlds models photos
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
