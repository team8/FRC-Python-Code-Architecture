from codeinternals.utils.controller_outputs import ControllerOutputs


class DriveOutputs:
    def __init__(self):
        self.__leftOutput = ControllerOutputs()
        self.__rightOutput = ControllerOutputs()
