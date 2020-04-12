from wpilib._wpilib import AddressableLED

from codeinternals.constants import lighting_constants
from codeinternals.subsystems.drive import Drive
from codeinternals.subsystems.lighting import Lighting


class Commands:
    wantedDriveState = Drive.State.IDLE
    wantedTurnAngle = 0
    wantedTargetDistance = 0
    wantedLightingState = Lighting.State.IDLE
    wantedLedBuffer = [AddressableLED.LEDData(0, 0, 0)] * lighting_constants.led_length

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

    def setDriveStateJoystickControl(self):
        self.wantedDriveState = Drive.State.JOYSTICK_DRIVE

    def getLightingWantedState(self):
        return self.wantedLightingState
