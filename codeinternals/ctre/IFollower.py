# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class IFollower(__pybind11_builtins.pybind11_object):
    """ Interface for followers """
    def follow(self, masterToFollow, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        follow(self: ctre._ctre.IFollower, masterToFollow: ctre::phoenix::motorcontrol::IMotorController) -> None
        
        Set the control mode and output value so that this motor controller will
        follow another motor controller. Currently supports following Victor SPX
        and Talon SRX.
        
        :param masterToFollow: Motor Controller object to follow.
        """
        pass

    def valueUpdated(self): # real signature unknown; restored from __doc__
        """
        valueUpdated(self: ctre._ctre.IFollower) -> None
        
        When master makes a device, this routine is called to signal the update.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.IFollower) -> None """
        pass


