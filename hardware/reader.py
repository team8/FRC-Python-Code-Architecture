from hardware import robot_state
from hardware import drive
from hardware import joysticks


def update_state():
    def update_drive():
        robot_state.gyro_compass_heading_degrees = drive.gyro.getCompassHeading()
        robot_state.active_trajectory_position = drive.right_master_falcon.getActiveTrajectoryPosition()
        robot_state.drive_joystick_y = -joysticks.drive_joystick.getY()
        robot_state.drive_joystick_x = -joysticks.drive_joystick.getX()
        robot_state.turn_joystick_x = joysticks.turnJoystick.getX()

    update_drive()
