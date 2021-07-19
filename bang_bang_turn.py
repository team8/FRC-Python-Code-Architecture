import hardware
from hardware import *

from ctre import ControlMode
from datetime import datetime


class BangBangTurn:

    def __init__(self, angle: int):
        self.wanted_angle = angle
        gyro.reset()

    def update(self):
        if self.wanted_angle <= gyro.getAngle():
            hardware.left_master.set(ControlMode.PercentOutput, 0.2)
            hardware.right_master.set(ControlMode.PercentOutput, 0.2)
        else:
            hardware.left_master.set(ControlMode.PercentOutput, -0.2)
            hardware.right_master.set(ControlMode.PercentOutput, -0.2)

    def is_done(self):
        if abs(self.wanted_angle - gyro.getAngle) < 1:
            return True
