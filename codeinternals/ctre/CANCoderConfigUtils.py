# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


from .CustomParamConfigUtil import CustomParamConfigUtil

class CANCoderConfigUtils(CustomParamConfigUtil):
    """ Util class to help with configuring CANCoder """
    def absoluteSensorRangeDifferent(self, settings): # real signature unknown; restored from __doc__
        """ absoluteSensorRangeDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def initializationStrategyDifferent(self, settings): # real signature unknown; restored from __doc__
        """ initializationStrategyDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def magnetOffsetDegreesDifferent(self, settings): # real signature unknown; restored from __doc__
        """ magnetOffsetDegreesDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def sensorCoefficientDifferent(self, settings): # real signature unknown; restored from __doc__
        """ sensorCoefficientDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def sensorDirectionDifferent(self, settings): # real signature unknown; restored from __doc__
        """ sensorDirectionDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def sensorTimeBaseDifferent(self, settings): # real signature unknown; restored from __doc__
        """ sensorTimeBaseDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def unitStringDifferent(self, settings): # real signature unknown; restored from __doc__
        """ unitStringDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def velocityMeasurementPeriodDifferent(self, settings): # real signature unknown; restored from __doc__
        """
        velocityMeasurementPeriodDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool
        
        Determine if specified value is different from default
        
        :param settings: settings to compare against
        
        :returns: if specified value is different from default
                  @{
        """
        return False

    def velocityMeasurementWindowDifferent(self, settings): # real signature unknown; restored from __doc__
        """ velocityMeasurementWindowDifferent(settings: ctre._ctre.CANCoderConfiguration) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.CANCoderConfigUtils) -> None """
        pass


