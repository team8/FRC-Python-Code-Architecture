from codeinternals.subsystems.drive import Drive


class Commands:
    wantedDriveState = Drive.State.IDLE
    wantedTurnAngle = 0
    wantedTargetDistance = 0

    def getDriveWantedState(self):
        return self.wantedDriveState

    def setDriveStateIdle(self):
        self.wantedDriveState = Drive.State.IDLE

    def setDriveStateTurn(self, turnAngle):
        self.wantedDriveState = Drive.State.TURN
        self.wantedTurnAngle = turnAngle

    def setDriveStateMoveStraight(self, targetDistance):
        self.wantedDriveState = Drive.State.MOVE_STRAIGHT
        self.wantedTargetDistance = targetDistance
