# noah_2dnav

This package contains the launch files for the robot navigation with their configuration files as well as the generated .yaml/.pgm 2D maps:

- 2dnav.launch is the main launch file for this package. Depending on the arguments it will launch the navigation stack to be able to move without a map, with the pre-saved map or with the SLAM node active in order to generate a map
- amcl.launch launches the amcl node with it's configurations.
- move_base.launch launches the move base node with varying configuration depending on if a map is loaded or not.
