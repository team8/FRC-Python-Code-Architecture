import wpilib

from codeinternals.hardware_reader import HardwareReader
from codeinternals.hardware_writer import HardwareWriter
from codeinternals.subsystems.drive import Drive
from codeinternals.subsystems.lighting import Lighting


class Robot(wpilib.TimedRobot):
    enabledSystems = [Drive.getInstance(), Lighting.getInstance()]

    def robotInit(self):

        """Happens on code deployment"""

    def autonomousInit(self):
        """Happens at beginning of autonomous sequence"""

    def autonomousPeriodic(self):
        """Called every 20ms through autonomous period"""

    def teleopInit(self):
        HardwareReader.configureState()
        for subsystem in self.enabledSystems: subsystem.start()
        HardwareWriter.configureSubsystems()

    def teleopPeriodic(self):
        HardwareReader.updateState()
        for subsystem in self.enabledSystems: subsystem.update()
        HardwareWriter.updateSubsystems()


if __name__ == "__main__":
    wpilib.run(Robot)
