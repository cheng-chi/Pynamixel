# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

import serial  # https://pypi.python.org/pypi/pyserial

# http://www.xevelabs.com/doku.php?id=product:usb2ax:usb2ax
# https://github.com/Xevel/usb2ax


class USB2AX(object):
    def __init__(self, port, baudrate):
        self.__port = serial.Serial(port=port, baudrate=baudrate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

    def send(self, data):
        self.__port.write("".join(chr(d) for d in data))

    def receive(self, count):
        return [ord(c) for c in self.__port.read(count)]


class USB2AXTestCase(unittest.TestCase):
    pass
