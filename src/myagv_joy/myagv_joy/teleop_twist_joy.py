#! /usr/bin/env python3
# joyからcmd_velへの変換
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class TeleopTwistJoy(Node):
    def __init__(self):
        super().__init__('teleop_twist_joy_node')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Joy, 'joy', self.listener_callback, 10)
        self.vel = Twist()

    def listener_callback(self, Joy):
        self.vel.linear.x = 0.2*Joy.axes[1]   #0.32 0.2 0.4
        self.vel.angular.z = 0.4*Joy.axes[3]  #-1.5 1.0 
        self.publisher.publish(self.vel)
        self.get_logger().info("Velocity: Linear=%f" % (self.vel.linear.x))
        self.get_logger().info("Velocity: Angular=%f" % (self.vel.angular.z))

def main(args=None):
    rclpy.init(args=args)
    teleop_twist_joy = TeleopTwistJoy()
    rclpy.spin(teleop_twist_joy)
    rclpy.shutdown()

if __name__ == '__main__':
    main()