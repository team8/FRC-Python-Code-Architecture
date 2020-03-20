from wpilib._wpilib import Joystick



class HardwareAdapter:
    class DriveHardware:
        TalonFX(0)

    class JoystickHardware:
        driveJoystick = Joystick(0)
        turnJoystick = Joystick(1)