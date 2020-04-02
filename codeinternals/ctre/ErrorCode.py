# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class ErrorCode(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      OK
    
      OKAY : //!< No Error - Function executed as expected
    
      CAN_MSG_STALE
    
      CAN_TX_FULL
    
      TxFailed : //!< Could not transmit the CAN frame.
    
      InvalidParamValue : //!< Caller passed an invalid param
    
      CAN_INVALID_PARAM
    
      RxTimeout : //!< CAN frame has not been received within specified period of time.
    
      CAN_MSG_NOT_FOUND
    
      TxTimeout : //!< Not used.
    
      CAN_NO_MORE_TX_JOBS
    
      UnexpectedArbId : //!< Specified CAN Id is invalid.
    
      CAN_NO_SESSIONS_AVAIL
    
      BufferFull : //!< Caller attempted to insert data into a buffer that is full.
    
      CAN_OVERFLOW
    
      SensorNotPresent : //!< Sensor is not present
    
      FirmwareTooOld
    
      CouldNotChangePeriod
    
      BufferFailure
    
      FirwmwareNonFRC
    
      GeneralError : //!< User Specified General Error
    
      GENERAL_ERROR
    
      SIG_NOT_UPDATED
    
      SigNotUpdated : //!< Have not received an value response for signal.
    
      NotAllPIDValuesUpdated
    
      GEN_PORT_ERROR
    
      PORT_MODULE_TYPE_MISMATCH
    
      GEN_MODULE_ERROR
    
      MODULE_NOT_INIT_SET_ERROR
    
      MODULE_NOT_INIT_GET_ERROR
    
      WheelRadiusTooSmall
    
      TicksPerRevZero
    
      DistanceBetweenWheelsTooSmall
    
      GainsAreNotSet
    
      WrongRemoteLimitSwitchSource
    
      DoubleVoltageCompensatingWPI
    
      IncompatibleMode
    
      InvalidHandle : //!< Handle does not match stored map of handles
    
      FeatureRequiresHigherFirm
    
      MotorControllerFeatureRequiresHigherFirm
    
      TalonFeatureRequiresHigherFirm
    
      ConfigFactoryDefaultRequiresHigherFirm
    
      ConfigMotionSCurveRequiresHigherFirm
    
      TalonFXFirmwarePreVBatDetect
    
      LibraryCouldNotBeLoaded
    
      MissingRoutineInLibrary
    
      ResourceNotAvailable
    
      MusicFileNotFound
    
      MusicFileWrongSize
    
      MusicFileTooNew
    
      MusicFileInvalid
    
      InvalidOrchestraAction
    
      MusicFileTooOld
    
      MusicInterrupted
    
      MusicNotSupported
    
      PulseWidthSensorNotPresent : //!< Special Code for "isSensorPresent"
    
      GeneralWarning
    
      FeatureNotSupported
    
      NotImplemented
    
      FirmVersionCouldNotBeRetrieved
    
      FeaturesNotAvailableYet
    
      ControlModeNotValid
    
      ControlModeNotSupportedYet
    
      CascadedPIDNotSupporteYet
    
      AuxiliaryPIDNotSupportedYet
    
      RemoteSensorsNotSupportedYet
    
      MotProfFirmThreshold
    
      MotProfFirmThreshold2
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
        """ __init__(self: ctre._ctre.ErrorCode, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: ctre._ctre.ErrorCode) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs):  # real signature unknown
        """ (self: ctre._ctre.ErrorCode, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""

    AuxiliaryPIDNotSupportedYet = ErrorCode.CascadedPIDNotSupporteYet
    BufferFailure = ErrorCode.BufferFailure
    BufferFull = ErrorCode.BufferFull
    CAN_INVALID_PARAM = ErrorCode.InvalidParamValue
    CAN_MSG_NOT_FOUND = ErrorCode.RxTimeout
    CAN_MSG_STALE = ErrorCode.CAN_MSG_STALE
    CAN_NO_MORE_TX_JOBS = ErrorCode.TxTimeout
    CAN_NO_SESSIONS_AVAIL = ErrorCode.UnexpectedArbId
    CAN_OVERFLOW = ErrorCode.CAN_OVERFLOW
    CAN_TX_FULL = ErrorCode.CAN_TX_FULL
    CascadedPIDNotSupporteYet = ErrorCode.CascadedPIDNotSupporteYet
    ConfigFactoryDefaultRequiresHigherFirm = ErrorCode.ConfigFactoryDefaultRequiresHigherFirm
    ConfigMotionSCurveRequiresHigherFirm = ErrorCode.ConfigMotionSCurveRequiresHigherFirm
    ControlModeNotSupportedYet = ErrorCode.ControlModeNotSupportedYet
    ControlModeNotValid = ErrorCode.ControlModeNotValid
    CouldNotChangePeriod = ErrorCode.CouldNotChangePeriod
    DistanceBetweenWheelsTooSmall = ErrorCode.DistanceBetweenWheelsTooSmall
    DoubleVoltageCompensatingWPI = ErrorCode.DoubleVoltageCompensatingWPI
    FeatureNotSupported = ErrorCode.FeatureNotSupported
    FeatureRequiresHigherFirm = ErrorCode.FeatureRequiresHigherFirm
    FeaturesNotAvailableYet = ErrorCode.FeaturesNotAvailableYet
    FirmVersionCouldNotBeRetrieved = ErrorCode.FirmVersionCouldNotBeRetrieved
    FirmwareTooOld = ErrorCode.FirmwareTooOld
    FirwmwareNonFRC = ErrorCode.FirwmwareNonFRC
    GainsAreNotSet = ErrorCode.GainsAreNotSet
    GeneralError = ErrorCode.GeneralError
    GeneralWarning = ErrorCode.GeneralWarning
    GENERAL_ERROR = ErrorCode.GeneralError
    GEN_MODULE_ERROR = ErrorCode.GEN_MODULE_ERROR
    GEN_PORT_ERROR = ErrorCode.GEN_PORT_ERROR
    IncompatibleMode = ErrorCode.IncompatibleMode
    InvalidHandle = ErrorCode.InvalidHandle
    InvalidOrchestraAction = ErrorCode.InvalidOrchestraAction
    InvalidParamValue = ErrorCode.InvalidParamValue
    LibraryCouldNotBeLoaded = ErrorCode.LibraryCouldNotBeLoaded
    MissingRoutineInLibrary = ErrorCode.MissingRoutineInLibrary
    MODULE_NOT_INIT_GET_ERROR = ErrorCode.MODULE_NOT_INIT_GET_ERROR
    MODULE_NOT_INIT_SET_ERROR = ErrorCode.MODULE_NOT_INIT_SET_ERROR
    MotorControllerFeatureRequiresHigherFirm = ErrorCode.MotorControllerFeatureRequiresHigherFirm
    MotProfFirmThreshold = ErrorCode.MotProfFirmThreshold
    MotProfFirmThreshold2 = ErrorCode.MotProfFirmThreshold2
    MusicFileInvalid = ErrorCode.MusicFileInvalid
    MusicFileNotFound = ErrorCode.MusicFileNotFound
    MusicFileTooNew = ErrorCode.MusicFileTooNew
    MusicFileTooOld = ErrorCode.MusicFileTooOld
    MusicFileWrongSize = ErrorCode.MusicFileWrongSize
    MusicInterrupted = ErrorCode.MusicInterrupted
    MusicNotSupported = ErrorCode.MusicNotSupported
    NotAllPIDValuesUpdated = ErrorCode.NotAllPIDValuesUpdated
    NotImplemented = ErrorCode.NotImplemented
    OK = ErrorCode.OK
    OKAY = ErrorCode.OK
    PORT_MODULE_TYPE_MISMATCH = ErrorCode.PORT_MODULE_TYPE_MISMATCH
    PulseWidthSensorNotPresent = ErrorCode.PulseWidthSensorNotPresent
    RemoteSensorsNotSupportedYet = ErrorCode.RemoteSensorsNotSupportedYet
    ResourceNotAvailable = ErrorCode.ResourceNotAvailable
    RxTimeout = ErrorCode.RxTimeout
    SensorNotPresent = ErrorCode.SensorNotPresent
    SigNotUpdated = ErrorCode.SIG_NOT_UPDATED
    SIG_NOT_UPDATED = ErrorCode.SIG_NOT_UPDATED
    TalonFeatureRequiresHigherFirm = ErrorCode.MotorControllerFeatureRequiresHigherFirm
    TalonFXFirmwarePreVBatDetect = ErrorCode.TalonFXFirmwarePreVBatDetect
    TicksPerRevZero = ErrorCode.TicksPerRevZero
    TxFailed = ErrorCode.CAN_TX_FULL
    TxTimeout = ErrorCode.TxTimeout
    UnexpectedArbId = ErrorCode.UnexpectedArbId
    WheelRadiusTooSmall = ErrorCode.WheelRadiusTooSmall
    WrongRemoteLimitSwitchSource = ErrorCode.WrongRemoteLimitSwitchSource
    __entries = {
        'AuxiliaryPIDNotSupportedYet': (
            ErrorCode.CascadedPIDNotSupporteYet,
            None,
        ),
        'BufferFailure': (
            ErrorCode.BufferFailure,
            None,
        ),
        'BufferFull': (
            ErrorCode.BufferFull,
            '//!< Caller attempted to insert data into a buffer that is full.',
        ),
        'CAN_INVALID_PARAM': (
            ErrorCode.InvalidParamValue,
            None,
        ),
        'CAN_MSG_NOT_FOUND': (
            ErrorCode.RxTimeout,
            None,
        ),
        'CAN_MSG_STALE': (
            ErrorCode.CAN_MSG_STALE,
            None,
        ),
        'CAN_NO_MORE_TX_JOBS': (
            ErrorCode.TxTimeout,
            None,
        ),
        'CAN_NO_SESSIONS_AVAIL': (
            ErrorCode.UnexpectedArbId,
            None,
        ),
        'CAN_OVERFLOW': (
            ErrorCode.CAN_OVERFLOW,
            None,
        ),
        'CAN_TX_FULL': (
            ErrorCode.CAN_TX_FULL,
            None,
        ),
        'CascadedPIDNotSupporteYet': '<value is a self-reference, replaced by this string>',
        'ConfigFactoryDefaultRequiresHigherFirm': (
            ErrorCode.ConfigFactoryDefaultRequiresHigherFirm,
            None,
        ),
        'ConfigMotionSCurveRequiresHigherFirm': (
            ErrorCode.ConfigMotionSCurveRequiresHigherFirm,
            None,
        ),
        'ControlModeNotSupportedYet': (
            ErrorCode.ControlModeNotSupportedYet,
            None,
        ),
        'ControlModeNotValid': (
            ErrorCode.ControlModeNotValid,
            None,
        ),
        'CouldNotChangePeriod': (
            ErrorCode.CouldNotChangePeriod,
            None,
        ),
        'DistanceBetweenWheelsTooSmall': (
            ErrorCode.DistanceBetweenWheelsTooSmall,
            None,
        ),
        'DoubleVoltageCompensatingWPI': (
            ErrorCode.DoubleVoltageCompensatingWPI,
            None,
        ),
        'FeatureNotSupported': (
            ErrorCode.FeatureNotSupported,
            None,
        ),
        'FeatureRequiresHigherFirm': (
            ErrorCode.FeatureRequiresHigherFirm,
            None,
        ),
        'FeaturesNotAvailableYet': (
            ErrorCode.FeaturesNotAvailableYet,
            None,
        ),
        'FirmVersionCouldNotBeRetrieved': (
            ErrorCode.FirmVersionCouldNotBeRetrieved,
            None,
        ),
        'FirmwareTooOld': (
            ErrorCode.FirmwareTooOld,
            None,
        ),
        'FirwmwareNonFRC': (
            ErrorCode.FirwmwareNonFRC,
            None,
        ),
        'GENERAL_ERROR': (
            ErrorCode.GeneralError,
            None,
        ),
        'GEN_MODULE_ERROR': (
            ErrorCode.GEN_MODULE_ERROR,
            None,
        ),
        'GEN_PORT_ERROR': (
            ErrorCode.GEN_PORT_ERROR,
            None,
        ),
        'GainsAreNotSet': (
            ErrorCode.GainsAreNotSet,
            None,
        ),
        'GeneralError': (
            '<value is a self-reference, replaced by this string>',
            '//!< User Specified General Error',
        ),
        'GeneralWarning': (
            ErrorCode.GeneralWarning,
            None,
        ),
        'IncompatibleMode': (
            ErrorCode.IncompatibleMode,
            None,
        ),
        'InvalidHandle': (
            ErrorCode.InvalidHandle,
            '//!< Handle does not match stored map of handles',
        ),
        'InvalidOrchestraAction': (
            ErrorCode.InvalidOrchestraAction,
            None,
        ),
        'InvalidParamValue': (
            '<value is a self-reference, replaced by this string>',
            '//!< Caller passed an invalid param',
        ),
        'LibraryCouldNotBeLoaded': (
            ErrorCode.LibraryCouldNotBeLoaded,
            None,
        ),
        'MODULE_NOT_INIT_GET_ERROR': (
            ErrorCode.MODULE_NOT_INIT_GET_ERROR,
            None,
        ),
        'MODULE_NOT_INIT_SET_ERROR': (
            ErrorCode.MODULE_NOT_INIT_SET_ERROR,
            None,
        ),
        'MissingRoutineInLibrary': (
            ErrorCode.MissingRoutineInLibrary,
            None,
        ),
        'MotProfFirmThreshold': (
            ErrorCode.MotProfFirmThreshold,
            None,
        ),
        'MotProfFirmThreshold2': (
            ErrorCode.MotProfFirmThreshold2,
            None,
        ),
        'MotorControllerFeatureRequiresHigherFirm': (
            ErrorCode.MotorControllerFeatureRequiresHigherFirm,
            None,
        ),
        'MusicFileInvalid': (
            ErrorCode.MusicFileInvalid,
            None,
        ),
        'MusicFileNotFound': (
            ErrorCode.MusicFileNotFound,
            None,
        ),
        'MusicFileTooNew': (
            ErrorCode.MusicFileTooNew,
            None,
        ),
        'MusicFileTooOld': (
            ErrorCode.MusicFileTooOld,
            None,
        ),
        'MusicFileWrongSize': (
            ErrorCode.MusicFileWrongSize,
            None,
        ),
        'MusicInterrupted': (
            ErrorCode.MusicInterrupted,
            None,
        ),
        'MusicNotSupported': (
            ErrorCode.MusicNotSupported,
            None,
        ),
        'NotAllPIDValuesUpdated': (
            ErrorCode.NotAllPIDValuesUpdated,
            None,
        ),
        'NotImplemented': (
            ErrorCode.NotImplemented,
            None,
        ),
        'OK': (
            ErrorCode.OK,
            None,
        ),
        'OKAY': (
            '<value is a self-reference, replaced by this string>',
            '//!< No Error - Function executed as expected',
        ),
        'PORT_MODULE_TYPE_MISMATCH': (
            ErrorCode.PORT_MODULE_TYPE_MISMATCH,
            None,
        ),
        'PulseWidthSensorNotPresent': (
            ErrorCode.PulseWidthSensorNotPresent,
            '//!< Special Code for "isSensorPresent"',
        ),
        'RemoteSensorsNotSupportedYet': (
            ErrorCode.RemoteSensorsNotSupportedYet,
            None,
        ),
        'ResourceNotAvailable': (
            ErrorCode.ResourceNotAvailable,
            None,
        ),
        'RxTimeout': (
            '<value is a self-reference, replaced by this string>',
            '//!< CAN frame has not been received within specified period of time.',
        ),
        'SIG_NOT_UPDATED': (
            ErrorCode.SIG_NOT_UPDATED,
            None,
        ),
        'SensorNotPresent': (
            ErrorCode.SensorNotPresent,
            '//!< Sensor is not present',
        ),
        'SigNotUpdated': (
            '<value is a self-reference, replaced by this string>',
            '//!< Have not received an value response for signal.',
        ),
        'TalonFXFirmwarePreVBatDetect': (
            ErrorCode.TalonFXFirmwarePreVBatDetect,
            None,
        ),
        'TalonFeatureRequiresHigherFirm': '<value is a self-reference, replaced by this string>',
        'TicksPerRevZero': (
            ErrorCode.TicksPerRevZero,
            None,
        ),
        'TxFailed': (
            '<value is a self-reference, replaced by this string>',
            '//!< Could not transmit the CAN frame.',
        ),
        'TxTimeout': (
            '<value is a self-reference, replaced by this string>',
            '//!< Not used.',
        ),
        'UnexpectedArbId': (
            '<value is a self-reference, replaced by this string>',
            '//!< Specified CAN Id is invalid.',
        ),
        'WheelRadiusTooSmall': (
            ErrorCode.WheelRadiusTooSmall,
            None,
        ),
        'WrongRemoteLimitSwitchSource': (
            ErrorCode.WrongRemoteLimitSwitchSource,
            None,
        ),
    }
    __members__ = {
        'AuxiliaryPIDNotSupportedYet': ErrorCode.CascadedPIDNotSupporteYet,
        'BufferFailure': ErrorCode.BufferFailure,
        'BufferFull': ErrorCode.BufferFull,
        'CAN_INVALID_PARAM': ErrorCode.InvalidParamValue,
        'CAN_MSG_NOT_FOUND': ErrorCode.RxTimeout,
        'CAN_MSG_STALE': ErrorCode.CAN_MSG_STALE,
        'CAN_NO_MORE_TX_JOBS': ErrorCode.TxTimeout,
        'CAN_NO_SESSIONS_AVAIL': ErrorCode.UnexpectedArbId,
        'CAN_OVERFLOW': ErrorCode.CAN_OVERFLOW,
        'CAN_TX_FULL': ErrorCode.CAN_TX_FULL,
        'CascadedPIDNotSupporteYet': '<value is a self-reference, replaced by this string>',
        'ConfigFactoryDefaultRequiresHigherFirm': ErrorCode.ConfigFactoryDefaultRequiresHigherFirm,
        'ConfigMotionSCurveRequiresHigherFirm': ErrorCode.ConfigMotionSCurveRequiresHigherFirm,
        'ControlModeNotSupportedYet': ErrorCode.ControlModeNotSupportedYet,
        'ControlModeNotValid': ErrorCode.ControlModeNotValid,
        'CouldNotChangePeriod': ErrorCode.CouldNotChangePeriod,
        'DistanceBetweenWheelsTooSmall': ErrorCode.DistanceBetweenWheelsTooSmall,
        'DoubleVoltageCompensatingWPI': ErrorCode.DoubleVoltageCompensatingWPI,
        'FeatureNotSupported': ErrorCode.FeatureNotSupported,
        'FeatureRequiresHigherFirm': ErrorCode.FeatureRequiresHigherFirm,
        'FeaturesNotAvailableYet': ErrorCode.FeaturesNotAvailableYet,
        'FirmVersionCouldNotBeRetrieved': ErrorCode.FirmVersionCouldNotBeRetrieved,
        'FirmwareTooOld': ErrorCode.FirmwareTooOld,
        'FirwmwareNonFRC': ErrorCode.FirwmwareNonFRC,
        'GENERAL_ERROR': ErrorCode.GeneralError,
        'GEN_MODULE_ERROR': ErrorCode.GEN_MODULE_ERROR,
        'GEN_PORT_ERROR': ErrorCode.GEN_PORT_ERROR,
        'GainsAreNotSet': ErrorCode.GainsAreNotSet,
        'GeneralError': '<value is a self-reference, replaced by this string>',
        'GeneralWarning': ErrorCode.GeneralWarning,
        'IncompatibleMode': ErrorCode.IncompatibleMode,
        'InvalidHandle': ErrorCode.InvalidHandle,
        'InvalidOrchestraAction': ErrorCode.InvalidOrchestraAction,
        'InvalidParamValue': '<value is a self-reference, replaced by this string>',
        'LibraryCouldNotBeLoaded': ErrorCode.LibraryCouldNotBeLoaded,
        'MODULE_NOT_INIT_GET_ERROR': ErrorCode.MODULE_NOT_INIT_GET_ERROR,
        'MODULE_NOT_INIT_SET_ERROR': ErrorCode.MODULE_NOT_INIT_SET_ERROR,
        'MissingRoutineInLibrary': ErrorCode.MissingRoutineInLibrary,
        'MotProfFirmThreshold': ErrorCode.MotProfFirmThreshold,
        'MotProfFirmThreshold2': ErrorCode.MotProfFirmThreshold2,
        'MotorControllerFeatureRequiresHigherFirm': ErrorCode.MotorControllerFeatureRequiresHigherFirm,
        'MusicFileInvalid': ErrorCode.MusicFileInvalid,
        'MusicFileNotFound': ErrorCode.MusicFileNotFound,
        'MusicFileTooNew': ErrorCode.MusicFileTooNew,
        'MusicFileTooOld': ErrorCode.MusicFileTooOld,
        'MusicFileWrongSize': ErrorCode.MusicFileWrongSize,
        'MusicInterrupted': ErrorCode.MusicInterrupted,
        'MusicNotSupported': ErrorCode.MusicNotSupported,
        'NotAllPIDValuesUpdated': ErrorCode.NotAllPIDValuesUpdated,
        'NotImplemented': ErrorCode.NotImplemented,
        'OK': ErrorCode.OK,
        'OKAY': '<value is a self-reference, replaced by this string>',
        'PORT_MODULE_TYPE_MISMATCH': ErrorCode.PORT_MODULE_TYPE_MISMATCH,
        'PulseWidthSensorNotPresent': ErrorCode.PulseWidthSensorNotPresent,
        'RemoteSensorsNotSupportedYet': ErrorCode.RemoteSensorsNotSupportedYet,
        'ResourceNotAvailable': ErrorCode.ResourceNotAvailable,
        'RxTimeout': '<value is a self-reference, replaced by this string>',
        'SIG_NOT_UPDATED': ErrorCode.SIG_NOT_UPDATED,
        'SensorNotPresent': ErrorCode.SensorNotPresent,
        'SigNotUpdated': '<value is a self-reference, replaced by this string>',
        'TalonFXFirmwarePreVBatDetect': ErrorCode.TalonFXFirmwarePreVBatDetect,
        'TalonFeatureRequiresHigherFirm': '<value is a self-reference, replaced by this string>',
        'TicksPerRevZero': ErrorCode.TicksPerRevZero,
        'TxFailed': '<value is a self-reference, replaced by this string>',
        'TxTimeout': '<value is a self-reference, replaced by this string>',
        'UnexpectedArbId': '<value is a self-reference, replaced by this string>',
        'WheelRadiusTooSmall': ErrorCode.WheelRadiusTooSmall,
        'WrongRemoteLimitSwitchSource': ErrorCode.WrongRemoteLimitSwitchSource,
    }
