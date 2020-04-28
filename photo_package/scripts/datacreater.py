#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
import os

imu = ''
k = bool()

def callback1(data):
	global k


	if data.data == 'start':
		k = True
		print('startanuli')
		folder_create()
	elif data.data == 'stop':
		k = False


def callback2(data):
	global imu
	global k
	global directory

	
	while k:
		imu += str(data)
	else:
		if imu != '':
			out = open(directory + "/" + "data_imu.txt", 'wb')
			out.write(imu)
			out.close()
			imu = ''
		else: 
			pass

def folder_create():
	global directory

	print(str(rospy.get_rostime()))

	directory = os.path.dirname(os.path.abspath(__file__))

	if directory != os.environ['HOME']:
		directory = directory[:directory.rfind("/")]

	try:
		os.mkdir(directory + '/result')
	except OSError:
		pass
	directory = directory + '/result'
	os.mkdir(directory + "/" + str(len(os.listdir(directory))+1))
	directory = directory + "/" + str(len(os.listdir(directory)))

def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("/start_stop", String, callback1)
	rospy.Subscriber("/android/imu", Imu, callback2)

	rospy.spin()





if __name__ == '__main__':
    listener()