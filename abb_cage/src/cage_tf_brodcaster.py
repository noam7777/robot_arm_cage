#! /usr/bin/env python
import rospy
import time
import tf
import math



if __name__ == '__main__':

    rospy.init_node('cage_tf_brodcaster')
    br = tf.TransformBroadcaster()
    listener = tf.TransformListener()
    rate = rospy.Rate(5.0)



    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 1.0),
                        rospy.Time.now(),
                        "/cage",
                        "/world")
        br.sendTransform((0.0, 0.0, 0.75),
                        (0.0, 0.0, 0.0, 1.0),
                        rospy.Time.now(),
                        "/cage_platform_center",
                        "/cage")
        
        rate.sleep()

