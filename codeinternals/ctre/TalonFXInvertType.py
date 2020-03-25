
class TalonFXInvertType():
    """
    Choose the invert type for a Talon FX based integrated motor controller.
    CCW is the equivalent of SetInverted(false), CW is the equivalent of SetInverted(true).
    FollowMaster/OpposeMaster will match/oppose a master Talon/Victor.  This requires device to be configured as a follower.
    
    Members:
    
      CounterClockwise : //!< Same as SetInverted(false)
    
      Clockwise : //!< Same as SetInverted(true)
    
      FollowMaster : //!< Follow the invert of the master this MC is following.
    
      OpposeMaster : //!< Opposite of the invert of the master this MC is following.
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
        """ __init__(self: ctre._ctre.TalonFXInvertType, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.TalonFXInvertType) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.TalonFXInvertType, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Clockwise = TalonFXInvertType.Clockwise
    CounterClockwise = TalonFXInvertType.CounterClockwise
    FollowMaster = TalonFXInvertType.FollowMaster
    OpposeMaster = TalonFXInvertType.OpposeMaster
    __entries = {
        'Clockwise': (
            TalonFXInvertType.Clockwise,
            '//!< Same as SetInverted(true)',
        ),
        'CounterClockwise': (
            TalonFXInvertType.CounterClockwise,
            '//!< Same as SetInverted(false)',
        ),
        'FollowMaster': (
            TalonFXInvertType.FollowMaster,
            '//!< Follow the invert of the master this MC is following.',
        ),
        'OpposeMaster': (
            TalonFXInvertType.OpposeMaster,
            '//!< Opposite of the invert of the master this MC is following.',
        ),
    }
    __members__ = {
        'Clockwise': TalonFXInvertType.Clockwise,
        'CounterClockwise': TalonFXInvertType.CounterClockwise,
        'FollowMaster': TalonFXInvertType.FollowMaster,
        'OpposeMaster': TalonFXInvertType.OpposeMaster,
    }


