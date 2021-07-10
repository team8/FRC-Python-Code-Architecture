from robot import commands
from subsystems.drive import State


class DriveForward:

    def __init__(self, distance):
        self.distance = distance

    def update(self):
        commands.wanted_target_distance = self.distance
        commands.wanted_drive_state = State.MOVE_STRAIGHT
