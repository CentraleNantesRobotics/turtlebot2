#!/usr/bin/env python3
#
# adapted to multi-robot + simple_launch, Olivier Kermorgant
import os
from simple_launch import SimpleLauncher


def generate_launch_description():
    
    sl = SimpleLauncher()
    
    # all happens in this namespace
    
    name = sl.declare_arg('name', os.uname().nodename)
    rsp = sl.declare_arg('rsp', True, description = 'If we should run a Robot State Publisher')
    
    sl.declare_arg('usb_port', default_value='/dev/ttyUSB0', description='Connected USB port')

    laser = sl.declare_arg('urg', default_value=True, description='If we should run the URG node')
    kinect = sl.declare_arg('kinect', default_value=False, description='If we should run the Kinect node')

    with sl.group(if_arg = 'rsp'):
        sl.include('turtlebot2_description', 'description_launch.py',
                   launch_arguments={'gz': False})


    with sl.group(ns=name):
        # run Kobuki interface
        params = {'acceleration_limiter': False,
                    'battery_capacity': 16.5,
                    'battery_low': 14.0,
                    'battery_dangerous': 13.2,
                    'device_port': sl.arg('usb_port',
                    'cmd_vel_timeout_sec': 0.6,
                    'odom_frame': name + '/odom',
                    'base_frame': name + '/base_footprint',
                    'publish_tf': True,
                    'use_imu_heading': True,
                    'wheel_left_joint_name': 'wheel_left_joint',
                    'wheel_right_joint_name': 'wheel_right_joint'}

        remappings=[
            ('commands/velocity', 'cmd_vel'),
            ('commands/led1', 'cmd/led1'),
            ('commands/led2', 'cmd/led2'),
            ('commands/digital_output', 'cmd/digital_output'),
            ('commands/external_power', 'cmd/external_power'),
            ('commands/sound', 'cmd/sound'),
            ('commands/reset_odometry', 'cmd/reset_odometry'),
            ('commands/motor_power', 'cmd/motor_power'),
            ('commands/controller_info', 'cmd/controller_info')]

        sl.node('kobuki_node','kobuki_ros_node',
                parameters = params,
                remappings = remappings)
        
        with sl.group(if_arg = 'urg'):
            1

        with sl.group(if_arg = 'kinect'):
            1

    return sl.launch_description()
