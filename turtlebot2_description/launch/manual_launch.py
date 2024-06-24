from simple_launch import SimpleLauncher

sl = SimpleLauncher()
sl.declare_arg('name', 'waffle1')


def generate_launch_description():

    with sl.group(ns = sl.arg('name')):
        sl.node('slider_publisher', arguments = sl.find('slider_publisher', 'Twist.yaml'))
    return sl.launch_description()
