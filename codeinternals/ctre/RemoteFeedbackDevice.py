# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class RemoteFeedbackDevice(__pybind11_builtins.pybind11_object):
    """
    Choose the remote feedback device for a motor controller.
    
    Members:
    
      FactoryDefaultOff : [[deprecated("Use None instead.")]]
    Factory default setting for non-enhanced motor controllers
    
      SensorSum : Use Sum0 + Sum1
    
      SensorDifference : Use Diff0 - Diff1
    
      RemoteSensor0 : Use the sensor configured
    in filter0
    
      RemoteSensor1 : Use the sensor configured
    in filter1
    
      None_ : Position and velocity will read 0.
    
      SoftwareEmulatedSensor : Motor Controller will fake a sensor based on applied motor output.
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
        """ __init__(self: ctre._ctre.RemoteFeedbackDevice, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.RemoteFeedbackDevice) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.RemoteFeedbackDevice, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    FactoryDefaultOff = RemoteFeedbackDevice.FactoryDefaultOff
    None_ = RemoteFeedbackDevice.None_
    RemoteSensor0 = RemoteFeedbackDevice.RemoteSensor0
    RemoteSensor1 = RemoteFeedbackDevice.RemoteSensor1
    SensorDifference = RemoteFeedbackDevice.SensorDifference
    SensorSum = RemoteFeedbackDevice.SensorSum
    SoftwareEmulatedSensor = RemoteFeedbackDevice.SoftwareEmulatedSensor
    __entries = {
        'FactoryDefaultOff': (
            RemoteFeedbackDevice.FactoryDefaultOff,
            '[[deprecated("Use None instead.")]]\nFactory default setting for non-enhanced motor controllers',
        ),
        'None_': (
            RemoteFeedbackDevice.None_,
            'Position and velocity will read 0.',
        ),
        'RemoteSensor0': (
            RemoteFeedbackDevice.RemoteSensor0,
            'Use the sensor configured\nin filter0',
        ),
        'RemoteSensor1': (
            RemoteFeedbackDevice.RemoteSensor1,
            'Use the sensor configured\nin filter1',
        ),
        'SensorDifference': (
            RemoteFeedbackDevice.SensorDifference,
            'Use Diff0 - Diff1',
        ),
        'SensorSum': (
            RemoteFeedbackDevice.SensorSum,
            'Use Sum0 + Sum1',
        ),
        'SoftwareEmulatedSensor': (
            RemoteFeedbackDevice.SoftwareEmulatedSensor,
            'Motor Controller will fake a sensor based on applied motor output.',
        ),
    }
    __members__ = {
        'FactoryDefaultOff': RemoteFeedbackDevice.FactoryDefaultOff,
        'None_': RemoteFeedbackDevice.None_,
        'RemoteSensor0': RemoteFeedbackDevice.RemoteSensor0,
        'RemoteSensor1': RemoteFeedbackDevice.RemoteSensor1,
        'SensorDifference': RemoteFeedbackDevice.SensorDifference,
        'SensorSum': RemoteFeedbackDevice.SensorSum,
        'SoftwareEmulatedSensor': RemoteFeedbackDevice.SoftwareEmulatedSensor,
    }


