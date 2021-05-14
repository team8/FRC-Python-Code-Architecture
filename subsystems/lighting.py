from enum import Enum

from wpilib._wpilib import AddressableLED

from codeinternals.constants import lighting_constants
from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase
from codeinternals.subsystems.lightingcontrollers.one_color_controller import OneColorController
from codeinternals.subsystems.subsystem_base import SubsystemBase
from codeinternals.utils import color


class Lighting(SubsystemBase):
    class State(Enum):
        IDLE = 0
        SHOOTING = 1

    def start(self):
        self.instance = Lighting()
        self.ledBuffer = [AddressableLED.LEDData(0, 0, 0)] * lighting_constants.led_length
        LightingControllerBase.timer.start()

    def update(self, commands, state):

        self.__wantedState = commands.getLightingWantedState()
        self.isNewState = self.state != self.__wantedState
        self.state = self.__wantedState

        if self.isNewState:
            if self.state == Lighting.State.IDLE:
                self.controller = OneColorController(color.off)

            elif self.state == Lighting.State.SHOOTING:
                self.controller = OneColorController(color.green, 1)

        if self.controller.isFinished():
            self.controller = OneColorController(color.off)

        self.ledBuffer = self.controller.update()

    def getOutput(self):
        return self.ledBuffer

    def getInstance(self):
        return self.instance
