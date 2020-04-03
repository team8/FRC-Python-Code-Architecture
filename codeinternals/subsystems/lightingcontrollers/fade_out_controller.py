from codeinternals.subsystems.lighting import Lighting
import time

from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FadeOutController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, duration=-1):

        self.start = time.time()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.duration = duration
        self.mTimer.start()

    def update(self):

        n = (self.mTimer % self.duration) / self.duration

        for d in self.ledBuffer:

            d.setHSV(self.h, self.s, int(self.v * n))

        return self.ledBuffer





