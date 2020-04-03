import time

from codeinternals.subsystems.lighting import Lighting
from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class OneColorController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, duration=-1):
        self.duration = duration
        self.start = time.time()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.mTimer.start()

    def update(self):
        for d in self.ledBuffer:
            d.setHSV(self.h, self.s, self.v)

        return self.ledBuffer

    def is_finished(self):
        if self.duration != -1 and self.duration >= self.mTimer.get():
            return True
        return False
