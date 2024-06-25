from simple_launch import SimpleLauncher


def generate_launch_description():
    sl = SimpleLauncher()
    sl.declare_arg('name', 'turtle1')

    with sl.group(ns = sl.arg('name')):
        sl.node('slider_publisher', arguments = sl.find('slider_publisher', 'Twist.yaml'))
    return sl.launch_description()
