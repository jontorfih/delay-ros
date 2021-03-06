#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, TwistStamped

def talker():
    loop_freq = 30
    messag = TwistStamped()
    messag.header = Header()
    pub = rospy.Publisher('chatter', TwistStamped, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(loop_freq) # 10hz
    while not rospy.is_shutdown():
        messag.header.stamp = rospy.Time.now()
        messag.twist.linear.x +=0.001
        messag.twist.linear.y = 2
        messag.twist.linear.z = 3
        pub.publish(messag)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass