# noah_control_utils

This package contains utilities to control the noah bot:

- Keyboard teleoperation to be able to move the robot using some keys
- Move base sequence launch file, to launch a node whose purpose is to receive waypoints and publish them in order to Move base.
- Wayposes publisher, a custom node created to send the wayposes defined in the mb_goals/mb_goals.yaml config file to the move_base_sequence node. This node will send the goals and move_base_sequence will be in charge of passing those points to move_base in a repeating order (as configured). The goals defined in the mb_goals.yaml configuration file are defined for the **small_house** world, they will most likely not work in another map.
