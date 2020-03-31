from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class MoveStraightController(DriveControllerBase):
    __targetDistance = 0

    def __init__(self, targetDistance):
        self.output = DriveOutputs()
        self.__targetDistance = targetDistance

    def update(self):
        # drive_constants.moveStraightGains.calculate()
        return self.output

    def checkFinished(self) -> bool:
        return True
