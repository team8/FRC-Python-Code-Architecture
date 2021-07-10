from enum import Enum
from wpilib._wpilib import AddressableLED
from hardware import lighting_constants
from hardware import port_constants
from robot import commands, robot_state
from subsystems.controllers.fade_in_fade_out_controller import FadeInFadeOutController
from subsystems.controllers.flashing_lights_controller import FlashingLightsController
from subsystems.controllers.one_color_controller import OneColorController
from utils import color


class State(Enum):
    IDLE = 0
    SHOOTING = 1


global led_buffer
global controller
global __wanted_state
global is_new_state
global is_controller_finished

def start():
    global led_buffer
    global controller
    controller = None
    led_buffer = [AddressableLED.LEDData(0, 0, 0)] * lighting_constants.led_length


def update():
    global led_buffer
    global controller
    global __wanted_state
    global is_new_state
    global is_controller_finished
    __wanted_state = commands.wanted_lighting_state
    is_new_state = robot_state.lighting_state != __wanted_state
    state = __wanted_state
    is_controller_finished = True if controller is None else controller.isFinished()
    if is_new_state and is_controller_finished:
        if state == State.IDLE:
            controller = OneColorController(color.off)

        elif state == State.SHOOTING:
            controller = FadeInFadeOutController(color.green, 10)

    if controller.isFinished():
        controller = OneColorController(color.off)

    led_buffer = controller.update(led_buffer)
