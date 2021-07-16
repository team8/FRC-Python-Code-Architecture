from ctre import TalonFX, PigeonIMU

left_master = TalonFX(12)
left_slave = TalonFX(13)
right_master = TalonFX(2)
right_slave = TalonFX(3)

gyro = PigeonIMU(9)
