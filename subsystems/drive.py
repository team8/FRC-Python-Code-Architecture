from enum import Enum

from hardware_reader import HardwareReader
from subsystems.drivecontrollers.joystick_drive_controller import JoystickDriveController
from subsystems.drivecontrollers.move_straight_controller import MoveStraightController
from subsystems.drivecontrollers.turn_controller import TurnYawController
from subsystems.subsystem_base import SubsystemBase


class Drive(SubsystemBase):
    class State(Enum):
        IDLE = 0
        MOVE_STRAIGHT = 1
        TURN = 2
        JOYSTICK_DRIVE = 3

    def start(self):
        self.instance = Drive()

    def update(self, commands, state):
        HardwareReader.resetGyro()
        self.__wantedState = commands.getDriveWantedState()
        self.isNewState = self.state != self.__wantedState
        self.isControllerFinished = True if self.controller is None else (
            True if self.controller.checkFinished() else False)
        if self.isNewState and self.isControllerFinished:
            self.state = self.__wantedState
            if self.state == Drive.State.IDLE:
                self.controller = None
            elif self.state == Drive.State.MOVE_STRAIGHT:
                self.controller = MoveStraightController(commands.wantedTargetDistance)
            elif self.state == Drive.State.TURN:
                self.controller = TurnYawController(commands.wantedTurnAngle)
            elif self.state == Drive.State.JOYSTICK_DRIVE:
                self.controller = JoystickDriveController()
        if self.controller is None:
            self.outputs = None
        else:
            self.outputs = self.controller.update()

    def getOutput(self):
        return self.outputs

    def getInstance(self):
        return self.instance
