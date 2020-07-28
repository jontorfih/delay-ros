#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped

def talker():
    loop_freq = 10
    messag = PoseStamped()
    messag.header = Header()
    pub = rospy.Publisher('chatter', PoseStamped, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(loop_freq) # 10hz
    while not rospy.is_shutdown():
        messag.header.stamp = rospy.Time.now()
        messag.pose.position.x +=0.001
        messag.pose.position.y = 2
        messag.pose.position.z = 3
        messag.pose.orientation.x = 11        
        pub.publish(messag)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass