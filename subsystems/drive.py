from enum import Enum
from robot import writer
from robot import commands

from subsystems.controllers.move_straight_controller import MoveStraightController
from subsystems.controllers.turn_controller import TurnYawController
from subsystems.controllers.joystick_drive_controller import JoystickDriveController


class State(Enum):
    IDLE = 0
    MOVE_STRAIGHT = 1
    TURN = 2
    JOYSTICK_DRIVE = 3


global wanted_state
global is_new_state
global drive_state
global is_controller_finished
global controller
global state
global outputs
global wanted_state
global is_new_state
global drive_state
global is_controller_finished
global controller
global state

def start():
    global wanted_state
    global is_new_state
    global drive_state
    global is_controller_finished
    global controller
    global state
    global outputs

    wanted_state = None
    is_new_state = False
    drive_state = None
    is_controller_finished = True
    controller = None
    state = State.MOVE_STRAIGHT
    outputs = None


def update():
    writer.reset_devices()

    global wanted_state
    global is_new_state
    global drive_state
    global is_controller_finished
    global controller
    global state
    global outputs

    wanted_state = commands.wanted_drive_state
    is_new_state = wanted_state != drive_state
    is_controller_finished = True if controller is None else controller.checkFinished()

    if is_new_state and is_controller_finished:
        state = wanted_state
        if state is None:
            controller = None
        if state == State.IDLE:
            controller = None
        if state == State.MOVE_STRAIGHT:
            controller = MoveStraightController(commands.wanted_target_distance)
        if state == State.TURN:
            controller = TurnYawController(commands.wanted_turn_angle)
        if state == State.JOYSTICK_DRIVE:
            controller = JoystickDriveController()

    if controller is None:
        outputs = None
    else:
        outputs = controller.update()
