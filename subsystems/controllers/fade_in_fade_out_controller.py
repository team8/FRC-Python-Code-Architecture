from subsystems.controllers.fade_in_controller import FadeInController
from subsystems.controllers.fade_out_controller import FadeOutController
from utils import math_util
from wpilib._wpilib import Timer


class FadeInFadeOutController:
    def __init__(self, wanted_color, duration):
        self.timer = Timer()
        self.fade_out = FadeOutController(wanted_color, duration)
        self.fade_in = FadeInController(wanted_color, duration)
        self.duration = duration
        self.timer.reset()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.toggle = True

    def update(self, led_buffer):
        if float(self.timer.get() % (self.duration / 2)) == 0.0:
            if self.toggle:
                self.toggle = False
            else:
                self.toggle = True

        if self.toggle:
            led_buffer2 = self.fade_in.update(led_buffer, self.timer.get())
        else:
            led_buffer2 = self.fade_out.update(led_buffer, self.timer.get())
        return led_buffer2

    def isFinished(self):
        if self.duration <= self.timer.get():
            return True
        return False
