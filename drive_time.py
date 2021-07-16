import hardware
from hardware import *

from ctre import ControlMode
from datetime import datetime


class DriveForward:

    def __init__(self, time: int):
        self.wanted_time = time
        self.start_time = datetime.now().second

    def update(self):
        hardware.left_master.set(ControlMode.PercentOutput, 0.2)
        hardware.right_master.set(ControlMode.PercentOutput, -0.2)

    def is_done(self):
        if datetime.now().second - self.start_time >= self.wanted_time:
            return True
