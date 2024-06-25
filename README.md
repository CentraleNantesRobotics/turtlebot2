# Turtlebot2 in ROS 2

This packages offers the full Turtlebot2 stack for ROS 2 with xacro models.

Use the `prefix` argument to rename all links e.g. `prefix:=turtle1/` leads to `turtle1/base_link`.

It is used to rename all links within the model, together with a namespaced execution, allowing an easy multi-robot setup.

It is compatible with spawning the models in Gazebo.

## Bringup

Assuming you have `simple_launch` and `nav2_common`, running the included `bringup_launch.py` will run ROS 2 on the Turtlebot and prefix or namespace nodes, topics and TF links with the `HOSTNAME` of the Turtlebot.

Running `bringup.sh` will launch this file in a detached screen.

Bringup can be run at boot with the package `robot-upstart`.


## Upload in Gazebo (Ignition)

The `upload_launch.py` will spawn a Turtlebot inside Gazebo.
