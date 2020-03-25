from codeinternals.ctre import BasePIDSetConfiguration


class VictorSPXPIDSetConfiguration(BasePIDSetConfiguration):
    """ Configurables available to VictorSPX's PID """
    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.VictorSPXPIDSetConfiguration) -> str
        
        
        
        :returns: String representation of all the configs
        
        2. toString(self: ctre._ctre.VictorSPXPIDSetConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: String representation of all the configs
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.VictorSPXPIDSetConfiguration) -> None """
        pass

    selectedFeedbackSensor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback device for a particular PID loop."""



