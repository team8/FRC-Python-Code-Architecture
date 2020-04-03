from enum import Enum
from codeinternals.subsystems.subsystem_base import SubsystemBase
from codeinternals.subsystems.lightingcontrollers.one_color_controller import OneColorController
from codeinternals.constants import lighting_constants
import time
from codeinternals.utils import color


class Lighting(SubsystemBase):
    class State(Enum):
        IDLE = 0
        SHOOTING = 1

    class AddressableLedBuffer:
        mBuffer = [(0, 0, 0) for i in range(lighting_constants.led_length)]

    def update(self, commands, state):

        self.__wantedState = commands.getLightingWantedState()
        self.isNewState = self.state != self.__wantedState
        self.state = self.__wantedState

        if self.isNewState:
            if self.state == Lighting.State.IDLE:
                self.led_buffer = None

            elif self.state == Lighting.State.SHOOTING:
                self.controller = OneColorController(color.green, lighting_constants.led_length, 5)

        if self.is_finished(self.controller):
            self.controller = None

        self.led_buffer = self.controller.update()

    def is_finished(self, controller):
        if controller.duration != -1:
            return False
        if (time.time() - controller.start) >= controller.start():
            return True
        else:
            return False

    def getOutput(self):
        return self.led_buffer
