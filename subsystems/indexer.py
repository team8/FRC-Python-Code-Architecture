import enum
from robot import commands, robot_state
from subsystems.controllers.index_controllers import FeedColumnController, IndexColumnController, ReverseFeedColumnController, UnIndexColumnController
# Using enum class create enumerations

class Inedexer():
    class ColumnState(enum.Enum):
        Index = 0,
        Un_index = 1,
        Feed = 2,
        Reverse_feed = 3,
        Idle = 4

    class VSingulatorState(enum.Enum):
        Forward = 0,
        Reverse = 1,
        Idle = 2,
    global mRunningController
    global mMasterIndexerColumnOutput
    global mSlaveIndexerColumnOutput
    global mRightVTalonOutput
    global mLeftVTalonOutput
    global mBlockingSolenoidOutput
    global mHopperSolenoidOutput

    def update(self, commands):
        isNewColumnState = mRunningController == None or mRunningController.isFinished(robot_state)

        if(isNewColumnState):
            switcher = {
                0: IndexColumnController(),
                1: UnIndexColumnController(),
                2: FeedColumnController(),
                3: ReverseFeedColumnController(),
                4: None
        }
