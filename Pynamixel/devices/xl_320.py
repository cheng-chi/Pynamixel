# coding: utf8

# Original work Copyright (c) 2015 Vincent Jacques <vincent@vincent-jacques.net>
# Modified work Copyright 2019 Cheng Chi <chicheng@umich.edu>

from .fields import RW8, RW16, R8, R16


class XL320(object):
    """
    @todoc
    """
    def __init__(self, system, ident):
        """
        @todoc
        """
        # http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm
        # EEPROM area
        self.model_number = R16(system, ident, 0x00, protocol=2)
        "@todoc all attributes"
        self.firmware_version = R8(system, ident, 0x02, protocol=2)
        self.ident = RW8(system, ident, 0x03, protocol=2)
        self.baud_rate = RW8(system, ident, 0x04, protocol=2)
        self.return_delay_time = RW8(system, ident, 0x05, protocol=2)
        self.clockwise_angle_limit = RW16(system, ident, 0x06, protocol=2)
        self.counter_clockwise_angle_limit = RW16(system, ident, 0x08, protocol=2)
        self.highest_limit_temperature = RW8(system, ident, 0x0B, protocol=2)
        self.lowest_limit_volage = RW8(system, ident, 0x0C, protocol=2)
        self.highest_limit_volage = RW8(system, ident, 0x0D, protocol=2)
        self.max_torque = RW16(system, ident, 0x0E, protocol=2)
        self.status_return_level = RW8(system, ident, 0x10, protocol=2)
        self.alarm_led = RW8(system, ident, 0x11, protocol=2)
        self.alarm_shutdown = RW8(system, ident, 0x12, protocol=2)
        # RAM area
        self.torque_enable = RW8(system, ident, 0x18, protocol=2)
        self.led = RW8(system, ident, 0x19, protocol=2)

        self.d_gain = RW8(system, ident, 0x1A, protocol=2)
        self.i_gain = RW8(system, ident, 0x1B, protocol=2)
        self.p_gain = RW8(system, ident, 0x1C, protocol=2)

        self.goal_position = RW16(system, ident, 0x1E, protocol=2)
        self.moving_speed = RW16(system, ident, 0x20, protocol=2)
        self.torque_limit = RW16(system, ident, 0x23, protocol=2)
        self.present_position = R16(system, ident, 0x25, protocol=2)
        self.present_speed = R16(system, ident, 0x27, protocol=2)
        self.present_load = R16(system, ident, 0x29, protocol=2)
        self.present_voltage = R8(system, ident, 0x2D, protocol=2)
        self.present_temperature = R8(system, ident, 0x2E, protocol=2)
        self.registered = R8(system, ident, 0x2F, protocol=2)
        self.moving = R8(system, ident, 0x31, protocol=2)
        self.punch = RW16(system, ident, 0x33, protocol=2)
