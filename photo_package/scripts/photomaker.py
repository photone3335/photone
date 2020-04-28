#!/usr/bin/env python

import urllib
import rospy
from std_msgs.msg import String
import os
import urllib

url='http://192.168.1.123:8080/photo.jpg'

def callback(data):
	parser()


def parser():
	global url

	pub = rospy.Publisher("/start_stop", String, queue_size=10)
	pub.publish('start')

	resource = urllib.urlopen(url)
	pub.publish('stop')

	#time1 = rospy.get_rostime()

	directory = os.path.dirname(os.path.abspath(__file__))

	if directory != os.environ['HOME']:
		directory = directory[:directory.rfind("/")]

	directory = directory + '/result'
	directory = directory + "/" + str(len(os.listdir(directory)))

	out = open(directory + "/" + "img.jpg", 'wb')
	out.write(resource.read())
	out.close()




def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("/photo", String, callback)


	rospy.spin()





if __name__ == '__main__':
    listener()