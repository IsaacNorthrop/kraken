#!/bin/bash

rm -rf /home/isaacn/code/kraken/ROS/install /home/isaacn/code/kraken/ROS/log
source /opt/ros/eloquent/setup.bash
rosdep install -i --from-path ROS/src --rosdistro eloquent -y
colcon build --packages-select kraken --symlink-install
source ~/code/kraken/ROS/install/setup.bash
. install/setup.bash
source ~/code/kraken/ROS/install/setup.bash
cd ~/code/kraken/ROS/src
ros2 run kraken $1