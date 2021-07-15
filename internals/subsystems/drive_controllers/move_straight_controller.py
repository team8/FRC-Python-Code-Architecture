from internals.utils.drive_outputs import DriveOutputs


class MoveStraightController:
    def __init__(self, target_distance, gains):
        self.output = DriveOutputs(gains)
        self.gains = gains
        self.__targetDistance = target_distance

    def update(self):
        self.output.left_output.setMotionMagicTargetPosition(self.__targetDistance, self.gains)
        self.output.right_output.setMotionMagicTargetPosition(self.__targetDistance, self.gains)
        return self.output

    def check_finished(self):
        return False
