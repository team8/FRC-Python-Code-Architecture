from codeinternals.subsystems.lighting import Lighting
from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FadeInController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, length, duration=-1):
        self.length = length

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.duration = duration
        self.timer.reset()

    def update(self):
        n = 1 - ((self.timer.get() % self.duration) / self.duration)

        for d in self.ledBuffer:
            d.setHSV(self.h, self.s, int(self.v * n))

        return self.ledBuffer

    def isFinished(self) -> bool:
        if self.duration != -1 and self.duration >= self.timer.get():
            return True
        return False
