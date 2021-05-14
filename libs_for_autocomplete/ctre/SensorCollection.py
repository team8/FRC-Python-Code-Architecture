# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class SensorCollection(__pybind11_builtins.pybind11_object):
    """
    Collection of sensors available to a motor controller.
    
    For best performance and update-rate,
    we recommend using the configSelectedFeedbackSensor() and getSelectedSensor*() routines.
    However there are occasions where accessing raw sensor values may be useful or convenient.
    Particularly if you are seeding one sensor based on another, or need to circumvent sensor-phase.
    
    Use the getSensorCollection() routine inside your motor controller to create a sensor collection.
    """

    def getAnalogIn(self):  # real signature unknown; restored from __doc__
        """ getAnalogIn(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getAnalogInRaw(self):  # real signature unknown; restored from __doc__
        """ getAnalogInRaw(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getAnalogInVel(self):  # real signature unknown; restored from __doc__
        """ getAnalogInVel(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPinStateQuadA(self):  # real signature unknown; restored from __doc__
        """ getPinStateQuadA(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPinStateQuadB(self):  # real signature unknown; restored from __doc__
        """ getPinStateQuadB(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPinStateQuadIdx(self):  # real signature unknown; restored from __doc__
        """ getPinStateQuadIdx(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPulseWidthPosition(self):  # real signature unknown; restored from __doc__
        """ getPulseWidthPosition(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPulseWidthRiseToFallUs(self):  # real signature unknown; restored from __doc__
        """ getPulseWidthRiseToFallUs(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPulseWidthRiseToRiseUs(self):  # real signature unknown; restored from __doc__
        """ getPulseWidthRiseToRiseUs(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getPulseWidthVelocity(self):  # real signature unknown; restored from __doc__
        """ getPulseWidthVelocity(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getQuadraturePosition(self):  # real signature unknown; restored from __doc__
        """ getQuadraturePosition(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def getQuadratureVelocity(self):  # real signature unknown; restored from __doc__
        """ getQuadratureVelocity(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def isFwdLimitSwitchClosed(self):  # real signature unknown; restored from __doc__
        """ isFwdLimitSwitchClosed(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def isRevLimitSwitchClosed(self):  # real signature unknown; restored from __doc__
        """ isRevLimitSwitchClosed(self: ctre._ctre.SensorCollection) -> int """
        return 0

    def setAnalogPosition(self, newPosition, timeoutMs=0):  # real signature unknown; restored from __doc__
        """ setAnalogPosition(self: ctre._ctre.SensorCollection, newPosition: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode """
        pass

    def setPulseWidthPosition(self, newPosition, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        setPulseWidthPosition(self: ctre._ctre.SensorCollection, newPosition: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Sets pulse width position.
        
        :param newPosition: The position value to apply to the sensor.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                   config success and report an error if it times out.
                   If zero, no blocking or checking is performed.
        
        :returns: an ErrErrorCode
        """
        pass

    def setQuadraturePosition(self, newPosition, timeoutMs=0):  # real signature unknown; restored from __doc__
        """ setQuadraturePosition(self: ctre._ctre.SensorCollection, newPosition: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode """
        pass

    def syncQuadratureWithPulseWidth(self, bookend0, bookend1, bCrossZeroOnInterval, offset=0,
                                     timeoutMs=0):  # real signature unknown; restored from __doc__
        """ syncQuadratureWithPulseWidth(self: ctre._ctre.SensorCollection, bookend0: int, bookend1: int, bCrossZeroOnInterval: bool, offset: int = 0, timeoutMs: int = 0) -> ctre._ctre.ErrorCode """
        pass

    def __init__(self, motorController, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__(self: ctre._ctre.SensorCollection, motorController: ctre::phoenix::motorcontrol::can::BaseTalon) -> None
        
        Constructor for SensorCollection
        
        :param motorController: Talon Motor Controller to connect Collection to
        """
        pass
