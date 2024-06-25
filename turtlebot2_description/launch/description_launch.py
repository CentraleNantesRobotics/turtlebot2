from simple_launch import SimpleLauncher


def generate_launch_description():

    sl = SimpleLauncher(use_sim_time=False)
    name = sl.declare_arg('name', 'turtle1')
    gz = sl.declare_arg('gazebo', False)
    
    with sl.group(ns=name):
        
        sl.robot_state_publisher('turtlebot2_description','turtlebot2.urdf.xacro',
                                 xacro_args={'prefix': name+'/', 'gazebo': gz})

        sl.joint_state_publisher()

    sl.include('turtlebot2_description', 'rviz_launch.py')

    sl.node('tf2_ros', 'static_transform_publisher',
            arguments=['--frame-id','turtle1/odom','--child-frame-id','turtle1/base_footprint'])

    return sl.launch_description()
