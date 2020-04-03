from codeinternals.subsystems.lighting import Lighting
import time


class OneColorController(Lighting.AddressableLedBuffer):
    def __init__(self, wanted_color, duration=-1):
        self.duration = duration
        self.start = time.time()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

    def update(self):
        for d in self.mBuffer:
            d.setHSV(self.h, self.s, self.v)

        return self.mBuffer
