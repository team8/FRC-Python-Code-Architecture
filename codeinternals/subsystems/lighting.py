from enum import Enum
from codeinternals.subsystems.subsystem_base import SubsystemBase
from codeinternals.subsystems.lightingcontrollers.one_color_controller import OneColorController
import time
from codeinternals.utils import color
from wpilib._wpilib import AddressableLED
from codeinternals.constants import lighting_constants


class Lighting(SubsystemBase):
    class State(Enum):
        IDLE = 0
        SHOOTING = 1

    def start(self):
        self.instance = Lighting()
        self.ledBuffer = [AddressableLED.LEDData(0, 0, 0)] * lighting_constants.led_length

    def update(self, commands, state):

        self.__wantedState = commands.getLightingWantedState()
        self.isNewState = self.state != self.__wantedState
        self.state = self.__wantedState

        if self.isNewState:
            if self.state == Lighting.State.IDLE:
                self.controller = OneColorController(color.off, lighting_constants.led_length)

            elif self.state == Lighting.State.SHOOTING:
                self.controller = OneColorController(color.green, lighting_constants.led_length, 5)

        if self.__is_finished(self.controller):
            self.controller = None

        self.ledBuffer = self.controller.update()

    def __is_finished(self, controller):
        if controller.duration != -1:
            return False
        if (time.time() - controller.start) >= controller.start():
            return True
        else:
            return False

    def getOutput(self):
        return self.ledBuffer

    def getInstance(self):
        return self.instance
