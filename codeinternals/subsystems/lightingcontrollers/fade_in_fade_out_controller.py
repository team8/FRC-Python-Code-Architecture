from codeinternals.utils.color import color
import time


class FadeInFadeOutController:
    def __init__(self, wanted_color, length, duration):

        self.length = length
        self.data = [(0, 0, 0) for i in range(self.length)]
        hsv = color(wanted_color)
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]
        self.duration = duration
        self.start = time.time()
        self.state = "fade_in"

    def update(self):
        if float(time.time() % self.duration) == 0.0:
            if self.state == "fade_in":
                self.state = "fade_out"
            else:
                self.state = "fade_in"

        if self.state == "fade_in":
            n = 1 - (((self.start - time.time()) % self.duration) / self.duration)

            for d in self.data:
                d.setHSV(self.h, self.s, int(self.v * n))

        else:
            n = ((self.start - time.time()) % self.duration) / self.duration

            for d in self.data:
                d.setHSV(self.h, self.s, int(self.v * n))

        return self.data



