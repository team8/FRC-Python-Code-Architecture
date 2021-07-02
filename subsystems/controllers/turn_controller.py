from constants import drive_constants
from utils import math_util
from utils.drive_outputs import DriveOutputs
from robot import robot_state


class TurnYawController:
    __targetAngle = 0
    __acceptableYawError = 5

    def __init__(self, target_angle):  # TODO add some sort of python doc where it says - means left, + means right etc.
        self.output = DriveOutputs()
        self.__targetAngle = target_angle

    def update(self):
        abs_angular_output = math_util.clamp(-0.4, 0.4, drive_constants.turnGains.calculate(
            self.__targetAngle - robot_state.gyro_compass_heading_degrees))
        self.output.right_output.setPercentageOutput(abs_angular_output)
        self.output.left_output.setPercentageOutput(-abs_angular_output)
        return self.output

    def checkFinished(self) -> bool:
        return abs(self.__targetAngle - robot_state.gyro_compass_heading_degrees) <= self.__acceptableYawError
