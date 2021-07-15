from wpilib._wpilib import Solenoid

from ctre import TalonSRX

from constants import port_constants

talon = TalonSRX(port_constants.intake_id)
solenoid = Solenoid(port_constants.intake_solenoid_id)
