# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports

from .CustomParamConfiguration import CustomParamConfiguration


class CANifierConfiguration(CustomParamConfiguration):
    """ Configurables available to CANifier """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.CANifierConfiguration) -> str
        
        
        
        :returns: String representation of configs
        
        2. toString(self: ctre._ctre.CANifierConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.CANifierConfiguration) -> None """
        pass

    clearPositionOnLimitF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to clear sensor position on forward limit"""

    clearPositionOnLimitR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to clear sensor position on reverse limit"""

    clearPositionOnQuadIdx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to clear sensor position on index"""

    velocityMeasurementPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Velocity measurement period to use"""

    velocityMeasurementWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Velocity measurement window to use"""
