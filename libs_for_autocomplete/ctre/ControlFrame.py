# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class ControlFrame(__pybind11_builtins.pybind11_object):
    """
    Control Frames for motor controllers
    
    Members:
    
      Control_3_General : Control
    
      Control_4_Advanced : Advanced Control
    
      Control_6_MotProfAddTrajPoint : Trajectory points
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
        """ __init__(self: ctre._ctre.ControlFrame, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.ControlFrame) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.ControlFrame, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Control_3_General = ControlFrame.Control_3_General
    Control_4_Advanced = ControlFrame.Control_4_Advanced
    Control_6_MotProfAddTrajPoint = ControlFrame.Control_6_MotProfAddTrajPoint
    __entries = {
        'Control_3_General': (
            ControlFrame.Control_3_General,
            'Control',
        ),
        'Control_4_Advanced': (
            ControlFrame.Control_4_Advanced,
            'Advanced Control',
        ),
        'Control_6_MotProfAddTrajPoint': (
            ControlFrame.Control_6_MotProfAddTrajPoint,
            'Trajectory points',
        ),
    }
    __members__ = {
        'Control_3_General': ControlFrame.Control_3_General,
        'Control_4_Advanced': ControlFrame.Control_4_Advanced,
        'Control_6_MotProfAddTrajPoint': ControlFrame.Control_6_MotProfAddTrajPoint,
    }
