# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>

from .fields import RW8, RW16, R8, R16


class USB2AX(object):
    """
    @todoc
    """
    fixed_ident = 0xFD  # USB2AX has a fixed id of 0XFD

    def __init__(self, system, ident):
        """
        @todoc
        """
        # http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm
        # EEPROM area
        ident = self.fixed_ident
        self.model_number = R16(system, ident, 0x00)
        "@todoc all attributes"
        self.firmware_version = R8(system, ident, 0x02)
        self.ident = RW8(system, ident, 0x03)
