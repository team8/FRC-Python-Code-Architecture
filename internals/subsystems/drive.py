from enum import Enum

from ctre import TalonFX, PigeonIMU
from rev import CANSparkMax, MotorType
from wpilib.controller import PIDController

import internals.commands
from robot import RobotName


class DriveState(Enum):
    IDLE = 0
    MOVE_STRAIGHT = 1
    TURN = 2
    JOYSTICK_DRIVE = 3


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

            # self.gyro = PigeonIMU()

        self.state = DriveState.IDLE
        self.wanted_state = None
        self.controller = None

        self.maxWheelPercentOutput = 0.4
        self.closedLoopRampSec = 2
        self.positionConversionFactor = 1000
        self.velocityConversionFactor = 1000
        self.moveStraightGains = PIDController(0.0, 0.0, 0.0)
        self.turnGains = PIDController(0.0, 0.0, 0.0)

    def update_state(self):
        pass

    def write_state(self):
        pass

    def update(self):
        self.update_state()
        self.write_state()
