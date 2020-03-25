# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class CustomParamConfiguration(__pybind11_builtins.pybind11_object):
    """ Configurables for any custom param configs """
    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.CustomParamConfiguration) -> str
        
        
        
        :returns: string representation of currently selected configs
        
        2. toString(self: ctre._ctre.CustomParamConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: string representation fo currently selected configs
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.CustomParamConfiguration) -> None """
        pass

    customParam0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom Param 0"""

    customParam1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom Param 1"""

    enableOptimizations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable optimizations for ConfigAll (defaults true)"""



