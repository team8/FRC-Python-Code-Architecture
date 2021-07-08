from robot import robot_state
from hardware import drive_constants
from utils import math_util
from utils.drive_outputs import DriveOutputs


class JoystickDriveController:

    def __init__(self):
        self.output = DriveOutputs()

    def update(self):
        self.output.right_output.setPercentageOutput(
            math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput,
                            robot_state.drive_joystick_y - robot_state.turn_joystick_x))
        self.output.left_output.setPercentageOutput(
            math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput,
                            robot_state.drive_joystick_y + robot_state.turn_joystick_x))
        return self.output

    def checkFinished(self):
        return True  # finished at all times so it can be overwritten by other drive controllers
