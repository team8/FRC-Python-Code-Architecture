from wpilib import AddressableLED
from codeinternals.utils import color


class OneColorController:
    def __init__(self, color1):
        self.led = AddressableLED(1)  # todo find real port

        a = color(color1)
        self.h = a[0]
        self.s = a[1]
        self.v = a[2]

    def update(self):
        self.data = self.led.LEDData(self.h, self.s, self.v)

        self.led.setData(self.data)
