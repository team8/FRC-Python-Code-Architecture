from ctre import NeutralMode, InvertType, DemandType

from constants import lighting_constants
from hardware import drive_hardware, lighting_hardware
from subsystems import drive, lighting


def reset_devices():
    def reset_gyro():
        #drive_hardware.gyro.setCompassAngle(0)
        lol = 0

    reset_gyro()


def configure_subsystems():
    def configure_drive():
        drive_hardware.left_slave_falcon.follow(drive_hardware.left_master_falcon)
        drive_hardware.right_slave_falcon.follow(drive_hardware.right_master_falcon)
        drive_hardware.right_master_falcon.setInverted(InvertType.InvertMotorOutput)
        #print("configured drive")

    def configure_lighting():
        lighting_hardware.led_strip.setLength(lighting_constants.led_length)
        lighting_hardware.led_strip.start()
        #print("configured lighting")

    configure_drive()
    configure_lighting()


def update_subsystems():
    def set_gains():
        drive_output = drive.outputs
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
        drive_hardware.left_master_falcon.configClosedloopRamp(drive_hardware.closedLoopRampSec)
        drive_hardware.right_master_falcon.configClosedloopRamp(drive_hardware.closedLoopRampSec)


    def update_drive():

        drive_output = drive.outputs


        if drive_output is not None:

            left_output = drive_output.leftOutput
            right_output = drive_output.rightOutput

            set_gains()
            drive_hardware.left_master_falcon.set(left_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                                  left_output.getGains().getFF())
            drive_hardware.right_master_falcon.set(right_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                                   right_output.getGains().getFF())


    def update_lighting():
        lighting_output = lighting.led_buffer
        print(lighting_output)
        if lighting_output is not None:
            lighting_hardware.led_strip.setData(lighting_output)

    update_drive()
    update_lighting()
