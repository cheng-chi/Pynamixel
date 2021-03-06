Pynamixel is a Python (2.7+ and 3.4+) library to use Robotis Dynamixel servos.
It supports several hardwares (see below) and adding a new one is easy.
It provides different layers allowing very precise control as well as a greater abstraction.

It's licensed under the `MIT license <http://choosealicense.com/licenses/mit/>`_.
It's available on the `Python package index <http://pypi.python.org/pypi/Pynamixel>`_,
its `documentation <https://jacquev6.github.io/Pynamixel/>`_
and `its source code <https://github.com/jacquev6/Pynamixel/>`_ are on GitHub.

Questions? Remarks? Bugs? Want to contribute? `Open an issue <https://github.com/jacquev6/Pynamixel/issues/>`_!

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

Quick start
===========

Install from PyPI::

    $ pip install Pynamixel

Import:

>>> import Pynamixel

.. The hardware is created in conf.py, doctest_global_setup. The next line is just for display and not for doctests.

Create a hardware::

    >>> hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)

Create a system and a device:

>>> system = Pynamixel.System(Pynamixel.Bus(hardware))
>>> servo = system.add_device(Pynamixel.devices.AX12, 1)

Set the servo's goal position:

>>> servo.goal_position.write(0x200)

And see that it's moving:

>>> servo.moving.read()
1
