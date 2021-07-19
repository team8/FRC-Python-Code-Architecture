from ctre import TalonFX, PigeonIMU
from wpilib._wpilib import Joystick
import rev

left_master = rev.CANSparkMax(12, rev.MotorType.kBrushless)
left_slave = rev.CANSparkMax(13, rev.MotorType.kBrushless)
left_slave_2 = rev.CANSparkMax(15, rev.MotorType.kBrushless)
right_master = rev.CANSparkMax(1, rev.MotorType.kBrushless)
right_slave = rev.CANSparkMax(2, rev.MotorType.kBrushless)
right_slave_2 = rev.CANSparkMax(3, rev.MotorType.kBrushless)


drive_joystick = Joystick(0)
turn_joystick = Joystick(1)

TalonFX(int)
gyro = PigeonIMU(9)
