from wpilib._wpilib import Timer

from subsystems.lighting import led_buffer


class OneColorController:
    def __init__(self, wanted_color, duration):
        self.timer = Timer()
        self.duration = duration
        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]
        self.timer.reset()

    def update(self):
        for d in led_buffer:
            d.setHSV(self.h, self.s, self.v)

        return led_buffer

    def isFinished(self):
        if self.duration <= self.timer.get():
            return True
        return False
