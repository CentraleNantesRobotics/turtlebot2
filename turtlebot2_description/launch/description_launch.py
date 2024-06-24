from simple_launch import SimpleLauncher


def generate_launch_description():

    sl = SimpleLauncher(use_sim_time=True)
    name = sl.declare_arg('name', 'turtle1')
    gz = sl.declare_arg('gazebo', False)
    
    with sl.group(ns=name):
        
        sl.robot_state_publisher('turtlebot2_description','turtlebot2.urdf.xacro',
                                 xacro_args={'prefix': name+'/', 'gazebo': gz})

    return sl.launch_description()
