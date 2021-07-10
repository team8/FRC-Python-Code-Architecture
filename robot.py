import wpilib

import user_input
import user_robot_code
from robot import writer, reader, robot_state

from subsystems import drive, lighting


# The file is already written, nothing needs to be done here. Write your code in user_robot_code.py!
# noinspection PyPep8Naming
class Robot(wpilib.TimedRobot):

    def robotInit(self):
        """Happens on code deployment"""

    def autonomousInit(self):
        writer.reset_devices()
        writer.configure_subsystems()

        self.routine = user_robot_code.auto_robot_code()

        drive.start()
        lighting.start()

    def autonomousPeriodic(self):
        reader.update_state()
        self.update_user_input()

        if len(self.routine) == 0:
            return

        self.routine[0].update()
        if self.routine[0].finished():
            self.routine.pop(0)

        drive.update()
        lighting.update()
        writer.update_subsystems()

    def teleopInit(self):
        writer.reset_devices()
        writer.configure_subsystems()

        drive.start()
        lighting.start()

    def teleopPeriodic(self):
        reader.update_state()
        self.update_user_input()

        user_robot_code.teleop_robot_code()

        drive.update()
        lighting.update()
        writer.update_subsystems()

    def update_user_input(self):
        user_input.turn_joystick = robot_state.turn_joystick_x
        user_input.drive_joystick = robot_state.drive_joystick_x


if __name__ == "__main__":
    wpilib.run(Robot)
