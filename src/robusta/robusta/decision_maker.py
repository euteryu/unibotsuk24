#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DecisionMaker(Node):

    def __init__(self):
        super().__init__('decision_maker')
        # Create a publisher for the topic
        self.publisher_ = self.create_publisher(String, '/decision', 1)
        # Set the publishing rate (in Hz)
        self.timer = self.create_timer(0.1, self.publish_message)  # 10 Hz publishing rate

    def publish_message(self):
        # Create a string message
        msg = String()
        msg.data = '0'
        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = DecisionMaker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
