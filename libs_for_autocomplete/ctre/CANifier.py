# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports

from .CANBusAddressable import CANBusAddressable


class CANifier(CANBusAddressable):
    """
    CTRE CANifier
    
    Device for interfacing common devices to the CAN bus.
    """

    def clearStickyFaults(self, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        clearStickyFaults(self: ctre._ctre.CANifier, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Clears the Sticky Faults
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configAllSettings(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configAllSettings(self: ctre._ctre.CANifier, allConfigs: ctre._ctre.CANifierConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures all persistent settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configClearPositionOnLimitF(self, clearPositionOnLimitF,
                                    timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configClearPositionOnLimitF(self: ctre._ctre.CANifier, clearPositionOnLimitF: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Enables clearing the position of the feedback sensor when the forward
        limit switch is triggered
        
        :param clearPositionOnLimitF: Whether clearing is enabled, defaults false
        
        :param timeoutMs:    Timeout value in ms. If nonzero, function will wait for
                             config success and report an error if it times out.
                             If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configClearPositionOnLimitR(self, clearPositionOnLimitR,
                                    timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configClearPositionOnLimitR(self: ctre._ctre.CANifier, clearPositionOnLimitR: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Enables clearing the position of the feedback sensor when the reverse
        limit switch is triggered
        
        :param clearPositionOnLimitR: Whether clearing is enabled, defaults false
        
        :param timeoutMs:    Timeout value in ms. If nonzero, function will wait for
                             config success and report an error if it times out.
                             If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configClearPositionOnQuadIdx(self, clearPositionOnQuadIdx,
                                     timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configClearPositionOnQuadIdx(self: ctre._ctre.CANifier, clearPositionOnQuadIdx: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Enables clearing the position of the feedback sensor when the quadrature index signal
        is detected
        
        :param clearPositionOnQuadIdx: Whether clearing is enabled, defaults false
        
        :param timeoutMs:     Timeout value in ms. If nonzero, function will wait for
                              config success and report an error if it times out.
                              If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configFactoryDefault(self, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configFactoryDefault(self: ctre._ctre.CANifier, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures all persistent settings to defaults (overloaded so timeoutMs is 50 ms).
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configGetCustomParam(self, paramIndex, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configGetCustomParam(self: ctre._ctre.CANifier, paramIndex: int, timeoutMs: int = 0) -> int
        
        Gets the value of a custom parameter. This is for arbitrary use.
        
        Sometimes it is necessary to save calibration/duty cycle/output
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.
        
        :param paramIndex: Index of custom parameter. [0-1]
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Value of the custom param.
        """
        return 0

    def configGetParameter(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        configGetParameter(*args, **kwargs)
        Overloaded function.
        
        1. configGetParameter(self: ctre._ctre.CANifier, param: ctre._ctre.ParamEnum, ordinal: int, timeoutMs: int = 0) -> float
        
        Gets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.
        
        :param param: Parameter enumeration.
        
        :param ordinal: Ordinal of parameter.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Value of parameter.
        
        2. configGetParameter(self: ctre._ctre.CANifier, param: ctre._ctre.ParamEnum, valueToSend: int, valueReceived: int, subValue: int, ordinal: int, timeoutMs: int) -> ctre._ctre.ErrorCode
        
        Gets a parameter by passing an int by reference
        
        :param param: Parameter enumeration
        
        :param valueToSend: Value to send to parameter
        
        :param valueReceived: Reference to integer to receive
        
        :param subValue: SubValue of parameter
        
        :param ordinal: Ordinal of parameter
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                     config success and report an error if it times out.
                     If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configSetCustomParam(self, newValue, paramIndex, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configSetCustomParam(self: ctre._ctre.CANifier, newValue: int, paramIndex: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the value of a custom parameter. This is for arbitrary use.
        
        Sometimes it is necessary to save calibration/duty cycle/output
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.
        
        :param newValue: Value for custom parameter.
        
        :param paramIndex: Index of custom parameter. [0-1]
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configSetParameter(self, param, value, subValue, ordinal,
                           timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configSetParameter(self: ctre._ctre.CANifier, param: ctre._ctre.ParamEnum, value: float, subValue: int, ordinal: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.
        
        :param param: Parameter enumeration.
        
        :param value: Value of parameter.
        
        :param subValue: Subvalue for parameter. Maximum value of 255.
        
        :param ordinal: Ordinal of parameter.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configVelocityMeasurementPeriod(self, period, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configVelocityMeasurementPeriod(self: ctre._ctre.CANifier, period: ctre._ctre.CANifierVelocityMeasPeriod, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Configures the period of each velocity sample.
        Every 1ms a position value is sampled, and the delta between that sample
        and the position sampled kPeriod ms ago is inserted into a filter.
        kPeriod is configured with this function.
        
        :param period: Desired period for the velocity measurement.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configVelocityMeasurementWindow(self, windowSize, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configVelocityMeasurementWindow(self: ctre._ctre.CANifier, windowSize: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the number of velocity samples used in the rolling average velocity
        measurement.
        
        :param windowSize: Number of samples in the rolling average of velocity
                  measurement. Valid values are 1,2,4,8,16,32. If another
                  value is specified, it will truncate to nearest support value.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def destroyAllCANifiers(self):  # real signature unknown; restored from __doc__
        """
        destroyAllCANifiers() -> None
        
        Destructs all CANifier objects
        """
        pass

    def enablePWMOutput(self, pwmChannel, bEnable):  # real signature unknown; restored from __doc__
        """
        enablePWMOutput(self: ctre._ctre.CANifier, pwmChannel: int, bEnable: bool) -> ctre._ctre.ErrorCode
        
        Enables PWM Outputs
        Currently supports PWM 0, PWM 1, and PWM 2
        
        :param pwmChannel: Index of the PWM channel to enable.
        
        :param bEnable: True" enables output on the pwm channel.
        """
        pass

    def getAllConfigs(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        getAllConfigs(self: ctre._ctre.CANifier, allConfigs: ctre._ctre.CANifierConfiguration, timeoutMs: int = 50) -> None
        
        Gets all persistant settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        """
        pass

    def getBusVoltage(self):  # real signature unknown; restored from __doc__
        """
        getBusVoltage(self: ctre._ctre.CANifier) -> float
        
        Gets the bus voltage seen by the device.
        
        :returns: The bus voltage value (in volts).
        """
        return 0.0

    def getFaults(self, toFill):  # real signature unknown; restored from __doc__
        """
        getFaults(self: ctre._ctre.CANifier, toFill: ctre._ctre.CANifierFaults) -> ctre._ctre.ErrorCode
        
        Gets the CANifier fault status
        
        :param toFill: Container for fault statuses.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def getFirmwareVersion(self):  # real signature unknown; restored from __doc__
        """
        getFirmwareVersion(self: ctre._ctre.CANifier) -> int
        
        Gets the firmware version of the device.
        
        :returns: Firmware version of device.
        """
        return 0

    def getGeneralInput(self, inputPin):  # real signature unknown; restored from __doc__
        """
        getGeneralInput(self: ctre._ctre.CANifier, inputPin: ctre._ctre.CANifier.GeneralPin) -> bool
        
        Gets the state of the specified pin
        
        :param inputPin: The index of the pin.
        
        :returns: The state of the pin.
        """
        return False

    def getGeneralInputs(self, allPins):  # real signature unknown; restored from __doc__
        """
        getGeneralInputs(self: ctre._ctre.CANifier, allPins: ctre._ctre.CANifier.PinValues) -> ctre._ctre.ErrorCode
        
        Gets the state of all General Pins
        
        :param allPins: A structure to fill with the current state of all pins.
        """
        pass

    def getLastError(self):  # real signature unknown; restored from __doc__
        """
        getLastError(self: ctre._ctre.CANifier) -> ctre._ctre.ErrorCode
        
        Call GetLastError() generated by this object.
        Not all functions return an error code but can
        potentially report errors.
        
        This function can be used to retrieve those error codes.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getPWMInput(self, pwmChannel):  # real signature unknown; restored from __doc__
        """
        getPWMInput(self: ctre._ctre.CANifier, pwmChannel: ctre._ctre.CANifier.PWMChannel) -> Tuple[ctre._ctre.ErrorCode, List[float[2]]]
        
        Gets the PWM Input
        
        :param pwmChannel: PWM channel to get.
        
        :param pulseWidthAndPeriod: Double array to hold Duty Cycle [0] and Period [1].
        """
        pass

    def getQuadraturePosition(self):  # real signature unknown; restored from __doc__
        """
        getQuadraturePosition(self: ctre._ctre.CANifier) -> int
        
        Gets the quadrature encoder's position
        
        :returns: Position of encoder
        """
        return 0

    def getQuadratureVelocity(self):  # real signature unknown; restored from __doc__
        """
        getQuadratureVelocity(self: ctre._ctre.CANifier) -> int
        
        Gets the quadrature encoder's velocity
        
        :returns: Velocity of encoder
        """
        return 0

    def getStatusFramePeriod(self, frame, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        getStatusFramePeriod(self: ctre._ctre.CANifier, frame: ctre._ctre.CANifierStatusFrame, timeoutMs: int = 0) -> int
        
        Gets the period of the given status frame.
        
        :param frame: Frame to get the period of.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Period of the given status frame.
        """
        return 0

    def getStickyFaults(self, toFill):  # real signature unknown; restored from __doc__
        """
        getStickyFaults(self: ctre._ctre.CANifier, toFill: ctre._ctre.CANifierStickyFaults) -> ctre._ctre.ErrorCode
        
        Gets the CANifier sticky fault status
        
        :param toFill: Container for sticky fault statuses.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def hasResetOccurred(self):  # real signature unknown; restored from __doc__
        """
        hasResetOccurred(self: ctre._ctre.CANifier) -> bool
        
        Returns true if the device has reset since last call.
        
        :returns: Has a Device Reset Occurred?
        """
        return False

    def setControlFramePeriod(self, frame, periodMs):  # real signature unknown; restored from __doc__
        """
        setControlFramePeriod(self: ctre._ctre.CANifier, frame: ctre._ctre.CANifierControlFrame, periodMs: int) -> ctre._ctre.ErrorCode
        
        Sets the period of the given control frame.
        
        :param frame: Frame whose period is to be changed.
        
        :param periodMs: Period in ms for the given frame.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def setGeneralOutput(self, outputPin, outputValue, outputEnable):  # real signature unknown; restored from __doc__
        """
        setGeneralOutput(self: ctre._ctre.CANifier, outputPin: ctre._ctre.CANifier.GeneralPin, outputValue: bool, outputEnable: bool) -> ctre._ctre.ErrorCode
        
        Sets the output of a General Pin
        
        :param outputPin: The pin to use as output.
        
        :param outputValue: The desired output state.
        
        :param outputEnable: Whether this pin is an output. "True" enables output.
        """
        pass

    def setGeneralOutputs(self, outputBits, isOutputBits):  # real signature unknown; restored from __doc__
        """
        setGeneralOutputs(self: ctre._ctre.CANifier, outputBits: int, isOutputBits: int) -> ctre._ctre.ErrorCode
        
        Sets the output of all General Pins
        
        :param outputBits: A bit mask of all the output states.  LSB->MSB is in the order of the #GeneralPin enum.
        
        :param isOutputBits: A boolean bit mask that sets the pins to be outputs or inputs.  A bit of 1 enables output.
        """
        pass

    def setLEDOutput(self, percentOutput, ledChannel):  # real signature unknown; restored from __doc__
        """
        setLEDOutput(self: ctre._ctre.CANifier, percentOutput: float, ledChannel: ctre._ctre.CANifier.LEDChannel) -> ctre._ctre.ErrorCode
        
        Sets the LED Output
        
        :param percentOutput: Output duty cycle expressed as percentage.
        
        :param ledChannel: Channel to set the output of.
        """
        pass

    def setPWMOutput(self, pwmChannel, dutyCycle):  # real signature unknown; restored from __doc__
        """
        setPWMOutput(self: ctre._ctre.CANifier, pwmChannel: int, dutyCycle: float) -> ctre._ctre.ErrorCode
        
        Sets the PWM Output
        Currently supports PWM 0, PWM 1, and PWM 2
        
        :param pwmChannel: Index of the PWM channel to output.
        
        :param dutyCycle: Duty Cycle (0 to 1) to output.  Default period of the signal is 4.2 ms.
        """
        pass

    def setQuadraturePosition(self, newPosition, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setQuadraturePosition(self: ctre._ctre.CANifier, newPosition: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the quadrature encoder's position
        
        :param newPosition: Position to set
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                   config success and report an error if it times out.
                   If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def setStatusFramePeriod(self, statusFrame, periodMs, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setStatusFramePeriod(self: ctre._ctre.CANifier, statusFrame: ctre._ctre.CANifierStatusFrame, periodMs: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the period of the given status frame.
        
        :param statusFrame: Frame whose period is to be changed.
        
        :param periodMs: Period in ms for the given frame.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                   config success and report an error if it times out.
                   If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def __init__(self, deviceNumber):  # real signature unknown; restored from __doc__
        """
        __init__(self: ctre._ctre.CANifier, deviceNumber: int) -> None
        
        Constructor.
        
        :param deviceNumber: The CAN Device ID of the CANifier.
        """
        pass

    PWMChannelCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of PWM channels available to CANifier"""

    GeneralPin = None  # (!) real value is "<class 'ctre._ctre.CANifier.GeneralPin'>"
    LEDChannel = None  # (!) real value is "<class 'ctre._ctre.CANifier.LEDChannel'>"
    PinValues = None  # (!) real value is "<class 'ctre._ctre.CANifier.PinValues'>"
    PWMChannel = None  # (!) real value is "<class 'ctre._ctre.CANifier.PWMChannel'>"