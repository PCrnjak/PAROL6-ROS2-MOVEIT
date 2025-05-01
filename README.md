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


Names of stuff for URDF needs to be lowercase!!!!!!

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 pkg list | grep parol6

ros2 run moveit_setup_assistant moveit_setup_assistant


ros2 launch moveit_robot_arm_sim demo.launch.py
LC_NUMERIC=en_US.UTF-8 ros2 launch parol6_moveit demo.launch.py


sudo apt update
sudo apt install --reinstall ros-humble-geometric-shapes

ros2 launch moveit_setup_assistant setup_assistant.launch.py

ili uninstall ros2 moveit i ovo:

sudo apt install ros-humble-moveit


https://robotics.stackexchange.com/questions/103300/error-loading-custom-robotic-manipulator-model-in-moveit2-on-ros2-humbleerror-l


package.xml for ros2:

<package format="3">
  <name>parol6</name>
  <version>1.0.0</version>
  <description>
    URDF Description package for PAROL6. This package contains configuration data,
    3D models, and launch files for the PAROL6 robot.
  </description>

  <maintainer email="TODO@email.com">TODO</maintainer>
  <license>BSD</license>

  <buildtool_depend>ament_cmake</buildtool_depend>

  <exec_depend>robot_state_publisher</exec_depend>
  <exec_depend>rviz2</exec_depend>
  <exec_depend>joint_state_publisher</exec_depend>
  <exec_depend>joint_state_publisher_gui</exec_depend>
  <exec_depend>gazebo_ros</exec_depend>

  <export>
    <build_type>ament_cmake</build_type>
  </export>
</package>


CMakeLists.txt

cmake_minimum_required(VERSION 3.5)
project(parol6)

find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf launch meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

