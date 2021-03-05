#!/usr/bin/env python

import sys
import rospy
import tf
import moveit_commander
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur5e_move')
group = [moveit_commander.MoveGroupCommander("manipulator")]

xx = 1

while not rospy.is_shutdown():
  if(xx%2 == 1):
    pose_goal.orientation.w = 0.0
    pose_goal.orientation.x = 2.1
    pose_goal.orientation.y = 0.0
    pose_goal.orientation.z = 0.0
    pose_goal.position.x = 0.0 # red line      0.2   0.2
    pose_goal.position.y = -0.4  # green line  0.15   0.15
    pose_goal.position.z = 0.3  # blue line   # 0.35   0.6
    group[0].set_pose_target(pose_goal)
    group[0].go(True)

    #print(xx)
    rospy.sleep(1)

  else:
    pose_goal.orientation.w = 0.0
    pose_goal.orientation.x = 2.1
    pose_goal.orientation.y = 0.0
    pose_goal.orientation.z = 0.0
    pose_goal.position.x = 0.0 # red line      0.2   0.2
    pose_goal.position.y = -0.6  # green line  0.15   0.15
    pose_goal.position.z = 0.3  # blue line   # 0.35   0.6
    group[0].set_pose_target(pose_goal)
    group[0].go(True)

    #print(xx)
    rospy.sleep(1)

  xx = xx + 1


'''
pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.4 # red line      0.2   0.2
pose_goal.position.y = 0.15  # green line  0.15   0.15
pose_goal.position.z = 0.5  # blue line   # 0.35   0.6
group[0].set_pose_target(pose_goal)
group[0].go(True)
'''
moveit_commander.roscpp_shutdown()
