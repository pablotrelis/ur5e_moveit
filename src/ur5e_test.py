#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
import math
from std_msgs.msg import String
from std_msgs.msg import Header
from std_msgs.msg import Duration

pub = rospy.Publisher('/scaled_pos_traj_controller/command' ,JointTrajectory, queue_size=10)
rospy.init_node('ur5e_test')
r = rospy.Rate(1) # 1hz
jt = JointTrajectory()
jtp = JointTrajectoryPoint()
while not rospy.is_shutdown():
    jt.joint_names = ['shoulder_pan_joint','shoulder_lift_joint','elbow_joint',
                  'wrist_1_joint','wrist_2_joint','wrist_3_joint']

    jtp.positions = [1,-1.57,1,1,1,0]
    jtp.velocities = [1,1,1,1,1,1]
    jtp.accelerations = [1,1,1,1,1,1]
    jtp.time_from_start = rospy.Duration(2)
    #jtp.time_from_start.nsecs = 100000
    jt.points.append(jtp)

    pub.publish(jt)
    r.sleep()
