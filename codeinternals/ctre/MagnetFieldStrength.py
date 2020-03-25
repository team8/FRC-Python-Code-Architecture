# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class MagnetFieldStrength(__pybind11_builtins.pybind11_object):
    """
    Indicates the magnet field strength of a magnet-based sensor
    
    Members:
    
      Invalid_Unknown : Magnet Field strength cannot be determined
    
      BadRange_RedLED : Magnet field is far too low (too far) or far too high (too close).
    
      Adequate_OrangeLED : Magnet field is adequate, sensor can be used in this range with slightly reduced accuracy.
    
      Good_GreenLED : Magnet field is ideal
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.MagnetFieldStrength, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.MagnetFieldStrength) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.MagnetFieldStrength, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Adequate_OrangeLED = MagnetFieldStrength.Adequate_OrangeLED
    BadRange_RedLED = MagnetFieldStrength.BadRange_RedLED
    Good_GreenLED = MagnetFieldStrength.Good_GreenLED
    Invalid_Unknown = MagnetFieldStrength.Invalid_Unknown
    __entries = {
        'Adequate_OrangeLED': (
            MagnetFieldStrength.Adequate_OrangeLED,
            'Magnet field is adequate, sensor can be used in this range with slightly reduced accuracy.',
        ),
        'BadRange_RedLED': (
            MagnetFieldStrength.BadRange_RedLED,
            'Magnet field is far too low (too far) or far too high (too close).',
        ),
        'Good_GreenLED': (
            MagnetFieldStrength.Good_GreenLED,
            'Magnet field is ideal',
        ),
        'Invalid_Unknown': (
            MagnetFieldStrength.Invalid_Unknown,
            'Magnet Field strength cannot be determined',
        ),
    }
    __members__ = {
        'Adequate_OrangeLED': MagnetFieldStrength.Adequate_OrangeLED,
        'BadRange_RedLED': MagnetFieldStrength.BadRange_RedLED,
        'Good_GreenLED': MagnetFieldStrength.Good_GreenLED,
        'Invalid_Unknown': MagnetFieldStrength.Invalid_Unknown,
    }


