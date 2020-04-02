# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class FeedbackDevice(__pybind11_builtins.pybind11_object):
    """
    Choose the feedback device for a motor controller.
    Consult product specific documentation to determine what is available/supported.
    
    Members:
    
      QuadEncoder : Quadrature encoder
    
      IntegratedSensor : TalonFX supports an integrated sensor.
    
      Analog : Analog potentiometer/encoder
    
      Tachometer : Tachometer
    
      PulseWidthEncodedPosition : CTRE Mag Encoder in Relative mode or
    any other device that uses PWM to encode its output
    
      SensorSum : Sum0 + Sum1
    
      SensorDifference : Diff0 - Diff1
    
      RemoteSensor0 : Sensor configured in RemoteFilter0
    
      RemoteSensor1 : Sensor configured in RemoteFilter1
    
      None_ : Position and velocity will read 0.
    
      SoftwareEmulatedSensor : Motor Controller will fake a sensor based on applied motor output.
    
      CTRE_MagEncoder_Absolute : CTR mag encoder configured in absolute, is the same
    as a PWM sensor.
    
      CTRE_MagEncoder_Relative : CTR mag encoder configured in relative, is the same
    as an quadrature encoder sensor.
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
        """ __init__(self: ctre._ctre.FeedbackDevice, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.FeedbackDevice) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.FeedbackDevice, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Analog = FeedbackDevice.Analog
    CTRE_MagEncoder_Absolute = FeedbackDevice.PulseWidthEncodedPosition
    CTRE_MagEncoder_Relative = FeedbackDevice.QuadEncoder
    IntegratedSensor = FeedbackDevice.IntegratedSensor
    None_ = FeedbackDevice.None_
    PulseWidthEncodedPosition = FeedbackDevice.PulseWidthEncodedPosition
    QuadEncoder = FeedbackDevice.QuadEncoder
    RemoteSensor0 = FeedbackDevice.RemoteSensor0
    RemoteSensor1 = FeedbackDevice.RemoteSensor1
    SensorDifference = FeedbackDevice.SensorDifference
    SensorSum = FeedbackDevice.SensorSum
    SoftwareEmulatedSensor = FeedbackDevice.SoftwareEmulatedSensor
    Tachometer = FeedbackDevice.Tachometer
    __entries = {
        'Analog': (
            FeedbackDevice.Analog,
            'Analog potentiometer/encoder',
        ),
        'CTRE_MagEncoder_Absolute': (
            FeedbackDevice.PulseWidthEncodedPosition,
            'CTR mag encoder configured in absolute, is the same\nas a PWM sensor.',
        ),
        'CTRE_MagEncoder_Relative': (
            FeedbackDevice.QuadEncoder,
            'CTR mag encoder configured in relative, is the same\nas an quadrature encoder sensor.',
        ),
        'IntegratedSensor': (
            FeedbackDevice.IntegratedSensor,
            'TalonFX supports an integrated sensor.',
        ),
        'None_': (
            FeedbackDevice.None_,
            'Position and velocity will read 0.',
        ),
        'PulseWidthEncodedPosition': (
            '<value is a self-reference, replaced by this string>',
            'CTRE Mag Encoder in Relative mode or\nany other device that uses PWM to encode its output',
        ),
        'QuadEncoder': (
            '<value is a self-reference, replaced by this string>',
            'Quadrature encoder',
        ),
        'RemoteSensor0': (
            FeedbackDevice.RemoteSensor0,
            'Sensor configured in RemoteFilter0',
        ),
        'RemoteSensor1': (
            FeedbackDevice.RemoteSensor1,
            'Sensor configured in RemoteFilter1',
        ),
        'SensorDifference': (
            FeedbackDevice.SensorDifference,
            'Diff0 - Diff1',
        ),
        'SensorSum': (
            FeedbackDevice.SensorSum,
            'Sum0 + Sum1',
        ),
        'SoftwareEmulatedSensor': (
            FeedbackDevice.SoftwareEmulatedSensor,
            'Motor Controller will fake a sensor based on applied motor output.',
        ),
        'Tachometer': (
            FeedbackDevice.Tachometer,
            'Tachometer',
        ),
    }
    __members__ = {
        'Analog': FeedbackDevice.Analog,
        'CTRE_MagEncoder_Absolute': FeedbackDevice.PulseWidthEncodedPosition,
        'CTRE_MagEncoder_Relative': FeedbackDevice.QuadEncoder,
        'IntegratedSensor': FeedbackDevice.IntegratedSensor,
        'None_': FeedbackDevice.None_,
        'PulseWidthEncodedPosition': '<value is a self-reference, replaced by this string>',
        'QuadEncoder': '<value is a self-reference, replaced by this string>',
        'RemoteSensor0': FeedbackDevice.RemoteSensor0,
        'RemoteSensor1': FeedbackDevice.RemoteSensor1,
        'SensorDifference': FeedbackDevice.SensorDifference,
        'SensorSum': FeedbackDevice.SensorSum,
        'SoftwareEmulatedSensor': FeedbackDevice.SoftwareEmulatedSensor,
        'Tachometer': FeedbackDevice.Tachometer,
    }
