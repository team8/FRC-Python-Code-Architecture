from constants import drive_constants
from subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from utils.drive_outputs import DriveOutputs


class MoveStraightController(DriveControllerBase):
    __targetDistance = 0

    def __init__(self, targetDistance):
        self.output = DriveOutputs()
        self.__targetDistance = targetDistance

    def update(self):
        self.output.left_output.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        self.output.right_output.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        return self.output

    def checkFinished(self) -> bool:
        return True
