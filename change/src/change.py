#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8


def cb (self,date):
    self.vel = date
def ch_cb(messege)
    global ch
    ch = messege.data

def __init__(self):
    rospy.init_node('cmd_change')

	self.vel_sub = rospy.Subscriber("/icart_mini/cmd_vel", Twist, self.cb)
    self.ch_sub =  nh.subscribe("ch_cmd", Int8, ch_cb)
    self.nav_vel_pub = rospy.Publisher('nav_vel',Twist,queue_size=10)
    self.cmd_vel_pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)


        if ch == 1:
        //終了nav_velへ書き換え
            nav_vel_pub.publish(self.vel)

        if ch == 2:
        //cmd_vel優位
            cmd_vel_pub.publish(self.vel)