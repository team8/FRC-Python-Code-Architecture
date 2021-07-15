from enum import Enum

from ctre import TalonFX, PigeonIMU
from rev import CANSparkMax, MotorType
from wpilib.controller import PIDController

import internals.commands
from internals.utils.controller_outputs import ControllerOutputs
from internals.utils.gains import Gains
from robot import RobotName


maxWheelPercentOutput = 0.4
closedLoopRampSec = 2
positionConversionFactor = 1000
velocityConversionFactor = 1000
moveStraightGains = PIDController(0.0, 0.0, 0.0)
turnGains = PIDController(0.0, 0.0, 0.0)


class DriveState(Enum):
    IDLE = 0
    MOVE_STRAIGHT = 1
    TURN = 2
    JOYSTICK_DRIVE = 3


class DriveOutputs:
    def __init__(self, drive_gains):
        self.left_output = ControllerOutputs(drive_gains)
        self.right_output = ControllerOutputs(drive_gains)


class Drive:
    def __init__(self, robot_type):
        if robot_type == RobotName.OSR:
            self.left_master = CANSparkMax(1, MotorType.kBrushless)
            left_spark_slave1 = CANSparkMax(2, MotorType.kBrushless)
            left_spark_slave2 = CANSparkMax(3, MotorType.kBrushless)
            self.right_master = CANSparkMax(12, MotorType.kBrushless)
            right_spark_slave_1 = CANSparkMax(13, MotorType.kBrushless)
            right_spark_slave_2 = CANSparkMax(15, MotorType.kBrushless)

            left_spark_slave1.follow(self.left_master)
            left_spark_slave2.follow(self.left_master)
            right_spark_slave_1.follow(self.right_master)
            right_spark_slave_2.follow(self.right_master)

            self.drive_gains = Gains(0.016, 0.0, 0.0, 0.0294, 0.0)

            # self.gyro = PigeonIMU()

        if robot_type == RobotName.NARI:
            self.left_master = TalonFX(12)
            left_slave = TalonFX(13)
            self.right_master = TalonFX(2)
            right_slave = TalonFX(3)

            left_slave.follow(self.left_master)
            right_slave.follow(self.right_master)

            # self.gyro = PigeonIMU()

        self.state = DriveState.IDLE
        self.wanted_state = None
        self.controller = None

    def update_state(self):
        pass

    def write_state(self):
        pass

    def update(self):
        self.update_state()
        self.write_state()
