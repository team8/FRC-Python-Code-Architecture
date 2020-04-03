from codeinternals.subsystems.lighting import Lighting
import time


class FlashingLightsController(Lighting.AddressableLedBuffer):
    def __init__(self, wanted_color, cycle_time, duration=-1):

        self.cycle_time = cycle_time
        self.duration = duration

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.start_time = time.time()

    def update(self):
        for d in self.mBuffer:
            if int(time.time() - self.start_time()) % self.cycle_time == 0:
                d.setHSV(self.h, self.s, self.v)

            else:
                d.setHSV(0, 0, 0)

        return self.mBuffer





