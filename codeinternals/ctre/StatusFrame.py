# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class StatusFrame(__pybind11_builtins.pybind11_object):
    """
    The different status frames available to motor controllers
    
    Members:
    
      Status_1_General_ : General Status
    
      Status_2_Feedback0_ : Main controller feedback
    
      Status_4_AinTempVbat_ : Analog sensor, motor controller
    temperature, and voltage at input leads
    
      Status_6_Misc_ : Miscellaneous signals
    
      Status_7_CommStatus_ : Communication status to controller
    
      Status_9_MotProfBuffer_ : Motion profile buffer status
    
      Status_10_MotionMagic_ : Old name for Status 10.
    Use @see #Status_10_Targets instead.
    
      Status_10_Targets_ : Correct name for Status 10.
    Functionally equivalent to @see #Status_10_MotionMagic
    
      Status_12_Feedback1_ : Secondary controller feedback
    
      Status_13_Base_PIDF0_ : Base PID
    
      Status_14_Turn_PIDF1_ : Auxiliary PID
    
      Status_15_FirmareApiStatus_ : Firmware & API status information
    
      Status_17_Targets1_ : MotionProfile Targets for Auxiliary PID1.
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
        """ __init__(self: ctre._ctre.StatusFrame, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.StatusFrame) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.StatusFrame, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Status_10_MotionMagic_ = StatusFrame.Status_10_MotionMagic_
    Status_10_Targets_ = StatusFrame.Status_10_MotionMagic_
    Status_12_Feedback1_ = StatusFrame.Status_12_Feedback1_
    Status_13_Base_PIDF0_ = StatusFrame.Status_13_Base_PIDF0_
    Status_14_Turn_PIDF1_ = StatusFrame.Status_14_Turn_PIDF1_
    Status_15_FirmareApiStatus_ = StatusFrame.Status_15_FirmareApiStatus_
    Status_17_Targets1_ = StatusFrame.Status_17_Targets1_
    Status_1_General_ = StatusFrame.Status_1_General_
    Status_2_Feedback0_ = StatusFrame.Status_2_Feedback0_
    Status_4_AinTempVbat_ = StatusFrame.Status_4_AinTempVbat_
    Status_6_Misc_ = StatusFrame.Status_6_Misc_
    Status_7_CommStatus_ = StatusFrame.Status_7_CommStatus_
    Status_9_MotProfBuffer_ = StatusFrame.Status_9_MotProfBuffer_
    __entries = {
        'Status_10_MotionMagic_': (
            StatusFrame.Status_10_MotionMagic_,
            'Old name for Status 10.\nUse @see #Status_10_Targets instead.',
        ),
        'Status_10_Targets_': (
            '<value is a self-reference, replaced by this string>',
            'Correct name for Status 10.\nFunctionally equivalent to @see #Status_10_MotionMagic',
        ),
        'Status_12_Feedback1_': (
            StatusFrame.Status_12_Feedback1_,
            'Secondary controller feedback',
        ),
        'Status_13_Base_PIDF0_': (
            StatusFrame.Status_13_Base_PIDF0_,
            'Base PID',
        ),
        'Status_14_Turn_PIDF1_': (
            StatusFrame.Status_14_Turn_PIDF1_,
            'Auxiliary PID',
        ),
        'Status_15_FirmareApiStatus_': (
            StatusFrame.Status_15_FirmareApiStatus_,
            'Firmware & API status information',
        ),
        'Status_17_Targets1_': (
            StatusFrame.Status_17_Targets1_,
            'MotionProfile Targets for Auxiliary PID1.',
        ),
        'Status_1_General_': (
            StatusFrame.Status_1_General_,
            'General Status',
        ),
        'Status_2_Feedback0_': (
            StatusFrame.Status_2_Feedback0_,
            'Main controller feedback',
        ),
        'Status_4_AinTempVbat_': (
            StatusFrame.Status_4_AinTempVbat_,
            'Analog sensor, motor controller\ntemperature, and voltage at input leads',
        ),
        'Status_6_Misc_': (
            StatusFrame.Status_6_Misc_,
            'Miscellaneous signals',
        ),
        'Status_7_CommStatus_': (
            StatusFrame.Status_7_CommStatus_,
            'Communication status to controller',
        ),
        'Status_9_MotProfBuffer_': (
            StatusFrame.Status_9_MotProfBuffer_,
            'Motion profile buffer status',
        ),
    }
    __members__ = {
        'Status_10_MotionMagic_': StatusFrame.Status_10_MotionMagic_,
        'Status_10_Targets_': '<value is a self-reference, replaced by this string>',
        'Status_12_Feedback1_': StatusFrame.Status_12_Feedback1_,
        'Status_13_Base_PIDF0_': StatusFrame.Status_13_Base_PIDF0_,
        'Status_14_Turn_PIDF1_': StatusFrame.Status_14_Turn_PIDF1_,
        'Status_15_FirmareApiStatus_': StatusFrame.Status_15_FirmareApiStatus_,
        'Status_17_Targets1_': StatusFrame.Status_17_Targets1_,
        'Status_1_General_': StatusFrame.Status_1_General_,
        'Status_2_Feedback0_': StatusFrame.Status_2_Feedback0_,
        'Status_4_AinTempVbat_': StatusFrame.Status_4_AinTempVbat_,
        'Status_6_Misc_': StatusFrame.Status_6_Misc_,
        'Status_7_CommStatus_': StatusFrame.Status_7_CommStatus_,
        'Status_9_MotProfBuffer_': StatusFrame.Status_9_MotProfBuffer_,
    }


