# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class RemoteLimitSwitchSource(__pybind11_builtins.pybind11_object):
    """
    Remote Limit switch source enum
    
    Members:
    
      FactoryDefaultOff : Don't use limit switch, this is the factory default value
    
      RemoteTalonSRX : Use Limit switch connected to TalonSRX on CAN
    
      RemoteCANifier : User Limit switch connected to CANifier
    
      Deactivated : Don't use a limit switch
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
        """ __init__(self: ctre._ctre.RemoteLimitSwitchSource, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.RemoteLimitSwitchSource) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.RemoteLimitSwitchSource, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Deactivated = RemoteLimitSwitchSource.Deactivated
    FactoryDefaultOff = RemoteLimitSwitchSource.FactoryDefaultOff
    RemoteCANifier = RemoteLimitSwitchSource.RemoteCANifier
    RemoteTalonSRX = RemoteLimitSwitchSource.RemoteTalonSRX
    __entries = {
        'Deactivated': (
            RemoteLimitSwitchSource.Deactivated,
            "Don't use a limit switch",
        ),
        'FactoryDefaultOff': (
            RemoteLimitSwitchSource.FactoryDefaultOff,
            "Don't use limit switch, this is the factory default value",
        ),
        'RemoteCANifier': (
            RemoteLimitSwitchSource.RemoteCANifier,
            'User Limit switch connected to CANifier',
        ),
        'RemoteTalonSRX': (
            RemoteLimitSwitchSource.RemoteTalonSRX,
            'Use Limit switch connected to TalonSRX on CAN',
        ),
    }
    __members__ = {
        'Deactivated': RemoteLimitSwitchSource.Deactivated,
        'FactoryDefaultOff': RemoteLimitSwitchSource.FactoryDefaultOff,
        'RemoteCANifier': RemoteLimitSwitchSource.RemoteCANifier,
        'RemoteTalonSRX': RemoteLimitSwitchSource.RemoteTalonSRX,
    }


