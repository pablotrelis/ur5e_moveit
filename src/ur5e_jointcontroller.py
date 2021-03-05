#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
import math


rospy.init_node('ur5e_jointcontroller')
jt_pub_ur5e = rospy.Publisher('/scaled_pos_traj_controller/command', JointTrajectory, queue_size=10)
def move_ur5e_joint_trajectory():
        jtpt = JointTrajectoryPoint()
        jt_ur5e = JointTrajectory()
    #while not rospy.is_shutdown():

        jt_ur5e.joint_names = ['shoulder_pan_joint','shoulder_lift_joint','elbow_joint',
                      'wrist_1_joint','wrist_2_joint','wrist_3_joint']

        jtpt.positions = [1.57,0,0,0,0,0]
        jtpt.velocities = [1,1,1,1,1,1]
        jtpt.accelerations = [1,1,1,1,1,1]
        jtpt.time_from_start = 2

        jt_ur5e.points.append(jtpt)
        jt_pub_ur5e.publish(jt_ur5e)

        #rospy.loginfo(jtpt)
        rospy.loginfo(jt_ur5e)
        rospy.sleep(1)
'''
jt_pub_ur5 = rospy.Publisher('/ur5/arm_controller/command', JointTrajectory)
def move_ur5_joint_trajectory(xopt, duration=0.1):

    global jt_pub_ur5
    jt_ur5 = JointTrajectory()
    jt_ur5.joint_names = ['shoulder_pan_joint','shoulder_lift_joint','elbow_joint',
                      'wrist_1_joint','wrist_2_joint','wrist_3_joint']

    jtpt = JointTrajectoryPoint()
    jtpt.positions = [xopt[0], xopt[1], xopt[2], xopt[3], xopt[4], xopt[5]]
    jtpt.time_from_start = rospy.Duration.from_sec(duration)

    jt_ur5.points.append(jtpt)
    jt_pub_ur5.publish(jt_ur5)
'''


if __name__ == '__main__':
    try:
        move_ur5e_joint_trajectory()
    except rospy.ROSInterruptException:
        pass
