import enum
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
