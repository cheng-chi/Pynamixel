from Pynamixel.devices.fields import RW16
import crcmod

hardware = Pynamixel.hardwares.USB2AX("/dev/cu.usbmodem14101", 1000000)
ident = 0x05

header = [0xFF, 0xFF, 0xFD, 0x00] + [ident]
instr = [0x03]

addr = [0x1E, 0x00]  # write
parameters = [0x00, 0x02]

length = len(addr + parameters) + 3
length_data = [x for x in (length).to_bytes(2, byteorder='little')]

crc16 = crcmod.mkCrcFun(0x18005, rev=False, initCrc=0x0000)

# data = [0xFF, 0xFF, 0xFD, 0x00] + [0x01] + [0x03, 0x00] + [0x01]
data = header + length_data + instr + addr + parameters
b = (crc16(bytearray(data))).to_bytes(2, byteorder='little')
crc_data = [x for x in b]

final_data = data + crc_data

hardware.send(final_data)


import time
cycles = 10000
start = time.time()
for i in range(cycles):
    ident = 0x05

    header = [0xFF, 0xFF, 0xFD, 0x00] + [ident]
    instr = [0x03]

    addr = [0x1E, 0x00]  # write
    parameters = [0x00, 0x01]

    length = len(addr + parameters) + 3
    length_data = [x for x in (length).to_bytes(2, byteorder='little')]

    crc16 = crcmod.mkCrcFun(0x18005, rev=False, initCrc=0x0000)

    # data = [0xFF, 0xFF, 0xFD, 0x00] + [0x01] + [0x03, 0x00] + [0x01]
    data = header + length_data + instr + addr + parameters
    b = (crc16(bytearray(data))).to_bytes(2, byteorder='little')
    crc_data = [x for x in b]

    final_data = data + crc_data

    hardware.send(final_data)
    # servo.goal_position.write(0x100)


end = time.time()

print("{:.1f}Hz".format(cycles / (end-start)))