import wpilib

from hardware import *
from drive_time import *


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
        self.routines = {DriveForward(3000)}
        self.current_routine = None

    def teleopPeriodic(self):
        print(self.current_routine)
        if self.current_routine is None:
            if len(self.routines) != 0:
                self.current_routine = self.routines.pop()

        print(self.current_routine)
        self.current_routine.update()

        print(self.current_routine)
        if self.current_routine.is_done():
            self.current_routine = None
        print(self.current_routine)


if __name__ == "__main__":
    wpilib.run(Robot)
