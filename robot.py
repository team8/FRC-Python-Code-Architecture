from enum import Enum

import wpilib


class RobotName(Enum):
    NARI = 0
    OSR = 1


# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming
class Robot(wpilib.TimedRobot):

    def robotInit(self):
        """Happens on code deployment"""

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
