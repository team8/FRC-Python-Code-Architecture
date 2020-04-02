# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports

from .CustomParamConfigUtil import CustomParamConfigUtil


class BaseMotorControllerUtil(CustomParamConfigUtil):
    """ Util class to help with Base Motor Controller configs """

    def auxPIDPolarityDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ auxPIDPolarityDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def clearPositionOnLimitFDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ clearPositionOnLimitFDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def clearPositionOnLimitRDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ clearPositionOnLimitRDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def clearPositionOnQuadIdxDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ clearPositionOnQuadIdxDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def closedloopRampDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ closedloopRampDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def feedbackNotContinuousDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ feedbackNotContinuousDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def forwardSoftLimitEnableDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ forwardSoftLimitEnableDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def forwardSoftLimitThresholdDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ forwardSoftLimitThresholdDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def limitSwitchDisableNeutralOnLOSDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ limitSwitchDisableNeutralOnLOSDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def motionAccelerationDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ motionAccelerationDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def motionCruiseVelocityDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ motionCruiseVelocityDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def motionProfileTrajectoryPeriodDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ motionProfileTrajectoryPeriodDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def motionSCurveStrength(self, settings):  # real signature unknown; restored from __doc__
        """ motionSCurveStrength(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def neutralDeadbandDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ neutralDeadbandDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def nominalOutputForwardDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ nominalOutputForwardDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def nominalOutputReverseDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ nominalOutputReverseDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def openloopRampDifferent(self, settings):  # real signature unknown; restored from __doc__
        """
        openloopRampDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool
        
        Determine if specified value is different from default
        
        :param settings: settings to compare against
        
        :returns: if specified value is different from default
                  @{
        """
        return False

    def peakOutputForwardDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ peakOutputForwardDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def peakOutputReverseDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ peakOutputReverseDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def pulseWidthPeriod_EdgesPerRotDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ pulseWidthPeriod_EdgesPerRotDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def pulseWidthPeriod_FilterWindowSzDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ pulseWidthPeriod_FilterWindowSzDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def remoteSensorClosedLoopDisableNeutralOnLOSDifferent(self,
                                                           settings):  # real signature unknown; restored from __doc__
        """ remoteSensorClosedLoopDisableNeutralOnLOSDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def reverseSoftLimitEnableDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ reverseSoftLimitEnableDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def reverseSoftLimitThresholdDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ reverseSoftLimitThresholdDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def softLimitDisableNeutralOnLOSDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ softLimitDisableNeutralOnLOSDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def trajectoryInterpolationEnableDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ trajectoryInterpolationEnableDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def velocityMeasurementPeriodDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ velocityMeasurementPeriodDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def velocityMeasurementWindowDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ velocityMeasurementWindowDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def voltageCompSaturationDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ voltageCompSaturationDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def voltageMeasurementFilterDifferent(self, settings):  # real signature unknown; restored from __doc__
        """ voltageMeasurementFilterDifferent(settings: ctre._ctre.BaseMotorControllerConfiguration) -> bool """
        return False

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.BaseMotorControllerUtil) -> None """
        pass
