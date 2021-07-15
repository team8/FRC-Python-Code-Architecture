from internals.utils.controller_outputs import ControllerOutputs


class DriveOutputs:
    def __init__(self, drive_gains):
        self.left_output = ControllerOutputs(drive_gains)
        self.right_output = ControllerOutputs(drive_gains)
