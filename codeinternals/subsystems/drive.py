from enum import Enum

from codeinternals.subsystems.drivecontrollers.move_straight_controller import MoveStraightController
from codeinternals.subsystems.drivecontrollers.turn_controller import TurnController
from codeinternals.subsystems.subsystem_base import SubsystemBase


class Drive(SubsystemBase):

    class State(Enum):
        IDLE = 0
        MOVE_STRAIGHT = 1
        TURN = 2

    def update(self, commands, state):
        self.__wantedState = commands.getDriveWantedState()
        self.isNewState = self.state != self.__wantedState

        self.isControllerFinished = True if self.controller is None else (True if self.controller.checkFinished() else False)
        print("Drive Subsystem Running...")
        if self.isNewState and self.isControllerFinished:
            self.state = self.__wantedState
            if self.state == Drive.State.IDLE:
                self.controller = None
            elif self.state == Drive.State.MOVE_STRAIGHT:
                self.controller = MoveStraightController()
            elif self.state == Drive.State.TURN:
                self.controller = TurnController()
        if self.controller is None:
            self.outputs = None
        else:
            self.outputs = self.controller.update()

    def getOutput(self):
        return self.outputs
