## Installing ROS2 Eloquent
Follow the tutorial listed [here](https://docs.ros.org/en/eloquent/Installation/Linux-Install-Debians.html).

## Adding files to ROS project on the Jetson
1. Add new ROS nodes to ~/kraken/ROS/src/kraken/kraken
2. Add included files to ~kraken/ROS/src/kraken/kraken/include
3. Open ~/kraken/ROS/src/kraken/setup.py
4. Within "console_scripts", add "<node_name> = kraken.<file_name>:main"
5. Run "colcon build --packages-select kraken"

## Running a node on the jetson
1. Ensure your environment is setup first by running "source /opt/ros/eloquent/setup.bash".
2. Open the python file of the node you want to run.
3. Change the `sys.path.append()` path to match your environment.
4. Run "source ~/<pwd>/kraken/ROS/install/setup.bash"
5. Run "cd ~/<pwd>/kraken/ROS/src"
6. Run "ros2 run kraken <node_name>"
