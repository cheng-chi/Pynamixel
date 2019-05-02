Pynamixel is a Python (2.7+ and 3.4+) library to use Robotis Dynamixel servos.
It supports several hardwares (see below) and adding a new one is easy.
It provides different layers allowing very precise control as well as a greater abstraction.

It's licensed under the `MIT license <http://choosealicense.com/licenses/mit/>`_.
Its `documentation <https://jacquev6.github.io/Pynamixel/>`_
and `its source code <https://gitlab.eecs.umich.edu/eecs467-cinebot/Pynamixel>`_ are on GitLab.

This project is forked from `Pynamixel <https://github.com/jacquev6/Pynamixel/>`_ library by Vincent Jacques.

Questions? Remarks? Bugs? Want to contribute? `Open an issue <https://gitlab.eecs.umich.edu/eecs467-cinebot/Pynamixel/issues/>`_!

.. image:: https://img.shields.io/travis/jacquev6/Pynamixel/master.svg
    :target: https://travis-ci.org/jacquev6/Pynamixel

.. image:: https://img.shields.io/coveralls/jacquev6/Pynamixel/master.svg
    :target: https://coveralls.io/r/jacquev6/Pynamixel

.. image:: https://img.shields.io/codeclimate/github/jacquev6/Pynamixel.svg
    :target: https://codeclimate.com/github/jacquev6/Pynamixel

.. image:: https://img.shields.io/scrutinizer/g/jacquev6/Pynamixel.svg
    :target: https://scrutinizer-ci.com/g/jacquev6/Pynamixel

.. image:: https://img.shields.io/pypi/dm/Pynamixel.svg
    :target: https://pypi.python.org/pypi/Pynamixel

.. image:: https://img.shields.io/pypi/l/Pynamixel.svg
    :target: https://pypi.python.org/pypi/Pynamixel

.. image:: https://img.shields.io/pypi/v/Pynamixel.svg
    :target: https://pypi.python.org/pypi/Pynamixel

.. image:: https://img.shields.io/pypi/pyversions/Pynamixel.svg
    :target: https://pypi.python.org/pypi/Pynamixel

.. image:: https://img.shields.io/pypi/status/Pynamixel.svg
    :target: https://pypi.python.org/pypi/Pynamixel

.. image:: https://img.shields.io/github/issues/jacquev6/Pynamixel.svg
    :target: https://github.com/jacquev6/Pynamixel/issues

.. image:: https://badge.waffle.io/jacquev6/Pynamixel.png?label=ready&title=ready
    :target: https://waffle.io/jacquev6/Pynamixel

.. image:: https://img.shields.io/github/forks/jacquev6/Pynamixel.svg
    :target: https://github.com/jacquev6/Pynamixel/network

.. image:: https://img.shields.io/github/stars/jacquev6/Pynamixel.svg
    :target: https://github.com/jacquev6/Pynamixel/stargazers

Supported hardwares
===================

"Full support" means on Windows, Linux and Mac OS X, with both Python 2.7+ and 3.4+.

- USB2AX: full support
- USB2Dynamixel: not yet
- U2D2: not yet

Note: `Firmware v5 <http://www.xevelabs.com/doku.php?id=product:usb2ax:firmware_update#getting_the_firmware>`_ for USB2AX fixed some critical bugs related to protocol v2.0.
Please consider updating if you are having return packet corruption problem.

Supported servos
===================

"Full support" means on Windows, Linux and Mac OS X, with both Python 2.7+ and 3.4+.

- AX12: full support (protocol v1)
- AXS1: full support (protocol v1)
- MX28: full support (protocol v1)
- XL320: partial support (protocol v2) Read, Write instructions only

Quick start
===========

Install from source::

    $ git clone git@gitlab.eecs.umich.edu:eecs467-cinebot/Pynamixel.git
    $ cd Pynamixel
    $ pip install -e .

Import:

>>> import Pynamixel

.. The hardware is created in conf.py, doctest_global_setup. The next line is just for display and not for doctests.

Create a hardware::

    >>> hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)  # for Linux
    >>> hardware = Pynamixel.hardwares.USB2AX("/dev/cu.usbmodem14101", 1000000)  # for MacOS

Create a system and a device:

>>> system = Pynamixel.System(Pynamixel.Bus(hardware))
>>> servo = system.add_device(Pynamixel.devices.AX12, 1)

Set the servo's goal position:

>>> servo.goal_position.write(0x200)

And see that it's moving:

>>> servo.moving.read()
1
