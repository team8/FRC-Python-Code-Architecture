from codeinternals.ctre import BaseMotorController


class WPI_BaseMotorController(BaseMotorController):
    """ VEX Victor SPX Motor Controller when used on CAN Bus. """

    def disable(self):  # real signature unknown; restored from __doc__
        """
        disable(self: ctre._ctre.WPI_BaseMotorController) -> None
        
        Common interface for disabling a motor.
        """
        pass

    def feed(self):  # real signature unknown; restored from __doc__
        """
        feed(self: ctre._ctre.WPI_BaseMotorController) -> None
        
        Feed the motor safety object.
        
        Resets the timer on this object that is used to do the timeouts.
        """
        pass

    def get(self):  # real signature unknown; restored from __doc__
        """
        get(self: ctre._ctre.WPI_BaseMotorController) -> float
        
        Common interface for getting the current set speed of a speed controller.
        
        :returns: The current set speed.  Value is between -1.0 and 1.0.
        """
        return 0.0

    def getDescription(self, desc, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        getDescription(self: ctre._ctre.WPI_BaseMotorController, desc: wpi::raw_ostream) -> None
        
        
        
        :returns: description of controller
        """
        pass

    def getExpiration(self):  # real signature unknown; restored from __doc__
        """
        getExpiration(self: ctre._ctre.WPI_BaseMotorController) -> float
        
        Retrieve the timeout value for the corresponding motor safety object.
        
        :returns: the timeout value in seconds.
        """
        return 0.0

    def getInverted(self):  # real signature unknown; restored from __doc__
        """
        getInverted(self: ctre._ctre.WPI_BaseMotorController) -> bool
        
        Common interface for returning the inversion state of a speed controller.
        
        :returns: isInverted The state of inversion, true is inverted.
        """
        return False

    def getMotorSafety(self):  # real signature unknown; restored from __doc__
        """
        getMotorSafety(self: ctre._ctre.WPI_BaseMotorController) -> wpilib._wpilib.MotorSafety
        
        
        
        :returns: the Motor Safety object corresponding to this device.
        """
        pass

    def isAlive(self):  # real signature unknown; restored from __doc__
        """
        isAlive(self: ctre._ctre.WPI_BaseMotorController) -> bool
        
        Determine if the motor is still operating or has timed out.
        
        :returns: true if the motor is still operating normally and hasn't timed out.
        """
        return False

    def isSafetyEnabled(self):  # real signature unknown; restored from __doc__
        """
        isSafetyEnabled(self: ctre._ctre.WPI_BaseMotorController) -> bool
        
        Return the state of the motor safety enabled flag.
        
        Return if the motor safety is currently enabled for this device.
        
        :returns: True if motor safety is enforced for this device.
        """
        return False

    def PIDWrite(self, output):  # real signature unknown; restored from __doc__
        """
        PIDWrite(self: ctre._ctre.WPI_BaseMotorController, output: float) -> None
        
        Special write for PID, same functionality as calling set
        
        :param output: Output to send to motor
        """
        pass

    def set(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        set(*args, **kwargs)
        Overloaded function.
        
        1. set(self: ctre._ctre.WPI_BaseMotorController, speed: float) -> None
        
        Common interface for setting the speed of a simple speed controller.
        
        :param speed: The speed to set.  Value should be between -1.0 and 1.0.
             Value is also saved for Get().
        
        2. set(self: ctre._ctre.WPI_BaseMotorController, mode: ctre._ctre.ControlMode, value: float) -> None
        
        Sets the appropriate output on the talon, depending on the mode.
        
        :param mode: The output mode to apply.
             In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
             In Current mode, output value is in amperes.
             In Velocity mode, output value is in position change / 100ms.
             In Position mode, output value is in encoder ticks or an analog value,
             depending on the sensor.
             In Follower mode, the output value is the integer device ID of the talon to
             duplicate.
        
        :param value: The setpoint value, as described above.
        
        
             Standard Driving Example:
             _talonLeft.set(ControlMode.PercentOutput, leftJoy);
             _talonRght.set(ControlMode.PercentOutput, rghtJoy);
        
        3. set(self: ctre._ctre.WPI_BaseMotorController, mode: ctre._ctre.ControlMode, demand0: float, demand1: float) -> None
        
        @deprecated use 4 parameter set
        
        :param mode: Sets the appropriate output on the talon, depending on the mode.
        
        :param demand0: The output value to apply.
               such as advanced feed forward and/or auxiliary close-looping in firmware.
               In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
               In Current mode, output value is in amperes.
               In Velocity mode, output value is in position change / 100ms.
               In Position mode, output value is in encoder ticks or an analog value,
               depending on the sensor. See
               In Follower mode, the output value is the integer device ID of the talon to
               duplicate.
        
        :param demand1: Supplemental value.  This will also be control mode specific for future features.
        
        4. set(self: ctre._ctre.WPI_BaseMotorController, mode: ctre._ctre.ControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        
        
        
        :param mode: Sets the appropriate output on the talon, depending on the mode.
        
        :param demand0: The output value to apply.
                   such as advanced feed forward and/or auxiliary close-looping in firmware.
                   In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
                   In Current mode, output value is in amperes.
                   In Velocity mode, output value is in position change / 100ms.
                   In Position mode, output value is in encoder ticks or an analog value,
                   depending on the sensor. See
                   In Follower mode, the output value is the integer device ID of the talon to
                   duplicate.
        
        :param demand1Type: The demand type for demand1.
                   Neutral: Ignore demand1 and apply no change to the demand0 output.
                   AuxPID: Use demand1 to set the target for the auxiliary PID 1.
                   ArbitraryFeedForward: Use demand1 as an arbitrary additive value to the
                   demand0 output.  In PercentOutput the demand0 output is the motor output,
                   and in closed-loop modes the demand0 output is the output of PID0.
        
        :param demand1: Supplmental output value.  Units match the set mode.
        
        
                   Arcade Drive Example:
                   _talonLeft.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, +joyTurn);
                   _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, -joyTurn);
        
                   Drive Straight Example:
                   Note: Selected Sensor Configuration is necessary for both PID0 and PID1.
                   _talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
                   _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.AuxPID, desiredRobotHeading);
        
                   Drive Straight to a Distance Example:
                   Note: Other configurations (sensor selection, PID gains, etc.) need to be set.
                   _talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
                   _talonRght.set(ControlMode.MotionMagic, targetDistance, DemandType.AuxPID, desiredRobotHeading);
        """
        pass

    def setExpiration(self, expirationTime):  # real signature unknown; restored from __doc__
        """
        setExpiration(self: ctre._ctre.WPI_BaseMotorController, expirationTime: float) -> None
        
        Set the expiration time for the corresponding motor safety object.
        
        :param expirationTime: The timeout value in seconds.
        """
        pass

    def setInverted(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        setInverted(*args, **kwargs)
        Overloaded function.
        
        1. setInverted(self: ctre._ctre.WPI_BaseMotorController, isInverted: bool) -> None
        
        Common interface for inverting direction of a speed controller.
        
        :param isInverted: The state of inversion, true is inverted.
        
        2. setInverted(self: ctre._ctre.WPI_BaseMotorController, invertType: ctre._ctre.InvertType) -> None
        
        Common interface for inverting direction of a speed controller.
        
        :param invertType: The invert strategy to use. Follower controllers
                  that mirror/oppose the master controller should
                  use this method.
        """
        pass

    def setSafetyEnabled(self, enabled):  # real signature unknown; restored from __doc__
        """
        setSafetyEnabled(self: ctre._ctre.WPI_BaseMotorController, enabled: bool) -> None
        
        Enable/disable motor safety for this device.
        
        Turn on and off the motor safety option for this PWM object.
        
        :param enabled: True if motor safety is enforced for this object.
        """
        pass

    def setVoltage(self, output):  # real signature unknown; restored from __doc__
        """
        setVoltage(self: ctre._ctre.WPI_BaseMotorController, output: volts) -> None
        
        Sets the voltage output of the SpeedController.  Compensates for
        the current bus voltage to ensure that the desired voltage is output even
        if the battery voltage is below 12V - highly useful when the voltage
        outputs are "meaningful" (e.g. they come from a feedforward calculation).
        
        NOTE: This function *must* be called regularly in order for voltage
        compensation to work properly - unlike the ordinary set function, it is not
        "set it and forget it."
        
        :param output: The voltage to output.
        """
        pass

    def stopMotor(self):  # real signature unknown; restored from __doc__
        """
        stopMotor(self: ctre._ctre.WPI_BaseMotorController) -> None
        
        Common interface to stop the motor until Set is called again.
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass
