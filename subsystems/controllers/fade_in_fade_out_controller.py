from subsystems.controllers.fade_in_controller import FadeInController
from subsystems.controllers.fade_out_controller import FadeOutController
from utils import math_util
from wpilib._wpilib import Timer

class FadeInFadeOutController(FadeInController, FadeOutController):
    def __init__(self, wanted_color, duration):
        self.timer = Timer()
        FadeOutController.__init__()
        FadeInController.__init__()
        self.duration = duration
        self.timer.reset()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.toggle = True

    def update(self, led_buffer):
        if math_util.float(self.timer.get() % (self.duration/2)) == 0.0:
            if self.toggle:
                self.toggle = False
            else:
                self.toggle = True

        if self.toggle:
            led_buffer = FadeInController.update(led_buffer)
        else:
            led_buffer = FadeOutController.update(led_buffer)
        return led_buffer

    def isFinished(self):
        if self.duration <= self.timer.get():
            return True
        return False