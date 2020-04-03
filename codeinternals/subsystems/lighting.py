from enum import Enum
from codeinternals.subsystems.subsystem_base import SubsystemBase
from codeinternals.subsystems.lightingcontrollers.one_color_controller import OneColorController
import time
from codeinternals.utils import color
from wpilib._wpilib import AddressableLED
from codeinternals.constants import lighting_constants
from wpilib._wpilib import Timer


class Lighting(SubsystemBase):
    class State(Enum):
        IDLE = 0
        SHOOTING = 1

    def start(self):
        self.instance = Lighting()
        self.ledBuffer = [AddressableLED.LEDData(0, 0, 0)] * lighting_constants.led_length
        self.mTimer = Timer()

    def update(self, commands, state):

        self.__wantedState = commands.getLightingWantedState()
        self.isNewState = self.state != self.__wantedState
        self.state = self.__wantedState

        if self.isNewState:
            if self.state == Lighting.State.IDLE:
                self.controller = OneColorController(color.off, lighting_constants.led_length)

            elif self.state == Lighting.State.SHOOTING:
                self.controller = OneColorController(color.green, lighting_constants.led_length, 5)

        if self.controller.is_finished():
            self.controller = None

        self.ledBuffer = self.controller.update()

    def getOutput(self):
        return self.ledBuffer

    def getInstance(self):
        return self.instance
