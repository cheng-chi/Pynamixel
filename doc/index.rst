=========
Pynamixel
=========

.. include:: ../README.rst

@todo This documentation assumes you're familiar with the Dynamixel concepts (@todo add links to docs of protocol, instructions, devices, etc.)

@todo List hardwares and their status (supported, externaly contributed, unimplemented) under Linux, Mac OS and Windows and Python2/3 if applicable.

@todo Document troubleshooting: under Linux, add user to dialout group. Or even verify and raise a specific exception.

@todo Logging (at bus level, at system level, etc.) to aid troubleshooting.

@todo Talk about abstraction layers and control models:
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and move servos in sequence (AX12.move calls WriteData)
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and register moves in sequence (AX12.reg_move calls RegWrite) then broadcast an Action instruction
 - Stay at Bus level and use SyncWrite

Contents
========

.. toctree::

    examples/spider
