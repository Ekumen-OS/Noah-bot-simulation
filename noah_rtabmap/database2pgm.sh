#!/bin/bash

# Script to convert from database (rtabmap output) to a .pgm and .yaml file of the 2D map. Uses the default
# map location.
# The user needs to pass the name of the database (without extension) as the first argument

rosrun rtabmap_ros rtabmap _database_path:=~/.ros/$1.db >/dev/null 2>&1 &
sleep 5
rosrun map_server map_saver map:=grid_map -f rtabmap  &
sleep 5
rosservice call /publish_map 1 1 0 &
sleep 5
rosnode kill rtabmap
