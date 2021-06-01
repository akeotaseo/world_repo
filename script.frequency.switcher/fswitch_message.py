import xbmcgui
import fswitch_config as fsconfig

def notifyInfo(title, msg):

    if fsconfig.radioNotifyOn:
        notifyDialog = xbmcgui.Dialog()
        notifyDialog.notification(title, msg, xbmcgui.NOTIFICATION_INFO, 2500, False)

def notifyQuickInfo(title, msg):

    if fsconfig.radioNotifyOn:
        notifyDialog = xbmcgui.Dialog()
        notifyDialog.notification(title, msg, xbmcgui.NOTIFICATION_INFO, 400, False)

def notifyWarn(title, msg):

    if fsconfig.radioNotifyOn:
        notifyDialog = xbmcgui.Dialog()
        notifyDialog.notification(title, msg, xbmcgui.NOTIFICATION_WARNING, 1000, False)

def notifyQuickWarn(title, msg):

    if fsconfig.radioNotifyOn:
        notifyDialog = xbmcgui.Dialog()
        notifyDialog.notification(title, msg, xbmcgui.NOTIFICATION_WARNING, 400, False)
