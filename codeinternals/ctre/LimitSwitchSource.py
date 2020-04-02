# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class LimitSwitchSource(__pybind11_builtins.pybind11_object):
    """
    Limit switch source enum
    
    Members:
    
      FeedbackConnector : Limit switch directly connected to motor controller
    
      RemoteTalonSRX : Use Limit switch connected to TalonSRX on CAN
    
      RemoteCANifier : User Limit switch connected to CANifier
    
      Deactivated : Don't use a limit switch
    """

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.LimitSwitchSource, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.LimitSwitchSource) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.LimitSwitchSource, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Deactivated = LimitSwitchSource.Deactivated
    FeedbackConnector = LimitSwitchSource.FeedbackConnector
    RemoteCANifier = LimitSwitchSource.RemoteCANifier
    RemoteTalonSRX = LimitSwitchSource.RemoteTalonSRX
    __entries = {
        'Deactivated': (
            LimitSwitchSource.Deactivated,
            "Don't use a limit switch",
        ),
        'FeedbackConnector': (
            LimitSwitchSource.FeedbackConnector,
            'Limit switch directly connected to motor controller',
        ),
        'RemoteCANifier': (
            LimitSwitchSource.RemoteCANifier,
            'User Limit switch connected to CANifier',
        ),
        'RemoteTalonSRX': (
            LimitSwitchSource.RemoteTalonSRX,
            'Use Limit switch connected to TalonSRX on CAN',
        ),
    }
    __members__ = {
        'Deactivated': LimitSwitchSource.Deactivated,
        'FeedbackConnector': LimitSwitchSource.FeedbackConnector,
        'RemoteCANifier': LimitSwitchSource.RemoteCANifier,
        'RemoteTalonSRX': LimitSwitchSource.RemoteTalonSRX,
    }
