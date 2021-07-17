from ctre import NeutralMode, InvertType, DemandType

from hardware import drive_hardware
from subsystems import drive
from subsystems import shooter
from hardware import shooter_hardware
from robot import robot_state


def reset_devices():
    def reset_gyro():
        drive_hardware.gyro.setCompassAngle(0)

    reset_gyro()


def configure_subsystems():
    def configure_drive():
        drive_hardware.left_slave_falcon.follow(drive_hardware.left_master_falcon)
        drive_hardware.right_slave_falcon.follow(drive_hardware.right_master_falcon)
        drive_hardware.right_master_falcon.setInverted(InvertType.InvertMotorOutput)

    def configure_shooter():
        shooter_hardware.shooter_master_neo.setInverted(True)
        #shooter_hardware.shooter_slave_neo.follow(shooter_hardware.shooter_master_neo, False)

    configure_drive()
    configure_shooter()


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

    def update_shooter():
        #print("f")
        shooter_hardware.shooter_blocker_solenoid.set(robot_state.shooter_blocker_extended)
        shooter_hardware.shooter_hood_solenoid.set(robot_state.shooter_hood_extended)
        #shooter_hardware.shooter_master_neo.set(0.1)
        #shooter_hardware.shooter_slave_neo.set(0.1)
        if robot_state.shooter_flywheel_running:
            shooter_hardware.shooter_master_neo.set(0.1)
            shooter_hardware.shooter_slave_neo.set(0.1)
        else:
            shooter_hardware.shooter_master_neo.set(0.0)
            shooter_hardware.shooter_slave_neo.set(0.0)

    update_drive()
    update_shooter()
