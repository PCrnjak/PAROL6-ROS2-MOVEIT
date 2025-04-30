# PAROL6-ROS2-MOVEIT
PAROL6 ROS2 MOVEIT

  Ubuntu version: 22.04
  Install ROS2 Humble: https://aleksandarhaber.com/how-to-properly-install-moveit2-in-ros2-humble-and-fix-tutorial-errors/
  
  Other option to install Moveit: sudo apt install ros-humble-moveit
  
  Create new workspace:
  mkdir -p ~/ros2_ws/src
  cd ~/ros2_ws
  
  Copy this repo to ros2_ws/src
  
  colcon build
  source /opt/ros/humble/setup.bash
  source install/setup.bash

  sudo apt update
  sudo apt install --reinstall ros-humble-geometric-shapes

  LC_NUMERIC=en_US.UTF-8 ros2 launch parol6_moveit demo.launch.py
