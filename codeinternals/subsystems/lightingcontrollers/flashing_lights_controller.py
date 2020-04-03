from codeinternals.subsystems.lighting import Lighting

from codeinternals.subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FlashingLightsController(LightingControllerBase, Lighting):
    def __init__(self, wanted_color, cycle_time, duration=-1):

        self.cycle_time = cycle_time
        self.duration = duration

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]
        self.timer.reset()

    def update(self):
        for d in self.ledBuffer:
            if self.timer.get() % self.cycle_time == 0:
                d.setHSV(self.h, self.s, self.v)

            else:
                d.setHSV(0, 0, 0)

        return self.ledBuffer

    def isFinished(self) -> bool:
        if self.duration != -1 and self.duration >= self.timer.get():
            return True
        return False
