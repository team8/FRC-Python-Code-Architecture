from codeinternals.subsystems.drive import Drive


class RobotState:
    driveState = Drive.State.IDLE

    def getDriveState(self):
        return self.driveState

