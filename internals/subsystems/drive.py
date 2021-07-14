from enum import Enum


class DriveState(Enum):
    IDLE = 0
    MOVE_STRAIGHT = 1
    TURN = 2
    JOYSTICK_DRIVE = 3


class Drive:
    def __init__(self):
        self.state = DriveState.IDLE
        self.wanted_state = None
        self.controller = None

    def update_state(self):
        pass

    def write_state(self):
        pass

    def update(self):
        self.update_state()
        self.write_state()
