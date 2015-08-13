# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest


def compute(data):
    return ~(sum(data)) & 0xFF


class ChecksumTestCase(unittest.TestCase):
    def test(self):
        # From http://support.robotis.com/en/product/dynamixel/communication/dxl_packet.htm
        self.assertEqual(compute([0x01, 0x05, 0x03, 0x0C, 0x64, 0xAA]), 0xDC)
