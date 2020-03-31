import wpilib
from wpilib.controller import PIDController

from codeinternals.hardware_reader import HardwareReader
from codeinternals.hardware_writer import HardwareWriter
from codeinternals.subsystems.drive import Drive


class Robot(wpilib.TimedRobot):
    enabledSystems = ["drive"]

    def robotInit(self):
        HardwareReader.configureState()
        HardwareWriter.configureSubsystems()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        # self.timer.reset()
        # self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    #
    # # Drive for two seconds
    # if self.timer.get() < 2.0:
    #     self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
    # else:
    #     self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        HardwareReader.updateState()
        HardwareWriter.updateSubsystems()

if __name__ == "__main__":
    wpilib.run(Robot)
