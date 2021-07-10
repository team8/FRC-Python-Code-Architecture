from wpilib._wpilib import Timer
from utils import math_util


class FadeInController:
    def __init__(self, wanted_color, duration):
        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.duration = duration

    def update(self, led_buffer, timer):
        n = 1 - ((timer % self.duration) / self.duration)

        for d in led_buffer:
            d.setHSV(self.h, self.s, int(self.v * n))

        print(v*n)
        return led_buffer

    def isFinished(self):
        if self.duration <= self.timer.get():
            return True
        return False