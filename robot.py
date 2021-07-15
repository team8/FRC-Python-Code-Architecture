import wpilib

from hardware import *

# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming
class Robot(wpilib.TimedRobot):

    def robotInit(self):
        left_slave.follow(left_master)
        right_slave.follow(right_master)

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
