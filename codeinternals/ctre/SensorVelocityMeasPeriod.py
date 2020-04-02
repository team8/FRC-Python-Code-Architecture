# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class SensorVelocityMeasPeriod(__pybind11_builtins.pybind11_object):
    """
    Enumerate filter periods for any sensor that measures velocity.
    
    Members:
    
      Period_1Ms : 1ms velocity measurement period
    
      Period_2Ms : 2ms velocity measurement period
    
      Period_5Ms : 5ms velocity measurement period
    
      Period_10Ms : 10ms velocity measurement period
    
      Period_20Ms : 20ms velocity measurement period
    
      Period_25Ms : 25ms velocity measurement period
    
      Period_50Ms : 50ms velocity measurement period
    
      Period_100Ms : 100ms velocity measurement period
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
        """ __init__(self: ctre._ctre.SensorVelocityMeasPeriod, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.SensorVelocityMeasPeriod) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.SensorVelocityMeasPeriod, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    Period_100Ms = SensorVelocityMeasPeriod.Period_100Ms
    Period_10Ms = SensorVelocityMeasPeriod.Period_10Ms
    Period_1Ms = SensorVelocityMeasPeriod.Period_1Ms
    Period_20Ms = SensorVelocityMeasPeriod.Period_20Ms
    Period_25Ms = SensorVelocityMeasPeriod.Period_25Ms
    Period_2Ms = SensorVelocityMeasPeriod.Period_2Ms
    Period_50Ms = SensorVelocityMeasPeriod.Period_50Ms
    Period_5Ms = SensorVelocityMeasPeriod.Period_5Ms
    __entries = {
        'Period_100Ms': (
            SensorVelocityMeasPeriod.Period_100Ms,
            '100ms velocity measurement period',
        ),
        'Period_10Ms': (
            SensorVelocityMeasPeriod.Period_10Ms,
            '10ms velocity measurement period',
        ),
        'Period_1Ms': (
            SensorVelocityMeasPeriod.Period_1Ms,
            '1ms velocity measurement period',
        ),
        'Period_20Ms': (
            SensorVelocityMeasPeriod.Period_20Ms,
            '20ms velocity measurement period',
        ),
        'Period_25Ms': (
            SensorVelocityMeasPeriod.Period_25Ms,
            '25ms velocity measurement period',
        ),
        'Period_2Ms': (
            SensorVelocityMeasPeriod.Period_2Ms,
            '2ms velocity measurement period',
        ),
        'Period_50Ms': (
            SensorVelocityMeasPeriod.Period_50Ms,
            '50ms velocity measurement period',
        ),
        'Period_5Ms': (
            SensorVelocityMeasPeriod.Period_5Ms,
            '5ms velocity measurement period',
        ),
    }
    __members__ = {
        'Period_100Ms': SensorVelocityMeasPeriod.Period_100Ms,
        'Period_10Ms': SensorVelocityMeasPeriod.Period_10Ms,
        'Period_1Ms': SensorVelocityMeasPeriod.Period_1Ms,
        'Period_20Ms': SensorVelocityMeasPeriod.Period_20Ms,
        'Period_25Ms': SensorVelocityMeasPeriod.Period_25Ms,
        'Period_2Ms': SensorVelocityMeasPeriod.Period_2Ms,
        'Period_50Ms': SensorVelocityMeasPeriod.Period_50Ms,
        'Period_5Ms': SensorVelocityMeasPeriod.Period_5Ms,
    }
