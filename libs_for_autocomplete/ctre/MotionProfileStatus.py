# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class MotionProfileStatus(__pybind11_builtins.pybind11_object):
    """
    Motion Profile Status
    This is simply a data transer object.
    """

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.MotionProfileStatus) -> None """
        pass

    activePointValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the active trajectory point is not empty, false otherwise.
The members in activePoint are only valid if this signal is set."""

    btledBufferCnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of points in the low level Talon/Victor buffer."""

    hasUnderrun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set if isUnderrun ever gets set.
Can be manually cleared by ClearMotionProfileHasUnderrun() or automatically cleared by StartMotionProfile().
@see clearMotionProfileHasUnderrun()"""

    isLast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the active trajectory point is the last point of the profile"""

    isUnderrun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is set if Talon/Victor needs to shift a point from its buffer into
the active trajectory point however the buffer is empty. This gets cleared
automatically when is resolved."""

    outputEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current output mode of the motion profile executer (disabled, enabled, or hold).
When changing the set() value in MP mode, it's important to check this signal to
confirm the change takes effect before interacting with the top buffer."""

    profileSlotSelect0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The selected PID[0] profile slot of current profile"""

    profileSlotSelect1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The selected auxiliary PID[1] profile slot of current profile"""

    timeDurMs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applied duration of the active trajectory point"""

    topBufferCnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of points in the top trajectory buffer."""

    topBufferRem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The available empty slots in the trajectory buffer.

The robot API holds a "top buffer" of trajectory points, so your applicaion
can dump several points at once.  The API will then stream them into the Talon's
low-level buffer, allowing the Talon to act on them."""
