# noah_description

This package contains the noah description in urdf format and a launch file to load it to rosparam. The urdf description uses xacro to format it and the meshes can be found in the "meshes" folder.

NOTE: Robot collisions are simple shapes, meshes were not used for the collisions, only the visuals.
NOTE 2: Due to the mismatch in origin position when generating the meshes (in SolidWorks) for the individual parts, the origins of these in the robot urdf description where placed manually to match the collision position.
