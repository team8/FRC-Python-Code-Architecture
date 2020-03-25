from codeinternals.subsystems.drivecontrollers.DriveControllerBase import DriveControllerBase


class MoveStraightController(DriveControllerBase):
    __targetDistance = 0
    def __init__(self, targetDistance):
        print("MoveController has started!")
        __targetDistance = targetDistance

    def update(self):
        print("Approaching Target")
        #Todo: Implement this with PD Loop

