from wpilib import AddressableLED
from codeinternals.utils.color import color
import time


class OneColorController:
    def __init__(self, wanted_color, length, duration):
        self.led = AddressableLED(1)
        self.led.setLength(30)

        hsv = color(wanted_color)
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]
        self.duration = duration
        self.length = length
        self.start = time.time()

    def update(self):
        self.data = [self.led.LEDData(255, 0, 0) for i in range(self.length)]

        n = ((self.start - time.time()) % self.length) / self.length

        for d in self.data:

            d.setHSV(self.h, self.s, int(self.v * n))

        self.led.setData(self.data)





