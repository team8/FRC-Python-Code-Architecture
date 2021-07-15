import ctre
from constants import port_constants
import wpilib
import rev

#shooter_master_neo = wpilib.Spark(port_constants.shooter_master_id)
#shooter_slave_neo = wpilib.Spark(port_constants.shooter_slave_id)
shooter_master_neo = rev.CANSparkMax(port_constants.shooter_master_id, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
shooter_slave_neo = rev.CANSparkMax(port_constants.shooter_slave_id, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
shooter_blocker_solenoid = wpilib.Solenoid(port_constants.shooter_hood_blocker_solenoid)