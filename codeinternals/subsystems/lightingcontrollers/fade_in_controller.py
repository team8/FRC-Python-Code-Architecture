from codeinternals.utils.color import color
import time


class FadeInController:
    def __init__(self, wanted_color, length, duration=-1):

        self.length = length
        self.data = [(0, 0, 0) for i in range(self.length)]
        hsv = color(wanted_color)
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]
        self.duration = duration
        self.start = time.time()

    def update(self):

        n = 1 - (((self.start - time.time()) % self.duration) / self.duration)

        for d in self.data:

            d.setHSV(self.h, self.s, int(self.v * n))

        return self.data




