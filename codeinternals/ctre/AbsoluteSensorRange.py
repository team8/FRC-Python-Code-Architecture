
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class AbsoluteSensorRange():
    """
    Enum for how to range the absolute sensor position.
    
    Members:
    
      Unsigned_0_to_360 : Express the absolute position as an unsigned value.
    E.g. [0,+1) rotations or [0,360) deg.
    
      Signed_PlusMinus180 : Express the absolute position as an signed value.
    E.g. [-0.5,+0.5) rotations or [-180,+180) deg.
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
        """ __init__(self: ctre._ctre.AbsoluteSensorRange, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.AbsoluteSensorRange) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.AbsoluteSensorRange, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    Signed_PlusMinus180 = AbsoluteSensorRange.Signed_PlusMinus180
    Unsigned_0_to_360 = AbsoluteSensorRange.Unsigned_0_to_360
    __entries = {
        'Signed_PlusMinus180': (
            AbsoluteSensorRange.Signed_PlusMinus180,
            'Express the absolute position as an signed value.\nE.g. [-0.5,+0.5) rotations or [-180,+180) deg.',
        ),
        'Unsigned_0_to_360': (
            AbsoluteSensorRange.Unsigned_0_to_360,
            'Express the absolute position as an unsigned value.\nE.g. [0,+1) rotations or [0,360) deg.',
        ),
    }
    __members__ = {
        'Signed_PlusMinus180': AbsoluteSensorRange.Signed_PlusMinus180,
        'Unsigned_0_to_360': AbsoluteSensorRange.Unsigned_0_to_360,
    }


