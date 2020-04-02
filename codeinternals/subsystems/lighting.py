from enum import Enum
from codeinternals.subsystems.subsystem_base import SubsystemBase
from codeinternals.subsystems.lightingcontrollers.one_color_controller import OneColorController
import time


class Lighting(SubsystemBase):
    class State(Enum):
        IDLE = 0
        SHOOTING = 1

    def update(self, commands, state):
        self.__wantedState = commands.getLightingWantedState()
        self.isNewState = self.state != self.__wantedState
        self.state = self.__wantedState

        if self.isNewState:
            if self.state == Lighting.State.IDLE:
                self.controller = None

            elif self.state == Lighting.State.SHOOTING:
                self.controller = OneColorController("green", 20, 5.0)

        if self.is_finished(self.controller):
            self.controller = OneColorController("off", 20)

    def is_finished(self, controller):
        if controller.duration != -1:
            return False
        if (time.time() - controller.start) >= controller.start():
            return True
        else:
            return False

    def getOutput(self):
        return self.controller
