# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class SlotConfiguration(__pybind11_builtins.pybind11_object):
    """ Configurables available to a slot """
    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.SlotConfiguration) -> str
        
        
        
        :returns: String representation of configs
        
        2. toString(self: ctre._ctre.SlotConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.SlotConfiguration) -> None """
        pass

    allowableClosedloopError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allowable closed loop error to neutral (in native units)"""

    closedLoopPeakOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Peak output from closed loop [0,1]"""

    closedLoopPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Desired period of closed loop [1,64]ms"""

    integralZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Integral zone (in native units)

If the (absolute) closed-loop error is outside of this zone, integral
accumulator is automatically cleared. This ensures than integral wind up
events will stop after the sensor gets far enough from its target."""

    kD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """D Gain

This is multiplied by derivative error (sensor units per PID loop, typically 1ms).
Note the closed loop output interprets a final value of 1023 as full output.
So use a gain of '250' to get full output if derr is 4096u (Mag Encoder 1 rotation) per 1000 loops (typ 1 sec)"""

    kF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """F Gain

See documentation for calculation details.
If using velocity, motion magic, or motion profile,
use (1023 * duty-cycle / sensor-velocity-sensor-units-per-100ms)."""

    kI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """I Gain

This is multiplied by accumulated closed loop error in sensor units every PID Loop.
Note the closed loop output interprets a final value of 1023 as full output.
So use a gain of '0.00025' to get full output if err is 4096u for 1000 loops (accumulater holds 4,096,000),
[which is equivalent to one CTRE mag encoder rotation for 1000 milliseconds]."""

    kP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """P Gain

This is multiplied by closed loop error in sensor units.
Note the closed loop output interprets a final value of 1023 as full output.
So use a gain of '0.25' to get full output if err is 4096u (Mag Encoder 1 rotation)"""

    maxIntegralAccumulator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Max integral accumulator (in native units)"""



