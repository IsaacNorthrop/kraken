#!/usr/bin/env python

"""
Depth sensor publisher node.
"""
import sys

sys.path.append("/home/auvic/kraken/src/kraken/kraken/include")

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

import ms5837

class DepthSensor(Node):

    def __init__(self):
    
        super().__init__('depth_sensor')
        
        self.logger = self.get_logger()
        self.publisher = self.create_publisher(Float32MultiArray, 'depth', 10)
        
        self.initialize_sensor()
        
        timer_period = 0.5 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def initialize_sensor(self):

        self.logger.info("initializing depth sensor node...")
        
        self.sensor = ms5837.MS5837_02BA()
        
        if not self.sensor.init():
            self.logger.error("sensor could not be initialized")
            exit(1)

        self.logger.info("...initialized depth sensor node")
     
    def poll_sensor(self):
        if not self.sensor.read():
            self.logger.error("cannot read sensor data")
            return None, None, None

        depth       = self.sensor.depth()
        pressure    = self.sensor.pressure(ms5837.UNITS_atm)
        temperature = self.sensor.temperature(ms5837.UNITS_Centigrade) 

        return depth, pressure, temperature
 
    def timer_callback(self):
        
        # Get data from the depth sensor
        depth, pressure, temperature = self.poll_sensor()

        if depth or pressure or temperature:
            self.logger.info("depth(m): %f, pressure(atm): %f, temperature(C): %f" % (depth, pressure, temperature))

            # Publish
            array = Float32MultiArray()
            array.data = [depth, pressure, temperature]
            self.publisher.publish(array)


def main(args=None):
    rclpy.init(args=args)

    publisher = DepthSensor()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

