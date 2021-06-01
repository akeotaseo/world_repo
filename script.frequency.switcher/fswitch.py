import sys
import xbmcgui
import fswitch_window as fswin
import fswitch_util as fsutil
import fswitch_message as fsmsg
import fswitch_configutil as fsconfigutil
import fswitch_config as fsconfig

class Main:
    'main function - determine platform and process arguments'

    @staticmethod
    def run():

        scriptMode = None

        # if the only argument is script name then run in setup mode
        if len(sys.argv) == 1:
            scriptMode = 'Setup'

        # otherwise select mode based on the first argument 
        else:
            scriptArg = sys.argv[1]

            if scriptArg == '4k2k-60hz':
                scriptMode = 'SetFreq'              
            elif scriptArg == '4k2k-50hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '4k2k-30hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '4k2k-25hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '4k2k-24hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '1080p-60hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '1080p-50hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '1080p-30hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '1080p-25hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '1080p-24hz':
                scriptMode = 'SetFreq'
            elif scriptArg == '720p-60hz':
                scriptMode = 'SetFreq'              
            elif scriptArg == '720p-50hz':
                scriptMode = 'SetFreq'
            elif scriptArg == 'auto':
                scriptMode = 'AutoSet'
            elif scriptArg == 'info':
                scriptMode = 'ShowInfo'

        # create default settings (if they don't already exist)
        fsconfigutil.createAllSettingsFiles()

        # load settings
        loadSettingsStatus = fsconfigutil.loadSettings()
        
        if scriptMode == 'Setup':
            # Create and show main configuration window
            fsMainWindow = fswin.MainWindow('Frequency Switcher configuration')
            fsMainWindow.doModal()

        elif scriptMode == 'SetFreq':
            # set the output mode
            setModeStatus, statusType = fsutil.setDisplayMode(scriptArg)

            # display notification
            if statusType == 'warn':
                fsmsg.notifyQuickWarn('Frequency Switcher', setModeStatus)    
            else:
                fsmsg.notifyInfo('Frequency Switcher', setModeStatus)

        elif scriptMode == 'AutoSet':
            # set the output mode automatically
            setModeStatus, statusType = fsutil.setDisplayModeAuto()

            # display notification
            if statusType == 'warn':
                fsmsg.notifyQuickWarn('Frequency Switcher', setModeStatus)    
            else:
                fsmsg.notifyInfo('Frequency Switcher', setModeStatus)

        elif scriptMode == 'ShowInfo':
            fsconfigutil.loadActiveInfoSetting()

            # disable info panel if currently active
            if fsconfig.activeInfo:

                # check that the active info panel flag file is not old (occurs if XBMC crashes)
                if fsconfigutil.activeInfoFlagIsOld():
                    fswin.InfoPanel.showInfo()

                # flag file is new so deactivate panel
                else:    
                    fsconfig.activeInfo = False
                    fsconfigutil.saveActiveInfoSetting()

            # show info panel if not currently active    
            else:              
                fswin.InfoPanel.showInfo()

        else:
            fsmsg.notifyInfo('Invalid script argument', scriptArg)


# only run main function if module is running directly (i.e. not imported)
if __name__ == '__main__':
    Main.run()

