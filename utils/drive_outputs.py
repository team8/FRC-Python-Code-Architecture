from utils.controller_outputs import ControllerOutputs
from utils.gains import Gains


class DriveOutputs:
    __drive_gains = Gains(0.016, 0.0, 0.0, 0.0294, 0.0)
    left_output = ControllerOutputs(__drive_gains)
    right_output = ControllerOutputs(__drive_gains)

