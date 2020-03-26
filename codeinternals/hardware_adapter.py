from wpilib._wpilib import Joystick

from codeinternals import ctre


class HardwareAdapter:
    class DriveHardware:
        def __init__(self):
            self.left_master_falcon = ctre.TalonFX(0)
            self.left_slave_falcon = ctre.TalonFX(2)
            self.right_master_falcon = ctre.TalonFX(3)
            self.right_slave_falcon = ctre.TalonFX(4)

        def __getInstance__(self):
            return self

    class JoystickHardware:
        def __init__(self):
            self.driveJoystick = Joystick(0)
            self.turnJoystick = Joystick(1)

        def __getInstance__(self):
            return self
