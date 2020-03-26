from codeinternals.ctre import NeutralMode
from codeinternals.hardware_adapter import HardwareAdapter
from codeinternals.robot import Robot
from codeinternals.subsystems.drive import Drive
from codeinternals.constants import drive_constants
from codeinternals.utils import math_util



class HardwareWriter:
    def configureSubsystems(self):
        if Robot.enabledSystems.__contains__("drive"):
            HardwareWriter.configureDrive()

    def updateSubsystems(self):
        if Robot.enabledSystems.__contains__("drive"):
            HardwareWriter.updateDrive()

    def configureDrive(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_hardware.left_slave_falcon.follow(drive_hardware.left_master_falcon)
        drive_hardware.right_slave_falcon.follow(drive_hardware.right_master_falcon)

    def updateDrive(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_output = Drive.getOutput()
        left_output = drive_output.leftOutput
        right_output = drive_output.rightOutput
        if drive_output is not None:
            # TODO This PID Configuration stuff is very messy so this is very barebone functionality. No motion magic
            # TODO Only uses Percent Output for now and you can use PIDController import for PID functionality
            drive_hardware.left_master_falcon.set(left_output.getControlMode(), math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput, left_output.getReference()))
            drive_hardware.right_master_falcon.set(right_output.getControlMode(), math_util.clamp(-drive_constants.maxWheelPercentOutput, drive_constants.maxWheelPercentOutput, right_output.getReference()))
        else:
            drive_hardware.left_master_falcon.setNeutralMode(NeutralMode.Brake)
            drive_hardware.right_master_falcon.setNeutralMode(NeutralMode.Brake)
