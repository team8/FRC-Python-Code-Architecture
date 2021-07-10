import ctre
from constants import port_constants
from ctre import PigeonIMU

from utils.pid_controller import PIDController

left_master_falcon = ctre.TalonFX(port_constants.left_master_falcon_id)
left_slave_falcon = ctre.TalonFX(port_constants.left_slave_falcon_id)
right_master_falcon = ctre.TalonFX(port_constants.right_master_falcon_id)
right_slave_falcon = ctre.TalonFX(port_constants.right_slave_falcon_id)
gyro = PigeonIMU(port_constants.gyro_id)
