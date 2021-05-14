import robot_state
from constants import drive_constants
from utils import math_util
from utils.drive_outputs import DriveOutputs


class JoystickDriveController:

    def __init__(self):
        self.output = DriveOutputs()

    def update(self):
        self.output.rightOutput.setPercentageOutput(
            math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput,
                            robot_state.driveJoystickY - robot_state.turnJoystickX))
        self.output.leftOutput.setPercentageOutput(
            math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput,
                            robot_state.driveJoystickY + robot_state.turnJoystickX))
        return self.output

    def checkFinished(self) -> bool:
        return True  # finished at all times so it can be overwritten by other drive controllers
