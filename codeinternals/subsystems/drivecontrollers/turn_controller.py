from codeinternals import robot_state
from codeinternals.constants import drive_constants
from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils import math_util
from codeinternals.utils.drive_outputs import DriveOutputs


class TurnYawController(DriveControllerBase):
    __targetAngle = 0
    __acceptableYawError = 5

    def __init__(self, targetAngle):  # TODO add some sort of python doc where it says - means left, + means right etc.
        self.output = DriveOutputs()
        self.__targetAngle = targetAngle
        drive_constants.turnGains.setTolerance(self.__acceptableYawError)

    def update(self):
        abs_angular_output = math_util.clamp(-0.4, 0.4, drive_constants.turnGains.calculate(
            self.__targetAngle - robot_state.gyroCompassHeadingDegrees))
        self.output.rightOutput.setPercentageOutput(abs_angular_output)
        self.output.leftOutput.setPercentageOutput(-abs_angular_output)
        return self.output

    def checkFinished(self) -> bool:
        return drive_constants.turnGains.atSetpoint()
