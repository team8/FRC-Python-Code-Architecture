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
        self.state = self.__wantedState
        print("Drive Subsystem Running...")
        if self.isNewState:
            if self.__wantedState == Drive.State.IDLE:
                self.controller = None
            if self.__wantedState == Drive.State.MOVE_STRAIGHT:
                self.controller = MoveStraightController()
            if self.__wantedState == Drive.State.TURN:
                self.controller = TurnController()
        if self.controller is None:
            self.outputs = None
        else:
            self.outputs = self.controller.update()

    def getOutput(self):
        return self.outputs
