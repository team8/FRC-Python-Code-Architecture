import wpilib

from hardware import *
from drive_time import *
from bang_bang_turn import *

# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming

#Write your robot code in the following methods

#Init functions run when it is first executed
#Periodic functions run every 20ms when still enabled

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        pass

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
