#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, TwistStamped
from threading import Thread
from collections import deque


mes = PoseStamped()
mes.header = Header()
start = True
xlist = deque([])
ylist = deque([])
zlist = deque([])

xorlist = deque([])
yorlist = deque([])
zorlist = deque([])
worlist = deque([])

def startchange(starts):
    d = rospy.Duration(0,10000)
    d = float(0.01)
    rospy.sleep(1)
    global start
    start = starts


def pub_mesg():
    if(start == True):
        startchange(False)
    
    pub = rospy.Publisher('pos_chatter', PoseStamped, queue_size=2000)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        mes.header.stamp = rospy.Time.now()
        mes.header.frame_id = 'map'
        mes.pose.position.x  = xlist[0]
        mes.pose.position.y  = ylist[0]
        mes.pose.position.z  = zlist[0]
        xlist.popleft()
        ylist.popleft()
        zlist.popleft()
        
        mes.pose.orientation.x = xorlist[0]
        mes.pose.orientation.y = yorlist[0]
        mes.pose.orientation.z = zorlist[0]
        pub.publish(mes)

        try:
            rate.sleep()
        except rospy.ROSInterruptException:
            pass

def callbacks(data):  
    xlist.append(data.pose.position.x)
    ylist.append(data.pose.position.y)
    zlist.append(data.pose.position.z)

    xorlist.append(data.pose.orientation.x)
    yorlist.append(data.pose.orientation.y)
    zorlist.append(data.pose.orientation.z)
    worlist.append(data.pose.orientation.w)
    
def listener():
        
    pub_thread = Thread(target=pub_mesg, args=())
    pub_thread.daemon = True
    pub_thread.start()
    
    rospy.init_node('pub_mesg', anonymous=True)

    #rospy.init_node('listener', anonymous=True)
    
    #rospy.init_node('pub_mesg', anonymous=True)
    
    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, callback= callbacks, queue_size=2000)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':   
    listener()
