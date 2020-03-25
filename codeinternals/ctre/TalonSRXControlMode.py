
class TalonSRXControlMode():
    """
    Choose the control mode for a Talon SRX.
    
    Members:
    
      PercentOutput : Percent output [-1,1]
    
      Position : Position closed loop
    
      Velocity : Velocity closed loop
    
      Current : Input current closed loop
    
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
        """ __init__(self: ctre._ctre.TalonSRXControlMode, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.TalonSRXControlMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.TalonSRXControlMode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Current = TalonSRXControlMode.Current
    Disabled = TalonSRXControlMode.Disabled
    Follower = TalonSRXControlMode.Follower
    MotionMagic = TalonSRXControlMode.MotionMagic
    MotionProfile = TalonSRXControlMode.MotionProfile
    MotionProfileArc = TalonSRXControlMode.MotionProfileArc
    PercentOutput = TalonSRXControlMode.PercentOutput
    Position = TalonSRXControlMode.Position
    Velocity = TalonSRXControlMode.Velocity
    __entries = {
        'Current': (
            TalonSRXControlMode.Current,
            'Input current closed loop',
        ),
        'Disabled': (
            TalonSRXControlMode.Disabled,
            'Disable Motor Controller',
        ),
        'Follower': (
            TalonSRXControlMode.Follower,
            'Follow other motor controller',
        ),
        'MotionMagic': (
            TalonSRXControlMode.MotionMagic,
            'Motion Magic',
        ),
        'MotionProfile': (
            TalonSRXControlMode.MotionProfile,
            'Motion Profile',
        ),
        'MotionProfileArc': (
            TalonSRXControlMode.MotionProfileArc,
            'Motion Profile with auxiliary output',
        ),
        'PercentOutput': (
            TalonSRXControlMode.PercentOutput,
            'Percent output [-1,1]',
        ),
        'Position': (
            TalonSRXControlMode.Position,
            'Position closed loop',
        ),
        'Velocity': (
            TalonSRXControlMode.Velocity,
            'Velocity closed loop',
        ),
    }
    __members__ = {
        'Current': TalonSRXControlMode.Current,
        'Disabled': TalonSRXControlMode.Disabled,
        'Follower': TalonSRXControlMode.Follower,
        'MotionMagic': TalonSRXControlMode.MotionMagic,
        'MotionProfile': TalonSRXControlMode.MotionProfile,
        'MotionProfileArc': TalonSRXControlMode.MotionProfileArc,
        'PercentOutput': TalonSRXControlMode.PercentOutput,
        'Position': TalonSRXControlMode.Position,
        'Velocity': TalonSRXControlMode.Velocity,
    }


