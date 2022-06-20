#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PKG = 'ts'
import roslib; roslib.load_manifest(PKG)
from turtlesim.srv import Spawn
vel =  1
flag = 0

rospy.init_node('turtle_bot')

rospy.wait_for_service('spawn')
spawn_turtle = rospy.ServiceProxy('spawn', Spawn)  
count = 1

class New_turtle():
    def __init__(self,name,x,y):
        global vel
        self.state = "clockwise"
        global count
        global spawn_turtle
        self.name = name
        self.x = x 
        self.y = y
        spawn_turtle(self.x,self.y,0,name)
        self.move()
        
    def callback1(self,data):
        self.x = data.x
        self.y = data.y
        
    def move(self):
        global flag 
        self.rot = Twist()
        global count
        self.pub = rospy.Publisher(self.name + "/cmd_vel",Twist,queue_size = 1)
        #rospy.loginfo(self.name)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            rospy.Subscriber(self.name + "/pose", Pose,self.callback1)
            if self.rot.linear.x == 0 or self.rot.linear.y ==0:
                self.rot.linear.x = vel
                self.rot.linear.y = vel
            if self.x >= 8 or self.y >= 8 or self.x <= 2 or self.y <= 2:
                count += 1
                #rospy.loginfo(f"a{count}")
                if self.x >= 8:
                    #rospy.loginfo("check")    
                    if self.rot.linear.x != -vel or  self.rot.linear.y != vel: 
                        self.rot.linear.x = -vel
                        self.rot.linear.y = vel
                elif self.x <=2:
                    if self.rot.linear.x != vel or  self.rot.linear.y != -vel:
                        self.rot.linear.x = vel                     
                        self.rot.linear.y = -vel
                elif self.y >=8:
                    if self.rot.linear.x != -vel or self.rot.linear.y != -vel:
                        self.rot.linear.x = -vel
                        self.rot.linear.y = -vel
                else:
                    if self.rot.linear.x != vel or self.rot.linear.y != vel:
                        self.rot.linear.x = vel 
                        self.rot.linear.y = vel
                if flag == 0:
                    rospy.loginfo(flag)
                    flag +=1
                    New_turtle(f"a{count}",self.x,self.y)
            self.pub.publish(self.rot)
            rate.sleep()





t = New_turtle("a1",5,5)
