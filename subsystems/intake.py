from enum import Enum

from constants import intake_constants
from hardware import intake_hardware
from robot import commands

from ctre import ControlMode


class State(Enum):
    RUNNING = 0
    STOWED = 1


global wanted_state
global is_new_state
global intake_state
global state


def start():
    global wanted_state
    global is_new_state
    global intake_state
    global state

    wanted_state = None
    is_new_state = False
    intake_state = None
    state = State.STOWED


def update():

    global wanted_state
    global is_new_state
    global intake_state
    global state

    wanted_state = commands.wanted_intake_state
    is_new_state = wanted_state != intake_state

    if is_new_state:
        state = wanted_state
        if state == State.RUNNING:
            intake_hardware.talon.set(ControlMode.PercentOutput, intake_constants.rollerPo)
            intake_hardware.solenoid.set(True)
        if state == State.STOWED:
            intake_hardware.talon.set(ControlMode.PercentOutput, 0)
            intake_hardware.solenoid.set(False)

