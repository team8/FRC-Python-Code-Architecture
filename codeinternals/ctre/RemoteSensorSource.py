# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins
import wpilib.interfaces._interfaces as __wpilib_interfaces__interfaces
import wpilib._wpilib as __wpilib__wpilib


class RemoteSensorSource(__pybind11_builtins.pybind11_object):
    """
    Choose the remote sensor source for a motor controller
    
    Members:
    
      Off : Don't use a sensor
    
      TalonSRX_SelectedSensor : Use a sensor connected to
    a TalonSRX and configured on
    the TalonSRX
    
      Pigeon_Yaw : Use a CAN Pigeon's Yaw value
    
      Pigeon_Pitch : Use a CAN Pigeon's Pitch value
    
      Pigeon_Roll : Use a CAN Pigeon's Roll value
    
      CANifier_Quadrature : Use a quadrature sensor
    connected to a CANifier
    
      CANifier_PWMInput0 : Use a PWM sensor connected
    to CANifier's PWM0
    
      CANifier_PWMInput1 : Use a PWM sensor connected
    to CANifier's PWM1
    
      CANifier_PWMInput2 : Use a PWM sensor connected
    to CANifier's PWM2
    
      CANifier_PWMInput3 : Use a PWM sensor connected
    to CANifier's PWM3
    
      GadgeteerPigeon_Yaw : Use the yaw value of a pigeon
    connected to a talon over ribbon cable
    
      GadgeteerPigeon_Pitch : Use the pitch value of a pigeon
    connected to a talon over ribbon cable
    
      GadgeteerPigeon_Roll : Use the roll value of a pigeon
    connected to a talon over ribbon cable
    
      CANCoder : Use CANCoder
    
      TalonFX_SelectedSensor : Use a sensor connected to
    a TalonFX and configured on
    the TalonFX
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
        """ __init__(self: ctre._ctre.RemoteSensorSource, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.RemoteSensorSource) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: ctre._ctre.RemoteSensorSource, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    CANCoder = RemoteSensorSource.CANCoder
    CANifier_PWMInput0 = RemoteSensorSource.CANifier_PWMInput0
    CANifier_PWMInput1 = RemoteSensorSource.CANifier_PWMInput1
    CANifier_PWMInput2 = RemoteSensorSource.CANifier_PWMInput2
    CANifier_PWMInput3 = RemoteSensorSource.CANifier_PWMInput3
    CANifier_Quadrature = RemoteSensorSource.CANifier_Quadrature
    GadgeteerPigeon_Pitch = RemoteSensorSource.GadgeteerPigeon_Pitch
    GadgeteerPigeon_Roll = RemoteSensorSource.GadgeteerPigeon_Roll
    GadgeteerPigeon_Yaw = RemoteSensorSource.GadgeteerPigeon_Yaw
    Off = RemoteSensorSource.Off
    Pigeon_Pitch = RemoteSensorSource.Pigeon_Pitch
    Pigeon_Roll = RemoteSensorSource.Pigeon_Roll
    Pigeon_Yaw = RemoteSensorSource.Pigeon_Yaw
    TalonFX_SelectedSensor = RemoteSensorSource.TalonSRX_SelectedSensor
    TalonSRX_SelectedSensor = RemoteSensorSource.TalonSRX_SelectedSensor
    __entries = {
        'CANCoder': (
            RemoteSensorSource.CANCoder,
            'Use CANCoder',
        ),
        'CANifier_PWMInput0': (
            RemoteSensorSource.CANifier_PWMInput0,
            "Use a PWM sensor connected\nto CANifier's PWM0",
        ),
        'CANifier_PWMInput1': (
            RemoteSensorSource.CANifier_PWMInput1,
            "Use a PWM sensor connected\nto CANifier's PWM1",
        ),
        'CANifier_PWMInput2': (
            RemoteSensorSource.CANifier_PWMInput2,
            "Use a PWM sensor connected\nto CANifier's PWM2",
        ),
        'CANifier_PWMInput3': (
            RemoteSensorSource.CANifier_PWMInput3,
            "Use a PWM sensor connected\nto CANifier's PWM3",
        ),
        'CANifier_Quadrature': (
            RemoteSensorSource.CANifier_Quadrature,
            'Use a quadrature sensor\nconnected to a CANifier',
        ),
        'GadgeteerPigeon_Pitch': (
            RemoteSensorSource.GadgeteerPigeon_Pitch,
            'Use the pitch value of a pigeon\nconnected to a talon over ribbon cable',
        ),
        'GadgeteerPigeon_Roll': (
            RemoteSensorSource.GadgeteerPigeon_Roll,
            'Use the roll value of a pigeon\nconnected to a talon over ribbon cable',
        ),
        'GadgeteerPigeon_Yaw': (
            RemoteSensorSource.GadgeteerPigeon_Yaw,
            'Use the yaw value of a pigeon\nconnected to a talon over ribbon cable',
        ),
        'Off': (
            RemoteSensorSource.Off,
            "Don't use a sensor",
        ),
        'Pigeon_Pitch': (
            RemoteSensorSource.Pigeon_Pitch,
            "Use a CAN Pigeon's Pitch value",
        ),
        'Pigeon_Roll': (
            RemoteSensorSource.Pigeon_Roll,
            "Use a CAN Pigeon's Roll value",
        ),
        'Pigeon_Yaw': (
            RemoteSensorSource.Pigeon_Yaw,
            "Use a CAN Pigeon's Yaw value",
        ),
        'TalonFX_SelectedSensor': (
            RemoteSensorSource.TalonSRX_SelectedSensor,
            'Use a sensor connected to\na TalonFX and configured on\nthe TalonFX',
        ),
        'TalonSRX_SelectedSensor': (
            '<value is a self-reference, replaced by this string>',
            'Use a sensor connected to\na TalonSRX and configured on\nthe TalonSRX',
        ),
    }
    __members__ = {
        'CANCoder': RemoteSensorSource.CANCoder,
        'CANifier_PWMInput0': RemoteSensorSource.CANifier_PWMInput0,
        'CANifier_PWMInput1': RemoteSensorSource.CANifier_PWMInput1,
        'CANifier_PWMInput2': RemoteSensorSource.CANifier_PWMInput2,
        'CANifier_PWMInput3': RemoteSensorSource.CANifier_PWMInput3,
        'CANifier_Quadrature': RemoteSensorSource.CANifier_Quadrature,
        'GadgeteerPigeon_Pitch': RemoteSensorSource.GadgeteerPigeon_Pitch,
        'GadgeteerPigeon_Roll': RemoteSensorSource.GadgeteerPigeon_Roll,
        'GadgeteerPigeon_Yaw': RemoteSensorSource.GadgeteerPigeon_Yaw,
        'Off': RemoteSensorSource.Off,
        'Pigeon_Pitch': RemoteSensorSource.Pigeon_Pitch,
        'Pigeon_Roll': RemoteSensorSource.Pigeon_Roll,
        'Pigeon_Yaw': RemoteSensorSource.Pigeon_Yaw,
        'TalonFX_SelectedSensor': RemoteSensorSource.TalonSRX_SelectedSensor,
        'TalonSRX_SelectedSensor': '<value is a self-reference, replaced by this string>',
    }


