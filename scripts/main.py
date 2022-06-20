#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PKG = 'ts'
import roslib; roslib.load_manifest(PKG)
from turtlesim.srv import Spawn
vel =  2
rot = Twist()
x,y= 5,5
arr_coord == []
arr_vel = []

def call(x,y):
    global spawn_turtle
    spawn_turtle(x,y,0,"main")


def callback1(data):
    global x,y
    x = data.x
    y = data.y

def move():
    global x,y
    rospy.Subscriber("one/pose", Pose,callback1)
    if x == 5 and y == 5:
        rot.linear.x = vel
        rot.linear.y = vel

    if x >= 8 or y >= 8 or x <= 2 or y <= 2:
        call(name,x,y) 
        if x >= 8:
            rot.linear.x = -vel
            rot.linear.y = vel
        elif x <=2:
            rot.linear.x = vel
            rot.linear.y = -vel
        elif y >=8:
            rot.linear.x = -vel
            rot.linear.y = -vel

        else:
            rot.linear.x = vel 
            rot.linear.y = vel
         
    rospy.init_node('turtle_bot')
    pub = rospy.Publisher('one/cmd_vel',Twist,queue_size = 1)
    rate = rospy.Rate(10)



def 

rospy.wait_for_service('spawn')
spawn_turtle = rospy.ServiceProxy('spawn', Spawn)  


while not rospy.is_shutdown():
    def make_new(num):
        move()
    pub.publish(rot)
    rate.sleep()