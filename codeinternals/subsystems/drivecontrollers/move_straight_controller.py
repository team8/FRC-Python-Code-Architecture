from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class MoveStraightController(DriveControllerBase):
    __targetDistance = 0

    def __init__(self, targetDistance):
        print("MoveController has started!")
        self.output = DriveOutputs()
        self.__targetDistance = targetDistance

    def update(self):
        print("Approaching Target")
        # Todo: Implement this with PD Loop
        return self.output
