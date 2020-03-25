# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


from .BasePIDSetConfiguration import BasePIDSetConfiguration

class BaseTalonPIDSetConfiguration(BasePIDSetConfiguration):
    """ Configurables available to BaseTalon's PID """
    def toString(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.BaseTalonPIDSetConfiguration) -> str
        
        
        
        :returns: string representation of configs
        
        2. toString(self: ctre._ctre.BaseTalonPIDSetConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to configs
        
        :returns: String representation of configs
        """
        pass

    def __init__(self, defaultFeedbackDevice): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BaseTalonPIDSetConfiguration, defaultFeedbackDevice: ctre._ctre.FeedbackDevice) -> None """
        pass

    selectedFeedbackSensor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback device for a particular PID loop.
Note the FeedbackDevice enum holds all possible sensor types.  Consult product documentation to confirm what is available.
Alternatively the product specific enum can be used instead.
@code
configs.primaryPID.selectedFeedbackSensor = (FeedbackDevice)TalonSRXFeedbackDevice::QuadEncoder;
configs.primaryPID.selectedFeedbackSensor = (FeedbackDevice)TalonFXFeedbackDevice::IntegratedSensor;
@endcode"""



