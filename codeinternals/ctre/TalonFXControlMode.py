class TalonFXControlMode:

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
        """ __init__(self: ctre._ctre.TalonFXControlMode, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.TalonFXControlMode) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.TalonFXControlMode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Current = TalonFXControlMode.Current
    Disabled = TalonFXControlMode.Disabled
    Follower = TalonFXControlMode.Follower
    MotionMagic = TalonFXControlMode.MotionMagic
    MotionProfile = TalonFXControlMode.MotionProfile
    MotionProfileArc = TalonFXControlMode.MotionProfileArc
    MusicTone = TalonFXControlMode.MusicTone
    PercentOutput = TalonFXControlMode.PercentOutput
    Position = TalonFXControlMode.Position
    Velocity = TalonFXControlMode.Velocity
    __entries = {
        'Current': (
            TalonFXControlMode.Current,
            'Input current closed loop',
        ),
        'Disabled': (
            TalonFXControlMode.Disabled,
            'Disable Motor Controller',
        ),
        'Follower': (
            TalonFXControlMode.Follower,
            'Follow other motor controller',
        ),
        'MotionMagic': (
            TalonFXControlMode.MotionMagic,
            'Motion Magic',
        ),
        'MotionProfile': (
            TalonFXControlMode.MotionProfile,
            'Motion Profile',
        ),
        'MotionProfileArc': (
            TalonFXControlMode.MotionProfileArc,
            'Motion Profile with auxiliary output',
        ),
        'MusicTone': (
            TalonFXControlMode.MusicTone,
            'Plays a single tone.  Frequency (hz) is passed into set.',
        ),
        'PercentOutput': (
            TalonFXControlMode.PercentOutput,
            'Percent output [-1,1]',
        ),
        'Position': (
            TalonFXControlMode.Position,
            'Position closed loop',
        ),
        'Velocity': (
            TalonFXControlMode.Velocity,
            'Velocity closed loop',
        ),
    }
    __members__ = {
        'Current': TalonFXControlMode.Current,
        'Disabled': TalonFXControlMode.Disabled,
        'Follower': TalonFXControlMode.Follower,
        'MotionMagic': TalonFXControlMode.MotionMagic,
        'MotionProfile': TalonFXControlMode.MotionProfile,
        'MotionProfileArc': TalonFXControlMode.MotionProfileArc,
        'MusicTone': TalonFXControlMode.MusicTone,
        'PercentOutput': TalonFXControlMode.PercentOutput,
        'Position': TalonFXControlMode.Position,
        'Velocity': TalonFXControlMode.Velocity,
    }
