#!/bin/bash

rosdep install -i --from-path src --rosdistro eloquent -y
colcon build --packages-select kraken
source /opt/ros/eloquent/setup.bash
source ~/code/kraken/ROS/install/setup.bash
cd ~/code/kraken/ROS/src
ros2 run kraken $1