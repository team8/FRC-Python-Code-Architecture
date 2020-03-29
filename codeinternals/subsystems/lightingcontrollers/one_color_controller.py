from wpilib import AddressableLED


class OneColorController:
    def __init__(self, color):
        self.led = AddressableLED(1)  # todo find real port

    def update(self):
        self.data = self.led.LEDData(255, 0, 0)

        self.led.setData(self.data)
