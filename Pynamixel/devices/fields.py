# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

from ..instructions import ReadData, WriteData, RegWrite


class R8(object):
    def __init__(self, bus, ident, address):
        self.__bus = bus
        self.__ident = ident
        self.__address = address

    def read(self):
        ident, error, response = self.__bus.send(ident, ReadData(self.__address, 1))
        return response.data[0]


class RW8(object):
    def __init__(self, bus, ident, address):
        self.__bus = bus
        self.__ident = ident
        self.__address = address

    def read(self):
        ident, error, response = self.__bus.send(ident, ReadData(self.__address, 1))
        return response.data[0]

    def write(self, value):
        self.__bus.send(ident, WriteData(self.__address, [value]))


class R16(object):
    def __init__(self, bus, ident, address):
        self.__bus = bus
        self.__ident = ident
        self.__address = address

    def read(self):
        ident, error, response = self.__bus.send(ident, ReadData(self.__address, 2))
        return response.data[0] + 0x100 * response.data[1]


class RW16(object):
    def __init__(self, bus, ident, address):
        self.__bus = bus
        self.__ident = ident
        self.__address = address

    def read(self):
        ident, error, response = self.__bus.send(ident, ReadData(self.__address, 2))
        return response.data[0] + 0x100 * response.data[1]

    def write(self, value):
        self.__bus.send(ident, WriteData(self.__address, [value % 0x100, value // 0x100]))


class FieldsTestCase(unittest.TestCase):
    pass
