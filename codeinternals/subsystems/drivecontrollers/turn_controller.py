from codeinternals.subsystems.drivecontrollers.drive_controller_base import DriveControllerBase
from codeinternals.utils.drive_outputs import DriveOutputs


class TurnController(DriveControllerBase):
    __targetAngle = 0

    def __init__(self, targetAngle): # TODO add some sort of python doc where it says - means left, + means right etc.
        print("MoveController has started!")
        self.output = DriveOutputs()
        self.__targetAngle = targetAngle

    def update(self):
        """numOfWheelRotationsToAngle = 2 * PI * driveWidth * Math.abs(self.targetAngle / (360 * targetPositionUnit(
        wheelRotations)) """
        print("Approaching Target")
        if self.__targetAngle < 0:
            """self.output.rightOutput.setTargetPosition(numOfWheelRotationsToAngle)"""
        else:
            """self.output.leftOutput.setTargetPosition(numOfWheelRotationsToAngle)"""

        return self.output

    def checkFinished(self) -> bool:
        return True