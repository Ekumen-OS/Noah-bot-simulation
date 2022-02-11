#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose, PoseArray

class WayposesPublisher():
    WAYPOSES_TOPIC = "/move_base_sequence/wayposes"
    WAYPOSES_FRAME = "map"

    def __init__(self):
        try:
            self.publisher = rospy.Publisher(self.WAYPOSES_TOPIC, PoseArray, queue_size=10, latch=True)
            self.get_pose_array()
        except Exception as e:
            rospy.logerr("Error: %s", e)

    def get_pose_array(self):
        self.pose_array = PoseArray()
        self.pose_array.header.frame_id = self.WAYPOSES_FRAME
        self.pose_array.header.stamp = rospy.Time.now()
        self.process_poses()

    def process_poses(self):
        try:
            poses_dict = rospy.get_param("/goal_poses")
            for pose in poses_dict:
                aux_pose = Pose()
                aux_pose.position.x = pose["position"]["x"]
                aux_pose.position.y = pose["position"]["y"]
                aux_pose.position.z = pose["position"]["z"]
                aux_pose.orientation.x = pose["orientation"]["x"]
                aux_pose.orientation.y = pose["orientation"]["y"]
                aux_pose.orientation.z = pose["orientation"]["z"]
                aux_pose.orientation.w = pose["orientation"]["w"]
                self.pose_array.poses.append(aux_pose)
        except KeyError:
            rospy.logerr("Poses not specified, terminating wayposes publisher")

    def publish_wayposes(self):
        self.publisher.publish(self.pose_array)

if __name__ == "__main__":
    rospy.init_node("wayposes_publisher", log_level=rospy.INFO)
    wayposes_publisher = WayposesPublisher()
    rospy.sleep(5)
    wayposes_publisher.publish_wayposes()
    rospy.spin()
