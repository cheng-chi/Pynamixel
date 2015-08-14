=========
Pynamixel
=========

.. include:: ../README.rst

@todo Talk about abstraction layers and control models:
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and move servos in sequence (AX12.move calls WriteData)
 - Use AX-12 abstraction, aggregate in Leg, Arm, etc. classes and register moves in sequence (AX12.reg_move calls RegWrite) then broadcast an Action instruction
 - Stay at Bus level and use SyncWrite
