# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class PigeonIMU_StatusFrame(__pybind11_builtins.pybind11_object):
    """
    Enumerated type for status frame types.
    
    Members:
    
      PigeonIMU_CondStatus_1_General
    
      PigeonIMU_CondStatus_9_SixDeg_YPR
    
      PigeonIMU_CondStatus_6_SensorFusion
    
      PigeonIMU_CondStatus_11_GyroAccum
    
      PigeonIMU_CondStatus_2_GeneralCompass
    
      PigeonIMU_CondStatus_3_GeneralAccel
    
      PigeonIMU_CondStatus_10_SixDeg_Quat
    
      PigeonIMU_RawStatus_4_Mag
    
      PigeonIMU_BiasedStatus_2_Gyro
    
      PigeonIMU_BiasedStatus_4_Mag
    
      PigeonIMU_BiasedStatus_6_Accel
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
        """ __init__(self: ctre._ctre.PigeonIMU_StatusFrame, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.PigeonIMU_StatusFrame) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.PigeonIMU_StatusFrame, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    PigeonIMU_BiasedStatus_2_Gyro = PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_2_Gyro
    PigeonIMU_BiasedStatus_4_Mag = PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag
    PigeonIMU_BiasedStatus_6_Accel = PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_6_Accel
    PigeonIMU_CondStatus_10_SixDeg_Quat = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_10_SixDeg_Quat
    PigeonIMU_CondStatus_11_GyroAccum = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_11_GyroAccum
    PigeonIMU_CondStatus_1_General = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_1_General
    PigeonIMU_CondStatus_2_GeneralCompass = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_2_GeneralCompass
    PigeonIMU_CondStatus_3_GeneralAccel = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_3_GeneralAccel
    PigeonIMU_CondStatus_6_SensorFusion = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_6_SensorFusion
    PigeonIMU_CondStatus_9_SixDeg_YPR = PigeonIMU_StatusFrame.PigeonIMU_CondStatus_9_SixDeg_YPR
    PigeonIMU_RawStatus_4_Mag = PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag
    __entries = {
        'PigeonIMU_BiasedStatus_2_Gyro': (
            PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_2_Gyro,
            None,
        ),
        'PigeonIMU_BiasedStatus_4_Mag': (
            PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag,
            None,
        ),
        'PigeonIMU_BiasedStatus_6_Accel': (
            PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_6_Accel,
            None,
        ),
        'PigeonIMU_CondStatus_10_SixDeg_Quat': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_10_SixDeg_Quat,
            None,
        ),
        'PigeonIMU_CondStatus_11_GyroAccum': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_11_GyroAccum,
            None,
        ),
        'PigeonIMU_CondStatus_1_General': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_1_General,
            None,
        ),
        'PigeonIMU_CondStatus_2_GeneralCompass': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_2_GeneralCompass,
            None,
        ),
        'PigeonIMU_CondStatus_3_GeneralAccel': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_3_GeneralAccel,
            None,
        ),
        'PigeonIMU_CondStatus_6_SensorFusion': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_6_SensorFusion,
            None,
        ),
        'PigeonIMU_CondStatus_9_SixDeg_YPR': (
            PigeonIMU_StatusFrame.PigeonIMU_CondStatus_9_SixDeg_YPR,
            None,
        ),
        'PigeonIMU_RawStatus_4_Mag': '<value is a self-reference, replaced by this string>',
    }
    __members__ = {
        'PigeonIMU_BiasedStatus_2_Gyro': PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_2_Gyro,
        'PigeonIMU_BiasedStatus_4_Mag': PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag,
        'PigeonIMU_BiasedStatus_6_Accel': PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_6_Accel,
        'PigeonIMU_CondStatus_10_SixDeg_Quat': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_10_SixDeg_Quat,
        'PigeonIMU_CondStatus_11_GyroAccum': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_11_GyroAccum,
        'PigeonIMU_CondStatus_1_General': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_1_General,
        'PigeonIMU_CondStatus_2_GeneralCompass': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_2_GeneralCompass,
        'PigeonIMU_CondStatus_3_GeneralAccel': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_3_GeneralAccel,
        'PigeonIMU_CondStatus_6_SensorFusion': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_6_SensorFusion,
        'PigeonIMU_CondStatus_9_SixDeg_YPR': PigeonIMU_StatusFrame.PigeonIMU_CondStatus_9_SixDeg_YPR,
        'PigeonIMU_RawStatus_4_Mag': '<value is a self-reference, replaced by this string>',
    }


