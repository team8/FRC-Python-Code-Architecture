class TrajectoryPoint():
    """
    Motion Profile Trajectory Point
    This is simply a data transfer object.
    """

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.TrajectoryPoint) -> None
        
        2. __init__(self: ctre._ctre.TrajectoryPoint, position: float, velocity: float, arbFeedFwd: float, auxiliaryPos: float, auxiliaryVel: float, auxiliaryArbFeedFwd: float, profileSlotSelect0: int, profileSlotSelect1: int, isLastPoint: bool, zeroPos: bool, timeDur: int, useAuxPID: bool) -> None
        """
        pass

    arbFeedFwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Added to the output of PID[0], should be within [-1,+1] where 0.01 = 1%."""

    auxiliaryArbFeedFwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Added to the output of PID[1], should be within [-1,+1] where 0.01 = 1%."""

    auxiliaryPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position for auxiliary PID[1] to target (in sensor units)."""

    auxiliaryVel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity for auxiliary PID[1] to target. (in sensor-units per 100ms)."""

    headingDeg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used.  Use auxiliaryPos instead.  @see auxiliaryPos"""

    isLastPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true to signal Talon that this is the final point, so do not
attempt to pop another trajectory point from out of the Talon buffer.
Instead continue processing this way point.  Typically the velocity
member variable should be zero so that the motor doesn't spin indefinitely."""

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position to servo to (in sensor units)."""

    profileSlotSelect0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Which slot to get PIDF gains.
PID is used for position servo.
F is used as the Kv constant for velocity feed-forward.
Typically this is hard-coded
to a particular slot, but you are free to gain schedule if need be.
gain schedule if need be.
Choose from [0,3]."""

    profileSlotSelect1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Which slot to get PIDF gains for auxiliary PID.
This only has impact during MotionProfileArc Control mode.
Choose from [0,3]."""

    timeDur = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Duration (ms) to apply this trajectory pt.
This time unit is ADDED to the existing base time set by
ConfigMotionProfileTrajectoryPeriod()."""

    useAuxPID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If using MotionProfileArc, this flag must be true on all points.
If using MotionProfile, this flag must be false on all points."""

    velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity to feed-forward (in sensor-units per 100ms)."""

    zeroPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true to signal Talon to zero the selected sensor.
When generating MPs, one simple method is to make the first target position zero,
and the final target position the target distance from the current position.
Then when you fire the MP, the current position gets set to zero.
If this is the intent, you can set zeroPos on the first trajectory point.

Otherwise you can leave this false for all points, and offset the positions
of all trajectory points so they are correct.

If using multiple sensor sources (Arc modes) we recommend you manually set sensor positions
before arming MP."""
