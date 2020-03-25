from enum import Enum

from codeinternals.subsystems.subsystem_base import SubsystemBase


class Drive(SubsystemBase):
    class State(Enum):
        IDLE = 0
        MOVE_STRAIGHT = 1
        TURN = 2
    def update(self):
        print("Drive Subsystem Running...")

