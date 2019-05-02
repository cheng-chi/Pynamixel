# coding: utf8

# Original work Copyright (c) 2015 Vincent Jacques <vincent@vincent-jacques.net>
# Modified work Copyright 2019 Cheng Chi <chicheng@umich.edu>

import unittest


class ReadDataResponse(object):
    """
    @todoc
    """
    def __init__(self, parameters):
        self.data = parameters


class ReadData(object):
    """
    @todoc
    """
    code = 0x02
    response_class = ReadDataResponse

    def __init__(self, address, length=1, protocol=1):
        self.__protocol = protocol
        self.__address = address
        self.__length = length

    @property
    def parameters(self):
        if self.__protocol == 1:
            return [self.__address, self.__length]
        elif self.__protocol == 2:
            return list(self.__address.to_bytes(2, byteorder='little')) \
                   + list(self.__length.to_bytes(2, byteorder='little'))


class ReadDataTestCase(unittest.TestCase):
    def test_parameters_without_length(self):
        r = ReadData(42)
        self.assertEqual(r.parameters, [42, 1])

    def test_parameters_with_length(self):
        r = ReadData(42, 3)
        self.assertEqual(r.parameters, [42, 3])

    def test_response(self):
        r = ReadDataResponse([34, 56])
        self.assertEqual(r.data, [34, 56])
