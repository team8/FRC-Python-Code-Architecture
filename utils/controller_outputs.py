from constants import drive_constants
from utils.gains import Gains
from ctre import TalonFXControlMode


class ControllerOutputs:
    __controlMode = TalonFXControlMode.Disabled
    __gains = Gains(0.0, 0.0, 0.0, 0.0, 0.0)
    __reference = 0.0

    def setPercentageOutput(self, output):
        self.__reference = output
        self.__gains = None
        self.__controlMode = TalonFXControlMode.PercentOutput

    def setTargetVelocity(self, targetVelocity, gains: Gains):
        self.__reference = targetVelocity / drive_constants.velocityConversionFactor
        self.__gains = gains
        self.__controlMode = TalonFXControlMode.Velocity

    def setTargetPosition(self, targetPosition, gains: Gains):
        self.__reference = targetPosition / drive_constants.positionConversionFactor
        self.__gains = gains
        self.__controlMode = TalonFXControlMode.Position

    def setMotionMagicTargetPosition(self, targetPosition, gains: Gains):
        self.__reference = targetPosition / drive_constants.positionConversionFactor
        self.__gains = gains
        self.__controlMode = TalonFXControlMode.MotionMagic

    def setIdle(self):
        self.setPercentageOutput(0)

    def getControlMode(self):
        return self.__controlMode

    def getGains(self):
        return self.__gains

    def getReference(self):
        return self.__reference
