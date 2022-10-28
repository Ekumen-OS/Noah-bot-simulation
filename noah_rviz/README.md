# noah_rviz

Package containing the launch file and RViz configuration file for the noah visualization.

## RViz configuration files

Three configuration files are provided:
- noah_navigation_mapless.rviz is used when launching the robot navigation in mapless mode, that is, when not loading the map or the SLAM node.
- noah_navigation.rviz is used when launching the robot in navigation mode with a known map
- noah_slam.rviz is used when launching the robot in SLAM mode.

- The launch file opens RViz with the corresponding RViz configuration file
