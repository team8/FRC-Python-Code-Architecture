from enum import Enum

from codeinternals.subsystems.SubystemBase import SubsystemBase


class Drive(SubsystemBase):
    class State(Enum):
        IDLE = 0
        MOVE_STRAIGHT = 1
        TURN = 2
    def update(self):
        print("Drive Subsystem Running...")

