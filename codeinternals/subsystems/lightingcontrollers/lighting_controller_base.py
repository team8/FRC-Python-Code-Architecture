from wpilib._wpilib import Timer


class LightingControllerBase:
    timer = Timer()

    def update(self) -> []:
        pass

    def isFinished(self) -> bool:
        pass
