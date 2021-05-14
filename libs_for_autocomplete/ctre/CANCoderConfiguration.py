from codeinternals.ctre import CustomParamConfiguration


class CANCoderConfiguration(CustomParamConfiguration):
    """ Configurables available to CANCoder """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.CANCoderConfiguration) -> str
        
        
        
        :returns: String representation of configs
        
        2. toString(self: ctre._ctre.CANCoderConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """
        __init__(self: ctre._ctre.CANCoderConfiguration) -> None
        
        Constructor
        """
        pass

    absoluteSensorRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired Sign / Range for the absolute position register.
Choose unsigned for an absolute range of[0, +1) rotations, [0, 360) deg, etc.
Choose signed for an absolute range of[-0.5, +0.5) rotations, [-180, +180) deg, etc."""

    initializationStrategy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sensor initialization strategy to use.This will impact the behavior the next time CANCoder boots up.

Pick the strategy on how to initialize the CANCoder's "Position" register.  Depending on the mechanism,
it may be desirable to auto set the Position register to match the Absolute Position(swerve for example).
Or it may be desired to zero the sensor on boot(drivetrain translation sensor or a relative servo).

TIP: Tuner's self-test feature will report what the boot sensor value will be in the event the CANCoder is reset."""

    magnetOffsetDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Adjusts the zero point for the absolute position register.
The absolute position of the sensor will always have a discontinuity (360 -> 0 deg) or (+180 -> -180)
and a hard-limited mechanism may have such a discontinuity in its functional range.
In which case use this config to move the discontinuity outside of the function range."""

    sensorCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scalar to multiply the CANCoder's native 12-bit resolute sensor. Defaults to 0.087890625 to produce degrees."""

    sensorDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Choose which direction is interpreted as positive displacement.
This affects both "Position"and "Absolute Position".
False(default) means positive rotation occurs when magnet
is spun counter - clockwise when observer is facing the LED side of CANCoder."""

    sensorTimeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired denominator to report velocity in. This impacts GetVelocityand the reported velocity in self-test in Tuner.
Default is "Per Second"."""

    unitString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String holding the unit to report in.  This impacts all routines(except for ConfigMagnetOffset) and the self-test in Tuner.
The string value itself is arbitrary.The max number of letters will depend on firmware versioning, but generally CANCoder
supports up to eight letters.However, common units such as "centimeters" are supported explicitly despite exceeding the eight-letter limit.
Default is "deg"""

    velocityMeasurementPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Velocity measurement period to use"""

    velocityMeasurementWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Velocity measurement window to use"""
