from wpilib._wpilib import Joystick
from constants import port_constants

drive_joystick = Joystick(port_constants.drive_joystick_id)
turnJoystick = Joystick(port_constants.turn_joystick_id)