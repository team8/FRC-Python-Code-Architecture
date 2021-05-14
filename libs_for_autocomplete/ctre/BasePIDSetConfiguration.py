class BasePIDSetConfiguration():
    """ Base set of configurables related to PID """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.BasePIDSetConfiguration) -> str
        
        
        
        :returns: String representation of configs
        
        2. toString(self: ctre._ctre.BasePIDSetConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BasePIDSetConfiguration) -> None """
        pass

    selectedFeedbackCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback coefficient of selected sensor"""
