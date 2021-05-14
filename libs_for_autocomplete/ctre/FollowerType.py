class FollowerType():
    """
    Choose the type of follower
    
    Members:
    
      PercentOutput : Follow the percentOutput the master is using
    
      AuxOutput1 : Follow the auxiliary output the master is
    calculating. Used for 2-axis control.
    This typically means apply PID0 - PID1 from master.
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
        """ __init__(self: ctre._ctre.FollowerType, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.FollowerType) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.FollowerType, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    AuxOutput1 = FollowerType.AuxOutput1
    PercentOutput = FollowerType.PercentOutput
    __entries = {
        'AuxOutput1': (
            FollowerType.AuxOutput1,
            'Follow the auxiliary output the master is\ncalculating. Used for 2-axis control.\nThis typically means apply PID0 - PID1 from master.',
        ),
        'PercentOutput': (
            FollowerType.PercentOutput,
            'Follow the percentOutput the master is using',
        ),
    }
    __members__ = {
        'AuxOutput1': FollowerType.AuxOutput1,
        'PercentOutput': FollowerType.PercentOutput,
    }
