from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class TurnController(DriveControllerBase):
    __targetAngle = 0

    def __init__(self, targetAngle): #TODO add some sort of python doc where it says - means left, + means right etc.
        print("MoveController has started!")
        self.output = DriveOutputs()
        self.__targetAngle = targetAngle

    def update(self):
        print("Approaching Target")
        # if self.__targetAngle < 0:
        #
        # else:
        #
        #
        # self.output.
        return self.output

    def checkFinished(self) -> bool:
        return True