from codeinternals.subsystems.lighting import Lighting
import time


class FadeInController(Lighting.AddressableLedBuffer):
    def __init__(self, wanted_color, length, duration=-1):

        self.length = length

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.duration = duration
        self.start = time.time()

    def update(self):

        n = 1 - (((self.start - time.time()) % self.duration) / self.duration)

        for d in self.mBuffer:

            d.setHSV(self.h, self.s, int(self.v * n))

        return self.mBuffer




