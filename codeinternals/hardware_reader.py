from codeinternals.hardware_adapter import HardwareAdapter
from codeinternals import robot_state


class HardwareReader:
    def configureState(self):
        self.configureDriveSensors()

    def updateState(self):
        self.updateDriveSensors()

    def configureDriveSensors(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_hardware.gyro.setCompassAngle(0)

    def updateDriveSensors(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        robot_state.gyroCompassHeadingDegrees = drive_hardware.gyro.getCompassHeading()
