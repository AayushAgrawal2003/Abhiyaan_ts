import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from os import system
class turtle:
    def __init__(self,pos,tp,velo):
        self.box_X0 = pos[0]
        self.box_X1 = pos[1]
        self.box_Y0 = pos[2]
        self.box_Y1 = pos[3]
        self.name = "turtle{}".format(int(time.time()*1000))
        system("rosservice call /spawn {} {} 0 {}".format(tp[0],tp[1],self.name))
        self.vel = rospy.Publisher("/{}/cmd_vel".format(self.name),Twist,queue_size = 10)
        self.rate = rospy.Rate(10)
        self.vm = Twist()
        self.vm.linear.x = velo[0]
        self.vm.linear.y = velo[1]
    def yourdutyisnotover(self):
        rospy.Subscriber("/{}/pose".format(self.name), Pose, self.cur_pos)
        self.vel.publish(self.vm)
    def cur_pos(self,data):
        print(self.name,self.vm.linear.x,self.vm.linear.y,data.x,data.y)
        self.vel.publish(self.vm)
        if data.x >= self.box_X1  or data.x <= self.box_X0 :
            self.vm.linear.x *= -1
            self.vel.publish(self.vm)
            cx = self.vm.linear.x
            cy = -1*self.vm.linear.y
            if data.x <= self.box_X0:
                px = data.x*101/100
            else:
                px = data.x * 99/100
            if data.y <=self.box_Y0:
                py = data.y*101/100
            else:
                py = data.y * 99/100
            ob = turtle([self.box_X0,self.box_X1,self.box_Y0,self.box_Y1],[px,py],[cx , cy])
            ob.yourdutyisnotover()
        if data.y <= self.box_Y0  or data.y >=  self.box_Y1:
            self.vm.linear.y *= -1
            self.vel.publish(self.vm)
            cx = -1*self.vm.linear.x
            cy = self.vm.linear.y
            if data.x <= self.box_X0:
                px = data.x*101/100
            else:
                px = data.x * 99/100
            if data.y <=self.box_Y0:
                py = data.y*101/100
            else:
                py = data.y * 99/100
            ob = turtle([self.box_X0,self.box_X1,self.box_Y0,self.box_Y1],[px,py],[cx , cy])
            ob.yourdutyisnotover()

rospy.init_node("Tut_Node")
for i in range(20):
    ob = turtle([1,6.5,1,6],[2,2],[1,0.2])
    ob.yourdutyisnotover()
    break
rospy.spin()