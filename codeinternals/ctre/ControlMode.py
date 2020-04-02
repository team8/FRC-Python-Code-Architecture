# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class ControlMode(__pybind11_builtins.pybind11_object):
    """
    Choose the control mode for a motor controller.
    Consult product specific documentation to determine what is available/supported.
    
    Members:
    
      PercentOutput : Percent output [-1,1]
    
      Position : Position closed loop
    
      Velocity : Velocity closed loop
    
      Current : Input current closed loop
    
      Follower : Follow other motor controller
    
      MotionProfile : Motion Profile
    
      MotionMagic : Motion Magic
    
      MotionProfileArc : Motion Profile with auxiliary output
    
      MusicTone : Plays a single tone.  Frequency (hz) is passed into set.
    
      Disabled : Disable Motor Controller
    """

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.ControlMode, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.ControlMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.ControlMode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Current = ControlMode.Current
    Disabled = ControlMode.Disabled
    Follower = ControlMode.Follower
    MotionMagic = ControlMode.MotionMagic
    MotionProfile = ControlMode.MotionProfile
    MotionProfileArc = ControlMode.MotionProfileArc
    MusicTone = ControlMode.MusicTone
    PercentOutput = ControlMode.PercentOutput
    Position = ControlMode.Position
    Velocity = ControlMode.Velocity
    __entries = {
        'Current': (
            ControlMode.Current,
            'Input current closed loop',
        ),
        'Disabled': (
            ControlMode.Disabled,
            'Disable Motor Controller',
        ),
        'Follower': (
            ControlMode.Follower,
            'Follow other motor controller',
        ),
        'MotionMagic': (
            ControlMode.MotionMagic,
            'Motion Magic',
        ),
        'MotionProfile': (
            ControlMode.MotionProfile,
            'Motion Profile',
        ),
        'MotionProfileArc': (
            ControlMode.MotionProfileArc,
            'Motion Profile with auxiliary output',
        ),
        'MusicTone': (
            ControlMode.MusicTone,
            'Plays a single tone.  Frequency (hz) is passed into set.',
        ),
        'PercentOutput': (
            ControlMode.PercentOutput,
            'Percent output [-1,1]',
        ),
        'Position': (
            ControlMode.Position,
            'Position closed loop',
        ),
        'Velocity': (
            ControlMode.Velocity,
            'Velocity closed loop',
        ),
    }
    __members__ = {
        'Current': ControlMode.Current,
        'Disabled': ControlMode.Disabled,
        'Follower': ControlMode.Follower,
        'MotionMagic': ControlMode.MotionMagic,
        'MotionProfile': ControlMode.MotionProfile,
        'MotionProfileArc': ControlMode.MotionProfileArc,
        'MusicTone': ControlMode.MusicTone,
        'PercentOutput': ControlMode.PercentOutput,
        'Position': ControlMode.Position,
        'Velocity': ControlMode.Velocity,
    }
