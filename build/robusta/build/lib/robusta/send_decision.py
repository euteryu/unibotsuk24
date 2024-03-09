#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class DecisionSender(Node):

    def __init__(self):
        super().__init__('send_decision')
        try:
            # Open the serial port
            self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with the actual serial port
            # Wait for 3s after serial port opens
            time.sleep(3)
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to open serial port: {e}")
            raise e

        # Subscribe to the topic
        self.subscription = self.create_subscription(
            String,
            '/decision',
            self.callback,
            10)
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        try:
            # Send the data via serial
            self.ser.write(msg.data.encode())
            self.get_logger().info(f"Data sent: {msg.data}")
        except serial.SerialException as e:
            self.get_logger().error(f"Serial communication error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DecisionSender()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # Close the serial port when the node is shut down
    if hasattr(node, 'ser'):
        node.ser.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()