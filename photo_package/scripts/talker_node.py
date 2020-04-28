#!/usr/bin/env python

import rospy
import roslib
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("/photo", String, queue_size=10)
    rospy.init_node('take_photo_plz', anonymous=True)
    rate = rospy.Rate(0.1)
    while not rospy.is_shutdown():
        pub.publish(str(raw_input('Enter a command to take a photo\n',)))
        rospy.loginfo("Wait a second...")
        rospy.loginfo(rospy.Time(rospy.get_time()))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass