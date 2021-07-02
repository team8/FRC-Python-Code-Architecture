from utils.controller_outputs import ControllerOutputs


class DriveOutputs:
    left_output = ControllerOutputs()
    right_output = ControllerOutputs()

    def getInstance(self):
        return self
