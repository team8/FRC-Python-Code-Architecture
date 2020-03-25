# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class StatorCurrentLimitConfiguration(__pybind11_builtins.pybind11_object):
    """ Describes the desired stator current limiting behavior. """
    def deserialize(self, doubles, doubleCnt): # real signature unknown; restored from __doc__
        """ deserialize(self: ctre._ctre.StatorCurrentLimitConfiguration, doubles: float, doubleCnt: int) -> None """
        pass

    def equals(self, rhs): # real signature unknown; restored from __doc__
        """ equals(self: ctre._ctre.StatorCurrentLimitConfiguration, rhs: ctre._ctre.StatorCurrentLimitConfiguration) -> bool """
        return False

    def toArray(self): # real signature unknown; restored from __doc__
        """ toArray(self: ctre._ctre.StatorCurrentLimitConfiguration) -> List[float] """
        return []

    def toString(self): # real signature unknown; restored from __doc__
        """
        toString(self: ctre._ctre.StatorCurrentLimitConfiguration) -> str
        
        
        
        :returns: string representation of current faults tripped
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.StatorCurrentLimitConfiguration) -> None
        
        Default c'tor.  Because currentLimit is zero, limiting id disabled.
        
        2. __init__(self: ctre._ctre.StatorCurrentLimitConfiguration, doubleArray: float, doubleArraySz: int) -> None
        
        3. __init__(self: ctre._ctre.StatorCurrentLimitConfiguration, enable: bool, currentLimit: float, triggerThresholdCurrent: float, triggerThresholdTime: float) -> None
        """
        pass

    currentLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The "holding" current (amperes) to limit to when feature is activated."""

    enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True/False to enable/disable limit feature."""

    triggerThresholdCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current must exceed this threshold (amperes) before limiting occurs.
If this value is less than currentLimit, then currentLimit is used as the threshold."""

    triggerThresholdTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How long current must exceed threshold (seconds) before limiting occurs."""



