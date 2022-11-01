# Noah-bot simulation

This repository contains a simulation for the Noah-bot robot. It contains an URDF model of the robot with visual meshes included, a Kinect camera, a laser sensor and a differential drive gazebo-ros plugin.

![image](https://user-images.githubusercontent.com/77001289/125287999-03e26b80-e2f4-11eb-9619-a15130b4b15f.png)

Packages where built to show how to use the robot to perform SLAM and navigate through an unknown or known map. Documentation on each individual package can be found in each one of them.

Developed in:
- Ubuntu 20.04
- ROS1 Noetic
- Gazebo 11
- Catkin


## Installation with docker

This project comes with a dockerfile for better portability. Keep in mind that if SLAM is ran while in the docker process, the database will be saved to a folder that's not mounted to the local machine, so when the docker process dies, the database generated from the SLAM will be lost.

1. [Install docker](https://docs.docker.com/engine/install/ubuntu/)
2. Clone this repository
3. Place yourself in the docker folder inside the project:
```
cd <PROJECT>/docker
```
4. Build the docker image:
```
./build
```
5. Run the script to run the docker image and mount the project. **IMPORTANT:** If the user does not own an nvidia gpu, delete the "`--gpus all \`" line
```
./run_docker
```
6. Download dependencies for the packages
```
cd /home/catkin_ws
sudo apt-get update
rosdep install --from-paths src --ignore-src -r -y
```
7. Build the project and source the workspace
```
cd /home/catkin_ws
catkin_make
source devel/setup.bash
```
8. Launch one of the [top level launchfiles](README.md#top-level-launch-files)!
9. If the user wants to open more terminals inside the docker process, in a new terminal run:
```
./run_docker
source /opt/ros/noetic/setup.bash
source /home/catkin_ws/devel/setup.bash
```


## Installation without Docker

Disclaimer: This has only been tested with the versions and software specified above. Running it with other versions is not guaranteed to work.

1. [Install ROS](http://wiki.ros.org/noetic/Installation/Ubuntu)
2. [Install Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu)
3. Clone this repository in the src folder of a catkin workspace
4. Place yourself in the catkin workspace. The folder structure should look like this: `<PATH>/catkin_ws/src/<REPOSITORY>`

5. Download dependencies for the packages
```
rosdep install --from-paths src --ignore-src -r -y
```
6. Build the project and source the workspace
```
catkin_make
source devel/setup.bash
```
7. Launch one of the [top level launchfiles](README.md#top-level-launch-files)!


## Top level launch files

- Launch SLAM node to map a world. Can move the robot with goals or with the keyboard control node:
    ```
    $ roslaunch noah_gazebo  noah_slam.launch database_name:=<DATABASE_NAME>
    ```

- Launch navigation node. Includes wayposes publisher node:
    ```
    $ roslaunch noah_gazebo noah_gazebo.launch map_name:=<MAP_NAME>
    ```

- Launch mapless navigation node:
    ```
    $ roslaunch noah_gazebo noah_gazebo.launch
    ```

- Launch keyboard control (useful to move robot when generating the SLAM):
    ```
    $ roslaunch noah_control keyboard_teleop.launch
    ```


## Testing worlds
- willowgarage -> Comes included with Gazebo. No map generated.
- small_house -> Taken from AWS open repository. A SLAM generated map is provided for this map.

## SLAM generated map
A map was generated for the "small_house" world using the SLAM Rtabmap package. This package creates a database from which the rtabmap.pgm and rtabmap.yaml files were taken. This files are used for the localization and move_base packages. The package stores the database in "~/.ros/rtabmap.db" (default location) from which the .pgm and .yaml can be extracted using the "database2pgm.sh" script located in "noah_rtabmap" package.

The user can specify the name of the database to be saved by passing the "database_name" argument to the slam launch file.

## Navigation launch file map name
The user can specify the map in the navigation launch file by specifying the argument "map_name". Maps are located in the noah_2dnav package inside the maps folder. The default value is "rtabmap".

## Wayposes publisher
A package was created to publish a set of goals for the move_base_sequence node. The goals are defined in a .yaml file located in noah_control_utils/mb_goals folder.
