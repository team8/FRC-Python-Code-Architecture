# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class CANCoderStickyFaults(__pybind11_builtins.pybind11_object):
    """ Sticky Faults for CANCoder (Currently has none) """

    def hasAnyFault(self):  # real signature unknown; restored from __doc__
        """
        hasAnyFault(self: ctre._ctre.CANCoderStickyFaults) -> bool
        
        
        
        :returns: true if any faults are tripped
        """
        return False

    def toBitfield(self):  # real signature unknown; restored from __doc__
        """
        toBitfield(self: ctre._ctre.CANCoderStickyFaults) -> int
        
        
        
        :returns: Current fault list as a bit field
        """
        return 0

    def update(self, bits):  # real signature unknown; restored from __doc__
        """
        update(self: ctre._ctre.CANCoderStickyFaults, bits: int) -> None
        
        Updates current fault list with specified bit field of faults
        
        :param bits: bit field of faults to update with
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.CANCoderStickyFaults, bits: int) -> None
        
        Updates current fault list with specified bit field of faults
        
        :param bits: bit field of faults to update with
        
        2. __init__(self: ctre._ctre.CANCoderStickyFaults) -> None
        """
        pass

    APIError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """API error detected.  Make sure API and firmware versions are compatible."""

    HardwareFault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device detects hardware failure"""

    MagnetTooWeak = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Magnet strength is too weak to provide reliable results
Make sure CANCoder is close to the magnet being used"""

    ResetDuringEn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device was powered-on or reset while robot is enabled.
Check your breakers and wiring."""

    UnderVoltage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device is under 6.5V"""
