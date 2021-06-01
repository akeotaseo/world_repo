import xbmc

# delay startup to improve stability
xbmc.sleep(2000)

import fswitch_config as fsconfig
import fswitch_configutil as fsconfigutil
import fswitch_player as fsplay

class ServiceMain:
 
    @staticmethod
    def run():

        # load settings
        loadSettingsStatus = fsconfigutil.loadSettings()

        # check whether service should be activated
        if fsconfig.radioOnPlayStart:

            # record service as active
            fsconfig.activeService = True
            fsconfigutil.saveActiveServiceSetting()

            # create Player subclass
            fsplayer = fsplay.fsPlayer()

            # check for configuration changes every four seconds
            monitor_abort = xbmc.Monitor()  # For Kodi >= 14
            while not monitor_abort.abortRequested()  and fsconfig.radioOnPlayStart:

                xbmc.sleep(4000)

                # reload settings - to allow service stop and configuration changes without exiting XBMC
                fsconfig.radioOnPlayStart = fsconfigutil.useServiceFlagGet()

                fsconfigutil.loadServiceConfig()

        # check that service flagged as 'not used' is not also flagged as 'active' (can happen when clean up not run prior to reinstall)
        else:
            fsconfigutil.loadActiveServiceSetting()

        # service is finished - record service as not active
        if fsconfig.activeService:

            fsconfig.activeService = False
            fsconfigutil.saveActiveServiceSetting()

# only run main function if module is running directly (i.e. not imported)
if __name__ == '__main__':

    ServiceMain.run()

