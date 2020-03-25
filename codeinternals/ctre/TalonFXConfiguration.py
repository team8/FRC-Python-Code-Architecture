
from .BaseTalonConfiguration import BaseTalonConfiguration

class TalonFXConfiguration(BaseTalonConfiguration):
    """ Configurables available to TalonFX """
    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.TalonFXConfiguration) -> str
        
        
        
        :returns: String representation of all the configs
        
        2. toString(self: ctre._ctre.TalonFXConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: String representation of all the configs
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.TalonFXConfiguration) -> None """
        pass

    absoluteSensorRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired Sign / Range for the absolute position register.
Choose unsigned for an absolute range of[0, +1) rotations, [0, 360) deg, etc.
Choose signed for an absolute range of[-0.5, +0.5) rotations, [-180, +180) deg, etc."""

    initializationStrategy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sensor initialization strategy to use.This will impact the behavior the next time device boots up.

Pick the strategy on how to initialize the "Position" register.  Depending on the mechanism,
it may be desirable to auto set the Position register to match the Absolute Position(swerve for example).
Or it may be desired to zero the sensor on boot(drivetrain translation sensor or a relative servo).

TIP: Tuner's self-test feature will report what the boot sensor value will be in the event the device is reset."""

    integratedSensorOffsetDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Adjusts the zero point for the absolute position register.
The absolute position of the sensor will always have a discontinuity (360 -> 0 deg) or (+180 -> -180)
and a hard-limited mechanism may have such a discontinuity in its functional range.
In which case use this config to move the discontinuity outside of the function range."""

    motorCommutation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Choose the type of motor commutation."""

    statorCurrLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stator-side current limiting.  This is typically used to limit acceleration/torque and heat generation."""

    supplyCurrLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Supply-side current limiting.  This is typically used to prevent breakers from tripping."""



