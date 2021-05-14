from .BaseTalonConfiguration import BaseTalonConfiguration


class TalonSRXConfiguration(BaseTalonConfiguration):
    """ Configurables available to TalonSRX """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.TalonSRXConfiguration) -> str
        
        
        
        :returns: String representation of all the configs
        
        2. toString(self: ctre._ctre.TalonSRXConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: String representation of all the configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.TalonSRXConfiguration) -> None """
        pass

    continuousCurrentLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Continuous current in amps

Current limit is activated when current exceeds the peak limit for longer
than the peak duration. Then software will limit to the continuous limit.
This ensures current limiting while allowing for momentary excess current
events."""

    peakCurrentDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Peak Current duration in milliseconds

Current limit is activated when current exceeds the peak limit for longer
than the peak duration. Then software will limit to the continuous limit.
This ensures current limiting while allowing for momentary excess current
events."""

    peakCurrentLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Peak current in amps

Current limit is activated when current exceeds the peak limit for longer
than the peak duration. Then software will limit to the continuous limit.
This ensures current limiting while allowing for momentary excess current
events."""
