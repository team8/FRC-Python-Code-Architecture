from wpilib._wpilib import Timer

from subsystems.lighting import led_buffer


class FlashingLightsController:
    def __init__(self, wanted_color, cycle_time, duration):

        self.timer = Timer()
        self.cycle_time = cycle_time
        self.duration = duration

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]
        self.timer.reset()

    def update(self):
        for d in led_buffer:
            if self.timer.get() % self.cycle_time == 0:
                d.setHSV(self.h, self.s, self.v)
            else:
                d.setHSV(0, 0, 0)

        return led_buffer

    def isFinished(self):
        if self.duration <= self.timer.get():
            return True
        return False
