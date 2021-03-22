#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float


def cb (self,date):
    self.vel = date 

def __init__(self):
    rospy.init_node('cmd_change')

	self.vel_sub = rospy.Subscriber("/icart_mini", Twist, self.cb)
    self.ch_sub =  nh.subscribe("ch_cmd", 1, &WaypointsNavigation::cmdVelCallback, this);
    self.nav_vel_pub = rospy.Publisher('nav_vel',Twist,queue_size=10)
    self.cmd_vel_pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)


        if ch == 1:
        //終了nav_velへ書き換え
            nav_vel_pub.publish(self.vel)

        if ch == 2:
        //cmd_vel優位
            cmd_vel_pub.publish(self.vel)