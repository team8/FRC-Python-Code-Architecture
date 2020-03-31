class PIDController:
    """ Implements a PID control loop. """

    def atSetpoint(self):  # real signature unknown; restored from __doc__
        """
        atSetpoint(self: wpilib.controller._controller.PIDController) -> bool

        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
        return False

    def calculate(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        calculate(*args, **kwargs)
        Overloaded function.

        1. calculate(self: wpilib.controller._controller.PIDController, measurement: float) -> float

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        2. calculate(self: wpilib.controller._controller.PIDController, measurement: float, setpoint: float) -> float

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        :param setpoint: The new setpoint of the controller.
        """
        pass

    def disableContinuousInput(self):  # real signature unknown; restored from __doc__
        """
        disableContinuousInput(self: wpilib.controller._controller.PIDController) -> None

        Disables continuous input.
        """
        pass

    def enableContinuousInput(self, minimumInput, maximumInput):  # real signature unknown; restored from __doc__
        """
        enableContinuousInput(self: wpilib.controller._controller.PIDController, minimumInput: float, maximumInput: float) -> None

        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.

        :param maximumInput: The maximum value expected from the input.
        """
        pass

    def getD(self):  # real signature unknown; restored from __doc__
        """
        getD(self: wpilib.controller._controller.PIDController) -> float

        Gets the differential coefficient.

        :returns: differential coefficient
        """
        return 0.0

    def getI(self):  # real signature unknown; restored from __doc__
        """
        getI(self: wpilib.controller._controller.PIDController) -> float

        Gets the integral coefficient.

        :returns: integral coefficient
        """
        return 0.0

    def getP(self):  # real signature unknown; restored from __doc__
        """
        getP(self: wpilib.controller._controller.PIDController) -> float

        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
        return 0.0

    def getPeriod(self):  # real signature unknown; restored from __doc__
        """
        getPeriod(self: wpilib.controller._controller.PIDController) -> seconds

        Gets the period of this controller.

        :returns: The period of the controller.
        """
        pass

    def getPositionError(self):  # real signature unknown; restored from __doc__
        """
        getPositionError(self: wpilib.controller._controller.PIDController) -> float

        Returns the difference between the setpoint and the measurement.
        """
        return 0.0

    def getSetpoint(self):  # real signature unknown; restored from __doc__
        """
        getSetpoint(self: wpilib.controller._controller.PIDController) -> float

        Returns the current setpoint of the PIDController.

        :returns: The current setpoint.
        """
        return 0.0

    def getVelocityError(self):  # real signature unknown; restored from __doc__
        """
        getVelocityError(self: wpilib.controller._controller.PIDController) -> float

        Returns the velocity error.
        """
        return 0.0

    def initSendable(self, builder):  # real signature unknown; restored from __doc__
        """ initSendable(self: wpilib.controller._controller.PIDController, builder: wpilib._wpilib.SendableBuilder) -> None """
        pass

    def reset(self):  # real signature unknown; restored from __doc__
        """
        reset(self: wpilib.controller._controller.PIDController) -> None

        Reset the previous error, the integral term, and disable the controller.
        """
        pass

    def setD(self, Kd):  # real signature unknown; restored from __doc__
        """
        setD(self: wpilib.controller._controller.PIDController, Kd: float) -> None

        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
        pass

    def setI(self, Ki):  # real signature unknown; restored from __doc__
        """
        setI(self: wpilib.controller._controller.PIDController, Ki: float) -> None

        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
        pass

    def setIntegratorRange(self, minimumIntegral, maximumIntegral):  # real signature unknown; restored from __doc__
        """
        setIntegratorRange(self: wpilib.controller._controller.PIDController, minimumIntegral: float, maximumIntegral: float) -> None

        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.

        :param maximumIntegral: The maximum value of the integrator.
        """
        pass

    def setP(self, Kp):  # real signature unknown; restored from __doc__
        """
        setP(self: wpilib.controller._controller.PIDController, Kp: float) -> None

        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
        pass

    def setPID(self, Kp, Ki, Kd):  # real signature unknown; restored from __doc__
        """
        setPID(self: wpilib.controller._controller.PIDController, Kp: float, Ki: float, Kd: float) -> None

        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient

        :param Ki: Integral coefficient

        :param Kd: Differential coefficient
        """
        pass

    def setSetpoint(self, setpoint):  # real signature unknown; restored from __doc__
        """
        setSetpoint(self: wpilib.controller._controller.PIDController, setpoint: float) -> None

        Sets the setpoint for the PIDController.

        :param setpoint: The desired setpoint.
        """
        pass

    def setTolerance(self, positionTolerance, velocityTolerance=None):  # real signature unknown; restored from __doc__
        """
        setTolerance(self: wpilib.controller._controller.PIDController, positionTolerance: float, velocityTolerance: float = inf) -> None

        Sets the error which is considered tolerable for use with AtSetpoint().

        :param positionTolerance: Position error which is tolerable.

        :param velociytTolerance: Velocity error which is tolerable.
        """
        pass

    def _getContinuousError(self, error):  # real signature unknown; restored from __doc__
        """
        _getContinuousError(self: wpilib.controller._controller.PIDController, error: float) -> float

        Wraps error around for continuous inputs. The original error is returned if
        continuous mode is disabled.

        :param error: The current error of the PID controller.

        :returns: Error for continuous inputs.
        """
        return 0.0

    def __init__(self, Kp, Ki, Kd, period=0.02):  # real signature unknown; restored from __doc__
        """
        __init__(self: wpilib.controller._controller.PIDController, Kp: float, Ki: float, Kd: float, period: seconds = 0.02) -> None

        Allocates a PIDController with the given constants for Kp, Ki, and Kd.

        :param Kp: The proportional coefficient.

        :param Ki: The integral coefficient.

        :param Kd: The derivative coefficient.

        :param period: The period between controller updates in seconds. The
              default is 20 milliseconds.
        """
        pass
