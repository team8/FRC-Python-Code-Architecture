import wpilib

from robot import writer
from robot import reader

from subsystems import drive

# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
class Robot(wpilib.TimedRobot):
    def robotInit(self):
        """Happens on code deployment"""

    def autonomousInit(self):
        """Happens at beginning of autonomous sequence"""

    def autonomousPeriodic(self):
        """Called every 20ms through autonomous period"""

    def teleopInit(self):
        writer.reset_devices()

        drive.update()

        HardwareWriter.configureSubsystems()

    def teleopPeriodic(self):
        HardwareReader.updateState()
        for subsystem in self.enabledSystems: subsystem.update()
        HardwareWriter.updateSubsystems()


if __name__ == "__main__":
    wpilib.run(Robot)
