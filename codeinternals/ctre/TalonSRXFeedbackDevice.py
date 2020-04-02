class TalonSRXFeedbackDevice():
    """
    Choose the feedback device for a Talon SRX
    
    Members:
    
      QuadEncoder : Quadrature encoder
    
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
        """ __init__(self: ctre._ctre.TalonSRXFeedbackDevice, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.TalonSRXFeedbackDevice) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.TalonSRXFeedbackDevice, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Analog = TalonSRXFeedbackDevice.Analog
    CTRE_MagEncoder_Absolute = TalonSRXFeedbackDevice.PulseWidthEncodedPosition
    CTRE_MagEncoder_Relative = TalonSRXFeedbackDevice.QuadEncoder
    None_ = TalonSRXFeedbackDevice.None_
    PulseWidthEncodedPosition = TalonSRXFeedbackDevice.PulseWidthEncodedPosition
    QuadEncoder = TalonSRXFeedbackDevice.QuadEncoder
    RemoteSensor0 = TalonSRXFeedbackDevice.RemoteSensor0
    RemoteSensor1 = TalonSRXFeedbackDevice.RemoteSensor1
    SensorDifference = TalonSRXFeedbackDevice.SensorDifference
    SensorSum = TalonSRXFeedbackDevice.SensorSum
    SoftwareEmulatedSensor = TalonSRXFeedbackDevice.SoftwareEmulatedSensor
    Tachometer = TalonSRXFeedbackDevice.Tachometer
    __entries = {
        'Analog': (
            TalonSRXFeedbackDevice.Analog,
            'Analog potentiometer/encoder',
        ),
        'CTRE_MagEncoder_Absolute': (
            TalonSRXFeedbackDevice.PulseWidthEncodedPosition,
            'CTR mag encoder configured in absolute, is the same\nas a PWM sensor.',
        ),
        'CTRE_MagEncoder_Relative': (
            TalonSRXFeedbackDevice.QuadEncoder,
            'CTR mag encoder configured in relative, is the same\nas an quadrature encoder sensor.',
        ),
        'None_': (
            TalonSRXFeedbackDevice.None_,
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
            TalonSRXFeedbackDevice.RemoteSensor0,
            'Sensor configured in RemoteFilter0',
        ),
        'RemoteSensor1': (
            TalonSRXFeedbackDevice.RemoteSensor1,
            'Sensor configured in RemoteFilter1',
        ),
        'SensorDifference': (
            TalonSRXFeedbackDevice.SensorDifference,
            'Diff0 - Diff1',
        ),
        'SensorSum': (
            TalonSRXFeedbackDevice.SensorSum,
            'Sum0 + Sum1',
        ),
        'SoftwareEmulatedSensor': (
            TalonSRXFeedbackDevice.SoftwareEmulatedSensor,
            'Motor Controller will fake a sensor based on applied motor output.',
        ),
        'Tachometer': (
            TalonSRXFeedbackDevice.Tachometer,
            'Tachometer',
        ),
    }
    __members__ = {
        'Analog': TalonSRXFeedbackDevice.Analog,
        'CTRE_MagEncoder_Absolute': TalonSRXFeedbackDevice.PulseWidthEncodedPosition,
        'CTRE_MagEncoder_Relative': TalonSRXFeedbackDevice.QuadEncoder,
        'None_': TalonSRXFeedbackDevice.None_,
        'PulseWidthEncodedPosition': '<value is a self-reference, replaced by this string>',
        'QuadEncoder': '<value is a self-reference, replaced by this string>',
        'RemoteSensor0': TalonSRXFeedbackDevice.RemoteSensor0,
        'RemoteSensor1': TalonSRXFeedbackDevice.RemoteSensor1,
        'SensorDifference': TalonSRXFeedbackDevice.SensorDifference,
        'SensorSum': TalonSRXFeedbackDevice.SensorSum,
        'SoftwareEmulatedSensor': TalonSRXFeedbackDevice.SoftwareEmulatedSensor,
        'Tachometer': TalonSRXFeedbackDevice.Tachometer,
    }
