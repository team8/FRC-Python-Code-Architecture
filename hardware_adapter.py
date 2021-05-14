from wpilib._wpilib import AddressableLED
from wpilib._wpilib import Joystick

import ctre
from constants import port_constants
from ctre import PigeonIMU


class HardwareAdapter:
    class DriveHardware:
        def __init__(self):
            self.left_master_falcon = ctre.TalonFX(port_constants.left_master_falcon_id)
            self.left_slave_falcon = ctre.TalonFX(port_constants.left_slave_falcon_id)
            self.right_master_falcon = ctre.TalonFX(port_constants.right_master_falcon_id)
            self.right_slave_falcon = ctre.TalonFX(port_constants.right_slave_falcon_id)
            self.left_falcon_encoder = ctre.CANCoder(port_constants.left_falcon_encoder_id)
            self.right_falcon_encoder = ctre.CANCoder(port_constants.right_falcon_encoder_id)
            self.gyro = PigeonIMU(port_constants.gyro_id)

        def __getInstance__(self):
            return self

    class JoystickHardware:
        def __init__(self):
            self.driveJoystick = Joystick(port_constants.drive_joystick_id)
            self.turnJoystick = Joystick(port_constants.turn_joystick_id)

        def __getInstance__(self):
            return self

    class LightingHardware:
        def __init__(self):
            self.led_strip = AddressableLED(port_constants.led_id)

        def __getInstance__(self):
            return self
