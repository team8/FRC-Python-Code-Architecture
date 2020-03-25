
class VictorSPXControlMode():
    """
    Choose the control mode for a Victor SPX.
    
    Members:
    
      PercentOutput : Percent output [-1,1]
    
      Position : Position closed loop
    
      Velocity : Velocity closed loop
    
      Follower : Follow other motor controller
    
      MotionProfile : Motion Profile
    
      MotionMagic : Motion Magic
    
      MotionProfileArc : Motion Profile with auxiliary output
    
      Disabled : Disable Motor Controller
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.VictorSPXControlMode, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.VictorSPXControlMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.VictorSPXControlMode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Disabled = VictorSPXControlMode.Disabled
    Follower = VictorSPXControlMode.Follower
    MotionMagic = VictorSPXControlMode.MotionMagic
    MotionProfile = VictorSPXControlMode.MotionProfile
    MotionProfileArc = VictorSPXControlMode.MotionProfileArc
    PercentOutput = VictorSPXControlMode.PercentOutput
    Position = VictorSPXControlMode.Position
    Velocity = VictorSPXControlMode.Velocity
    __entries = {
        'Disabled': (
            VictorSPXControlMode.Disabled,
            'Disable Motor Controller',
        ),
        'Follower': (
            VictorSPXControlMode.Follower,
            'Follow other motor controller',
        ),
        'MotionMagic': (
            VictorSPXControlMode.MotionMagic,
            'Motion Magic',
        ),
        'MotionProfile': (
            VictorSPXControlMode.MotionProfile,
            'Motion Profile',
        ),
        'MotionProfileArc': (
            VictorSPXControlMode.MotionProfileArc,
            'Motion Profile with auxiliary output',
        ),
        'PercentOutput': (
            VictorSPXControlMode.PercentOutput,
            'Percent output [-1,1]',
        ),
        'Position': (
            VictorSPXControlMode.Position,
            'Position closed loop',
        ),
        'Velocity': (
            VictorSPXControlMode.Velocity,
            'Velocity closed loop',
        ),
    }
    __members__ = {
        'Disabled': VictorSPXControlMode.Disabled,
        'Follower': VictorSPXControlMode.Follower,
        'MotionMagic': VictorSPXControlMode.MotionMagic,
        'MotionProfile': VictorSPXControlMode.MotionProfile,
        'MotionProfileArc': VictorSPXControlMode.MotionProfileArc,
        'PercentOutput': VictorSPXControlMode.PercentOutput,
        'Position': VictorSPXControlMode.Position,
        'Velocity': VictorSPXControlMode.Velocity,
    }


