Perception with UBR-1
=====================

UBR-1 comes with higher level robot functions which can be used as building
blocks when creating your robot application. One of the key building blocks of
robot applications is perception. UBR-1 comes with a complete sensor suite for
perceiving the world around it, as well as software tools to carry out basic
perception tasks.

Using Camera Data
-----------------

This section provides an overview of how to access the head camera data and
some of the popular ROS vision tools available on UBR-1.

The head camera in the UBR-1 is capable of producing both 2d and 3d images.
These are available over ROS topics, of both ``sensor_msgs/Image`` and
``sensor_msgs/PointCloud2``. The first thing you might notice when looking
at the available ROS topics, is that there are a lot of them that start with
``head_camera``. The drivers for the head camera allow access to a number of
different image and point cloud formats, in color and monochrome, at a selection
of frequencies, and at a number of different resolutions.

TODO: describe available topics in detail.

TODO: describe topics available

TODO: cv_bridge with python/C++

TODO: overview of opencv features

TODO: overview of PCL features

Basic Grasping Perception
-------------------------

The ``basic_grasping_perception`` package allows the robot to segment the world
into objects and support surfaces, and then plan grasps to those objects.
``basic_grasping_perception`` is used in the 
:ref:`pick and place demo <pick_and_place>`.
