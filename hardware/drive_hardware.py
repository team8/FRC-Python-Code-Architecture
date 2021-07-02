from wpilib._wpilib import AddressableLED
from wpilib._wpilib import Joystick

import ctre
from constants import port_constants
from ctre import PigeonIMU

from utils.pid_controller import PIDController

left_master_falcon = ctre.TalonFX(port_constants.left_master_falcon_id)
left_slave_falcon = ctre.TalonFX(port_constants.left_slave_falcon_id)
right_master_falcon = ctre.TalonFX(port_constants.right_master_falcon_id)
right_slave_falcon = ctre.TalonFX(port_constants.right_slave_falcon_id)
left_falcon_encoder = ctre.CANCoder(port_constants.left_falcon_encoder_id)
right_falcon_encoder = ctre.CANCoder(port_constants.right_falcon_encoder_id)
gyro = PigeonIMU(port_constants.gyro_id)

maxWheelPercentOutput = 0.4
closedLoopRampSec = 2
positionConversionFactor = 1000
velocityConversionFactor = 1000
moveStraightGains = PIDController(0.0, 0.0, 0.0)
turnGains = PIDController(0.0, 0.0, 0.0)