from codeinternals.ctre import CANBusAddressable


class PigeonIMU(CANBusAddressable):
    """
    Pigeon IMU Class.
    Class supports communicating over CANbus and over ribbon-cable (CAN Talon SRX).
    """

    def addFusedHeading(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        addFusedHeading(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Atomically add to the Fused Heading register.
        
        :param angleDeg: Degrees to add to the Fused Heading register.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def addYaw(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        addYaw(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Atomically add to the Yaw register.
        
        :param angleDeg: Degrees to add to the Yaw register.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def clearStickyFaults(self, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        clearStickyFaults(self: ctre._ctre.PigeonIMU, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Clears the Sticky Faults
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configAllSettings(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configAllSettings(self: ctre._ctre.PigeonIMU, allConfigs: ctre._ctre.PigeonIMUConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures all persistent settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configFactoryDefault(self, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configFactoryDefault(self: ctre._ctre.PigeonIMU, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures all persistent settings to defaults.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configGetCustomParam(self, paramIndex, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configGetCustomParam(self: ctre._ctre.PigeonIMU, paramIndex: int, timeoutMs: int = 0) -> int
        
        Gets the value of a custom parameter. This is for arbitrary use.
        
        Sometimes it is necessary to save calibration/declination/offset
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
        
        1. configGetParameter(self: ctre._ctre.PigeonIMU, param: ctre._ctre.ParamEnum, ordinal: int, timeoutMs: int = 0) -> float
        
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
        
        2. configGetParameter(self: ctre._ctre.PigeonIMU, param: ctre._ctre.ParamEnum, valueToSend: int, valueReceived: int, subValue: int, ordinal: int, timeoutMs: int) -> ctre._ctre.ErrorCode
        
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
        configSetCustomParam(self: ctre._ctre.PigeonIMU, newValue: int, paramIndex: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the value of a custom parameter. This is for arbitrary use.
        
        Sometimes it is necessary to save calibration/declination/offset
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
        configSetParameter(self: ctre._ctre.PigeonIMU, param: ctre._ctre.ParamEnum, value: float, subValue: int, ordinal: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
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

    def configTemperatureCompensationEnable(self, bTempCompEnable,
                                            timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configTemperatureCompensationEnable(self: ctre._ctre.PigeonIMU, bTempCompEnable: bool, timeoutMs: int = 0) -> int
        
        @deprecated use setTemperatureCompensationDisable instead
        This was done to better match with the lower level API.
        NOTE: this isn't a persistant config, every boot temperature
        compensation will be enabled
        This was also done so the default value for the paramter is false instead of true.
        Enable/Disable Temp compensation. Pigeon defaults with this on at boot.
        
        :param bTempCompEnable: Set to "True" to enable temperature compensation.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                       config success and report an error if it times out.
                       If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def destroyAllPigeonIMUs(self):  # real signature unknown; restored from __doc__
        """
        destroyAllPigeonIMUs() -> None
        
        Destructs all pigeon objects
        """
        pass

    def enterCalibrationMode(self, calMode, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        enterCalibrationMode(self: ctre._ctre.PigeonIMU, calMode: ctre._ctre.PigeonIMU.CalibrationMode, timeoutMs: int = 0) -> int
        
        Enters the Calbration mode.  See the Pigeon IMU documentation for More
        information on Calibration.
        
        Note that you can instead use Phoenix Tuner to accomplish this.
        Note you should NOT be calling this during normal robot operation.
        
        :param calMode: Calibration to execute
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def get6dQuaternion(self):  # real signature unknown; restored from __doc__
        """
        get6dQuaternion(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[float[4]]]
        
        Get 6d Quaternion data.
        
        :param wxyz: Array to fill with quaternion data w[0], x[1], y[2], z[3]
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getAbsoluteCompassHeading(self):  # real signature unknown; restored from __doc__
        """
        getAbsoluteCompassHeading(self: ctre._ctre.PigeonIMU) -> float
        
        Get the absolute compass heading.
        
        :returns: compass heading [0,360) degrees.
        """
        return 0.0

    def getAccelerometerAngles(self):  # real signature unknown; restored from __doc__
        """
        getAccelerometerAngles(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[float[3]]]
        
        Get Accelerometer tilt angles.
        
        :param tiltAngles: Array to fill with x[0], y[1], and z[2] angles in degrees.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getAccumGyro(self):  # real signature unknown; restored from __doc__
        """
        getAccumGyro(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[float[3]]]
        
        Get AccumGyro data.
        AccumGyro is the integrated gyro value on each axis.
        
        :param xyz_deg: Array to fill with x[0], y[1], and z[2] AccumGyro data
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getAllConfigs(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        getAllConfigs(self: ctre._ctre.PigeonIMU, allConfigs: ctre._ctre.PigeonIMUConfiguration, timeoutMs: int = 50) -> None
        
        Gets all persistant settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        """
        pass

    def getBiasedAccelerometer(self):  # real signature unknown; restored from __doc__
        """
        getBiasedAccelerometer(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[int[3]]]
        
        Get Biased Accelerometer data.
        
        :param ba_xyz: Array to fill with x[0], y[1], and z[2] data.
              These are in fixed point notation Q2.14.  eg. 16384 = 1G
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getBiasedMagnetometer(self):  # real signature unknown; restored from __doc__
        """
        getBiasedMagnetometer(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[int[3]]]
        
        Get Biased Magnetometer data.
        
        :param bm_xyz: Array to fill with x[0], y[1], and z[2] data
              Number is equal to 0.6 microTeslas per unit.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getCompassFieldStrength(self):  # real signature unknown; restored from __doc__
        """
        getCompassFieldStrength(self: ctre._ctre.PigeonIMU) -> float
        
        Gets the compass' measured magnetic field strength.
        
        :returns: field strength in Microteslas (uT).
        """
        return 0.0

    def getCompassHeading(self):  # real signature unknown; restored from __doc__
        """
        getCompassHeading(self: ctre._ctre.PigeonIMU) -> float
        
        Get the continuous compass heading.
        
        :returns: continuous compass heading [-23040, 23040) degrees. Use
                  SetCompassHeading to modify the wrap-around portion.
        """
        return 0.0

    def getFaults(self, toFill, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        getFaults(self: ctre._ctre.PigeonIMU, toFill: ctre::phoenix::sensors::PigeonIMU_Faults) -> ctre._ctre.ErrorCode
        
        Gets the fault status
        
        :param toFill: Container for fault statuses.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def getFirmVers(self):  # real signature unknown; restored from __doc__
        """
        getFirmVers(self: ctre._ctre.PigeonIMU) -> int
        
        
        
        :returns: firmware version of Pigeon
        """
        return 0

    def getFirmwareVersion(self):  # real signature unknown; restored from __doc__
        """
        getFirmwareVersion(self: ctre._ctre.PigeonIMU) -> int
        
        Gets the firmware version of the device.
        
        :returns: param holds the firmware version of the device. Device must be powered
                  cycled at least once.
        """
        return 0

    def getFusedHeading(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        getFusedHeading(*args, **kwargs)
        Overloaded function.
        
        1. getFusedHeading(self: ctre._ctre.PigeonIMU, status: ctre._ctre.PigeonIMU.FusionStatus) -> float
        
        Get the current Fusion Status (including fused heading)
        
        :param status: object reference to fill with fusion status flags.
              Caller may pass null if flags are not needed.
        
        :returns: The fused heading in degrees.
        
        2. getFusedHeading(self: ctre._ctre.PigeonIMU) -> float
        
        Gets the Fused Heading
        
        :returns: The fused heading in degrees.
        """
        pass

    def getGeneralStatus(self, statusToFill):  # real signature unknown; restored from __doc__
        """
        getGeneralStatus(self: ctre._ctre.PigeonIMU, statusToFill: ctre._ctre.PigeonIMU.GeneralStatus) -> int
        
        Get the status of the current (or previousley complete) calibration.
        
        :param out: statusToFill Container for the status information.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def getLastError(self):  # real signature unknown; restored from __doc__
        """
        getLastError(self: ctre._ctre.PigeonIMU) -> ctre._ctre.ErrorCode
        
        Call GetLastError() generated by this object.
        Not all functions return an error code but can
        potentially report errors.
        
        This function can be used to retrieve those error codes.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getLowLevelHandle(self):  # real signature unknown; restored from __doc__
        """
        getLowLevelHandle(self: ctre._ctre.PigeonIMU) -> capsule
        
        
        
        :returns: Pigeon resource handle.
        """
        pass

    def getRawGyro(self):  # real signature unknown; restored from __doc__
        """
        getRawGyro(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[float[3]]]
        
        Get Raw Gyro data.
        
        :param xyz_dps: Array to fill with x[0], y[1], and z[2] data in degrees per second.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getRawMagnetometer(self):  # real signature unknown; restored from __doc__
        """
        getRawMagnetometer(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[int[3]]]
        
        Get Raw Magnetometer data.
        
        :param rm_xyz: Array to fill with x[0], y[1], and z[2] data
              Number is equal to 0.6 microTeslas per unit.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def getResetCount(self):  # real signature unknown; restored from __doc__
        """
        getResetCount(self: ctre._ctre.PigeonIMU) -> int
        
        
        
        :returns: number of times Pigeon Reset
        """
        return 0

    def getResetFlags(self):  # real signature unknown; restored from __doc__
        """
        getResetFlags(self: ctre._ctre.PigeonIMU) -> int
        
        
        
        :returns: Reset flags for Pigeon
        """
        return 0

    def getState(self):  # real signature unknown; restored from __doc__
        """
        getState(self: ctre._ctre.PigeonIMU) -> ctre._ctre.PigeonIMU.PigeonState
        
        Gets the current Pigeon state
        
        :returns: PigeonState enum
        """
        pass

    def getStatusFramePeriod(self, frame, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        getStatusFramePeriod(self: ctre._ctre.PigeonIMU, frame: ctre._ctre.PigeonIMU_StatusFrame, timeoutMs: int = 0) -> int
        
        Gets the period of the given status frame.
        
        :param frame: Frame to get the period of.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Period of the given status frame.
        """
        return 0

    def getStickyFaults(self, toFill, *args,
                        **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        getStickyFaults(self: ctre._ctre.PigeonIMU, toFill: ctre::phoenix::sensors::PigeonIMU_StickyFaults) -> ctre._ctre.ErrorCode
        
        Gets the sticky fault status
        
        :param toFill: Container for sticky fault statuses.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def getTemp(self):  # real signature unknown; restored from __doc__
        """
        getTemp(self: ctre._ctre.PigeonIMU) -> float
        
        Gets the temperature of the pigeon.
        
        :returns: Temperature in ('C)
        """
        return 0.0

    def getUpTime(self):  # real signature unknown; restored from __doc__
        """
        getUpTime(self: ctre._ctre.PigeonIMU) -> int
        
        Gets the current Pigeon uptime.
        
        :returns: How long has Pigeon been running in whole seconds. Value caps at
                  255.
        """
        return 0

    def getYawPitchRoll(self):  # real signature unknown; restored from __doc__
        """
        getYawPitchRoll(self: ctre._ctre.PigeonIMU) -> Tuple[int, List[float[3]]]
        
        Get Yaw, Pitch, and Roll data.
        
        :param ypr: Array to fill with yaw[0], pitch[1], and roll[2] data.
           Yaw is within [-368,640, +368,640] degrees.
           Pitch is within [-90,+90] degrees.
           Roll is within [-90,+90] degrees.
        
        :returns: The last ErrorCode generated.
        """
        pass

    def hasResetOccurred(self):  # real signature unknown; restored from __doc__
        """
        hasResetOccurred(self: ctre._ctre.PigeonIMU) -> bool
        
        
        
        :returns: true iff a reset has occurred since last call.
        """
        return False

    def setAccumZAngle(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setAccumZAngle(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Sets the AccumZAngle.
        
        :param angleDeg: Degrees to set AccumZAngle to.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setCompassAngle(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setCompassAngle(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Sets the compass angle. Although compass is absolute [0,360) degrees, the
        continuous compass register holds the wrap-arounds.
        
        :param angleDeg: Degrees to set continuous compass angle to.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setCompassDeclination(self, angleDegOffset, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setCompassDeclination(self: ctre._ctre.PigeonIMU, angleDegOffset: float, timeoutMs: int = 0) -> int
        
        Set the declination for compass. Declination is the difference between
        Earth Magnetic north, and the geographic "True North".
        
        :param angleDegOffset: Degrees to set Compass Declination to.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                      config success and report an error if it times out.
                      If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setControlFramePeriod(self, frame, periodMs):  # real signature unknown; restored from __doc__
        """
        setControlFramePeriod(self: ctre._ctre.PigeonIMU, frame: ctre._ctre.PigeonIMU_ControlFrame, periodMs: int) -> ctre._ctre.ErrorCode
        
        Sets the period of the given control frame.
        
        :param frame: Frame whose period is to be changed.
        
        :param periodMs: Period in ms for the given frame.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def setFusedHeading(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setFusedHeading(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Sets the Fused Heading to the specified value.
        
        :param angleDeg: New fused-heading in degrees [+/- 23,040 degrees]
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setFusedHeadingToCompass(self, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setFusedHeadingToCompass(self: ctre._ctre.PigeonIMU, timeoutMs: int = 0) -> int
        
        Sets the Fused Heading register to match the current compass value.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setStatusFramePeriod(self, statusFrame, periodMs, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setStatusFramePeriod(self: ctre._ctre.PigeonIMU, statusFrame: ctre._ctre.PigeonIMU_StatusFrame, periodMs: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets the period of the given status frame.
        
        :param statusFrame: Frame whose period is to be changed.
        
        :param periodMs: Period in ms for the given frame.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                   config success and report an error if it times out.
                   If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def setTemperatureCompensationDisable(self, bTempCompDisable,
                                          timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setTemperatureCompensationDisable(self: ctre._ctre.PigeonIMU, bTempCompDisable: bool, timeoutMs: int = 0) -> int
        
        Disable/Enable Temp compensation. Pigeon has this on/False at boot.
        
        :param bTempCompDisable: Set to "False" to enable temperature compensation.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                        config success and report an error if it times out.
                        If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setYaw(self, angleDeg, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setYaw(self: ctre._ctre.PigeonIMU, angleDeg: float, timeoutMs: int = 0) -> int
        
        Sets the Yaw register to the specified value.
        
        :param angleDeg: Degree of Yaw  [+/- 368,640 degrees]
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def setYawToCompass(self, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setYawToCompass(self: ctre._ctre.PigeonIMU, timeoutMs: int = 0) -> int
        
        Sets the Yaw register to match the current compass value.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        return 0

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(state: ctre._ctre.PigeonIMU.PigeonState) -> str
        
        Gets the string representation of a PigeonState
        
        :param state: PigeonState to get the string representation of
        
        :returns: string representation of specified PigeonState
        
        2. toString(cm: ctre._ctre.PigeonIMU.CalibrationMode) -> str
        
        Gets the string representation of a CalibrationMode
        
        :param cm: CalibrationMode to get the string representation of
        
        :returns: string representation of specified CalibrationMode
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.PigeonIMU, deviceNumber: int) -> None
        
        Create a Pigeon object that communicates with Pigeon on CAN Bus.
        
        :param deviceNumber: CAN Device Id of Pigeon [0,62]
        
        2. __init__(self: ctre._ctre.PigeonIMU, talonSrx: ctre::phoenix::motorcontrol::can::TalonSRX) -> None
        
        Create a Pigeon object that communciates with Pigeon through the
        Gadgeteer ribbon cable connected to a Talon on CAN Bus.
        
        :param talonSrx: Object for the TalonSRX connected via ribbon cable.
        """
        pass

    CalibrationMode = None  # (!) real value is "<class 'ctre._ctre.PigeonIMU.CalibrationMode'>"
    FusionStatus = None  # (!) real value is "<class 'ctre._ctre.PigeonIMU.FusionStatus'>"
    GeneralStatus = None  # (!) real value is "<class 'ctre._ctre.PigeonIMU.GeneralStatus'>"
    PigeonState = None  # (!) real value is "<class 'ctre._ctre.PigeonIMU.PigeonState'>"