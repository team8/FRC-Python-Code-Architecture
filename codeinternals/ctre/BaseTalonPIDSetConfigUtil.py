# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class BaseTalonPIDSetConfigUtil(__pybind11_builtins.pybind11_object):
    """ Util class to help with BaseTalon's PID configs """
    def selectedFeedbackCoefficientDifferent(self, settings): # real signature unknown; restored from __doc__
        """ selectedFeedbackCoefficientDifferent(settings: ctre._ctre.BaseTalonPIDSetConfiguration) -> bool """
        return False

    def selectedFeedbackSensorDifferent(self, settings): # real signature unknown; restored from __doc__
        """
        selectedFeedbackSensorDifferent(settings: ctre._ctre.BaseTalonPIDSetConfiguration) -> bool
        
        Determine if specified value is different from default
        
        :param settings: settings to compare against
        
        :returns: if specified value is different from default
                  @{
        """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BaseTalonPIDSetConfigUtil) -> None """
        pass


