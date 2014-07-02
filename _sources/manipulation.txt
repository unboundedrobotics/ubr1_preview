Manipulation with UBR-1
=======================

UBR-1 comes with higher level robot functions which can be used as building
blocks when creating your robot application. One of these building blocks is
MoveIt! which allows high level control of the arm.

Internally MoveIt comprises many modules offering everything from kinematics
and planning to plan execution and some perception.

Starting MoveIt! on the UBR-1
-----------------------------

.. code-block:: c

  ubr@brain:~$ roslaunch ubr1_moveit move_group.launch

Using the MoveIt! RVIZ Plugin
-----------------------------

TODO: show how to use the plugin to move the arm around

video?

Sending Commands in Python
--------------------------
TODO: moveit_python example?

Sending Commands in C++
-----------------------


.. _pick_and_place:

Running the Pick and Place Demo
-------------------------------

TODO: show how to run the demo

::

    roslaunch ubr1_grasping grasping.launch
    rosrun ubr1_grasping pick_and_place.py --once
