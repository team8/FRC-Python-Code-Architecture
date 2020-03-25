from wpilib._wpilib import Joystick

from codeinternals import ctre


class HardwareAdapter:
    class DriveHardware:
        leftTalonMaster = ctre.TalonFX(0);
        rightTalonMaster = ctre.TalonFX(1);
        leftMiddleTalonSlave = ctre.TalonFX(2);
        #todo Finish


    class JoystickHardware:
        driveJoystick = Joystick(0)
        turnJoystick = Joystick(1)