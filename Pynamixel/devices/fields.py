# coding: utf8

# Original work Copyright (c) 2015 Vincent Jacques <vincent@vincent-jacques.net>
# Modified work Copyright 2019 Cheng Chi <chicheng@umich.edu>

from ..instructions import ReadData


class R8(object):
    def __init__(self, system, ident, address, protocol=1):
        self.__system = system
        self.__ident = ident
        self.__address = address
        self.__protocol = protocol

    def read(self):
        if self.__protocol == 1:
            ident, error, response = self.__system.bus.send(self.__ident, ReadData(self.__address, 1))
            return response.data[0]
        elif self.__protocol == 2:
            ident, error, response = self.__system.bus.send_v2(self.__ident, ReadData(self.__address, 1, protocol=2))
            return int.from_bytes(response.data, byteorder='little')


class RW8(object):
    def __init__(self, system, ident, address, protocol=1):
        self.__system = system
        self.__ident = ident
        self.__address = address
        self.__protocol = protocol

    def read(self):
        if self.__protocol == 1:
            ident, error, response = self.__system.bus.send(self.__ident, ReadData(self.__address, 1))
            return response.data[0]
        elif self.__protocol == 2:
            ident, error, response = self.__system.bus.send_v2(self.__ident, ReadData(self.__address, 1, protocol=2))
            return int.from_bytes(response.data, byteorder='little')

    def write(self, value):
        value_bytes = [value]
        if self.__protocol == 1:
            self.__system.bus.send(
                self.__ident,
                self.__system.instruction_for_writes(self.__address, value_bytes)
            )
        elif self.__protocol == 2:
            self.__system.bus.send_v2(
                self.__ident,
                self.__system.instruction_for_writes(self.__address, value_bytes, protocol=2)
            )


class R16(object):
    def __init__(self, system, ident, address, protocol=1):
        self.__system = system
        self.__ident = ident
        self.__address = address
        self.__protocol = protocol

    def read(self):
        if self.__protocol == 1:
            ident, error, response = self.__system.bus.send(self.__ident, ReadData(self.__address, 2))
            return response.data[0] + 0x100 * response.data[1]
        elif self.__protocol == 2:
            ident, error, response = self.__system.bus.send_v2(self.__ident, ReadData(self.__address, 2, protocol=2))
            return int.from_bytes(response.data, byteorder='little')


class RW16(object):
    def __init__(self, system, ident, address, protocol=1):
        self.__system = system
        self.__ident = ident
        self.__address = address
        self.__protocol = protocol

    def read(self):
        if self.__protocol == 1:
            ident, error, response = self.__system.bus.send(self.__ident, ReadData(self.__address, 2))
            return response.data[0] + 0x100 * response.data[1]
        elif self.__protocol == 2:
            ident, error, response = self.__system.bus.send_v2(self.__ident, ReadData(self.__address, 2, protocol=2))
            return int.from_bytes(response.data, byteorder='little')

    def write(self, value):
        value_bytes = [value % 0x100, value // 0x100]
        if self.__protocol == 1:
            self.__system.bus.send(
                self.__ident,
                self.__system.instruction_for_writes(self.__address, value_bytes)
            )
        elif self.__protocol == 2:
            self.__system.bus.send_v2(
                self.__ident,
                self.__system.instruction_for_writes(self.__address, value_bytes, protocol=2)
            )
