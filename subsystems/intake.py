from enum import Enum
from robot import writer
from robot import commands
from robot import robot_state

from utils.controller_outputs import ControllerOutputs


class State(Enum):
    RUNNING = 0
    STOWED = 1


global wanted_state
global is_new_state
global intake_state
global controller
global state
global outputs
global solenoid_output
falcon_output = ControllerOutputs()

def start():
    global wanted_state
    global is_new_state
    global intake_state
    global controller
    global state
    global outputs
    global solenoid_output

    wanted_state = None
    is_new_state = False
    intake_state = None
    controller = None
    state = State.STOWED
    outputs = None


def update():
    writer.reset_devices()

    global wanted_state
    global is_new_state
    global intake_state
    global controller
    global state
    global outputs
    global solenoid_output

    wanted_state = commands.wanted_intake_state
    is_new_state = wanted_state != intake_state

    if is_new_state:
        state = wanted_state
        if state is None:
            controller = None
        if state == State.RUNNING:
            if not robot_state.intake_transitioning and robot_state.intake_extended:
                falcon_output.setPercentageOutput(commands.wanted_intake_po)
            else:
                falcon_output.setIdle()
            solenoid_output = True
            controller = 'Running'
        if state == State.STOWED:
            falcon_output.setIdle()
            solenoid_output = False
            controller = 'Stowed'

    if controller is None:
        outputs = None
    else:
        outputs = falcon_output
