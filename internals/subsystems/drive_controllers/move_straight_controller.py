from internals.subsystems.drive import *


class MoveStraightController:
    def __init__(self, target_distance, outputs):
        self.output = outputs
        self.__targetDistance = target_distance

    def update(self):
        self.output.left_output.setMotionMagicTargetPosition(self.__targetDistance, moveStraightGains)
        self.output.right_output.setMotionMagicTargetPosition(self.__targetDistance, moveStraightGains)
        return self.output

    def check_finished(self):
        return True
