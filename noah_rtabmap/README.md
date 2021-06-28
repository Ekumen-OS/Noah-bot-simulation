# noah_rtabmap

This package contains:

- The launch file used to launch the rtab node and nodelet used for SLAM. This launchfile is called in the higher level "noah_slam.launch" launch file in the noah_gazebo package.
- A user script (database2pgm.sh) to convert from the database that rtab generates to the 2D map.pgm and map.yaml files used for the map server. This script accepts the name (without extension) of the database as a first and only argument and assumes the database is saves in its default location in "~/.ros/<DBNAME>.db".
