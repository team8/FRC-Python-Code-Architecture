from wpilib import AddressableLED
from codeinternals.utils.color import color
import time

class OneColorController:
    def __init__(self, wanted_color, length):
        self.led = AddressableLED(1)
        self.led.setLength(30)

        hsv = color(wanted_color)
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]

        self.length = length

        self.start_time = time.time()

    def update(self):
        self.data = [self.led.LEDData(255, 0, 0) for i in range(self.length)]

        for d in self.data:
            if int(time.time() - self.start_time()) % 2 == 0:
                d.setHSV(self.h, self.s, self.v)

            else:
                d.setHSV(0, 0, 0)

        self.led.setData(self.data)





