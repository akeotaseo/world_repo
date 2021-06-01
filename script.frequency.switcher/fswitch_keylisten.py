import xbmc
import xbmcaddon
import xbmcgui
import shutil

from threading import Timer

# translate object
translate = xbmcaddon.Addon().getLocalizedString

class KeyListener(xbmcgui.WindowXMLDialog):
    'function for getting pressed key code method and associated dialog window'

    TIMEOUT = 8

    KAITOAST_HEADING = 401
    KAITOAST_MESSAGE = 402

    MSG_PRESSKEY = 30000
    MSG_TIMEOUT  = 30001

    # object creation
    def __new__(cls):
        try: 
            version = xbmc.getInfoLabel('system.buildversion')
            if version[0:2] >= "17":
                return super(KeyListener, cls).__new__(cls, "DialogNotification.xml", "")
            else:
                return super(KeyListener, cls).__new__(cls, "DialogKaiToast.xml", "")
        except:
            xbmc.log("NOTICE = KeyListener no found")

    # object initialization
    def __init__(self):
        self.keyPressed = None

    # initialization event
    def onInit(self):
        try:
            self.getControl(self.KAITOAST_HEADING).addLabel(translate(self.MSG_PRESSKEY))
            self.getControl(self.KAITOAST_MESSAGE).addLabel(translate(self.MSG_TIMEOUT) % self.TIMEOUT)
        except AttributeError:
            self.getControl(self.KAITOAST_HEADING).setLabel(translate(self.MSG_PRESSKEY))
            self.getControl(self.KAITOAST_MESSAGE).setLabel(translate(self.MSG_TIMEOUT) % self.TIMEOUT)

    # window event (key listener)
    def onAction(self, action):

        # set key pressed to none
        self.keyPressed = None

        # get key pressed button code
        keyCode = action.getButtonCode()

        # check for a valid button code (ignore mouse input etc)
        if keyCode != 0:

            # convert button code to a string
            self.keyPressed = str(keyCode)

            # close dialog window
            self.close()

    @staticmethod
    def getKeyPressed():

        # create the dialog window 
        getkeyDialog = KeyListener()

        # create a timer to close dialog window
        getkeyTimer = Timer(KeyListener.TIMEOUT, getkeyDialog.close)

        # start the time
        getkeyTimer.start()

        # show the dialog window and wait for it to close
        getkeyDialog.doModal()

        # cancel the timer (if window closed before timer has ended)
        getkeyTimer.cancel()

        # get the key pressed from the dialog window 
        keyPressed = getkeyDialog.keyPressed

        # destroy the dialog window object
        del getkeyDialog

        # return the key pressed
        return keyPressed

