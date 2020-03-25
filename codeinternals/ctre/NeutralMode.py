# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class NeutralMode(__pybind11_builtins.pybind11_object):
    """
    Choose the neutral mode for a motor controller
    
    Members:
    
      EEPROMSetting : Use the NeutralMode that is set in the MC's persistent storage.
    
      Coast : When commanded to neutral, motor leads are set to high-impedance, allowing mechanism to coast.
    
      Brake : When commanded to neutral, motor leads are commonized electrically to reduce motion.
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
        """ __init__(self: ctre._ctre.NeutralMode, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.NeutralMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.NeutralMode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Brake = NeutralMode.Brake
    Coast = NeutralMode.Coast
    EEPROMSetting = NeutralMode.EEPROMSetting
    __entries = {
        'Brake': (
            NeutralMode.Brake,
            'When commanded to neutral, motor leads are commonized electrically to reduce motion.',
        ),
        'Coast': (
            NeutralMode.Coast,
            'When commanded to neutral, motor leads are set to high-impedance, allowing mechanism to coast.',
        ),
        'EEPROMSetting': (
            NeutralMode.EEPROMSetting,
            "Use the NeutralMode that is set in the MC's persistent storage.",
        ),
    }
    __members__ = {
        'Brake': NeutralMode.Brake,
        'Coast': NeutralMode.Coast,
        'EEPROMSetting': NeutralMode.EEPROMSetting,
    }


