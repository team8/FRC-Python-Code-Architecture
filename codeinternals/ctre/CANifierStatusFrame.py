# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class CANifierStatusFrame(__pybind11_builtins.pybind11_object):
    """
    Enumerated type for status frame types.
    
    Members:
    
      Status_1_General
    
      Status_2_General
    
      Status_3_PwmInputs0
    
      Status_4_PwmInputs1
    
      Status_5_PwmInputs2
    
      Status_6_PwmInputs3
    
      Status_8_Misc
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
        """ __init__(self: ctre._ctre.CANifierStatusFrame, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.CANifierStatusFrame) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.CANifierStatusFrame, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Status_1_General = CANifierStatusFrame.Status_1_General
    Status_2_General = CANifierStatusFrame.Status_2_General
    Status_3_PwmInputs0 = CANifierStatusFrame.Status_3_PwmInputs0
    Status_4_PwmInputs1 = CANifierStatusFrame.Status_4_PwmInputs1
    Status_5_PwmInputs2 = CANifierStatusFrame.Status_5_PwmInputs2
    Status_6_PwmInputs3 = CANifierStatusFrame.Status_6_PwmInputs3
    Status_8_Misc = CANifierStatusFrame.Status_8_Misc
    __entries = {
        'Status_1_General': (
            CANifierStatusFrame.Status_1_General,
            None,
        ),
        'Status_2_General': (
            CANifierStatusFrame.Status_2_General,
            None,
        ),
        'Status_3_PwmInputs0': (
            CANifierStatusFrame.Status_3_PwmInputs0,
            None,
        ),
        'Status_4_PwmInputs1': (
            CANifierStatusFrame.Status_4_PwmInputs1,
            None,
        ),
        'Status_5_PwmInputs2': (
            CANifierStatusFrame.Status_5_PwmInputs2,
            None,
        ),
        'Status_6_PwmInputs3': (
            CANifierStatusFrame.Status_6_PwmInputs3,
            None,
        ),
        'Status_8_Misc': (
            CANifierStatusFrame.Status_8_Misc,
            None,
        ),
    }
    __members__ = {
        'Status_1_General': CANifierStatusFrame.Status_1_General,
        'Status_2_General': CANifierStatusFrame.Status_2_General,
        'Status_3_PwmInputs0': CANifierStatusFrame.Status_3_PwmInputs0,
        'Status_4_PwmInputs1': CANifierStatusFrame.Status_4_PwmInputs1,
        'Status_5_PwmInputs2': CANifierStatusFrame.Status_5_PwmInputs2,
        'Status_6_PwmInputs3': CANifierStatusFrame.Status_6_PwmInputs3,
        'Status_8_Misc': CANifierStatusFrame.Status_8_Misc,
    }


