# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class StickyFaults(__pybind11_builtins.pybind11_object):
    """ All the sticky faults available to motor controllers """

    def hasAnyFault(self):  # real signature unknown; restored from __doc__
        """
        hasAnyFault(self: ctre._ctre.StickyFaults) -> bool
        
        
        
        :returns: true if any faults are tripped
        """
        return False

    def toBitfield(self):  # real signature unknown; restored from __doc__
        """
        toBitfield(self: ctre._ctre.StickyFaults) -> int
        
        
        
        :returns: Current fault list as a bit field
        """
        return 0

    def toString(self):  # real signature unknown; restored from __doc__
        """
        toString(self: ctre._ctre.StickyFaults) -> str
        
        
        
        :returns: string representation of current faults tripped
        """
        return ""

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.StickyFaults, bits: int) -> None
        
        Creates fault list with specified bit field of faults
        
        :param bits: bit field of faults to update with
        
        2. __init__(self: ctre._ctre.StickyFaults) -> None
        """
        pass

    APIError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device detects an API error"""

    ForwardLimitSwitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward limit switch is tripped and device is trying to go forward
Only trips when the device is limited"""

    ForwardSoftLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sensor is beyond forward soft limit and device is trying to go forward
Only trips when the device is limited"""

    HardwareESDReset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used, @see #ResetDuringEn"""

    RemoteLossOfSignal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Remote Sensor is no longer detected on bus"""

    ResetDuringEn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device was powered-on or reset while robot is enabled.
Check your breakers and wiring."""

    ReverseLimitSwitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse limit switch is tripped and device is trying to go reverse
Only trips when the device is limited"""

    ReverseSoftLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sensor is beyond reverse soft limit and device is trying to go reverse
Only trips when the device is limited"""

    SensorOutOfPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device detects its sensor is out of phase"""

    SensorOverflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device's sensor overflowed"""

    SupplyOverV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Supply is well above the rated voltage of the hardware. This fault is specific to Brushless."""

    SupplyUnstable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Supply is rapidly fluctuating and unstable. This fault is specific to Brushless."""

    UnderVoltage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Motor Controller is under 6.5V"""
