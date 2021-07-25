import hardware
from hardware import *

from ctre import ControlMode
from datetime import datetime


class DriveForward:

    def __init__(self, dist, tolerance):
        self.wantedDistance = dist
        self.pos = 0
        self.tolerance = tolerance

    def update(self):
        if(self.pos < self.wantedDistance):
            hardware.left_master.set(ControlMode.PercentOutput, 0.2)
            hardware.right_master.set(ControlMode.PercentOutput, -0.2)
        else:
            hardware.left_master.set(ControlMode.PercentOutput, -0.2)
            hardware.right_master.set(ControlMode.PercentOutput, 0.2)

    def is_done(self):
        return math.abs(self.pos - self.wantedDistance < self.tolerance)
