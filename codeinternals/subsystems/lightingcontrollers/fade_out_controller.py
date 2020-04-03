from codeinternals.subsystems.lighting import Lighting

from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FadeOutController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, duration=-1):
        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.duration = duration
        self.timer.reset()

    def update(self):
        n = (self.timer.get() % self.duration) / self.duration

        for d in self.ledBuffer:
            d.setHSV(self.h, self.s, int(self.v * n))

        return self.ledBuffer

    def isFinished(self) -> bool:
        if self.duration != -1 and self.duration >= self.timer.get():
            return True
        return False
