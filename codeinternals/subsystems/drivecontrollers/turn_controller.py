from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class TurnController(DriveControllerBase):
    __targetAngle = 0

    def __init__(self, targetAngle):
        print("MoveController has started!")
        self.output = DriveOutputs()
        self.__targetAngle = targetAngle

    def update(self):
        print("Approaching Target")
        # Todo: Implement this with talon pid functions
        return self.output
