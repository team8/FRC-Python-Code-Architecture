from hardware import shooter_hardware
from hardware import joysticks
from robot import robot_state
from wpilib._wpilib import Joystick

def update():
    if joysticks.drive_joystick.getRawButton(5):
        robot_state.shooter_hood_extended = True
    if joysticks.drive_joystick.getRawButton(6):
        robot_state.shooter_hood_extended = False
    if joysticks.drive_joystick.getRawButton(3):
        robot_state.shooter_blocker_extended = True
    if joysticks.drive_joystick.getRawButton(4):
        robot_state.shooter_blocker_extended = False
    if joysticks.turnJoystick.getRawButton(3):
        robot_state.shooter_flywheel_running = True
    else:
        robot_state.shooter_flywheel_running = False
