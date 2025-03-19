#!/usr/bin/env python

"""
Depth sensor publisher node.
"""
import sys
import argparse as ap

sys.path.append("/home/isaacn/code/kraken/ROS/src/kraken/kraken/include")

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

# import motor_controller_stuff maybe?

class MotorController(Node):

    def __init__(self):
    
        super().__init__('depth_sensor')
        parser = ap.ArgumentParser()
        parser.add_argument("-l", "--log", metavar="FILE", help="log data to a file", type=str)
        parser.add_argument("-v", "--verbose", help="display collected data", action="store_true")
        self.args = parser.parse_args()
        if self.args.log:
            self.log_file = open(self.args.log, "w")
            self.log_file.write("depth,pressure,temperature\n")
        
        
        self.logger = self.get_logger()
        self.publisher = self.create_publisher(Float32MultiArray, 'depth', 10)
        
        self.initialize_sensor()
        
        timer_period = 0.5 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        


def main(args=None):
    rclpy.init(args=args)

    publisher = MotorController()

    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

