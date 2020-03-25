# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class StatusFrameEnhanced(__pybind11_builtins.pybind11_object):
    """
    The different status frames available to enhanced motor controllers
    
    Members:
    
      Status_1_General : General Status
    
      Status_2_Feedback0 : Feedback for selected sensor on primary PID[0].
    
      Status_4_AinTempVbat : Analog sensor, motor controller
    temperature, and voltage at input leads
    
      Status_6_Misc : Miscellaneous signals
    
      Status_7_CommStatus : Communication status
    
      Status_9_MotProfBuffer : Motion profile buffer status
    
      Status_10_MotionMagic : Old name for Status 10.
    Use @see #Status_10_Targets instead.
    
      Status_10_Targets : Correct name for Status 10.
    Functionally equivalent to @see #Status_10_MotionMagic
    
      Status_12_Feedback1 : Feedback for selected sensor on aux PID[1].
    
      Status_13_Base_PIDF0 : Primary PID
    
      Status_14_Turn_PIDF1 : Auxiliary PID
    
      Status_15_FirmareApiStatus : Firmware & API status information
    
      Status_17_Targets1 : MotionProfile Targets for Auxiliary PID1.
    
      Status_3_Quadrature : Quadrature sensor
    
      Status_8_PulseWidth : Pulse width sensor
    
      Status_11_UartGadgeteer : Gadgeteer status
    
      Status_Brushless_Current : Brushless Current Status.
    Includes Stator and Supply Current for Talon FX.
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
        """ __init__(self: ctre._ctre.StatusFrameEnhanced, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.StatusFrameEnhanced) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.StatusFrameEnhanced, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Status_10_MotionMagic = StatusFrameEnhanced.Status_10_MotionMagic
    Status_10_Targets = StatusFrameEnhanced.Status_10_MotionMagic
    Status_11_UartGadgeteer = StatusFrameEnhanced.Status_11_UartGadgeteer
    Status_12_Feedback1 = StatusFrameEnhanced.Status_12_Feedback1
    Status_13_Base_PIDF0 = StatusFrameEnhanced.Status_13_Base_PIDF0
    Status_14_Turn_PIDF1 = StatusFrameEnhanced.Status_14_Turn_PIDF1
    Status_15_FirmareApiStatus = StatusFrameEnhanced.Status_15_FirmareApiStatus
    Status_17_Targets1 = StatusFrameEnhanced.Status_17_Targets1
    Status_1_General = StatusFrameEnhanced.Status_1_General
    Status_2_Feedback0 = StatusFrameEnhanced.Status_2_Feedback0
    Status_3_Quadrature = StatusFrameEnhanced.Status_3_Quadrature
    Status_4_AinTempVbat = StatusFrameEnhanced.Status_4_AinTempVbat
    Status_6_Misc = StatusFrameEnhanced.Status_6_Misc
    Status_7_CommStatus = StatusFrameEnhanced.Status_7_CommStatus
    Status_8_PulseWidth = StatusFrameEnhanced.Status_8_PulseWidth
    Status_9_MotProfBuffer = StatusFrameEnhanced.Status_9_MotProfBuffer
    Status_Brushless_Current = StatusFrameEnhanced.Status_Brushless_Current
    __entries = {
        'Status_10_MotionMagic': (
            StatusFrameEnhanced.Status_10_MotionMagic,
            'Old name for Status 10.\nUse @see #Status_10_Targets instead.',
        ),
        'Status_10_Targets': (
            '<value is a self-reference, replaced by this string>',
            'Correct name for Status 10.\nFunctionally equivalent to @see #Status_10_MotionMagic',
        ),
        'Status_11_UartGadgeteer': (
            StatusFrameEnhanced.Status_11_UartGadgeteer,
            'Gadgeteer status',
        ),
        'Status_12_Feedback1': (
            StatusFrameEnhanced.Status_12_Feedback1,
            'Feedback for selected sensor on aux PID[1].',
        ),
        'Status_13_Base_PIDF0': (
            StatusFrameEnhanced.Status_13_Base_PIDF0,
            'Primary PID',
        ),
        'Status_14_Turn_PIDF1': (
            StatusFrameEnhanced.Status_14_Turn_PIDF1,
            'Auxiliary PID',
        ),
        'Status_15_FirmareApiStatus': (
            StatusFrameEnhanced.Status_15_FirmareApiStatus,
            'Firmware & API status information',
        ),
        'Status_17_Targets1': (
            StatusFrameEnhanced.Status_17_Targets1,
            'MotionProfile Targets for Auxiliary PID1.',
        ),
        'Status_1_General': (
            StatusFrameEnhanced.Status_1_General,
            'General Status',
        ),
        'Status_2_Feedback0': (
            StatusFrameEnhanced.Status_2_Feedback0,
            'Feedback for selected sensor on primary PID[0].',
        ),
        'Status_3_Quadrature': (
            StatusFrameEnhanced.Status_3_Quadrature,
            'Quadrature sensor',
        ),
        'Status_4_AinTempVbat': (
            StatusFrameEnhanced.Status_4_AinTempVbat,
            'Analog sensor, motor controller\ntemperature, and voltage at input leads',
        ),
        'Status_6_Misc': (
            StatusFrameEnhanced.Status_6_Misc,
            'Miscellaneous signals',
        ),
        'Status_7_CommStatus': (
            StatusFrameEnhanced.Status_7_CommStatus,
            'Communication status',
        ),
        'Status_8_PulseWidth': (
            StatusFrameEnhanced.Status_8_PulseWidth,
            'Pulse width sensor',
        ),
        'Status_9_MotProfBuffer': (
            StatusFrameEnhanced.Status_9_MotProfBuffer,
            'Motion profile buffer status',
        ),
        'Status_Brushless_Current': (
            StatusFrameEnhanced.Status_Brushless_Current,
            'Brushless Current Status.\nIncludes Stator and Supply Current for Talon FX.',
        ),
    }
    __members__ = {
        'Status_10_MotionMagic': StatusFrameEnhanced.Status_10_MotionMagic,
        'Status_10_Targets': '<value is a self-reference, replaced by this string>',
        'Status_11_UartGadgeteer': StatusFrameEnhanced.Status_11_UartGadgeteer,
        'Status_12_Feedback1': StatusFrameEnhanced.Status_12_Feedback1,
        'Status_13_Base_PIDF0': StatusFrameEnhanced.Status_13_Base_PIDF0,
        'Status_14_Turn_PIDF1': StatusFrameEnhanced.Status_14_Turn_PIDF1,
        'Status_15_FirmareApiStatus': StatusFrameEnhanced.Status_15_FirmareApiStatus,
        'Status_17_Targets1': StatusFrameEnhanced.Status_17_Targets1,
        'Status_1_General': StatusFrameEnhanced.Status_1_General,
        'Status_2_Feedback0': StatusFrameEnhanced.Status_2_Feedback0,
        'Status_3_Quadrature': StatusFrameEnhanced.Status_3_Quadrature,
        'Status_4_AinTempVbat': StatusFrameEnhanced.Status_4_AinTempVbat,
        'Status_6_Misc': StatusFrameEnhanced.Status_6_Misc,
        'Status_7_CommStatus': StatusFrameEnhanced.Status_7_CommStatus,
        'Status_8_PulseWidth': StatusFrameEnhanced.Status_8_PulseWidth,
        'Status_9_MotProfBuffer': StatusFrameEnhanced.Status_9_MotProfBuffer,
        'Status_Brushless_Current': StatusFrameEnhanced.Status_Brushless_Current,
    }


