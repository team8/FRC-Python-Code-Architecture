# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class InvertType(__pybind11_builtins.pybind11_object):
    """
    Choose the invert type of the motor controller.
    None is the equivalent of SetInverted(false), where positive request yields positive voltage on M+.
    InvertMotorOutput is the equivelant of SetInverted(true), where positive request yields positive voltage on M-.
    FollowMaster/OpposeMaster will match/oppose a master Talon/Victor.  This requires device to be configured as a follower.
    
    Members:
    
      None_ : //!< Same as SetInverted(false)
    
      InvertMotorOutput : //!< Same as SetInverted(true)
    
      FollowMaster : //!< Follow the invert of the master this MC is following.
    
      OpposeMaster : //!< Opposite of the invert of the master this MC is following.
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
        """ __init__(self: ctre._ctre.InvertType, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.InvertType) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.InvertType, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    FollowMaster = InvertType.FollowMaster
    InvertMotorOutput = InvertType.InvertMotorOutput
    None_ = InvertType.None_
    OpposeMaster = InvertType.OpposeMaster
    __entries = {
        'FollowMaster': (
            InvertType.FollowMaster,
            '//!< Follow the invert of the master this MC is following.',
        ),
        'InvertMotorOutput': (
            InvertType.InvertMotorOutput,
            '//!< Same as SetInverted(true)',
        ),
        'None_': (
            InvertType.None_,
            '//!< Same as SetInverted(false)',
        ),
        'OpposeMaster': (
            InvertType.OpposeMaster,
            '//!< Opposite of the invert of the master this MC is following.',
        ),
    }
    __members__ = {
        'FollowMaster': InvertType.FollowMaster,
        'InvertMotorOutput': InvertType.InvertMotorOutput,
        'None_': InvertType.None_,
        'OpposeMaster': InvertType.OpposeMaster,
    }


