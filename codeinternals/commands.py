from codeinternals.subsystems.drive import Drive


class Commands:
    wantedDriveState = Drive.State.IDLE

    def getDriveWantedState(self):
        return self.wantedDriveState
