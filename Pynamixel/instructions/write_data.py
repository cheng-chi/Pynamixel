# coding: utf8

# Original work Copyright (c) 2015 Vincent Jacques <vincent@vincent-jacques.net>
# Modified work Copyright 2019 Cheng Chi <chicheng@umich.edu>

import unittest


class WriteDataResponse(object):
    """
    @todoc
    """
    def __init__(self, parameters):
        assert len(parameters) == 0


class WriteData(object):
    """
    @todoc
    """
    code = 0x03
    response_class = WriteDataResponse

    def __init__(self, address, data, protocol=1):
        self.__protocol = protocol
        self.__address = address
        if isinstance(data, int):
            data = [data]
        self.__data = data

    @property
    def parameters(self):
        if self.__protocol == 1:
            return [self.__address] + self.__data
        elif self.__protocol == 2:
            return list(self.__address.to_bytes(2, byteorder='little')) + self.__data


class WriteDataTestCase(unittest.TestCase):
    def test_parameters_with_array_data(self):
        w = WriteData(0, [1, 2, 3])
        self.assertEqual(w.parameters, [0, 1, 2, 3])

    def test_parameters_with_int_data(self):
        w = WriteData(0, 1)
        self.assertEqual(w.parameters, [0, 1])
