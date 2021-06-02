import xbmc
import xbmcaddon
import os
import calendar
import time

try:  # Python 2
    import cPickle as pickle

except ImportError:  # Python 3
    import _pickle as pickle

import fswitch_config as fsconfig

def settingsFolder():
    # global settings folder
    globalSettingsFolder = xbmc.translatePath('special://userdata')
    globalSettingsFolder = os.path.join(globalSettingsFolder, 'addon_data')
    globalSettingsFolder = os.path.join(globalSettingsFolder, 'script.frequency.switcher')
    return globalSettingsFolder


def settingsFile():
    # global settings file
    globalSettingsFolder = settingsFolder()
    globalSettingsFile = os.path.join(globalSettingsFolder, 'global_settings.p')
    return globalSettingsFile

def settingsLastFpsFile():
    # last FPS settings file
    globalSettingsFolder = settingsFolder()
    globalLastFpsFile = os.path.join(globalSettingsFolder, 'global_lastfps.p')
    return globalLastFpsFile

def settingsLastChangeFile():
    # last frequency change time file
    globalSettingsFolder = settingsFolder()
    globalLastChangeFile = os.path.join(globalSettingsFolder, 'global_lastchange.p')
    return globalLastChangeFile 

def settingsAutoSyncFile():
    # global auto sync file
    globalSettingsFolder = settingsFolder()
    globalAutoSyncFile = os.path.join(globalSettingsFolder, 'global_autosync.p')
    return globalAutoSyncFile 

def settingsServiceConfigFile():
    # global service config file
    globalSettingsFolder = settingsFolder()
    globalServiceConfigFile = os.path.join(globalSettingsFolder, 'global_serviceconfig.p')
    return globalServiceConfigFile


def createAllSettingsFiles():

    # create settings folder if it doesn't already exist
    golbalSettingsFolder = settingsFolder()
    if not os.path.isdir(golbalSettingsFolder):
        os.makedirs(golbalSettingsFolder)

    # create settings files if they don't already exist
    globalSettingsFile = settingsFile()
    if not os.path.isfile(globalSettingsFile):
        resetSettingsFile()

    globalLastFps = settingsLastFpsFile()
    if not os.path.isfile(globalLastFps):
        resetLastDetectedFpsFile()

    globalLastChange = settingsLastChangeFile()
    if not os.path.isfile(globalLastChange):
        resetLastFreqChangeSettingFile()

    globalAutoSync = settingsAutoSyncFile()
    if not os.path.isfile(globalAutoSync):
        resetAutoSyncSettingsFile()

    globalServiceConfig = settingsServiceConfigFile()
    if not os.path.isfile(globalServiceConfig):
        resetServiceConfigFile()

def deleteAllSettingsFiles():

    # delete settings files
    try:
        globalSettingsFile = settingsFile()
        if os.path.isfile(globalSettingsFile):
            os.remove(globalSettingsFile)

        globalLastFps = settingsLastFpsFile()
        if os.path.isfile(globalLastFps):
            os.remove(globalLastFps)

        globalLastChange = settingsLastChangeFile()
        if os.path.isfile(globalLastChange):
            os.remove(globalLastChange)

        globalAutoSync = settingsAutoSyncFile()
        if os.path.isfile(globalAutoSync):
            os.remove(globalAutoSync)

        globalServiceConfig = settingsServiceConfigFile()
        if os.path.isfile(globalServiceConfig):
            os.remove(globalServiceConfig)

        infoStateFlagFile = activeInfoFlagFile()
        if os.path.isfile(infoStateFlagFile):
            os.remove(infoStateFlagFile)

        # delete settings folder if empty
        golbalSettingsFolder = settingsFolder()
        if os.path.isdir(golbalSettingsFolder):
            os.rmdir(golbalSettingsFolder)

        settingsDeleted = True
    except Exception:
        settingsDeleted = False


def resetSettingsFile():

    globalSettingsFile = settingsFile()

    # default settings
    fsSettings = {}

    # platform
    fsSettings['osPlatform'] = 'unknown'

    # key mapping
    fsSettings['radio60hz'] = False
    fsSettings['radio50hz'] = False
    fsSettings['radio30hz'] = False
    fsSettings['radio25hz'] = False
    fsSettings['radio24hz'] = False
    fsSettings['radioAuto'] = False
    fsSettings['radioInfo'] = False

    fsSettings['key60hz'] = ''
    fsSettings['key50hz'] = ''
    fsSettings['key30hz'] = ''
    fsSettings['key25hz'] = ''
    fsSettings['key24hz'] = ''
    fsSettings['keyAuto'] = ''
    fsSettings['keyInfo'] = ''

    fsSettings['status60hz'] = ''
    fsSettings['status50hz'] = ''
    fsSettings['status30hz'] = ''
    fsSettings['status25hz'] = ''
    fsSettings['status24hz'] = ''
    fsSettings['statusAuto'] = ''
    fsSettings['statusInfo'] = ''

    fsSettings['keymapRes'] = ''

    # create or overwrite settings file
    try:
        with open(globalSettingsFile, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        resetSettingsStatus = 'Reset settings'
    except Exception:
        resetSettingsStatus = 'Failed to reset settings'

    resetLastDetectedFpsFile()

    resetLastFreqChangeSettingFile()

    resetAutoSyncSettingsFile()

    resetServiceConfigFile()

def resetLastDetectedFpsFile():

    globalLastFps = settingsLastFpsFile()

    # default settings
    fsSettings = {}

    fsSettings['lastDetectedFps'] = ''
    fsSettings['lastDetectedFile'] = ''

    # create or overwrite settings file
    try:
        with open(globalLastFps, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        resetSettingsStatus = 'Reset last FPS settings'
    except Exception:
        resetSettingsStatus = 'Failed to reset last FPS settings'

def resetLastFreqChangeSettingFile():

    globalLastChange = settingsLastChangeFile()

    # default settings
    fsSettings = {}

    fsSettings['lastFreqChange'] = 0

    # create or overwrite settings file
    try:
        with open(globalLastChange, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        resetSettingsStatus = 'Reset last change time setting'
    except Exception:
        resetSettingsStatus = 'Failed to reset last change time setting'

def resetAutoSyncSettingsFile():

    globalAutoSync = settingsAutoSyncFile()

    # default settings
    fsSettings = {}

    # auto-set configuration
    fsSettings['radioAuto60hz'] = True
    fsSettings['radioAuto50hz'] = True
    fsSettings['radioAuto30hz'] = False
    fsSettings['radioAuto25hz'] = False
    fsSettings['radioAuto24hz'] = True

    fsSettings['edit60hzFps1'] = '59.940'
    fsSettings['edit60hzFps2'] = '29.970'
    fsSettings['edit60hzFps3'] = ''
    fsSettings['edit60hzFps4'] = ''

    fsSettings['edit50hzFps1'] = '50.000'
    fsSettings['edit50hzFps2'] = '25.000'
    fsSettings['edit50hzFps3'] = ''
    fsSettings['edit50hzFps4'] = ''

    fsSettings['edit30hzFps1'] = ''
    fsSettings['edit30hzFps2'] = ''
    fsSettings['edit30hzFps3'] = ''
    fsSettings['edit30hzFps4'] = ''

    fsSettings['edit25hzFps1'] = ''
    fsSettings['edit25hzFps2'] = ''
    fsSettings['edit25hzFps3'] = ''
    fsSettings['edit25hzFps4'] = ''

    fsSettings['edit24hzFps1'] = '24.000'
    fsSettings['edit24hzFps2'] = '23.976'
    fsSettings['edit24hzFps3'] = ''
    fsSettings['edit24hzFps4'] = ''

    # create or overwrite settings file
    try:
        with open(globalAutoSync, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        resetSettingsStatus = 'Reset auto sync settings'
    except Exception:
        resetSettingsStatus = 'Failed to reset auto sync settings'

def resetServiceConfigFile():

    globalServiceConfig = settingsServiceConfigFile()

    # default settings
    fsSettings = {}
    
    # service config
    fsSettings['radioOnPlayStop60'] = False
    fsSettings['radioOnPlayStop50'] = False
    fsSettings['radioNotifyOn'] = True

    # create or overwrite settings file
    try:
        with open(globalServiceConfig, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)
                
        resetSettingsStatus = 'Reset service configuration'
    except Exception:
        resetSettingsStatus = 'Failed to reset service configuration'


def loadSettings():

    # load service configuration (first to allow for fsmsg debugging)
    loadServiceConfig()

    globalSettingsFile = settingsFile()

    # read settings file
    try:
        with open(globalSettingsFile, 'rb') as settingsFileHandle: 
            fsSettings = pickle.load(settingsFileHandle)

            # platform
            fsconfig.osPlatform = fsSettings['osPlatform']

            # key mapping
            fsconfig.radio60hz = fsSettings['radio60hz']
            fsconfig.radio50hz = fsSettings['radio50hz']
            fsconfig.radio30hz = fsSettings['radio30hz']
            fsconfig.radio25hz = fsSettings['radio25hz']
            fsconfig.radio24hz = fsSettings['radio24hz']
            fsconfig.radioAuto = fsSettings['radioAuto']
            fsconfig.radioInfo = fsSettings['radioInfo']

            fsconfig.key60hz = fsSettings['key60hz']
            fsconfig.key50hz = fsSettings['key50hz']
            fsconfig.key30hz = fsSettings['key30hz']
            fsconfig.key25hz = fsSettings['key25hz']
            fsconfig.key24hz = fsSettings['key24hz']
            fsconfig.keyAuto = fsSettings['keyAuto']
            fsconfig.keyInfo = fsSettings['keyInfo']

            fsconfig.status60hz = fsSettings['status60hz']
            fsconfig.status50hz = fsSettings['status50hz']
            fsconfig.status30hz = fsSettings['status30hz']
            fsconfig.status25hz = fsSettings['status25hz']
            fsconfig.status24hz = fsSettings['status24hz']
            fsconfig.statusAuto = fsSettings['statusAuto']
            fsconfig.statusInfo = fsSettings['statusInfo']

            fsconfig.keymapRes = fsSettings['keymapRes']

        loadSettingsStatus = 'Loaded settings'
    except Exception:
        loadSettingsStatus = 'Failed to load settings'

    # load auto-set configuration
    loadAutoSyncSettings()

    # load use service flag
    fsconfig.radioOnPlayStart = useServiceFlagGet()

    return loadSettingsStatus

def saveSettings():

    globalSettingsFile = settingsFile()

    fsSettings = {}

    # platform
    fsSettings['osPlatform'] = fsconfig.osPlatform

    # key mapping
    fsSettings['radio60hz'] = fsconfig.radio60hz
    fsSettings['radio50hz'] = fsconfig.radio50hz
    fsSettings['radio30hz'] = fsconfig.radio30hz
    fsSettings['radio25hz'] = fsconfig.radio25hz
    fsSettings['radio24hz'] = fsconfig.radio24hz
    fsSettings['radioAuto'] = fsconfig.radioAuto
    fsSettings['radioInfo'] = fsconfig.radioInfo

    fsSettings['key60hz'] = fsconfig.key60hz
    fsSettings['key50hz'] = fsconfig.key50hz
    fsSettings['key30hz'] = fsconfig.key30hz
    fsSettings['key25hz'] = fsconfig.key25hz
    fsSettings['key24hz'] = fsconfig.key24hz
    fsSettings['keyAuto'] = fsconfig.keyAuto
    fsSettings['keyInfo'] = fsconfig.keyInfo

    fsSettings['status60hz'] = fsconfig.status60hz
    fsSettings['status50hz'] = fsconfig.status50hz
    fsSettings['status30hz'] = fsconfig.status30hz
    fsSettings['status25hz'] = fsconfig.status25hz
    fsSettings['status24hz'] = fsconfig.status24hz
    fsSettings['statusAuto'] = fsconfig.statusAuto
    fsSettings['statusInfo'] = fsconfig.statusInfo

    fsSettings['keymapRes'] = fsconfig.keymapRes

    # create or overwrite settings file
    try:
        with open(globalSettingsFile, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        saveSettingsStatus = 'Settings saved'
    except Exception:
        saveSettingsStatus = 'Failed to save settings'

    # save auto-set configuration
    saveAutoSyncSettings()

    # save service configuration
    saveServiceConfig()

    # save use service flag
    if fsconfig.radioOnPlayStart:
        useServiceFlagSet()
    else:
        useServiceFlagDel()

    return saveSettingsStatus


def loadLastDetectedFps():

    globalLastFps = settingsLastFpsFile()

    # read settings file
    try:
        with open(globalLastFps, 'rb') as settingsFileHandle: 
            fsSettings = pickle.load(settingsFileHandle)

            fsconfig.lastDetectedFps = fsSettings['lastDetectedFps']
            fsconfig.lastDetectedFile = fsSettings['lastDetectedFile']

        loadSettingsStatus = 'Loaded last FPS'
    except Exception:
        loadSettingsStatus = 'Failed to load last FPS'

    return loadSettingsStatus

def saveLastDetectedFps():

    globalLastFps = settingsLastFpsFile()

    fsSettings = {}
    fsSettings['lastDetectedFps'] = fsconfig.lastDetectedFps
    fsSettings['lastDetectedFile'] = fsconfig.lastDetectedFile

    # create or overwrite settings file
    try:
        with open(globalLastFps, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        saveSettingsStatus = 'Last FPS saved'
    except Exception:
        saveSettingsStatus = 'Failed to save last FPS'

    return saveSettingsStatus


def loadLastFreqChangeSetting():

    globalLastChange = settingsLastChangeFile()

    # read settings file
    try:
        with open(globalLastChange, 'rb') as settingsFileHandle: 
            fsSettings = pickle.load(settingsFileHandle)

            fsconfig.lastFreqChange = fsSettings['lastFreqChange']

        loadSettingsStatus = 'Loaded last change time'
    except Exception:
        loadSettingsStatus = 'Failed to load last change time'

    return loadSettingsStatus    

def saveLastFreqChangeSetting():

    globalLastChange = settingsLastChangeFile()

    fsSettings = {}

    fsSettings['lastFreqChange'] = fsconfig.lastFreqChange

    # create or overwrite settings file
    try:
        with open(globalLastChange, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        saveSettingsStatus = 'Last change time saved'
    except Exception:
        saveSettingsStatus = 'Failed to save last change time'

    return saveSettingsStatus


def loadAutoSyncSettings():

    globalAutoSync = settingsAutoSyncFile()

    # read settings file
    try:
        with open(globalAutoSync, 'rb') as settingsFileHandle: 
            fsSettings = pickle.load(settingsFileHandle)

            # auto-set configuration
            fsconfig.radioAuto60hz = fsSettings['radioAuto60hz']
            fsconfig.radioAuto50hz = fsSettings['radioAuto50hz']
            fsconfig.radioAuto30hz = fsSettings['radioAuto30hz']
            fsconfig.radioAuto25hz = fsSettings['radioAuto25hz']
            fsconfig.radioAuto24hz = fsSettings['radioAuto24hz']

            fsconfig.edit60hzFps1 = fsSettings['edit60hzFps1']
            fsconfig.edit60hzFps2 = fsSettings['edit60hzFps2']
            fsconfig.edit60hzFps3 = fsSettings['edit60hzFps3']
            fsconfig.edit60hzFps4 = fsSettings['edit60hzFps4']

            fsconfig.edit50hzFps1 = fsSettings['edit50hzFps1']
            fsconfig.edit50hzFps2 = fsSettings['edit50hzFps2']
            fsconfig.edit50hzFps3 = fsSettings['edit50hzFps3']
            fsconfig.edit50hzFps4 = fsSettings['edit50hzFps4']

            fsconfig.edit30hzFps1 = fsSettings['edit30hzFps1']
            fsconfig.edit30hzFps2 = fsSettings['edit30hzFps2']
            fsconfig.edit30hzFps3 = fsSettings['edit30hzFps3']
            fsconfig.edit30hzFps4 = fsSettings['edit30hzFps4']

            fsconfig.edit25hzFps1 = fsSettings['edit25hzFps1']
            fsconfig.edit25hzFps2 = fsSettings['edit25hzFps2']
            fsconfig.edit25hzFps3 = fsSettings['edit25hzFps3']
            fsconfig.edit25hzFps4 = fsSettings['edit25hzFps4']

            fsconfig.edit24hzFps1 = fsSettings['edit24hzFps1']
            fsconfig.edit24hzFps2 = fsSettings['edit24hzFps2']
            fsconfig.edit24hzFps3 = fsSettings['edit24hzFps3']
            fsconfig.edit24hzFps4 = fsSettings['edit24hzFps4']

        loadSettingsStatus = 'Loaded auto sync settings'
    except Exception:
        loadSettingsStatus = 'Failed to load auto sync settings'

    return loadSettingsStatus

def saveAutoSyncSettings():

    globalAutoSync = settingsAutoSyncFile()

    fsSettings = {}

    # auto-set configuration
    fsSettings['radioAuto60hz'] = fsconfig.radioAuto60hz
    fsSettings['radioAuto50hz'] = fsconfig.radioAuto50hz
    fsSettings['radioAuto30hz'] = fsconfig.radioAuto30hz
    fsSettings['radioAuto25hz'] = fsconfig.radioAuto25hz
    fsSettings['radioAuto24hz'] = fsconfig.radioAuto24hz

    fsSettings['edit60hzFps1'] = fsconfig.edit60hzFps1
    fsSettings['edit60hzFps2'] = fsconfig.edit60hzFps2
    fsSettings['edit60hzFps3'] = fsconfig.edit60hzFps3
    fsSettings['edit60hzFps4'] = fsconfig.edit60hzFps4

    fsSettings['edit50hzFps1'] = fsconfig.edit50hzFps1
    fsSettings['edit50hzFps2'] = fsconfig.edit50hzFps2
    fsSettings['edit50hzFps3'] = fsconfig.edit50hzFps3
    fsSettings['edit50hzFps4'] = fsconfig.edit50hzFps4

    fsSettings['edit30hzFps1'] = fsconfig.edit30hzFps1
    fsSettings['edit30hzFps2'] = fsconfig.edit30hzFps2
    fsSettings['edit30hzFps3'] = fsconfig.edit30hzFps3
    fsSettings['edit30hzFps4'] = fsconfig.edit30hzFps4

    fsSettings['edit25hzFps1'] = fsconfig.edit25hzFps1
    fsSettings['edit25hzFps2'] = fsconfig.edit25hzFps2
    fsSettings['edit25hzFps3'] = fsconfig.edit25hzFps3
    fsSettings['edit25hzFps4'] = fsconfig.edit25hzFps4

    fsSettings['edit24hzFps1'] = fsconfig.edit24hzFps1
    fsSettings['edit24hzFps2'] = fsconfig.edit24hzFps2
    fsSettings['edit24hzFps3'] = fsconfig.edit24hzFps3
    fsSettings['edit24hzFps4'] = fsconfig.edit24hzFps4

    # create or overwrite settings file
    try:
        with open(globalAutoSync, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        saveSettingsStatus = 'Auto sync settings saved'
    except Exception:
        saveSettingsStatus = 'Failed to save auto sync settings'

    return saveSettingsStatus

  
def loadServiceConfig():

    globalServiceConfig = settingsServiceConfigFile()

    # read settings file
    try:
        with open(globalServiceConfig, 'rb') as settingsFileHandle: 
            fsSettings = pickle.load(settingsFileHandle)

            # service config
            fsconfig.radioOnPlayStop60 = fsSettings['radioOnPlayStop60']
            fsconfig.radioOnPlayStop50 = fsSettings['radioOnPlayStop50']
            fsconfig.radioNotifyOn = fsSettings['radioNotifyOn']

        loadSettingsStatus = 'Loaded service configuration'
    except Exception:
        loadSettingsStatus = 'Failed to load service configuration'

    return loadSettingsStatus

def saveServiceConfig():

    globalServiceConfig = settingsServiceConfigFile()

    fsSettings = {}

    # service
    fsSettings['radioOnPlayStop60'] = fsconfig.radioOnPlayStop60
    fsSettings['radioOnPlayStop50'] = fsconfig.radioOnPlayStop50
    fsSettings['radioNotifyOn'] = fsconfig.radioNotifyOn

    # create or overwrite settings file
    try:
        with open(globalServiceConfig, 'wb') as settingsFileHandle: 
            pickle.dump(fsSettings, settingsFileHandle)

        saveSettingsStatus = 'Service configuration saved'
    except Exception:
        saveSettingsStatus = 'Failed to save service configuration'

    return saveSettingsStatus



def loadActiveServiceSetting():

    fsconfig.activeService = activeServiceFlagGet()

def saveActiveServiceSetting():

    if fsconfig.activeService:
        activeServiceFlagSet()
    else:
        activeServiceFlagDel()


def loadActiveInfoSetting():

    fsconfig.activeInfo = activeInfoFlagGet()

def saveActiveInfoSetting():

    if fsconfig.activeInfo:
        activeInfoFlagSet()
    else:
        activeInfoFlagDel()


def activeServiceFlagGet():

    # active-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_service_active')

    # check whether flag file exists
    if os.path.isfile(serviceStateFlagFile):
        return True
    else:
        return False

def activeServiceFlagSet():

    # active-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_service_active')

    # check file does not already exist
    if not os.path.isfile(serviceStateFlagFile):

        # create active-service flag file
        open(serviceStateFlagFile, 'w').close()

def activeServiceFlagDel():

    # active-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_service_active')

    # check file exists
    if os.path.isfile(serviceStateFlagFile):

        # delete active-service flag file
        os.remove(serviceStateFlagFile)


def useServiceFlagGet():

    # use-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_use_service')

    # check whether flag file exists
    if os.path.isfile(serviceStateFlagFile):
        return True
    else:
        return False

def useServiceFlagSet():

    # use-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_use_service')

    # check file does not already exist
    if not os.path.isfile(serviceStateFlagFile):

        # create use-service flag file
        open(serviceStateFlagFile, 'w').close()

def useServiceFlagDel():

    # use-service flag file
    serviceStateFlagFolder = settingsFolder()
    serviceStateFlagFile = os.path.join(serviceStateFlagFolder, 'fs_use_service')

    # check file exists
    if os.path.isfile(serviceStateFlagFile):

        # delete use-service flag file
        os.remove(serviceStateFlagFile)

def activeInfoFlagFile():
    # active info panel flag file
    infoStateFlagFolder = settingsFolder()
    infoStateFlagFile = os.path.join(infoStateFlagFolder, 'fs_info_active')
    return infoStateFlagFile

def activeInfoFlagIsOld():

    # active info panel flag file
    infoStateFlagFile = activeInfoFlagFile()

    # check whether flag file exists
    if os.path.isfile(infoStateFlagFile):

        # check age of file (modified time) - seconds since epoch
        infoFileTime = os.path.getmtime(infoStateFlagFile)

        # compare file age with current time
        currentTime = calendar.timegm(time.gmtime())
        ageInSeconds = currentTime - infoFileTime

        # file is older than four seconds
        if ageInSeconds > 4:
            return True

        # file is active - i.e. not older than four seconds
        else:
            return False

    # file does not exist - treat as not old
    else:
        return False

def activeInfoFlagGet():

    # active info panel flag file
    infoStateFlagFile = activeInfoFlagFile()

    # check whether flag file exists
    if os.path.isfile(infoStateFlagFile):
        return True
    else:
        return False

def activeInfoFlagSet():

    # active info panel flag file
    infoStateFlagFile = activeInfoFlagFile()

    # check file does not already exist - NOT NECESSARY AS NEED TO CONTINUALLY FLAG INFO PANEL AS ACTIVE WHILE RUNNING
    # if not os.path.isfile(infoStateFlagFile):

    # create active-info flag file
    open(infoStateFlagFile, 'w').close()


def activeInfoFlagDel():

    # active info panel flag file
    infoStateFlagFile = activeInfoFlagFile()

    # check file exists
    if os.path.isfile(infoStateFlagFile):

        # delete active-service flag file
        os.remove(infoStateFlagFile)

