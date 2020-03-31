from wpilib import AddressableLED
from codeinternals.utils.color import color


class OneColorController:
    def __init__(self, wantedcolor, length):
        self.led = AddressableLED(1)  # todo find real port
        self.led.setLength(30)

        hsv = color(wantedcolor)
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]

        self.length = length

    def update(self):
        self.data = [self.led.LEDData(255, 0, 0) for i in range(self.length)]

        for d in self.data:
            d.setHSV(self.h, self.s, self.v)

        self.led.setData(self.data)





