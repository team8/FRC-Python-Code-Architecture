from subsystems.lightingcontrollers.fade_in_controller import FadeInController
from subsystems.lightingcontrollers.fade_out_controller import FadeOutController

from subsystems.lightingcontrollers.lighting_controller_base import LightingControllerBase


class FadeInFadeOutController(LightingControllerBase, FadeInController, FadeOutController):
    def __init__(self, wanted_color, duration=-1):
        FadeOutController.__init__()
        FadeInController.__init__()
        self.duration = duration
        super().timer.reset()

        self.h = wanted_color[0]
        self.s = wanted_color[1]
        self.v = wanted_color[2]

        self.toggle = True

    def update(self):
        if float(self.timer.get() % self.duration) == 0.0:
            if self.toggle:
                self.toggle = False
            else:
                self.toggle = True

        if self.toggle:
            self.ledBuffer = FadeInController.update()
        else:
            self.ledBuffer = FadeOutController.update()
        return self.ledBuffer

    def isFinished(self) -> bool:
        if self.duration != -1 and self.duration >= self.timer.get():
            return True
        return False
