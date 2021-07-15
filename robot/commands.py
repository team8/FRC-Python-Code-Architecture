from subsystems import drive
from subsystems import intake

wanted_drive_state = None
wanted_turn_angle = 0
wanted_turn_distance = 0
wanted_lighting_state = None  # TODO: get lighting ready
wanted_target_distance = 0
wanted_intake_state = intake.State.RUNNING
wanted_intake_po = 0.7
