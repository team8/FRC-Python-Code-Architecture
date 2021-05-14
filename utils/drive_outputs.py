from codeinternals.utils.controller_outputs import ControllerOutputs


class DriveOutputs:
    leftOutput = ControllerOutputs()
    rightOutput = ControllerOutputs()

    def getInstance(self):
        return self
