import rev
import wpilib
from constants import port_constants
from ctre import TalonFX

from ctre import ControlMode

global slave_spark
global master_spark
global joystick
global shooter
global shooter2
global talon7
global talon4
global talon8
global joystick2

def start():
    global slave_spark
    global master_spark
    global shooter
    global shooter2
    global talon7
    global talon4
    global talon8
    global joystick
    global joystick2
    slave_spark = rev.CANSparkMax(port_constants.indexer_slave_id, rev.MotorType.kBrushless)
    master_spark = rev.CANSparkMax(port_constants.indexer_master_id, rev.MotorType.kBrushless)
    talon7 = TalonFX(7)
    talon4 = TalonFX(4)
    talon8 = TalonFX(8)
    shooter = rev.CANSparkMax(16, rev.MotorType.kBrushless)
    shooter2 = rev.CANSparkMax(1, rev.MotorType.kBrushless)
    joystick = wpilib.Joystick(port_constants.drive_joystick_id)
    joystick2 = wpilib.Joystick(port_constants.turn_joystick_id)
    slave_spark.follow(master_spark)

def update():
    master_spark.set(joystick.getX())
    shooter2.set(joystick2.getX())
    shooter.set(-joystick2.getX())
    talon7.set(ControlMode.PercentOutput, 0.6*joystick.getX())
    talon4.set(ControlMode.PercentOutput, -0.6*joystick.getX())
    talon8.set(ControlMode.PercentOutput, 0.5*joystick.getX())




