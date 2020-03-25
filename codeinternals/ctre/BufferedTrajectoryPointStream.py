# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class BufferedTrajectoryPointStream(__pybind11_builtins.pybind11_object):
    """ Stream of trajectory points for Talon/Victor motion profiling. """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear(self: ctre._ctre.BufferedTrajectoryPointStream) -> ctre._ctre.ErrorCode
        
        Clear all trajectory points.
        
        :returns: nonzero error code if operation fails.
        """
        pass

    def getHandle(self): # real signature unknown; restored from __doc__
        """
        getHandle(self: ctre._ctre.BufferedTrajectoryPointStream) -> capsule
        
        
        
        :returns: raw handle for resource management.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        write(*args, **kwargs)
        Overloaded function.
        
        1. write(self: ctre._ctre.BufferedTrajectoryPointStream, trajPt: ctre::phoenix::motion::TrajectoryPoint) -> ctre._ctre.ErrorCode
        
        Write a single trajectory point into the buffer.
        
        :returns: nonzero error code if operation fails.
        
        2. write(self: ctre._ctre.BufferedTrajectoryPointStream, trajPts: ctre::phoenix::motion::TrajectoryPoint, trajPtCount: int) -> ctre._ctre.ErrorCode
        
        Writes an array of trajectory point into the buffer.
        
        :returns: nonzero error code if operation fails.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BufferedTrajectoryPointStream) -> None """
        pass


