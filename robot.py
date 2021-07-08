import wpilib

import user_robot_code
from robot import writer
from robot import reader

from subsystems import drive


# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming
class Robot(wpilib.TimedRobot):

    def robotInit(self):
        """Happens on code deployment"""

    def autonomousInit(self):
        writer.reset_devices()
        writer.configure_subsystems()


    def autonomousPeriodic(self):
        reader.update_state()

        user_robot_code.auto_robot_code()

        drive.update()

        writer.update_subsystems()

    def teleopInit(self):
        writer.reset_devices()
        writer.configure_subsystems()

    def teleopPeriodic(self):
        reader.update_state()

        user_robot_code.teleop_robot_code()

        drive.update()

        writer.update_subsystems()


if __name__ == "__main__":
    wpilib.run(Robot)
