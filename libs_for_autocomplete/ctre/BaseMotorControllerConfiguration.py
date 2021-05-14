# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports

from .CustomParamConfiguration import CustomParamConfiguration


class BaseMotorControllerConfiguration(CustomParamConfiguration):
    """ Configurables available to base motor controllers """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.BaseMotorControllerConfiguration) -> str
        
        
        
        :returns: String representation of configs
        
        2. toString(self: ctre._ctre.BaseMotorControllerConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BaseMotorControllerConfiguration) -> None """
        pass

    auxPIDPolarity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PID polarity inversion

Standard Polarity:
Primary Output = PID0 + PID1,
Auxiliary Output = PID0 - PID1,

Inverted Polarity:
Primary Output = PID0 - PID1,
Auxiliary Output = PID0 + PID1,"""

    clearPositionOnLimitF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Clear the position on forward limit"""

    clearPositionOnLimitR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Clear the position on reverse limit"""

    clearPositionOnQuadIdx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Clear the position on index"""

    closedloopRamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Seconds to go from 0 to full in closed loop"""

    feedbackNotContinuous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine whether feedback sensor is continuous or not"""

    forwardSoftLimitEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable forward soft limit"""

    forwardSoftLimitThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Threshold for soft limits in forward direction (in raw sensor units)"""

    limitSwitchDisableNeutralOnLOS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Disable neutral'ing the motor when remote limit switch is lost on CAN bus"""

    motionAcceleration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Motion Magic acceleration in (raw sensor units per 100 ms) per second."""

    motionCruiseVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Motion Magic cruise velocity in raw sensor units per 100 ms."""

    motionCurveStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Zero to use trapezoidal motion during motion magic.  [1,8] for S-Curve, higher value for greater smoothing."""

    motionProfileTrajectoryPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Motion profile base trajectory period in milliseconds.

The period specified in a trajectory point will be
added on to this value"""

    neutralDeadband = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Neutral deadband [0.001, 0.25]"""

    nominalOutputForward = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nominal/Minimum output in forward direction [0,1]"""

    nominalOutputReverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nominal/Minimum output in reverse direction [-1,0]"""

    openloopRamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Seconds to go from 0 to full in open loop"""

    peakOutputForward = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Peak output in forward direction [0,1]"""

    peakOutputReverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Peak output in reverse direction [-1,0]"""

    pulseWidthPeriod_EdgesPerRot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of edges per rotation for a tachometer sensor"""

    pulseWidthPeriod_FilterWindowSz = property(lambda self: object(), lambda self, v: None,
                                               lambda self: None)  # default
    """Desired window size for a tachometer sensor"""

    remoteFilter0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for RemoteFilter 0"""

    remoteFilter1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for RemoteFilter 1"""

    remoteSensorClosedLoopDisableNeutralOnLOS = property(lambda self: object(), lambda self, v: None,
                                                         lambda self: None)  # default
    """Disable neutral'ing the motor when remote sensor is lost on CAN bus"""

    reverseSoftLimitEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable reverse soft limit"""

    reverseSoftLimitThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Threshold for soft limits in reverse direction (in raw sensor units)"""

    slot0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for slot 0"""

    slot1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for slot 1"""

    slot2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for slot 2"""

    slot3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configuration for slot 3"""

    softLimitDisableNeutralOnLOS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Disable neutral'ing the motor when remote soft limit is lost on CAN bus"""

    trajectoryInterpolationEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable motion profile trajectory point interpolation (defaults to true)."""

    velocityMeasurementPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired period for velocity measurement"""

    velocityMeasurementWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired window for velocity measurement"""

    voltageCompSaturation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is the max voltage to apply to the hbridge when voltage
compensation is enabled.  For example, if 10 (volts) is specified
and a TalonSRX is commanded to 0.5 (PercentOutput, closed-loop, etc)
then the TalonSRX will attempt to apply a duty-cycle to produce 5V."""

    voltageMeasurementFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of samples in rolling average for voltage"""
