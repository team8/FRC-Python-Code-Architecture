from codeinternals.ctre import TalonFXControlMode


class ControllerOutputs:
    __controlMode = TalonFXControlMode.Disabled
    __gains = None
    __reference = 0.0

    def setPercentageOutput(self, output):
        self.__reference = output
        self.__gains = None
        self.__controlMode = TalonFXControlMode.PercentOutput

    def setTargetVelocity(self, targetVelocity, gains):
        self.__reference = targetVelocity
        self.__gains = gains
        self.__controlMode = TalonFXControlMode.Velocity

    def setTargetPosition(self, targetPosition, gains):
        self.__reference = targetPosition
        self.__gains = gains
        self.__controlMode = TalonFXControlMode.Position

    def setIdle(self):
        self.setPercentageOutput(0)
