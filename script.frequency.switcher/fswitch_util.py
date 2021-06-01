import os
import sys
import platform
import time
import subprocess
import xbmc
import xbmcaddon
import fswitch_config as fsconfig
import fswitch_configutil as fsconfigutil

def getSourceFPS():
# function for getting for source frame rate from the XBMC log file

    # initialize constants
    refVideoOpen = 'NOTICE: DVDPlayer: Opening: '
    refVideoFPSstart = 'NOTICE:  fps: '
    refVideoFPSend = ', pwidth: '

    # initialize return values
    videoFileName = None
    videoFPSValue = None

    # get location of log file
    if fsconfig.osPlatform[0:7] == 'Windows':
        logFileName = xbmc.translatePath('special://home\kodi.log')
    else:
        if  os.path.isfile(xbmc.translatePath('special://temp/ftmc.log')):
            logFileName = xbmc.translatePath('special://temp/ftmc.log')
        elif os.path.isfile(xbmc.translatePath('special://temp/spmc.log')):
            logFileName = xbmc.translatePath('special://temp/spmc.log')
        else:
            logFileName = xbmc.translatePath('special://temp/kodi.log')

    # wait 0.40 second for log file to update (with debug on W7: 0.35 not quite long enough for some files)
    xbmc.sleep(400)

    # check osPlatform linux2 (Krypton) 
    osPlatform, osVariant = getPlatformType()

    version = xbmc.getInfoLabel('system.buildversion')
    if version[0:2] >= "17":
        videoFPSValue = xbmc.getInfoLabel('Player.Process(VideoFps)')
        videoFileName = xbmc.Player().getPlayingFile()
    else:
        # open log file as read only
        with open(logFileName, 'r') as logFile:

            # move pointer to the EOF
            logFile.seek(0, 2)

            # get pointer location as the file size
            logFileSize = logFile.tell()

            # move pointer to 40k characters before EOF (or to BOF)   
            logFile.seek(max(logFileSize - 40000, 0), 0)

            # create list of lines from pointer to EOF
            logFileLines = logFile.readlines()

        # slice list to include just the last 1000 lines (with debug on W7: 200=10sec, 600=30sec, 800=45sec, 1000=2min40sec)
        logFileLines = logFileLines[-1000:]

        # reverse the list so most recent entry is first
        logFileLines.reverse() 

        # parse the list (from most recent backwards)
        for logFileIndex, logFileLine in enumerate(logFileLines):

            # find reference to video opening
            if refVideoOpen in logFileLine:

                # find start of video file name  
                linePointer = logFileLine.find(refVideoOpen) + len(refVideoOpen)
            
                # read video file name
                videoFileName = logFileLine[linePointer:].rstrip('\n')

                # Now find the FPS

                # slice new list at current index
                logFileLines2 = logFileLines[:logFileIndex]

                # reverse list2 so oldest entry is first
                logFileLines2.reverse() 

                # parse list2 (from video opening reference forward)
                for logFileLine2 in logFileLines2:

                    # find reference to FPS
                    if refVideoFPSstart in logFileLine2:

                        # find start and end of FPS value
                        linePointerStart = logFileLine2.find(refVideoFPSstart) + len(refVideoFPSstart)
                        linePointerEnd = logFileLine2.find(refVideoFPSend)

                        # read FPS value
                        videoFPSValue = logFileLine2[linePointerStart:linePointerEnd]

                        # truncate FPS to three decimal places
                        decSplit = videoFPSValue.find('.') + 4
                        videoFPSValue = videoFPSValue[0:decSplit]

                        # only save FPS if not 0.000 (seen on one dvd-iso)
                        if videoFPSValue != '0.000':

                            # save FPS for use in setDisplayModeAuto
                            fsconfig.lastDetectedFps = videoFPSValue
                            fsconfig.lastDetectedFile = videoFileName
                            fsconfigutil.saveLastDetectedFps()

                            # found FPS - stop parsing list2
                            break

                        # FPS is 0.000 - treat as not found
                        else:
                            videoFPSValue = None

                # found video open and FPS (if not 0.000) - stop parsing the list
                break

    # only save FPS if not 0.000 (seen on one dvd-iso)
    if videoFPSValue != '0.000':
        # save FPS for use in setDisplayModeAuto
        fsconfig.lastDetectedFps = videoFPSValue
        fsconfig.lastDetectedFile = videoFileName
        fsconfigutil.saveLastDetectedFps()
    else:
        videoFPSValue = None

    return videoFileName, videoFPSValue

def getPlatformType():
# function for getting platform type

    osPlatform = sys.platform

    if osPlatform == 'win32':
        osVariant = platform.system() + ' ' + platform.release()

    elif (osPlatform[0:5] == 'linux') and os.path.isfile("/sys/class/display/mode"):
        try:
            productBrand = subprocess.Popen(['getprop', 'ro.product.brand'], stdout=subprocess.PIPE).communicate()[0].strip()
            productDevice = subprocess.Popen(['getprop', 'ro.product.device'], stdout=subprocess.PIPE).communicate()[0].strip()
            osVariant = productBrand + ' ' + productDevice
        except:
            osVariant = platform.system() + ' ' + platform.release()
    else:
        osVariant = 'unsupported'

    return osPlatform, osVariant

def getDisplayMode():
# function to read the current output mode from display/mode

    modeFile = None
    outputMode = None
    amlogicMode = None

    modeFileAndroid = "/sys/class/display/mode"
    modeFileWindows = "d:\\x8mode.txt"

    if fsconfig.osPlatform[0:7] == 'Windows':
        modeFile = modeFileWindows 
    else:
        modeFile = modeFileAndroid

    # check file exists
    if os.path.isfile(modeFile):
        # check file is writable
        if os.access(modeFile, os.R_OK):
            with open(modeFile, 'r') as modeFileHandle:      
                amlogicMode = modeFileHandle.readline().strip()

                # convert AMLOGIC output mode to more descriptive mode
                if amlogicMode == '1080p':
                    outputMode = '1080p-60hz'
                elif amlogicMode == '1080p60hz':
                    outputMode = '1080p-60hz'
                elif amlogicMode == '1080p50hz':
                    outputMode = '1080p-50hz'
                elif amlogicMode == '1080p30hz':
                    outputMode = '1080p-30hz'
                elif amlogicMode == '1080p25hz':
                    outputMode = '1080p-25hz'
                elif amlogicMode == '1080p24hz':
                    outputMode = '1080p-24hz'
                elif amlogicMode == '720p':
                    outputMode = '720p-60hz'
                elif amlogicMode == '720p50hz':
                    outputMode = '720p-50hz'
                elif amlogicMode == '2160p60hz':
                    outputMode = '4k2k-60hz'
                elif amlogicMode == '2160p50hz':
                    outputMode = '4k2k-50hz'
                elif amlogicMode == '2160p30hz':
                    outputMode = '4k2k-30hz'
                elif amlogicMode == '2160p25hz':
                    outputMode = '4k2k-25hz'
                elif amlogicMode == '2160p24hz':
                    outputMode = '4k2k-24hz'
                else:
                    outputMode = "unsupported"

            if amlogicMode == '':
                outputMode = "invalid"
                amlogicMode = 'Mode file read, but is empty.'
        else:
            outputMode = "invalid"
            amlogicMode = 'Mode file found, but could not read.'                
    else:
        outputMode = "invalid"
        amlogicMode = 'Mode file not found.'

    return outputMode, amlogicMode

def getDisplayModeFileStatus():
# function to check that the display/mode file exists and is writable

    modeFile = None
    fileStatus = None
    
    modeFileAndroid = "/sys/class/display/mode"
    modeFileWindows = "d:\\x8mode.txt"

    if fsconfig.osPlatform[0:7] == 'Windows':
        modeFile = modeFileWindows 
    else:
        modeFile = modeFileAndroid
        try:
            subprocess.call(["su", "root", "chmod", "666", "/sys/class/display/mode"])
            subprocess.call(["su", "root", "chmod", "666", "/sys/class/amhdmitx/amhdmitx0/hdcp_mode"])
        except:
            pass

    # check file exists
    if os.path.isfile(modeFile):
        # check file is writable
        if os.access(modeFile, os.W_OK):
            fileStatus = 'OK: Frequency switching is supported'
        else:
            fileStatus = 'HDMI mode file is read only'                
    else:
        fileStatus = 'HDMI mode file not found'

    return modeFile, fileStatus

def setDisplayMode(newOutputMode):
    # function to write the current output mode from display/mode

    # check whether display/mode file it writable 
    modeFile, fileStatus = getDisplayModeFileStatus()
     
    # display/mode file is not writable
    if fileStatus[:2] != 'OK':
        setModeStatus = fileStatus
        statusType = 'warn'

    # display/mode file is writable
    else:

        # convert output mode to a valid AMLOGIC mode
        if newOutputMode == '1080p-60hz':
            newAmlogicMode = '1080p60hz'
        elif newOutputMode == '1080p-50hz':
            newAmlogicMode = '1080p50hz'
        elif newOutputMode == '1080p-30hz':
            newAmlogicMode = '1080p30hz'
        elif newOutputMode == '1080p-25hz':
            newAmlogicMode = '1080p25hz'
        elif newOutputMode == '1080p-24hz':
            newAmlogicMode = '1080p24hz'
        elif newOutputMode == '720p-60hz':
            newAmlogicMode = '720p'
        elif newOutputMode == '720p-50hz':
            newAmlogicMode = '720p50hz'
        elif newOutputMode == '4k2k-60hz':
            newAmlogicMode = '2160p60hz'
        elif newOutputMode == '4k2k-50hz':
            newAmlogicMode = '2160p50hz'
        elif newOutputMode == '4k2k-30hz':
            newAmlogicMode = '2160p30hz'
        elif newOutputMode == '4k2k-25hz':
            newAmlogicMode = '2160p25hz'
        elif newOutputMode == '4k2k-24hz':
            newAmlogicMode = '2160p24hz'
        else:
            setModeStatus = 'Unsupported mode requested.'
            statusType = 'warn'
            return setModeStatus, statusType

        # check current display mode setting
        currentOutputMode, currentAmlogicMode = getDisplayMode()
               
        # get current resolution
        resSplit = currentOutputMode.find('-')
        currentRes = currentOutputMode[0:resSplit]

        # get new resolution
        resSplit = newOutputMode.find('-')
        newRes = newOutputMode[0:resSplit]
        
        # get new frequency
        freqSplit = newOutputMode.find('-') + 1
        newFreq = newOutputMode[freqSplit:len(newOutputMode)]

        # current output mode is the same as new output mode
        if currentOutputMode == newOutputMode:
            setModeStatus = 'Frequency already set to ' + newFreq 
            statusType = 'warn'

        # current output mode is different to new output mode
        else:
            
            # new resolution is different to current resolution
            if newRes != currentRes:
                setModeStatus = 'Resolution changed, please reconfigure'
                statusType = 'warn'

            # new resolution is the same as the current resolution
            else: 
                fsconfigutil.loadLastFreqChangeSetting()

                # check that at least 4 seconds has elapsed since the last frequency change
                secToNextFreqChange = 4 - (int(time.time()) - fsconfig.lastFreqChange)
                if secToNextFreqChange > 1:
                    setModeStatus = 'Stand-down ' + str(secToNextFreqChange) + ' seconds'               
                    statusType = 'warn'
                elif secToNextFreqChange == 1:
                    setModeStatus = 'Stand-down ' + str(secToNextFreqChange) + ' second' 
                    statusType = 'warn'

                # more than 4 seconds has elapsed since the last frequency change 
                else:
                    # set new display mode
                    with open(modeFile, 'w') as modeFileHandle: 
                        modeFileHandle.write(newAmlogicMode)

                    # save time display mode was changed
                    fsconfig.lastFreqChange = int(time.time())
                    fsconfigutil.saveLastFreqChangeSetting()
                    
                    setModeStatus = 'Frequency changed to ' + newFreq
                    statusType = 'info'

        try:
            with open("/sys/class/amhdmitx/amhdmitx0/hdcp_mode", 'w') as modeFileamhdmitx:
                modeFileamhdmitx.write('11')
        except:
            pass

    return setModeStatus, statusType

def getCurrentFPS():
    
    # get currently playing video
    videoFileNamePlay = getPlayingVideo()

    # playing video not detected
    if videoFileNamePlay is None:
        setModeStatus = 'No playing video detected.'
        statusType = 'warn'
    
    # playing video detected
    else:

        # check last detected info (before reading the log file)
        fsconfigutil.loadLastDetectedFps()

        # last detected file name matches currently playing video, so use last detected FPS
        if fsconfig.lastDetectedFile == videoFileNamePlay:
            videoFileNameLog = fsconfig.lastDetectedFile
            videoFPSValue = fsconfig.lastDetectedFps

        # FPS not stored as last detected FPS
        else:
            # read FPS from XBMC log
            videoFileNameLog, videoFPSValue = getSourceFPS()

        # FPS not detected
        if videoFPSValue is None:
            setModeStatus = 'Failed to get source framerate.'
            statusType = 'warn'

        # FPS detected
        else:
            # log file name doesn't match currently playing video
            if videoFileNameLog != videoFileNamePlay:
                setModeStatus = 'Found source framerate for wrong video file.'
                statusType = 'warn'

            # log file name matches currently playing video
            else:
                setModeStatus = videoFPSValue
                statusType = 'ok'

    return setModeStatus, statusType

def setDisplayModeAuto():
    # function to write the current output mode based on FPS to Frequency configuration

    # check current display mode setting
    currentOutputMode, currentAmlogicMode = getDisplayMode()

    if currentOutputMode == 'unsupported':
        setModeStatus = 'Unsupported resolution: ' + currentAmlogicMode           
        statusType = 'warn'

    elif currentOutputMode == 'invalid':
        setModeStatus = 'Error, unexpected mode: ' + currentAmlogicMode       
        statusType = 'warn'

    else:
        # load auto sync settings
        fsconfigutil.loadAutoSyncSettings()

        # get current resolution
        resSplit = currentOutputMode.find('-')
        currentRes = currentOutputMode[0:resSplit]

        mode60hz = currentRes + '-60hz'
        mode50hz = currentRes + '-50hz'
        mode30hz = currentRes + '-30hz'
        mode25hz = currentRes + '-25hz'
        mode24hz = currentRes + '-24hz'

        autoSync = []

        syncConfig = []        
        if fsconfig.radioAuto60hz:
            syncConfig.extend([(fsconfig.edit60hzFps1, mode60hz),
                               (fsconfig.edit60hzFps2, mode60hz), 
                               (fsconfig.edit60hzFps3, mode60hz), 
                               (fsconfig.edit60hzFps4, mode60hz)])

        if fsconfig.radioAuto50hz:
            syncConfig.extend([(fsconfig.edit50hzFps1, mode50hz), 
                               (fsconfig.edit50hzFps2, mode50hz), 
                               (fsconfig.edit50hzFps3, mode50hz), 
                               (fsconfig.edit50hzFps4, mode50hz)])

        if fsconfig.radioAuto30hz:
            syncConfig.extend([(fsconfig.edit30hzFps1, mode30hz), 
                               (fsconfig.edit30hzFps2, mode30hz), 
                               (fsconfig.edit30hzFps3, mode30hz), 
                               (fsconfig.edit30hzFps4, mode30hz)])

        if fsconfig.radioAuto25hz:
            syncConfig.extend([(fsconfig.edit25hzFps1, mode25hz), 
                               (fsconfig.edit25hzFps2, mode25hz), 
                               (fsconfig.edit25hzFps3, mode25hz), 
                               (fsconfig.edit25hzFps4, mode25hz)])

        if fsconfig.radioAuto24hz:
            syncConfig.extend([(fsconfig.edit24hzFps1, mode24hz), 
                               (fsconfig.edit24hzFps2, mode24hz),
                               (fsconfig.edit24hzFps3, mode24hz),
                               (fsconfig.edit24hzFps4, mode24hz)])        

        # build auto sync list
        for (syncFPS, syncMode) in syncConfig:
            if syncFPS != '':
                autoSync.insert(0, (syncFPS, syncMode))

        if not autoSync:
            setModeStatus = 'No FPS to frequency configuration defined'       
            statusType = 'warn'

        else:

            # get FPS of currently playing video
            setModeStatus, statusType = getCurrentFPS()

            if statusType == 'ok':
                videoFPSValue = setModeStatus

                # search auto sync list for FPS
                fpsFoundInSyncList = False
                for (syncFPS, syncFreq) in autoSync:
                    if syncFPS == videoFPSValue:
                        fpsFoundInSyncList = True
                        break

                # FPS not found configured in auto sync list
                if not fpsFoundInSyncList:
                    setModeStatus = 'Source framerate not configured: ' + videoFPSValue                        
                    statusType = 'warn'

                # FPS found in auto sync list       
                else:

                    # check for unsupported mode '720p-24hz'
                    if syncFreq == '720p-24hz':
                        setModeStatus = syncFreq + ' is not supported'
                        statusType = 'warn'                      

                    else:
                        # set the output mode
                        setModeStatus, statusType = setDisplayMode(syncFreq)

    return setModeStatus, statusType

def mapKey(keyScope, keyMappings):
# function for saving key mappings - rewrites entire zswitch.xml file

    # build key map
    mapStart = '<keymap><' + keyScope + '><keyboard>'
    keyStart = '<key id="'
    keyMiddle = '">runaddon(script.frequency.switcher,'
    keyEnd = ')</key>'
    mapEnd = '</keyboard></global></keymap>'  

    keyMap = mapStart
    for (keyCode, keyFunction) in keyMappings:
        keyMap = keyMap + keyStart + keyCode + keyMiddle + keyFunction + keyEnd
    keyMap = keyMap + mapEnd

    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')

    # create keymap folder if it doesn't already exist
    if not os.path.exists(keymapFolder):
        os.makedirs(keymapFolder)

    # create or overwrite keymap file
    try:
        with open(keymapFile, 'w') as keymapFileHandle: 
            keymapFileHandle.write(keyMap)
        mapKeyStatus = 'Keys activated'
    except Exception:
        mapKeyStatus = 'Failed to activate keys'

    # load updated key maps
    xbmc.executebuiltin('action(reloadkeymaps)')

    return mapKeyStatus

def mapKeyReset():
    
    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')

    # check file exists
    if not os.path.isfile(keymapFile):
        mapKeyResetStatus = 'No keys currently active'
        return mapKeyResetStatus

    # delete key map file
    try:
        os.remove(keymapFile)
        mapKeyResetStatus = 'Keys deactivated'
    except Exception:
        mapKeyResetStatus = 'Failed to deactivate keys'

    # load updated key maps
    xbmc.executebuiltin('action(reloadkeymaps)')

    return mapKeyResetStatus

def mapKeyActive():

    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')

    # check file exists
    return os.path.isfile(keymapFile)

def getPlayingVideo():
# function to get the file name of the currently playing video

    if xbmc.Player().isPlayingVideo():
        videoFileName = xbmc.Player().getPlayingFile() 
    else:
        videoFileName = None

    return videoFileName
