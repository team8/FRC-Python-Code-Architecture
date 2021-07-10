from robot import robot_state
from hardware import drive_hardware
from hardware import joysticks


def update_state():
    def update_drive():
        robot_state.gyro_compass_heading_degrees = drive_hardware.gyro.getCompassHeading()
        robot_state.active_trajectory_position = 0
        #robot_state.active_trajectory_position = drive_hardware.right_master_falcon.getActiveTrajectoryPosition()
        robot_state.drive_joystick_y = -joysticks.drive_joystick.getY()
        robot_state.drive_joystick_x = -joysticks.drive_joystick.getX()
        robot_state.turn_joystick_x = joysticks.turnJoystick.getX()
        print("updated red drive")

    update_drive()
