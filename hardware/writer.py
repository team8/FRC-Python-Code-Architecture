from hardware import drive


def reset_devices():
    def reset_gyro():
        drive.gyro.setCompassAngle(0)

    reset_gyro()
