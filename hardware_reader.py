from codeinternals import robot_state
from codeinternals.hardware_adapter import HardwareAdapter


class HardwareReader:
    def configureState(self):
        self.__configureDriveSensors()

    def updateState(self):
        self.__updateDriveSensors()

    def __configureDriveSensors(self):
        self.resetGyro()

    def __updateDriveSensors(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        joystick_hardware = HardwareAdapter.JoystickHardware.__getInstance__()
        robot_state.gyroCompassHeadingDegrees = drive_hardware.gyro.getCompassHeading()
        robot_state.activeTrajectoryPosition = drive_hardware.right_master_falcon.getActiveTrajectoryPosition()
        robot_state.driveJoystickY = -joystick_hardware.driveJoystick.getY()
        robot_state.driveJoystickX = joystick_hardware.driveJoystick.getX()
        robot_state.turnJoystickX = joystick_hardware.turnJoystick.getX()

    def resetGyro(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_hardware.gyro.setCompassAngle(0)
