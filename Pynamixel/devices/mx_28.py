# coding: utf8

from .fields import RW8, RW16, R8, R16


class MX28(object):
    """
    @todoc
    """
    def __init__(self, system, ident):
        """
        @todoc
        """
        # http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm
        # EEPROM area
        self.model_number = R16(system, ident, 0x00)
        "@todoc all attributes"
        self.firmware_version = R8(system, ident, 0x02)
        self.ident = RW8(system, ident, 0x03)
        self.baud_rate = RW8(system, ident, 0x04)
        self.return_delay_time = RW8(system, ident, 0x05)
        self.clockwise_angle_limit = RW16(system, ident, 0x06)
        self.counter_clockwise_angle_limit = RW16(system, ident, 0x08)
        self.highest_limit_temperature = RW8(system, ident, 0x0B)
        self.lowest_limit_volage = RW8(system, ident, 0x0C)
        self.highest_limit_volage = RW8(system, ident, 0x0D)
        self.max_torque = RW16(system, ident, 0x0E)
        self.status_return_level = RW8(system, ident, 0x10)
        self.alarm_led = RW8(system, ident, 0x11)
        self.alarm_shutdown = RW8(system, ident, 0x12)
        # RAM area
        self.torque_enable = RW8(system, ident, 0x18)
        self.led = RW8(system, ident, 0x19)

        self.d_gain = RW8(system, ident, 0x1A)
        self.i_gain = RW8(system, ident, 0x1B)
        self.p_gain = RW8(system, ident, 0x1C)

        self.goal_position = RW16(system, ident, 0x1E)
        self.moving_speed = RW16(system, ident, 0x20)
        self.torque_limit = RW16(system, ident, 0x22)
        self.present_position = R16(system, ident, 0x24)
        self.present_speed = R16(system, ident, 0x26)
        self.present_load = R16(system, ident, 0x28)
        self.present_voltage = R8(system, ident, 0x2A)
        self.present_temperature = R8(system, ident, 0x2B)
        self.registered = R8(system, ident, 0x2C)
        self.moving = R8(system, ident, 0x2E)
        self.lock = RW8(system, ident, 0x2F)
        self.punch = RW16(system, ident, 0x30)
