# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class FilterConfiguration(__pybind11_builtins.pybind11_object):
    """ Configurations for filters """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.FilterConfiguration) -> str
        
        
        
        :returns: string representation of currently selected configs
        
        2. toString(self: ctre._ctre.FilterConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: string representation fo currently selected configs
        """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.FilterConfiguration) -> None """
        pass

    remoteSensorDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Remote Sensor's device ID"""

    remoteSensorSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The remote sensor device and signal type to bind."""
