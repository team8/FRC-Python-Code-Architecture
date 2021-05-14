from codeinternals.ctre import VictorSPX, WPI_BaseMotorController


class WPI_VictorSPX(VictorSPX, WPI_BaseMotorController):
    """ VEX Victor SPX Motor Controller when used on CAN Bus. """

    def configSelectedFeedbackSensor(self, feedbackDevice, pidIdx=0,
                                     timeoutMs=0):  # real signature unknown; restored from __doc__
        """ configSelectedFeedbackSensor(self: ctre._ctre.WPI_VictorSPX, feedbackDevice: ctre._ctre.RemoteFeedbackDevice, pidIdx: int = 0, timeoutMs: int = 0) -> ctre._ctre.ErrorCode """
        pass

    def set(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        set(*args, **kwargs)
        Overloaded function.
        
        1. set(self: ctre._ctre.WPI_VictorSPX, value: float) -> None
        
        2. set(self: ctre._ctre.WPI_VictorSPX, mode: ctre._ctre.ControlMode, value: float) -> None
        
        3. set(self: ctre._ctre.WPI_VictorSPX, mode: ctre._ctre.ControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        
        4. set(self: ctre._ctre.WPI_VictorSPX, mode: ctre._ctre.VictorSPXControlMode, value: float) -> None
        
        5. set(self: ctre._ctre.WPI_VictorSPX, mode: ctre._ctre.VictorSPXControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        """
        pass

    def setInverted(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        setInverted(*args, **kwargs)
        Overloaded function.
        
        1. setInverted(self: ctre._ctre.WPI_VictorSPX, invertType: ctre._ctre.InvertType) -> None
        
        2. setInverted(self: ctre._ctre.WPI_VictorSPX, bInvert: bool) -> None
        """
        pass

    def setVoltage(self, output):  # real signature unknown; restored from __doc__
        """ setVoltage(self: ctre._ctre.WPI_VictorSPX, output: volts) -> None """
        pass

    def __init__(self, deviceNumber):  # real signature unknown; restored from __doc__
        """
        __init__(self: ctre._ctre.WPI_VictorSPX, deviceNumber: int) -> None
        
        Constructor for a WPI_VictorSPX
        
        :param deviceNumber: Device ID of VictorSPX
        """
        pass
