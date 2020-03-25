# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class SensorInitializationStrategy(__pybind11_builtins.pybind11_object):
    """
    Enum for how CANCoder should initialize its position register on boot.
    
    Members:
    
      BootToZero : On boot up, set position to zero.
    
      BootToAbsolutePosition : On boot up, sync to the Absolute Position signal.  The Absolute position signal will be signed according to the selected Absolute Sensor Range.
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
        """ __init__(self: ctre._ctre.SensorInitializationStrategy, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.SensorInitializationStrategy) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.SensorInitializationStrategy, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    BootToAbsolutePosition = SensorInitializationStrategy.BootToAbsolutePosition
    BootToZero = SensorInitializationStrategy.BootToZero
    __entries = {
        'BootToAbsolutePosition': (
            SensorInitializationStrategy.BootToAbsolutePosition,
            'On boot up, sync to the Absolute Position signal.  The Absolute position signal will be signed according to the selected Absolute Sensor Range.',
        ),
        'BootToZero': (
            SensorInitializationStrategy.BootToZero,
            'On boot up, set position to zero.',
        ),
    }
    __members__ = {
        'BootToAbsolutePosition': SensorInitializationStrategy.BootToAbsolutePosition,
        'BootToZero': SensorInitializationStrategy.BootToZero,
    }


