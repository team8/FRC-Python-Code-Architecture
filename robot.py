import wpilib

from hardware import *
from drive_time import *
from bang_bang_turn import *

# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming
class Robot(wpilib.TimedRobot):

    def robotInit(self):
        left_slave.follow(left_master)
        left_slave_2.follow(left_master)
        right_slave.follow(right_master)
        right_slave_2.follow(right_master)
        gyro.calibrate()

    def autonomousInit(self):
        self.routines = {BangBangTurn(90)}
        self.current_routine = None

    def autonomousPeriodic(self):
        if self.current_routine is None:
            if len(self.routines) != 0:
                self.current_routine = self.routines.pop()

        self.current_routine.update()

        if self.current_routine.is_done():
            self.current_routine = None

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        left_master.set(0.75*(drive_joystick.getY()/2 - turn_joystick.getX()/2))
        right_master.set(-0.75*(drive_joystick.getY()/2 + turn_joystick.getX()/2))


if __name__ == "__main__":
    wpilib.run(Robot)
