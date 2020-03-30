from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class MoveStraightController(DriveControllerBase):
    targetDistance = 0

    def __init__(self, targetDistance):
        print("MoveController has started!")
        self.output = DriveOutputs()
        self.targetDistance = targetDistance

    def update(self):
        print("Approaching Target")
        # drive_constants.moveStraightGains.calculate()
        return self.output

    def checkFinished(self) -> bool:
        return True
