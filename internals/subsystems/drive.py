from enum import Enum

from ctre import TalonFX, PigeonIMU, DemandType
from rev import CANSparkMax, MotorType
from wpilib.controller import PIDController

from internals import commands
from internals.subsystems.drive_controllers.move_straight_controller import MoveStraightController
from internals.utils.controller_outputs import ControllerOutputs
from internals.utils.gains import Gains
from internals.commands import RobotName


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

            self.drive_gains = Gains(0.016, 0.0, 0.0, 0.0294, 0.0)

            # self.left_master.config_kP(self.drive_gains.getP())
            # self.left_master.config_kI(self.drive_gains.getI())
            # self.left_master.config_kD(self.drive_gains.getD())
            # self.left_master.config_kF(self.drive_gains.getF())
            # self.right_master.config_kP(self.drive_gains.getP())
            # self.right_master.config_kI(self.drive_gains.getI())
            # self.right_master.config_kD(self.drive_gains.getD())
            # self.right_master.config_kF(self.drive_gains.getF())
            # self.right_master.configMotionAcceleration(self.drive_gains.getAcceleration())
            # self.right_master.configMotionCruiseVelocity(self.drive_gains.getVelocity())
            # self.left_master.configMotionAcceleration(self.drive_gains.getAcceleration())
            # self.left_master.configMotionCruiseVelocity(self.drive_gains.getVelocity())
            # self.left_master.configClosedloopRamp(closedLoopRampSec)
            # self.right_master.configClosedloopRamp(closedLoopRampSec)

            # self.gyro = PigeonIMU()

        if robot_type == RobotName.NARI:
            self.left_master = TalonFX(12)
            left_slave = TalonFX(13)
            self.right_master = TalonFX(2)
            right_slave = TalonFX(3)

            left_slave.follow(self.left_master)
            right_slave.follow(self.right_master)

            self.drive_gains = Gains(0.016, 0.0, 0.0, 0.0294, 0.0)

            # self.left_master.config_kP(0, self.drive_gains.getP())
            # self.left_master.config_kI(0, self.drive_gains.getI())
            # self.left_master.config_kD(0, self.drive_gains.getD())
            # self.left_master.config_kF(0, self.drive_gains.getF())
            # self.right_master.config_kP(0, self.drive_gains.getP())
            # self.right_master.config_kI(0, self.drive_gains.getI())
            # self.right_master.config_kD(0, self.drive_gains.getD())
            # self.right_master.config_kF(0, self.drive_gains.getF())
            # self.right_master.configMotionAcceleration(self.drive_gains.getAcceleration())
            # self.right_master.configMotionCruiseVelocity(self.drive_gains.getVelocity())
            # self.left_master.configMotionAcceleration(self.drive_gains.getAcceleration())
            # self.left_master.configMotionCruiseVelocity(self.drive_gains.getVelocity())
            # self.left_master.configClosedloopRamp(closedLoopRampSec)
            # self.right_master.configClosedloopRamp(closedLoopRampSec)

            # self.gyro = PigeonIMU()

        self.state = DriveState.IDLE
        self.wanted_state = None
        self.controller = None

    def update_state(self):
        is_new_state = commands.wanted_drive_state != self.state
        is_controller_finished = True if self.controller is None else self.controller.check_finished()

        if is_new_state and is_controller_finished:
            self.state = commands.wanted_drive_state
            if self.state is None:
                self.controller = None
            if self.state == DriveState.IDLE:
                self.controller = None
            if self.state == DriveState.MOVE_STRAIGHT:
                self.controller = MoveStraightController(commands.wanted_drive_target_distance, self.drive_gains)
            # if self.state == DriveState.TURN:
            #     self.controller = TurnYawController(commands.wanted_turn_angle)
            # if self.state == DriveState.JOYSTICK_DRIVE:
            #     self.controller = JoystickDriveController()

    def write_state(self):
        if self.controller is not None:
            output = self.controller.update()

            print(output.left_output.getControlMode())
            self.left_master.set(output.left_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                 self.drive_gains.getFF())
            self.right_master.set(output.left_output.getControlMode(), DemandType.ArbitraryFeedForward,
                                  self.drive_gains.getFF())

    def update(self):
        self.update_state()
        self.write_state()
