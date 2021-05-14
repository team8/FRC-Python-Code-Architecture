from constants import drive_constants
from constants import lighting_constants
from ctre import NeutralMode, InvertType, DemandType
from hardware_adapter import HardwareAdapter
from robot import Robot
from subsystems.drive import Drive
from subsystems.lighting import Lighting


class HardwareWriter:
    def configureSubsystems(self):
        if Robot.enabledSystems.__contains__(Drive.getInstance()):
            self.__configureDrive()
        if Robot.enabledSystems.__contains__(Lighting.getInstance()):
            self.__configureLighting()

    def updateSubsystems(self):
        if Robot.enabledSystems.__contains__(Drive.getInstance()):
            self.__updateDrive()
        if Robot.enabledSystems.__contains__(Lighting.getInstance()):
            self.__updateLighting()

    def __configureDrive(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_hardware.left_slave_falcon.follow(drive_hardware.left_master_falcon)
        drive_hardware.right_slave_falcon.follow(drive_hardware.right_master_falcon)
        drive_hardware.right_master_falcon.setInverted(InvertType.InvertMotorOutput)

    def __configureLighting(self):
        lighting_hardware = HardwareAdapter.LightingHardware.__getInstance__()
        lighting_hardware.led_strip.setLength(lighting_constants.led_length)
        lighting_hardware.led_strip.start()

    def __updateDrive(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_output = Drive.getOutput()
        left_output = drive_output.leftOutput
        right_output = drive_output.rightOutput
        if drive_output is not None:
            self.__setGains()
            drive_hardware.left_master_falcon.set(left_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                                  left_output.getGains().getFF())
            drive_hardware.right_master_falcon.set(right_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                                   right_output.getGains().getFF())
        else:
            drive_hardware.left_master_falcon.setNeutralMode(NeutralMode.Brake)
            drive_hardware.right_master_falcon.setNeutralMode(NeutralMode.Brake)

    def __setGains(self):
        drive_hardware = HardwareAdapter.DriveHardware.__getInstance__()
        drive_output = Drive.getOutput()
        left_output = drive_output.leftOutput
        right_output = drive_output.rightOutput
        drive_hardware.left_master_falcon.config_kP(left_output.getGains().getP())
        drive_hardware.left_master_falcon.config_kI(left_output.getGains().getI())
        drive_hardware.left_master_falcon.config_kD(left_output.getGains().getD())
        drive_hardware.left_master_falcon.config_kF(left_output.getGains().getF())
        drive_hardware.right_master_falcon.config_kP(right_output.getGains().getP())
        drive_hardware.right_master_falcon.config_kI(right_output.getGains().getI())
        drive_hardware.right_master_falcon.config_kD(right_output.getGains().getD())
        drive_hardware.right_master_falcon.config_kF(right_output.getGains().getF())
        drive_hardware.right_master_falcon.configMotionAcceleration(right_output.getGains().getAcceleration())
        drive_hardware.right_master_falcon.configMotionCruiseVelocity(right_output.getGains().getVelocity())
        drive_hardware.left_master_falcon.configMotionAcceleration(right_output.getGains().getAcceleration())
        drive_hardware.left_master_falcon.configMotionCruiseVelocity(right_output.getGains().getVelocity())
        drive_hardware.left_master_falcon.configClosedloopRamp(drive_constants.closedLoopRampSec)
        drive_hardware.right_master_falcon.configClosedloopRamp(drive_constants.closedLoopRampSec)

    def __updateLighting(self):
        lighting_hardware = HardwareAdapter.LightingHardware.__getInstance__()
        lighting_output = Lighting.getOutput()
        lighting_hardware.led_strip.setData(lighting_output)
