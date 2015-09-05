==========
User guide
==========

@todoc This documentation assumes you're familiar with the Dynamixel concepts (@todoc add links to docs of protocol, instructions, devices, etc.)

@todoc List hardwares and their status (supported, externaly contributed, unimplemented) under Linux, Mac OS and Windows and Python2/3 if applicable.

@todoc Document troubleshooting: under Linux, add user to dialout group. Or even verify and raise a specific exception.

@todoc Logging (at bus level, at system level, etc.) to aid troubleshooting.

@todoc Talk about abstraction layers and control models:
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and move servos in sequence (AX12.move calls WriteData)
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and register moves in sequence (AX12.reg_move calls RegWrite) then broadcast an Action instruction
 - Stay at Bus level and use SyncWrite

@todoc

Introduction
============

Layers
======

Higher-level concepts and utilities
===================================

Using registered writes
=======================

Creating a new hardware
=======================
