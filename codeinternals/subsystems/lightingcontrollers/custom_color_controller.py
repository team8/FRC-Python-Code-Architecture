from codeinternals.subsystems.lighting import Lighting
from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase
from codeinternals.commands import Commands


class CustomColorController(LightingControllerBase, Lighting):

    def update(self):
        self.ledBuffer = Commands.wantedLedBuffer.copy()
        return self.ledBuffer

    def isFinished(self) -> bool:
        return True
