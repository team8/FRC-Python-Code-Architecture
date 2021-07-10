from ctre import NeutralMode, InvertType, DemandType, ControlMode

from hardware import drive_hardware
from hardware import intake_hardware
from subsystems import drive
from subsystems import intake


def reset_devices():
    def reset_gyro():
        drive_hardware.gyro.setCompassAngle(0)

    reset_gyro()


def configure_subsystems():
    def configure_drive():
        drive_hardware.left_slave_falcon.follow(drive_hardware.left_master_falcon)
        drive_hardware.right_slave_falcon.follow(drive_hardware.right_master_falcon)
        drive_hardware.right_master_falcon.setInverted(InvertType.InvertMotorOutput)

    configure_drive()


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

    def update_intake():
        intake_output = intake.outputs
        solenoid_output = intake.solenoid_output

        if intake_output is not None:
            intake_hardware.talon.set(ControlMode.PercentOutput, 0.7)
            intake_hardware.solenoid.set(solenoid_output)
    update_drive()
    update_intake()
