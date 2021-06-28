# noah_2dnav

This package contains the launch files for the robot navigation and the generated .yaml/.pgm 2D maps:

- 2dnav_mapless.launch launches only move_base.
- 2dnav.launch runs the map server node with the map located in the "maps" folder, specified by argument ("rtabmap" by default), runs the amcl self localization node and lastly the move_base launch file from the "move_base_utils" package.
- Generated 2D maps should be places in the maps folder inside this package.
