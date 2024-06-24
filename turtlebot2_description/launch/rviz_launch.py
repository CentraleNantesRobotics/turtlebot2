from simple_launch import SimpleLauncher

sl = SimpleLauncher()
sl.declare_arg('name', 'turtle1')


def launch_setup():

    rviz = sl.find('turtlebot2_description', 'model.rviz')
    rviz_adapted = '/tmp/turtlebot.rviz'

    with open(rviz) as f:
        config = f.read()
    config = config.replace('turtlebot/', f'{sl.arg("name")}/')
    with open(rviz_adapted, 'w') as f:
        f.write(config)

    sl.rviz(rviz_adapted)

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
