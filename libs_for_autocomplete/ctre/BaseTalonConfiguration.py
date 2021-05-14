# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports

from .BaseMotorControllerConfiguration import BaseMotorControllerConfiguration


class BaseTalonConfiguration(BaseMotorControllerConfiguration):
    """ Configurables available to BaseTalon """

    def toString(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        toString(*args, **kwargs)
        Overloaded function.
        
        1. toString(self: ctre._ctre.BaseTalonConfiguration) -> str
        
        
        
        :returns: String representation of all the configs
        
        2. toString(self: ctre._ctre.BaseTalonConfiguration, prependString: str) -> str
        
        
        
        :param prependString: String to prepend to all the configs
        
        :returns: String representation of all the configs
        """
        pass

    def __init__(self, defaultFeedbackDevice):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BaseTalonConfiguration, defaultFeedbackDevice: ctre._ctre.FeedbackDevice) -> None """
        pass

    auxiliaryPID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Auxiliary PID configuration"""

    diff0Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Diff 0 Term
Note the FeedbackDevice enum holds all possible sensor types.  Consult product documentation to confirm what is available.
Alternatively the product specific enum can be used instead.
@code
configs.diff0Term = (FeedbackDevice)TalonSRXFeedbackDevice::QuadEncoder;
configs.diff0Term = (FeedbackDevice)TalonFXFeedbackDevice::IntegratedSensor;
@endcode"""

    diff1Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Diff 1 Term
Note the FeedbackDevice enum holds all possible sensor types.  Consult product documentation to confirm what is available.
Alternatively the product specific enum can be used instead.
@code
configs.diff1Term = (FeedbackDevice)TalonSRXFeedbackDevice::QuadEncoder;
configs.diff1Term = (FeedbackDevice)TalonFXFeedbackDevice::IntegratedSensor;
@endcode"""

    forwardLimitSwitchDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward limit switch device ID

Limit Switch device id isn't used unless device is a remote"""

    forwardLimitSwitchNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward limit switch normally open/closed"""

    forwardLimitSwitchSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forward Limit Switch Source

User can choose between the feedback connector, remote Talon SRX, CANifier, or deactivate the feature"""

    primaryPID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Primary PID configuration"""

    reverseLimitSwitchDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse limit switch device ID

Limit Switch device id isn't used unless device is a remote"""

    reverseLimitSwitchNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse limit switch normally open/closed"""

    reverseLimitSwitchSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reverse Limit Switch Source

User can choose between the feedback connector, remote Talon SRX, CANifier, or deactivate the feature"""

    sum0Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Sum 0 Term
Note the FeedbackDevice enum holds all possible sensor types.  Consult product documentation to confirm what is available.
Alternatively the product specific enum can be used instead.
@code
configs.sum0Term = (FeedbackDevice)TalonSRXFeedbackDevice::QuadEncoder;
configs.sum0Term = (FeedbackDevice)TalonFXFeedbackDevice::IntegratedSensor;
@endcode"""

    sum1Term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Feedback Device for Sum 1 Term
Note the FeedbackDevice enum holds all possible sensor types.  Consult product documentation to confirm what is available.
Alternatively the product specific enum can be used instead.
@code
configs.sum1Term = (FeedbackDevice)TalonSRXFeedbackDevice::QuadEncoder;
configs.sum1Term = (FeedbackDevice)TalonFXFeedbackDevice::IntegratedSensor;
@endcode"""
