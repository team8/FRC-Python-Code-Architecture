class TalonFXFeedbackDevice():
    """
    Choose the feedback device for a Talon FX/Falcon 500.
    
    Members:
    
      IntegratedSensor : TalonFX supports an integrated sensor.
    
      SensorSum : Sum0 + Sum1
    
      SensorDifference : Diff0 - Diff1
    
      RemoteSensor0 : Sensor configured in RemoteFilter0
    
      RemoteSensor1 : Sensor configured in RemoteFilter1
    
      None_ : Position and velocity will read 0.
    
      SoftwareEmulatedSensor : Motor Controller will fake a sensor based on applied motor output.
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
        """ __init__(self: ctre._ctre.TalonFXFeedbackDevice, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.TalonFXFeedbackDevice) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.TalonFXFeedbackDevice, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    IntegratedSensor = TalonFXFeedbackDevice.IntegratedSensor
    None_ = TalonFXFeedbackDevice.None_
    RemoteSensor0 = TalonFXFeedbackDevice.RemoteSensor0
    RemoteSensor1 = TalonFXFeedbackDevice.RemoteSensor1
    SensorDifference = TalonFXFeedbackDevice.SensorDifference
    SensorSum = TalonFXFeedbackDevice.SensorSum
    SoftwareEmulatedSensor = TalonFXFeedbackDevice.SoftwareEmulatedSensor
    __entries = {
        'IntegratedSensor': (
            TalonFXFeedbackDevice.IntegratedSensor,
            'TalonFX supports an integrated sensor.',
        ),
        'None_': (
            TalonFXFeedbackDevice.None_,
            'Position and velocity will read 0.',
        ),
        'RemoteSensor0': (
            TalonFXFeedbackDevice.RemoteSensor0,
            'Sensor configured in RemoteFilter0',
        ),
        'RemoteSensor1': (
            TalonFXFeedbackDevice.RemoteSensor1,
            'Sensor configured in RemoteFilter1',
        ),
        'SensorDifference': (
            TalonFXFeedbackDevice.SensorDifference,
            'Diff0 - Diff1',
        ),
        'SensorSum': (
            TalonFXFeedbackDevice.SensorSum,
            'Sum0 + Sum1',
        ),
        'SoftwareEmulatedSensor': (
            TalonFXFeedbackDevice.SoftwareEmulatedSensor,
            'Motor Controller will fake a sensor based on applied motor output.',
        ),
    }
    __members__ = {
        'IntegratedSensor': TalonFXFeedbackDevice.IntegratedSensor,
        'None_': TalonFXFeedbackDevice.None_,
        'RemoteSensor0': TalonFXFeedbackDevice.RemoteSensor0,
        'RemoteSensor1': TalonFXFeedbackDevice.RemoteSensor1,
        'SensorDifference': TalonFXFeedbackDevice.SensorDifference,
        'SensorSum': TalonFXFeedbackDevice.SensorSum,
        'SoftwareEmulatedSensor': TalonFXFeedbackDevice.SoftwareEmulatedSensor,
    }
