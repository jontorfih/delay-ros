#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from threading import Thread


mes = PoseStamped()
start = True
def startchange(starts):
    rospy.sleep(10)
    global start
    start = starts


def pub_mesg():
    if(start == True):
        startchange(False)
    
    pub = rospy.Publisher('chatter2', PoseStamped, queue_size=2000)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(mes)

        try:
            rate.sleep()
        except rospy.ROSInterruptException:
            pass

def callbacks(data):  
    mess = data
    rosinmess.pose.position.x
    
    
def listener():

    pub_thread = Thread(target=pub_mesg, args=())
    pub_thread.daemon = True
    pub_thread.start()
    
    rospy.init_node('listener', anonymous=True)

    
    rospy.Subscriber("chatter", PoseStamped, callback= callbacks, queue_size=2000)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    listener()