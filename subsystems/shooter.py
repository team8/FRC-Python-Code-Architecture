from hardware import shooter_hardware
from hardware import joysticks
from robot import robot_state

def update():
    if joysticks.drive_joystick.getRawButton(5):
        robot_state.shooter_hood_extended = True
    if joysticks.drive_joystick.getRawButton(6):
        robot_state.shooter_hood_extended = False