from codeinternals.subsystems.lighting import Lighting
import time

from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FadeInFadeOutController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, duration=-1):

        self.duration = duration
        self.start = time.time()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.state = "fade_in"

    def update(self):
        if float(time.time() % self.duration) == 0.0:
            if self.state == "fade_in":
                self.state = "fade_out"
            else:
                self.state = "fade_in"

        if self.state == "fade_in":
            n = 1 - (((self.start - time.time()) % self.duration) / self.duration)

            for d in self.ledBuffer:
                d.setHSV(self.h, self.s, int(self.v * n))

        else:
            n = ((self.start - time.time()) % self.duration) / self.duration

            for d in self.ledBuffer:
                d.setHSV(self.h, self.s, int(self.v * n))

        return self.ledBuffer



