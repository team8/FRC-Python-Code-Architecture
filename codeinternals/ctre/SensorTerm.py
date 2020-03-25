# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class SensorTerm(__pybind11_builtins.pybind11_object):
    """
    Choose the sensor term for a motor controller
    
    Members:
    
      Sum0 : Choose Sum0 for a term
    
      Sum1 : Choose Sum1 for a term
    
      Diff0 : Choose Diff0 for a term
    
      Diff1 : Choose Diff1 for a term
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
        """ __init__(self: ctre._ctre.SensorTerm, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.SensorTerm) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.SensorTerm, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Diff0 = SensorTerm.Diff0
    Diff1 = SensorTerm.Diff1
    Sum0 = SensorTerm.Sum0
    Sum1 = SensorTerm.Sum1
    __entries = {
        'Diff0': (
            SensorTerm.Diff0,
            'Choose Diff0 for a term',
        ),
        'Diff1': (
            SensorTerm.Diff1,
            'Choose Diff1 for a term',
        ),
        'Sum0': (
            SensorTerm.Sum0,
            'Choose Sum0 for a term',
        ),
        'Sum1': (
            SensorTerm.Sum1,
            'Choose Sum1 for a term',
        ),
    }
    __members__ = {
        'Diff0': SensorTerm.Diff0,
        'Diff1': SensorTerm.Diff1,
        'Sum0': SensorTerm.Sum0,
        'Sum1': SensorTerm.Sum1,
    }


