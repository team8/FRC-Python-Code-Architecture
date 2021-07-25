import rev
import wpilib
from constants import port_constants
from ctre import TalonFX

from ctre import ControlMode

global slave_spark
global master_spark
global master_shooter
global slave_shooter
global drive_joystick
global turn_joystick
global inner_intake_master
global inner_intake_slave
global outer_intake

def init():
    global inner_intake_master
    global inner_intake_slave
    global outer_intake
    inner_intake_master = TalonFX(7)
    inner_intake_slave = TalonFX(4)
    outer_intake = TalonFX(8)
def start():
    global slave_spark
    global master_spark
    global master_shooter
    global slave_shooter
    global drive_joystick
    global turn_joystick
    slave_spark = rev.CANSparkMax(port_constants.indexer_slave_id, rev.MotorType.kBrushless)
    master_spark = rev.CANSparkMax(port_constants.indexer_master_id, rev.MotorType.kBrushless)
    master_shooter = rev.CANSparkMax(16, rev.MotorType.kBrushless)
    slave_shooter = rev.CANSparkMax(1, rev.MotorType.kBrushless)
    drive_joystick = wpilib.Joystick(port_constants.drive_joystick_id)
    turn_joystick = wpilib.Joystick(port_constants.turn_joystick_id)
    slave_spark.follow(master_spark)

def update():
    if turn_joystick.getTrigger():
        slave_shooter.set(0.7)
        master_shooter.set(-0.7)
    else:
        slave_shooter.set(0)
        master_shooter.set(0)

    if drive_joystick.getTrigger():
        master_spark.set(-0.7)
        inner_intake_master.set(ControlMode.PercentOutput, -0.5)
        inner_intake_slave.set(ControlMode.PercentOutput, -0.5)
        outer_intake.set(ControlMode.PercentOutput, -0.5)
    else:
        inner_intake_master.set(ControlMode.PercentOutput, 0)
        inner_intake_slave.set(ControlMode.PercentOutput, 0)
        outer_intake.set(ControlMode.PercentOutput, 0)
        master_spark.set(0)

    master_spark.set(-drive_joystick.getX())



