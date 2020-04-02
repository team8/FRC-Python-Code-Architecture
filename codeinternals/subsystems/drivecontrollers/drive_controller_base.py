from codeinternals.utils import drive_outputs

class DriveControllerBase:
    def update(self) -> drive_outputs.DriveOutputs:
        pass

    def checkFinished(self) -> bool:
        pass
