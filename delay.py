#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, TwistStamped
from threading import Thread
from collections import deque


mes = TwistStamped()
mes.header = Header()
start = True
xlist = deque([])
ylist = deque([])
zlist = deque([])

def startchange(starts):
    d = rospy.Duration(0,10000)
    d = float(0.01)
    rospy.sleep(3)
    global start
    start = starts


def pub_mesg():
    if(start == True):
        startchange(False)
    
    pub = rospy.Publisher('chatter2', TwistStamped, queue_size=2000)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        mes.header.stamp = rospy.Time.now()
        mes.twist.linear.x  = xlist[0]
        mes.twist.linear.y  = ylist[0]
        mes.twist.linear.z  = zlist[0]
        xlist.popleft()
        ylist.popleft()
        zlist.popleft()
        pub.publish(mes)

        try:
            rate.sleep()
        except rospy.ROSInterruptException:
            pass

def callbacks(data):  
    xlist.append(data.twist.linear.x)
    ylist.append(data.twist.linear.y)
    zlist.append(data.twist.linear.z)

    
    
def listener():
        
    pub_thread = Thread(target=pub_mesg, args=())
    pub_thread.daemon = True
    pub_thread.start()
    
    rospy.init_node('pub_mesg', anonymous=True)

    #rospy.init_node('listener', anonymous=True)
    
    #rospy.init_node('pub_mesg', anonymous=True)
    
    rospy.Subscriber("chatter", TwistStamped, callback= callbacks, queue_size=2000)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':   
    listener()