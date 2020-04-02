# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class LimitSwitchNormal(__pybind11_builtins.pybind11_object):
    """
    Choose whether the limit switch is normally
    open or normally closed
    
    Members:
    
      NormallyOpen : Limit Switch is tripped when
    the circuit is closed
    
      NormallyClosed : Limit Switch is tripped when
    the circuit is open
    
      Disabled : Limit switch is disabled
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
        """ __init__(self: ctre._ctre.LimitSwitchNormal, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.LimitSwitchNormal) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.LimitSwitchNormal, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Disabled = LimitSwitchNormal.Disabled
    NormallyClosed = LimitSwitchNormal.NormallyClosed
    NormallyOpen = LimitSwitchNormal.NormallyOpen
    __entries = {
        'Disabled': (
            LimitSwitchNormal.Disabled,
            'Limit switch is disabled',
        ),
        'NormallyClosed': (
            LimitSwitchNormal.NormallyClosed,
            'Limit Switch is tripped when\nthe circuit is open',
        ),
        'NormallyOpen': (
            LimitSwitchNormal.NormallyOpen,
            'Limit Switch is tripped when\nthe circuit is closed',
        ),
    }
    __members__ = {
        'Disabled': LimitSwitchNormal.Disabled,
        'NormallyClosed': LimitSwitchNormal.NormallyClosed,
        'NormallyOpen': LimitSwitchNormal.NormallyOpen,
    }
