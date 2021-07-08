from hardware import drive_constants
from utils.drive_outputs import DriveOutputs


class MoveStraightController:
    __targetDistance = 0

    def __init__(self, target_distance):
        self.output = DriveOutputs()
        self.__targetDistance = target_distance

    def update(self):
        self.output.left_output.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        self.output.right_output.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        return self.output

    def checkFinished(self):
        return True
