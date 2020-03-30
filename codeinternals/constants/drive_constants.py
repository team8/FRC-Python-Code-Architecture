from codeinternals.utils.pid_controller import PIDController

maxWheelPercentOutput = 0.4
closedLoopRampSec = 2
positionConversionFactor = 1000
velocityConversionFactor = 1000
moveStraightGains = PIDController(0.0, 0.0, 0.0)
turnGains = PIDController(0.0, 0.0, 0.0)