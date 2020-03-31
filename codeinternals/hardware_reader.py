from codeinternals.hardware_adapter import HardwareAdapter
from codeinternals import robot_state


class HardwareReader:
    def configureState(self):
        self.__configureDriveSensors()

    def updateState(self):
        self.__updateDriveSensors()

    def __configureDriveSensors(self):
        self.resetGyro()

    def __updateDriveSensors(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        robot_state.gyroCompassHeadingDegrees = drive_hardware.gyro.getCompassHeading()

    def resetGyro(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_hardware.gyro.setCompassAngle(0)
