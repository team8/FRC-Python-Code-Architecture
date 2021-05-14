# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class ParamEnum(__pybind11_builtins.pybind11_object):
    """
    Signal enumeration for generic signal access.
    
    Members:
    
      eOnBoot_BrakeMode
    
      eQuadFilterEn
    
      eQuadIdxPolarity
    
      eMotionProfileHasUnderrunErr
    
      eMotionProfileTrajectoryPointDurationMs
    
      eMotionProfileTrajectoryInterpolDis
    
      eStatusFramePeriod
    
      eOpenloopRamp
    
      eClosedloopRamp
    
      eNeutralDeadband
    
      ePeakPosOutput
    
      eNominalPosOutput
    
      ePeakNegOutput
    
      eNominalNegOutput
    
      eProfileParamSlot_P
    
      eProfileParamSlot_I
    
      eProfileParamSlot_D
    
      eProfileParamSlot_F
    
      eProfileParamSlot_IZone
    
      eProfileParamSlot_AllowableErr
    
      eProfileParamSlot_MaxIAccum
    
      eProfileParamSlot_PeakOutput
    
      eClearPositionOnLimitF
    
      eClearPositionOnLimitR
    
      eClearPositionOnQuadIdx
    
      eClearPosOnLimitF
    
      eClearPosOnLimitR
    
      eClearPositionOnIdx
    
      eSampleVelocityPeriod
    
      eSampleVelocityWindow
    
      eFeedbackSensorType
    
      eSelectedSensorPosition
    
      eFeedbackNotContinuous
    
      eRemoteSensorSource
    
      eRemoteSensorDeviceID
    
      eSensorTerm
    
      eRemoteSensorClosedLoopDisableNeutralOnLOS
    
      ePIDLoopPolarity
    
      ePIDLoopPeriod
    
      eSelectedSensorCoefficient
    
      eForwardSoftLimitThreshold
    
      eReverseSoftLimitThreshold
    
      eForwardSoftLimitEnable
    
      eReverseSoftLimitEnable
    
      eNominalBatteryVoltage
    
      eBatteryVoltageFilterSize
    
      eContinuousCurrentLimitAmps
    
      ePeakCurrentLimitMs
    
      ePeakCurrentLimitAmps
    
      eCurrLimit_Amps
    
      eCurrThres_Amps
    
      eCurrEnable
    
      eCurrThres_Ms
    
      eClosedLoopIAccum
    
      eCustomParam
    
      eStickyFaults
    
      eAnalogPosition
    
      eQuadraturePosition
    
      ePulseWidthPosition
    
      eIntegratedSensor
    
      eMotMag_Accel
    
      eMotMag_VelCruise
    
      eMotMag_SCurveLevel
    
      eLimitSwitchSource
    
      eLimitSwitchNormClosedAndDis
    
      eLimitSwitchDisableNeutralOnLOS
    
      eLimitSwitchRemoteDevID
    
      eSoftLimitDisableNeutralOnLOS
    
      ePulseWidthPeriod_EdgesPerRot
    
      ePulseWidthPeriod_FilterWindowSz
    
      eYawOffset
    
      eCompassOffset
    
      eBetaGain
    
      eEnableCompassFusion
    
      eGyroNoMotionCal
    
      eEnterCalibration
    
      eFusedHeadingOffset
    
      eStatusFrameRate
    
      eAccumZ
    
      eTempCompDisable
    
      eMotionMeas_tap_threshX
    
      eMotionMeas_tap_threshY
    
      eMotionMeas_tap_threshZ
    
      eMotionMeas_tap_count
    
      eMotionMeas_tap_time
    
      eMotionMeas_tap_time_multi
    
      eMotionMeas_shake_reject_thresh
    
      eMotionMeas_shake_reject_time
    
      eMotionMeas_shake_reject_timeout
    
      eUnitString
    
      eFeedbackTimeBase
    
      eDefaultConfig
    
      eFastWriteCount
    
      eWriteCount
    
      eReserved1
    
      eMotorCommutation
    
      eSensorInitStrategy
    
      eSensorDirection
    
      eMagnetOffset
    
      eSensorSync
    
      eAbsSensorRange
    """

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: ctre._ctre.ParamEnum, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.ParamEnum) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.ParamEnum, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    eAbsSensorRange = ParamEnum.eAbsSensorRange
    eAccumZ = ParamEnum.eAccumZ
    eAnalogPosition = ParamEnum.eAnalogPosition
    eBatteryVoltageFilterSize = ParamEnum.eBatteryVoltageFilterSize
    eBetaGain = ParamEnum.eBetaGain
    eClearPositionOnIdx = ParamEnum.eClearPositionOnQuadIdx
    eClearPositionOnLimitF = ParamEnum.eClearPositionOnLimitF
    eClearPositionOnLimitR = ParamEnum.eClearPositionOnLimitR
    eClearPositionOnQuadIdx = ParamEnum.eClearPositionOnQuadIdx
    eClearPosOnLimitF = ParamEnum.eClearPositionOnLimitF
    eClearPosOnLimitR = ParamEnum.eClearPositionOnLimitR
    eClosedLoopIAccum = ParamEnum.eClosedLoopIAccum
    eClosedloopRamp = ParamEnum.eClosedloopRamp
    eCompassOffset = ParamEnum.eCompassOffset
    eContinuousCurrentLimitAmps = ParamEnum.eContinuousCurrentLimitAmps
    eCurrEnable = ParamEnum.eCurrEnable
    eCurrLimit_Amps = ParamEnum.eContinuousCurrentLimitAmps
    eCurrThres_Amps = ParamEnum.ePeakCurrentLimitAmps
    eCurrThres_Ms = ParamEnum.eCurrThres_Ms
    eCustomParam = ParamEnum.eCustomParam
    eDefaultConfig = ParamEnum.eDefaultConfig
    eEnableCompassFusion = ParamEnum.eEnableCompassFusion
    eEnterCalibration = ParamEnum.eEnterCalibration
    eFastWriteCount = ParamEnum.eFastWriteCount
    eFeedbackNotContinuous = ParamEnum.eFeedbackNotContinuous
    eFeedbackSensorType = ParamEnum.eFeedbackSensorType
    eFeedbackTimeBase = ParamEnum.eFeedbackTimeBase
    eForwardSoftLimitEnable = ParamEnum.eForwardSoftLimitEnable
    eForwardSoftLimitThreshold = ParamEnum.eForwardSoftLimitThreshold
    eFusedHeadingOffset = ParamEnum.eFusedHeadingOffset
    eGyroNoMotionCal = ParamEnum.eGyroNoMotionCal
    eIntegratedSensor = ParamEnum.eIntegratedSensor
    eLimitSwitchDisableNeutralOnLOS = ParamEnum.eLimitSwitchDisableNeutralOnLOS
    eLimitSwitchNormClosedAndDis = ParamEnum.eLimitSwitchNormClosedAndDis
    eLimitSwitchRemoteDevID = ParamEnum.eLimitSwitchRemoteDevID
    eLimitSwitchSource = ParamEnum.eLimitSwitchSource
    eMagnetOffset = ParamEnum.eMagnetOffset
    eMotionMeas_shake_reject_thresh = ParamEnum.eMotionMeas_shake_reject_thresh
    eMotionMeas_shake_reject_time = ParamEnum.eMotionMeas_shake_reject_time
    eMotionMeas_shake_reject_timeout = ParamEnum.eMotionMeas_shake_reject_timeout
    eMotionMeas_tap_count = ParamEnum.eMotionMeas_tap_count
    eMotionMeas_tap_threshX = ParamEnum.eMotionMeas_tap_threshX
    eMotionMeas_tap_threshY = ParamEnum.eMotionMeas_tap_threshY
    eMotionMeas_tap_threshZ = ParamEnum.eMotionMeas_tap_threshZ
    eMotionMeas_tap_time = ParamEnum.eMotionMeas_tap_time
    eMotionMeas_tap_time_multi = ParamEnum.eMotionMeas_tap_time_multi
    eMotionProfileHasUnderrunErr = ParamEnum.eMotionProfileHasUnderrunErr
    eMotionProfileTrajectoryInterpolDis = ParamEnum.eMotionProfileTrajectoryInterpolDis
    eMotionProfileTrajectoryPointDurationMs = ParamEnum.eMotionProfileTrajectoryPointDurationMs
    eMotMag_Accel = ParamEnum.eMotMag_Accel
    eMotMag_SCurveLevel = ParamEnum.eMotMag_SCurveLevel
    eMotMag_VelCruise = ParamEnum.eMotMag_VelCruise
    eMotorCommutation = ParamEnum.eMotorCommutation
    eNeutralDeadband = ParamEnum.eNeutralDeadband
    eNominalBatteryVoltage = ParamEnum.eNominalBatteryVoltage
    eNominalNegOutput = ParamEnum.eNominalNegOutput
    eNominalPosOutput = ParamEnum.eNominalPosOutput
    eOnBoot_BrakeMode = ParamEnum.eOnBoot_BrakeMode
    eOpenloopRamp = ParamEnum.eOpenloopRamp
    ePeakCurrentLimitAmps = ParamEnum.ePeakCurrentLimitAmps
    ePeakCurrentLimitMs = ParamEnum.ePeakCurrentLimitMs
    ePeakNegOutput = ParamEnum.ePeakNegOutput
    ePeakPosOutput = ParamEnum.ePeakPosOutput
    ePIDLoopPeriod = ParamEnum.ePIDLoopPeriod
    ePIDLoopPolarity = ParamEnum.ePIDLoopPolarity
    eProfileParamSlot_AllowableErr = ParamEnum.eProfileParamSlot_AllowableErr
    eProfileParamSlot_D = ParamEnum.eProfileParamSlot_D
    eProfileParamSlot_F = ParamEnum.eProfileParamSlot_F
    eProfileParamSlot_I = ParamEnum.eProfileParamSlot_I
    eProfileParamSlot_IZone = ParamEnum.eProfileParamSlot_IZone
    eProfileParamSlot_MaxIAccum = ParamEnum.eProfileParamSlot_MaxIAccum
    eProfileParamSlot_P = ParamEnum.eProfileParamSlot_P
    eProfileParamSlot_PeakOutput = ParamEnum.eProfileParamSlot_PeakOutput
    ePulseWidthPeriod_EdgesPerRot = ParamEnum.ePulseWidthPeriod_EdgesPerRot
    ePulseWidthPeriod_FilterWindowSz = ParamEnum.ePulseWidthPeriod_FilterWindowSz
    ePulseWidthPosition = ParamEnum.ePulseWidthPosition
    eQuadFilterEn = ParamEnum.eQuadFilterEn
    eQuadIdxPolarity = ParamEnum.eQuadIdxPolarity
    eQuadraturePosition = ParamEnum.eQuadraturePosition
    eRemoteSensorClosedLoopDisableNeutralOnLOS = ParamEnum.eRemoteSensorClosedLoopDisableNeutralOnLOS
    eRemoteSensorDeviceID = ParamEnum.eRemoteSensorDeviceID
    eRemoteSensorSource = ParamEnum.eRemoteSensorSource
    eReserved1 = ParamEnum.eReserved1
    eReverseSoftLimitEnable = ParamEnum.eReverseSoftLimitEnable
    eReverseSoftLimitThreshold = ParamEnum.eReverseSoftLimitThreshold
    eSampleVelocityPeriod = ParamEnum.eSampleVelocityPeriod
    eSampleVelocityWindow = ParamEnum.eSampleVelocityWindow
    eSelectedSensorCoefficient = ParamEnum.eSelectedSensorCoefficient
    eSelectedSensorPosition = ParamEnum.eSelectedSensorPosition
    eSensorDirection = ParamEnum.eSensorDirection
    eSensorInitStrategy = ParamEnum.eSensorInitStrategy
    eSensorSync = ParamEnum.eSensorSync
    eSensorTerm = ParamEnum.eSensorTerm
    eSoftLimitDisableNeutralOnLOS = ParamEnum.eSoftLimitDisableNeutralOnLOS
    eStatusFramePeriod = ParamEnum.eStatusFramePeriod
    eStatusFrameRate = ParamEnum.eStatusFrameRate
    eStickyFaults = ParamEnum.eStickyFaults
    eTempCompDisable = ParamEnum.eTempCompDisable
    eUnitString = ParamEnum.eUnitString
    eWriteCount = ParamEnum.eWriteCount
    eYawOffset = ParamEnum.eYawOffset
    __entries = {
        'eAbsSensorRange': (
            ParamEnum.eAbsSensorRange,
            None,
        ),
        'eAccumZ': (
            ParamEnum.eAccumZ,
            None,
        ),
        'eAnalogPosition': (
            ParamEnum.eAnalogPosition,
            None,
        ),
        'eBatteryVoltageFilterSize': (
            ParamEnum.eBatteryVoltageFilterSize,
            None,
        ),
        'eBetaGain': (
            ParamEnum.eBetaGain,
            None,
        ),
        'eClearPosOnLimitF': (
            ParamEnum.eClearPositionOnLimitF,
            None,
        ),
        'eClearPosOnLimitR': (
            ParamEnum.eClearPositionOnLimitR,
            None,
        ),
        'eClearPositionOnIdx': (
            ParamEnum.eClearPositionOnQuadIdx,
            None,
        ),
        'eClearPositionOnLimitF': '<value is a self-reference, replaced by this string>',
        'eClearPositionOnLimitR': '<value is a self-reference, replaced by this string>',
        'eClearPositionOnQuadIdx': '<value is a self-reference, replaced by this string>',
        'eClosedLoopIAccum': (
            ParamEnum.eClosedLoopIAccum,
            None,
        ),
        'eClosedloopRamp': (
            ParamEnum.eClosedloopRamp,
            None,
        ),
        'eCompassOffset': (
            ParamEnum.eCompassOffset,
            None,
        ),
        'eContinuousCurrentLimitAmps': (
            ParamEnum.eContinuousCurrentLimitAmps,
            None,
        ),
        'eCurrEnable': (
            ParamEnum.eCurrEnable,
            None,
        ),
        'eCurrLimit_Amps': '<value is a self-reference, replaced by this string>',
        'eCurrThres_Amps': (
            ParamEnum.ePeakCurrentLimitAmps,
            None,
        ),
        'eCurrThres_Ms': (
            ParamEnum.eCurrThres_Ms,
            None,
        ),
        'eCustomParam': (
            ParamEnum.eCustomParam,
            None,
        ),
        'eDefaultConfig': (
            ParamEnum.eDefaultConfig,
            None,
        ),
        'eEnableCompassFusion': (
            ParamEnum.eEnableCompassFusion,
            None,
        ),
        'eEnterCalibration': (
            ParamEnum.eEnterCalibration,
            None,
        ),
        'eFastWriteCount': (
            ParamEnum.eFastWriteCount,
            None,
        ),
        'eFeedbackNotContinuous': (
            ParamEnum.eFeedbackNotContinuous,
            None,
        ),
        'eFeedbackSensorType': (
            ParamEnum.eFeedbackSensorType,
            None,
        ),
        'eFeedbackTimeBase': (
            ParamEnum.eFeedbackTimeBase,
            None,
        ),
        'eForwardSoftLimitEnable': (
            ParamEnum.eForwardSoftLimitEnable,
            None,
        ),
        'eForwardSoftLimitThreshold': (
            ParamEnum.eForwardSoftLimitThreshold,
            None,
        ),
        'eFusedHeadingOffset': (
            ParamEnum.eFusedHeadingOffset,
            None,
        ),
        'eGyroNoMotionCal': (
            ParamEnum.eGyroNoMotionCal,
            None,
        ),
        'eIntegratedSensor': (
            ParamEnum.eIntegratedSensor,
            None,
        ),
        'eLimitSwitchDisableNeutralOnLOS': (
            ParamEnum.eLimitSwitchDisableNeutralOnLOS,
            None,
        ),
        'eLimitSwitchNormClosedAndDis': (
            ParamEnum.eLimitSwitchNormClosedAndDis,
            None,
        ),
        'eLimitSwitchRemoteDevID': (
            ParamEnum.eLimitSwitchRemoteDevID,
            None,
        ),
        'eLimitSwitchSource': (
            ParamEnum.eLimitSwitchSource,
            None,
        ),
        'eMagnetOffset': (
            ParamEnum.eMagnetOffset,
            None,
        ),
        'eMotMag_Accel': (
            ParamEnum.eMotMag_Accel,
            None,
        ),
        'eMotMag_SCurveLevel': (
            ParamEnum.eMotMag_SCurveLevel,
            None,
        ),
        'eMotMag_VelCruise': (
            ParamEnum.eMotMag_VelCruise,
            None,
        ),
        'eMotionMeas_shake_reject_thresh': (
            ParamEnum.eMotionMeas_shake_reject_thresh,
            None,
        ),
        'eMotionMeas_shake_reject_time': (
            ParamEnum.eMotionMeas_shake_reject_time,
            None,
        ),
        'eMotionMeas_shake_reject_timeout': (
            ParamEnum.eMotionMeas_shake_reject_timeout,
            None,
        ),
        'eMotionMeas_tap_count': (
            ParamEnum.eMotionMeas_tap_count,
            None,
        ),
        'eMotionMeas_tap_threshX': (
            ParamEnum.eMotionMeas_tap_threshX,
            None,
        ),
        'eMotionMeas_tap_threshY': (
            ParamEnum.eMotionMeas_tap_threshY,
            None,
        ),
        'eMotionMeas_tap_threshZ': (
            ParamEnum.eMotionMeas_tap_threshZ,
            None,
        ),
        'eMotionMeas_tap_time': (
            ParamEnum.eMotionMeas_tap_time,
            None,
        ),
        'eMotionMeas_tap_time_multi': (
            ParamEnum.eMotionMeas_tap_time_multi,
            None,
        ),
        'eMotionProfileHasUnderrunErr': (
            ParamEnum.eMotionProfileHasUnderrunErr,
            None,
        ),
        'eMotionProfileTrajectoryInterpolDis': (
            ParamEnum.eMotionProfileTrajectoryInterpolDis,
            None,
        ),
        'eMotionProfileTrajectoryPointDurationMs': (
            ParamEnum.eMotionProfileTrajectoryPointDurationMs,
            None,
        ),
        'eMotorCommutation': (
            ParamEnum.eMotorCommutation,
            None,
        ),
        'eNeutralDeadband': (
            ParamEnum.eNeutralDeadband,
            None,
        ),
        'eNominalBatteryVoltage': (
            ParamEnum.eNominalBatteryVoltage,
            None,
        ),
        'eNominalNegOutput': (
            ParamEnum.eNominalNegOutput,
            None,
        ),
        'eNominalPosOutput': (
            ParamEnum.eNominalPosOutput,
            None,
        ),
        'eOnBoot_BrakeMode': (
            ParamEnum.eOnBoot_BrakeMode,
            None,
        ),
        'eOpenloopRamp': (
            ParamEnum.eOpenloopRamp,
            None,
        ),
        'ePIDLoopPeriod': (
            ParamEnum.ePIDLoopPeriod,
            None,
        ),
        'ePIDLoopPolarity': (
            ParamEnum.ePIDLoopPolarity,
            None,
        ),
        'ePeakCurrentLimitAmps': '<value is a self-reference, replaced by this string>',
        'ePeakCurrentLimitMs': (
            ParamEnum.ePeakCurrentLimitMs,
            None,
        ),
        'ePeakNegOutput': (
            ParamEnum.ePeakNegOutput,
            None,
        ),
        'ePeakPosOutput': (
            ParamEnum.ePeakPosOutput,
            None,
        ),
        'eProfileParamSlot_AllowableErr': (
            ParamEnum.eProfileParamSlot_AllowableErr,
            None,
        ),
        'eProfileParamSlot_D': (
            ParamEnum.eProfileParamSlot_D,
            None,
        ),
        'eProfileParamSlot_F': (
            ParamEnum.eProfileParamSlot_F,
            None,
        ),
        'eProfileParamSlot_I': (
            ParamEnum.eProfileParamSlot_I,
            None,
        ),
        'eProfileParamSlot_IZone': (
            ParamEnum.eProfileParamSlot_IZone,
            None,
        ),
        'eProfileParamSlot_MaxIAccum': (
            ParamEnum.eProfileParamSlot_MaxIAccum,
            None,
        ),
        'eProfileParamSlot_P': (
            ParamEnum.eProfileParamSlot_P,
            None,
        ),
        'eProfileParamSlot_PeakOutput': (
            ParamEnum.eProfileParamSlot_PeakOutput,
            None,
        ),
        'ePulseWidthPeriod_EdgesPerRot': (
            ParamEnum.ePulseWidthPeriod_EdgesPerRot,
            None,
        ),
        'ePulseWidthPeriod_FilterWindowSz': (
            ParamEnum.ePulseWidthPeriod_FilterWindowSz,
            None,
        ),
        'ePulseWidthPosition': (
            ParamEnum.ePulseWidthPosition,
            None,
        ),
        'eQuadFilterEn': (
            ParamEnum.eQuadFilterEn,
            None,
        ),
        'eQuadIdxPolarity': (
            ParamEnum.eQuadIdxPolarity,
            None,
        ),
        'eQuadraturePosition': (
            ParamEnum.eQuadraturePosition,
            None,
        ),
        'eRemoteSensorClosedLoopDisableNeutralOnLOS': (
            ParamEnum.eRemoteSensorClosedLoopDisableNeutralOnLOS,
            None,
        ),
        'eRemoteSensorDeviceID': (
            ParamEnum.eRemoteSensorDeviceID,
            None,
        ),
        'eRemoteSensorSource': (
            ParamEnum.eRemoteSensorSource,
            None,
        ),
        'eReserved1': (
            ParamEnum.eReserved1,
            None,
        ),
        'eReverseSoftLimitEnable': (
            ParamEnum.eReverseSoftLimitEnable,
            None,
        ),
        'eReverseSoftLimitThreshold': (
            ParamEnum.eReverseSoftLimitThreshold,
            None,
        ),
        'eSampleVelocityPeriod': (
            ParamEnum.eSampleVelocityPeriod,
            None,
        ),
        'eSampleVelocityWindow': (
            ParamEnum.eSampleVelocityWindow,
            None,
        ),
        'eSelectedSensorCoefficient': (
            ParamEnum.eSelectedSensorCoefficient,
            None,
        ),
        'eSelectedSensorPosition': (
            ParamEnum.eSelectedSensorPosition,
            None,
        ),
        'eSensorDirection': (
            ParamEnum.eSensorDirection,
            None,
        ),
        'eSensorInitStrategy': (
            ParamEnum.eSensorInitStrategy,
            None,
        ),
        'eSensorSync': (
            ParamEnum.eSensorSync,
            None,
        ),
        'eSensorTerm': (
            ParamEnum.eSensorTerm,
            None,
        ),
        'eSoftLimitDisableNeutralOnLOS': (
            ParamEnum.eSoftLimitDisableNeutralOnLOS,
            None,
        ),
        'eStatusFramePeriod': (
            ParamEnum.eStatusFramePeriod,
            None,
        ),
        'eStatusFrameRate': (
            ParamEnum.eStatusFrameRate,
            None,
        ),
        'eStickyFaults': (
            ParamEnum.eStickyFaults,
            None,
        ),
        'eTempCompDisable': (
            ParamEnum.eTempCompDisable,
            None,
        ),
        'eUnitString': (
            ParamEnum.eUnitString,
            None,
        ),
        'eWriteCount': (
            ParamEnum.eWriteCount,
            None,
        ),
        'eYawOffset': (
            ParamEnum.eYawOffset,
            None,
        ),
    }
    __members__ = {
        'eAbsSensorRange': ParamEnum.eAbsSensorRange,
        'eAccumZ': ParamEnum.eAccumZ,
        'eAnalogPosition': ParamEnum.eAnalogPosition,
        'eBatteryVoltageFilterSize': ParamEnum.eBatteryVoltageFilterSize,
        'eBetaGain': ParamEnum.eBetaGain,
        'eClearPosOnLimitF': ParamEnum.eClearPositionOnLimitF,
        'eClearPosOnLimitR': ParamEnum.eClearPositionOnLimitR,
        'eClearPositionOnIdx': ParamEnum.eClearPositionOnQuadIdx,
        'eClearPositionOnLimitF': '<value is a self-reference, replaced by this string>',
        'eClearPositionOnLimitR': '<value is a self-reference, replaced by this string>',
        'eClearPositionOnQuadIdx': '<value is a self-reference, replaced by this string>',
        'eClosedLoopIAccum': ParamEnum.eClosedLoopIAccum,
        'eClosedloopRamp': ParamEnum.eClosedloopRamp,
        'eCompassOffset': ParamEnum.eCompassOffset,
        'eContinuousCurrentLimitAmps': ParamEnum.eContinuousCurrentLimitAmps,
        'eCurrEnable': ParamEnum.eCurrEnable,
        'eCurrLimit_Amps': '<value is a self-reference, replaced by this string>',
        'eCurrThres_Amps': ParamEnum.ePeakCurrentLimitAmps,
        'eCurrThres_Ms': ParamEnum.eCurrThres_Ms,
        'eCustomParam': ParamEnum.eCustomParam,
        'eDefaultConfig': ParamEnum.eDefaultConfig,
        'eEnableCompassFusion': ParamEnum.eEnableCompassFusion,
        'eEnterCalibration': ParamEnum.eEnterCalibration,
        'eFastWriteCount': ParamEnum.eFastWriteCount,
        'eFeedbackNotContinuous': ParamEnum.eFeedbackNotContinuous,
        'eFeedbackSensorType': ParamEnum.eFeedbackSensorType,
        'eFeedbackTimeBase': ParamEnum.eFeedbackTimeBase,
        'eForwardSoftLimitEnable': ParamEnum.eForwardSoftLimitEnable,
        'eForwardSoftLimitThreshold': ParamEnum.eForwardSoftLimitThreshold,
        'eFusedHeadingOffset': ParamEnum.eFusedHeadingOffset,
        'eGyroNoMotionCal': ParamEnum.eGyroNoMotionCal,
        'eIntegratedSensor': ParamEnum.eIntegratedSensor,
        'eLimitSwitchDisableNeutralOnLOS': ParamEnum.eLimitSwitchDisableNeutralOnLOS,
        'eLimitSwitchNormClosedAndDis': ParamEnum.eLimitSwitchNormClosedAndDis,
        'eLimitSwitchRemoteDevID': ParamEnum.eLimitSwitchRemoteDevID,
        'eLimitSwitchSource': ParamEnum.eLimitSwitchSource,
        'eMagnetOffset': ParamEnum.eMagnetOffset,
        'eMotMag_Accel': ParamEnum.eMotMag_Accel,
        'eMotMag_SCurveLevel': ParamEnum.eMotMag_SCurveLevel,
        'eMotMag_VelCruise': ParamEnum.eMotMag_VelCruise,
        'eMotionMeas_shake_reject_thresh': ParamEnum.eMotionMeas_shake_reject_thresh,
        'eMotionMeas_shake_reject_time': ParamEnum.eMotionMeas_shake_reject_time,
        'eMotionMeas_shake_reject_timeout': ParamEnum.eMotionMeas_shake_reject_timeout,
        'eMotionMeas_tap_count': ParamEnum.eMotionMeas_tap_count,
        'eMotionMeas_tap_threshX': ParamEnum.eMotionMeas_tap_threshX,
        'eMotionMeas_tap_threshY': ParamEnum.eMotionMeas_tap_threshY,
        'eMotionMeas_tap_threshZ': ParamEnum.eMotionMeas_tap_threshZ,
        'eMotionMeas_tap_time': ParamEnum.eMotionMeas_tap_time,
        'eMotionMeas_tap_time_multi': ParamEnum.eMotionMeas_tap_time_multi,
        'eMotionProfileHasUnderrunErr': ParamEnum.eMotionProfileHasUnderrunErr,
        'eMotionProfileTrajectoryInterpolDis': ParamEnum.eMotionProfileTrajectoryInterpolDis,
        'eMotionProfileTrajectoryPointDurationMs': ParamEnum.eMotionProfileTrajectoryPointDurationMs,
        'eMotorCommutation': ParamEnum.eMotorCommutation,
        'eNeutralDeadband': ParamEnum.eNeutralDeadband,
        'eNominalBatteryVoltage': ParamEnum.eNominalBatteryVoltage,
        'eNominalNegOutput': ParamEnum.eNominalNegOutput,
        'eNominalPosOutput': ParamEnum.eNominalPosOutput,
        'eOnBoot_BrakeMode': ParamEnum.eOnBoot_BrakeMode,
        'eOpenloopRamp': ParamEnum.eOpenloopRamp,
        'ePIDLoopPeriod': ParamEnum.ePIDLoopPeriod,
        'ePIDLoopPolarity': ParamEnum.ePIDLoopPolarity,
        'ePeakCurrentLimitAmps': '<value is a self-reference, replaced by this string>',
        'ePeakCurrentLimitMs': ParamEnum.ePeakCurrentLimitMs,
        'ePeakNegOutput': ParamEnum.ePeakNegOutput,
        'ePeakPosOutput': ParamEnum.ePeakPosOutput,
        'eProfileParamSlot_AllowableErr': ParamEnum.eProfileParamSlot_AllowableErr,
        'eProfileParamSlot_D': ParamEnum.eProfileParamSlot_D,
        'eProfileParamSlot_F': ParamEnum.eProfileParamSlot_F,
        'eProfileParamSlot_I': ParamEnum.eProfileParamSlot_I,
        'eProfileParamSlot_IZone': ParamEnum.eProfileParamSlot_IZone,
        'eProfileParamSlot_MaxIAccum': ParamEnum.eProfileParamSlot_MaxIAccum,
        'eProfileParamSlot_P': ParamEnum.eProfileParamSlot_P,
        'eProfileParamSlot_PeakOutput': ParamEnum.eProfileParamSlot_PeakOutput,
        'ePulseWidthPeriod_EdgesPerRot': ParamEnum.ePulseWidthPeriod_EdgesPerRot,
        'ePulseWidthPeriod_FilterWindowSz': ParamEnum.ePulseWidthPeriod_FilterWindowSz,
        'ePulseWidthPosition': ParamEnum.ePulseWidthPosition,
        'eQuadFilterEn': ParamEnum.eQuadFilterEn,
        'eQuadIdxPolarity': ParamEnum.eQuadIdxPolarity,
        'eQuadraturePosition': ParamEnum.eQuadraturePosition,
        'eRemoteSensorClosedLoopDisableNeutralOnLOS': ParamEnum.eRemoteSensorClosedLoopDisableNeutralOnLOS,
        'eRemoteSensorDeviceID': ParamEnum.eRemoteSensorDeviceID,
        'eRemoteSensorSource': ParamEnum.eRemoteSensorSource,
        'eReserved1': ParamEnum.eReserved1,
        'eReverseSoftLimitEnable': ParamEnum.eReverseSoftLimitEnable,
        'eReverseSoftLimitThreshold': ParamEnum.eReverseSoftLimitThreshold,
        'eSampleVelocityPeriod': ParamEnum.eSampleVelocityPeriod,
        'eSampleVelocityWindow': ParamEnum.eSampleVelocityWindow,
        'eSelectedSensorCoefficient': ParamEnum.eSelectedSensorCoefficient,
        'eSelectedSensorPosition': ParamEnum.eSelectedSensorPosition,
        'eSensorDirection': ParamEnum.eSensorDirection,
        'eSensorInitStrategy': ParamEnum.eSensorInitStrategy,
        'eSensorSync': ParamEnum.eSensorSync,
        'eSensorTerm': ParamEnum.eSensorTerm,
        'eSoftLimitDisableNeutralOnLOS': ParamEnum.eSoftLimitDisableNeutralOnLOS,
        'eStatusFramePeriod': ParamEnum.eStatusFramePeriod,
        'eStatusFrameRate': ParamEnum.eStatusFrameRate,
        'eStickyFaults': ParamEnum.eStickyFaults,
        'eTempCompDisable': ParamEnum.eTempCompDisable,
        'eUnitString': ParamEnum.eUnitString,
        'eWriteCount': ParamEnum.eWriteCount,
        'eYawOffset': ParamEnum.eYawOffset,
    }
