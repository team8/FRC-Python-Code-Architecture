# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class LimitSwitchRoutines(__pybind11_builtins.pybind11_object):
    """ Class to handle various functions regarding limit switches """
    def isRemote(self, limitSwitchSource): # real signature unknown; restored from __doc__
        """
        isRemote(limitSwitchSource: ctre._ctre.LimitSwitchSource) -> bool
        
        Checks if a limit switch is one of the remote values
        (i.e. RemoteTalonSRX or RemoteCANifier)
        
        :param limitSwitchSource: limitSwitchSource to check
        
        :returns: true if it's a remote limit switch source
        """
        return False

    def promote(self, limitSwitchSource): # real signature unknown; restored from __doc__
        """
        promote(limitSwitchSource: ctre._ctre.RemoteLimitSwitchSource) -> ctre._ctre.LimitSwitchSource
        
        Takes a RemoteLimitSwitchSource and brings it up to a LimitSwitchSource
        
        :param limitSwitchSource: LimitSwitchSource to promote
        
        :returns: promoted limitSwitchSource
        """
        pass

    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(value: ctre._ctre.LimitSwitchSource) -> str
        
        
        
        :param value: LimitSwitchSource to get the string value of
        
        :returns: string representation of value
        
        2. toString(value: ctre._ctre.RemoteLimitSwitchSource) -> str
        
        
        
        :param value: LimitSwitchSource to get the string value of
        
        :returns: string representation of value
        
        3. toString(value: ctre._ctre.LimitSwitchNormal) -> str
        
        
        
        :param value: LimitSwitchNormal to get the string value of
        
        :returns: string representation of value
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.LimitSwitchRoutines) -> None """
        pass


