import Pynamixel
import time

hardware = Pynamixel.hardwares.USB2AX("/dev/cu.usbmodem14101", 1000000)
system = Pynamixel.System(Pynamixel.Bus(hardware))

usb2ax = system.add_device(Pynamixel.devices.USB2AX, 0xFD)

joints = []
joints.append(system.add_device(Pynamixel.devices.MX28, 0))
joints.append(system.add_device(Pynamixel.devices.MX28, 1))
joints.append(system.add_device(Pynamixel.devices.MX28, 2))
joints.append(system.add_device(Pynamixel.devices.AX12, 3))
joints.append(system.add_device(Pynamixel.devices.AX12, 4))
joints.append(system.add_device(Pynamixel.devices.XL320, 5))


results = [x.led.write(0x1) for x in joints]
results = [x.led.read() for x in joints]

results = [x.torque_enable.write(0x1) for x in joints]
results = [x.torque_enable.write(0x0) for x in joints]

results = [x.present_position.read() for x in joints]

angles = [1967, 2016, 2088, 506, 525, 500]
results = [joints[i].goal_position.write(angles[i]) for i in range(len(joints))]
results = [x.goal_position.read() for x in joints]


repeat = 1000
angles = [1967, 2016, 2088, 506, 525, 500]
start = time.time()
for i in range(repeat):
    results = [joints[i].goal_position.write(angles[i]) for i in range(len(joints))]
end = time.time()
print(repeat / (end - start))

hardware.flush()
