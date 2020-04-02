from codeinternals.ctre import BaseMotorControllerConfiguration


class VictorSPXConfiguration(BaseMotorControllerConfiguration):
    """ Configurables available to VictorSPX """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.VictorSPXConfiguration) -> str
        
        
        
        :returns: String representation of all the configs
        
        2. toString(self: ctre._ctre.VictorSPXConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: String representation of all the configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.VictorSPXConfiguration) -> None """
        pass

    auxiliaryPID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Auxiliary PID configuration"""

    diff0Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Diff 0 Term"""

    diff1Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Diff 1 Term"""

    forwardLimitSwitchDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward limit switch device ID

Limit Switch device id isn't used unless device is a remote"""

    forwardLimitSwitchNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward limit switch normally open/closed"""

    forwardLimitSwitchSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward Limit Switch Source

User can choose between the feedback connector, remote Talon SRX, CANifier, or deactivate the feature"""

    primaryPID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Primary PID configuration"""

    reverseLimitSwitchDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse limit switch device ID

Limit Switch device id isn't used unless device is a remote"""

    reverseLimitSwitchNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse limit switch normally open/closed"""

    reverseLimitSwitchSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse Limit Switch Source

User can choose between the feedback connector, remote Talon SRX, CANifier, or deactivate the feature"""

    sum0Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Sum 0 Term"""

    sum1Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Sum 1 Term"""
