#!/usr/bin/env python3
import numpy as np
import rospy

from duckietown.dtros import DTROS, NodeType, TopicType
from duckietown_msgs.msg import WheelEncoderStamped, Twist2DStamped
from geometry_msgs.msg import PoseStamped

from std_msgs.msg import Bool


class WheelsCalibrationNode(DTROS):
    """
        Computes an estimate of the Duckiebot pose using the wheel encoders.
        Args:
            node_name (:obj:`str`): a unique, descriptive name for the ROS node
        Configuration:

        Publisher:
            ~encoder_localization (:obj:`PoseStamped`): The computed position
        Subscribers:
            ~/left_wheel_encoder_node/tick (:obj:`WheelEncoderStamped`):
                encoder ticks
            ~/right_wheel_encoder_node/tick (:obj:`WheelEncoderStamped`):
                encoder ticks
    """

    def __init__(self, node_name):

        # Initialize the DTROS parent class
        super(WheelsCalibrationNode, self).__init__(
            node_name=node_name,
            node_type=NodeType.LOCALIZATION
        )
        # get the name of the robot
        self.veh = rospy.get_namespace().strip("/")

        # Add the node parameters to the parameters dictionary
        self.delta_phi_left = 0
        self.left_tick_prev = 0

        self.delta_phi_right = 0
        self.right_tick_prev = 0

        self.ticks_left = 0
        self.ticks_right = 0

        # nominal R and L:
        self.R = rospy.get_param(f'/{self.veh}/kinematics_node/radius', 100)
        self.L = rospy.get_param(f'/{self.veh}/kinematics_node/baseline', 100)

        # Wheel encoders subscribers:
        keypress_topic = f'/{self.veh}/EnterPressed'
        _ = rospy.Subscriber(
            keypress_topic,
            Bool,
            self.cbEnterPressed,
            queue_size=1
        )

        left_encoder_topic = f'/{self.veh}/left_wheel_encoder_node/tick'
        self.enco_left = rospy.Subscriber(
            left_encoder_topic,
            WheelEncoderStamped,
            self.cbLeftEncoder,
            queue_size=1
        )

        right_encoder_topic = f'/{self.veh}/right_wheel_encoder_node/tick'
        self.enco_right = rospy.Subscriber(
            right_encoder_topic,
            WheelEncoderStamped,
            self.cbRightEncoder,
            queue_size=1
        )

        # Param names
        self.START_MOVING = False
        self.TRIM_PARAM = f'/{self.veh}/kinematics_node/trim'

        self.log("Initialized!")

    def cbEnterPressed(self, msg):
        if msg.data == True:
            if not self.START_MOVING:
                self.ticks_left = self.left_tick_prev = 0
                self.ticks_right = self.right_tick_prev = 0
                self.START_MOVING = True
            else:
                if self.ticks_right > self.ticks_left:
                    trim = -self.ticks_left/self.ticks_right
                else:
                    trim = self.ticks_right/self.ticks_left
                print(f"Suggested trim = {trim}")
                rospy.set_param(self.TRIM_PARAM, trim)
                self.START_MOVING = False

    def cbLeftEncoder(self, msg_encoder):
        """
            Wheel encoder callback, the rotation of the wheel.
            Args:
                msg_encoder (:obj:`WheelEncoderStamped`) encoder ROS message.
        """
        ticks = msg_encoder.data
        if not self.START_MOVING:
            self.left_tick_prev = ticks

        delta_ticks = ticks-self.left_tick_prev
        self.left_tick_prev = ticks

        self.ticks_left += delta_ticks
        print(f"LEFT ticks : {self.ticks_left}")

    def cbRightEncoder(self, msg_encoder):
        """
            Wheel encoder callback, the rotation of the wheel.
            Args:
                msg_encoder (:obj:`WheelEncoderStamped`) encoder ROS message.
        """
        ticks = msg_encoder.data
        if not self.START_MOVING:
            self.right_tick_prev = ticks

        delta_ticks = ticks-self.right_tick_prev
        self.right_tick_prev = ticks

        self.ticks_right += delta_ticks
        print(f"RIGHT ticks : {self.ticks_right}")

    def onShutdown(self):
        print("Shutting down, bye, bye!")


if __name__ == "__main__":
    # Initialize the node
    wheels_calibration_node = WheelsCalibrationNode(
        node_name='wheels_calibration_node')
    # Keep it spinning
    rospy.spin()
    rospy.on_shutdown(wheels_calibration_node.onShutdown)
