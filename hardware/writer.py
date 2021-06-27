from hardware import drive


def reset_gyro():
    drive.gyro.setCompassAngle(0)

def update_state():