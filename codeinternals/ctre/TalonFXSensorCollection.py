
class TalonFXSensorCollection():
    """
    Collection of sensors available to the Talon FX.
    
    For best performance and update-rate,
    we recommend using the configSelectedFeedbackSensor() and getSelectedSensor*() routines.
    However there are occasions where accessing raw sensor values may be useful or convenient.
    Particularly if you are seeding one sensor based on another, or need to circumvent sensor-phase.
    
    Use the GetTalonFXSensorCollection() routine inside your motor controller to create a sensor collection.
    """
    def getIntegratedSensorAbsolutePosition(self): # real signature unknown; restored from __doc__
        """
        getIntegratedSensorAbsolutePosition(self: ctre._ctre.TalonFXSensorCollection) -> float
        
        Get the IntegratedSensor absolute position of the Talon FX, regardless of whether
        it is actually being used for feedback.  This will be within one rotation (2048 units).
        The signage and range will depend on the configuration.
        Note : Future versions of software may support scaling features (rotations, radians, degrees, etc) depending on the configuration.
        
        :returns: the IntegratedSensor absolute position.
        """
        return 0.0

    def getIntegratedSensorPosition(self): # real signature unknown; restored from __doc__
        """ getIntegratedSensorPosition(self: ctre._ctre.TalonFXSensorCollection) -> float """
        return 0.0

    def getIntegratedSensorVelocity(self): # real signature unknown; restored from __doc__
        """
        getIntegratedSensorVelocity(self: ctre._ctre.TalonFXSensorCollection) -> float
        
        Get the IntegratedSensor velocity of the Talon FX, regardless of whether
        it is actually being used for feedback.
        One unit represents one position unit per 100ms (2048 position units per 100ms).
        The signage and range will depend on the configuration.
        Note : Future versions of software may support scaling features (rotations, radians, degrees, etc) depending on the configuration.
        
        :returns: the IntegratedSensor velocity.
        """
        return 0.0

    def isFwdLimitSwitchClosed(self): # real signature unknown; restored from __doc__
        """ isFwdLimitSwitchClosed(self: ctre._ctre.TalonFXSensorCollection) -> int """
        return 0

    def isRevLimitSwitchClosed(self): # real signature unknown; restored from __doc__
        """ isRevLimitSwitchClosed(self: ctre._ctre.TalonFXSensorCollection) -> int """
        return 0

    def setIntegratedSensorPosition(self, newPosition, timeoutMs=0): # real signature unknown; restored from __doc__
        """
        setIntegratedSensorPosition(self: ctre._ctre.TalonFXSensorCollection, newPosition: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Set the IntegratedSensor reported position.  Typically this is used to "zero" the
        sensor. This only works with IntegratedSensor.  To set the selected sensor position
        regardless of what type it is, see SetSelectedSensorPosition in the motor controller class.
        
        :param newPosition: The position value to apply to the sensor.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                   config success and report an error if it times out.
                   If zero, no blocking or checking is performed.
        
        :returns: error code.
        """
        pass

    def setIntegratedSensorPositionToAbsolute(self, timeoutMs=0): # real signature unknown; restored from __doc__
        """
        setIntegratedSensorPositionToAbsolute(self: ctre._ctre.TalonFXSensorCollection, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Set the IntegratedSensor reported position based on the absolute position.
        This can also be done automatically on power boot depending on configuration.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: error code.
        """
        pass

    def __init__(self, motorController, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__(self: ctre._ctre.TalonFXSensorCollection, motorController: ctre::phoenix::motorcontrol::can::BaseTalon) -> None
        
        Constructor for TalonFXSensorCollection
        
        :param motorController: Talon Motor Controller to connect Collection to
        """
        pass


