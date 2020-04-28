cmake_minimum_required(VERSION 2.8.3)
project(photo_package)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
)

catkin_package()

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(
	PROGRAMS
	    scripts/photo_node.py
	DESTINATION
	    ${CATKIN_PACKAGE_BIN_DESTINATION}
)
