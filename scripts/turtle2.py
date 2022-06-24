#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

count = 1
spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
bounds = [1,9]
vel =3 
class Turtle:
    def __init__(self,c,spawn_location, vx, vy):
        rospy.wait_for_service('spawn')
        self.vx = vx
        self.vy = vy
        [a,b] = spawn_location
        self.name = f"a{c}"
        self.count = c
        self.rot = Twist()
        
        self.rot.linear.z = 0
        self.rot.angular.x = 0
        self.rot.angular.y = 0
        self.rot.angular.z = 0
        
        spawn_turtle(a, b, 0, self.name)
        rospy.Subscriber(f"/a{c}/pose", Pose, self.current_pose)
        self.pub = rospy.Publisher(f"/a{c}/cmd_vel", Twist, queue_size=100)

    def current_pose(self, k):
        
        if (k.x < 1 and self.vx < 0) or (k.x > 10 and self.vx > 0) or (
                k.y < 1 and self.vy < 0) or (k.y > 10 and self.vy > 0):
            self.New_turtle(k.x, k.y)
        else:
            self.rot.linear.x = self.vx
            self.rot.linear.y = self.vy

            self.pub.publish(self.rot)
        

    def New_turtle(self, x, y):
        global count
        count += 1
        if x > bounds[1] or x < bounds[0]:
            self.vx *= -1
            self.rot.linear.x = self.vx            
            Turtle(count, (x, y), self.vx, -self.vy)

        elif y > bounds[1] or y < bounds[0]:
            self.vy *= -1
            self.rot.linear.y = self.vy
            Turtle(count, (x, y), -self.vx, self.vy)
        self.pub.publish(self.rot)

    


    

if __name__ == '__main__':
    rospy.init_node('turtle')
    Turtle(1, [5, 5], vel,vel-1)
    rate = rospy.Rate(200)
    while not rospy.is_shutdown():
        rate.sleep()
