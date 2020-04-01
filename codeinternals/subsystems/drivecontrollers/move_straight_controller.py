from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs
from codeinternals.constants import drive_constants

class MoveStraightController(DriveControllerBase):
    __targetDistance = 0

    def __init__(self, targetDistance):
        self.output = DriveOutputs()
        self.__targetDistance = targetDistance

    def update(self):
        self.output.leftOutput.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        self.output.rightOutput.setMotionMagicTargetPosition(self.__targetDistance, drive_constants.moveStraightGains)
        return self.output

    def checkFinished(self) -> bool:
        return True
