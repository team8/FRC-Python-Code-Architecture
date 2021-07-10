from wpilib._wpilib import Solenoid

import ctre

from constants import port_constants

talon = ctre.TalonSRX(port_constants.intake_id)
solenoid = Solenoid(port_constants.intake_solenoid_id)
