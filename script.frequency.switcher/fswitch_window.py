import xbmc
import xbmcgui
import os
import fswitch_config as fsconfig
import fswitch_configutil as fsconfigutil
import fswitch_util as fsutil
import fswitch_keylisten as fskeylisten

from pyxbmct.addonwindow import *

class MapKeysWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MapKeysWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 13)

        # create, place, then set objects
        self.labelCurrentRes = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCurrentRes, 1, 1, columnspan=10, pad_y=11)

        self.radio60hz = RadioButton('60 hz')
        self.placeControl(self.radio60hz, 2, 1, columnspan=3)
        self.radio60hz.setSelected(fsconfig.radio60hz)

        self.radio50hz = RadioButton('50 hz')
        self.placeControl(self.radio50hz, 3, 1, columnspan=3)
        self.radio50hz.setSelected(fsconfig.radio50hz)

        self.radio30hz = RadioButton('30 hz')
        self.placeControl(self.radio30hz, 4, 1, columnspan=3)
        self.radio30hz.setSelected(fsconfig.radio30hz)

        self.radio25hz = RadioButton('25 hz')
        self.placeControl(self.radio25hz, 5, 1, columnspan=3)
        self.radio25hz.setSelected(fsconfig.radio25hz)

        self.radio24hz = RadioButton('24 hz')
        self.placeControl(self.radio24hz, 6, 1, columnspan=3)
        self.radio24hz.setSelected(fsconfig.radio24hz)

        self.radioAuto = RadioButton('Automatic')
        self.placeControl(self.radioAuto, 7, 1, columnspan=3)
        self.radioAuto.setSelected(fsconfig.radioAuto)

        self.radioInfo = RadioButton('Info.')
        self.placeControl(self.radioInfo, 8, 1, columnspan=3)
        self.radioInfo.setSelected(fsconfig.radioInfo)

        self.buttonMap60hz = Button('Select Key')
        self.placeControl(self.buttonMap60hz, 2, 7, columnspan=3)

        self.buttonMap50hz = Button('Select Key')
        self.placeControl(self.buttonMap50hz, 3, 7, columnspan=3)

        self.buttonMap30hz = Button('Select Key')
        self.placeControl(self.buttonMap30hz, 4, 7, columnspan=3)

        self.buttonMap25hz = Button('Select Key')
        self.placeControl(self.buttonMap25hz, 5, 7, columnspan=3)

        self.buttonMap24hz = Button('Select Key')
        self.placeControl(self.buttonMap24hz, 6, 7, columnspan=3)

        self.buttonMapAuto = Button('Select Key')
        self.placeControl(self.buttonMapAuto, 7, 7, columnspan=3)

        self.buttonMapInfo = Button('Select Key')
        self.placeControl(self.buttonMapInfo, 8, 7, columnspan=3)

        self.labelKey60hz = Label('')
        self.placeControl(self.labelKey60hz, 2, 5, columnspan=2, pad_y=11)
        self.labelKey60hz.setLabel(fsconfig.key60hz)

        self.labelKey50hz = Label('')
        self.placeControl(self.labelKey50hz, 3, 5, columnspan=2, pad_y=11)
        self.labelKey50hz.setLabel(fsconfig.key50hz)

        self.labelKey30hz = Label('')
        self.placeControl(self.labelKey30hz, 4, 5, columnspan=2, pad_y=11)
        self.labelKey30hz.setLabel(fsconfig.key30hz)

        self.labelKey25hz = Label('')
        self.placeControl(self.labelKey25hz, 5, 5, columnspan=2, pad_y=11)
        self.labelKey25hz.setLabel(fsconfig.key25hz)

        self.labelKey24hz = Label('')
        self.placeControl(self.labelKey24hz, 6, 5, columnspan=2, pad_y=11)
        self.labelKey24hz.setLabel(fsconfig.key24hz)

        self.labelKeyAuto = Label('')
        self.placeControl(self.labelKeyAuto, 7, 5, columnspan=2, pad_y=11)
        self.labelKeyAuto.setLabel(fsconfig.keyAuto)

        self.labelKeyInfo = Label('')
        self.placeControl(self.labelKeyInfo, 8, 5, columnspan=2, pad_y=11)
        self.labelKeyInfo.setLabel(fsconfig.keyInfo)

        self.buttonMapKeysSave = Button('Activate Keys')
        self.placeControl(self.buttonMapKeysSave, 10, 1, columnspan=4)

        self.buttonMapKeysReset = Button('Deactivate Keys')
        self.placeControl(self.buttonMapKeysReset, 11, 1, columnspan=4)

        self.checkKeyMap()  

        self.labelStatus60hz = Label('')
        self.placeControl(self.labelStatus60hz, 2, 11, columnspan=2, pad_y=11)
        self.labelStatus60hz.setLabel(fsconfig.status60hz)

        self.labelStatus50hz = Label('')
        self.placeControl(self.labelStatus50hz, 3, 11, columnspan=2, pad_y=11)
        self.labelStatus50hz.setLabel(fsconfig.status50hz)

        self.labelStatus30hz = Label('')
        self.placeControl(self.labelStatus30hz, 4, 11, columnspan=2, pad_y=11)
        self.labelStatus30hz.setLabel(fsconfig.status30hz)

        self.labelStatus25hz = Label('')
        self.placeControl(self.labelStatus25hz, 5, 11, columnspan=2, pad_y=11)
        self.labelStatus25hz.setLabel(fsconfig.status25hz)

        self.labelStatus24hz = Label('')
        self.placeControl(self.labelStatus24hz, 6, 11, columnspan=2, pad_y=11)
        self.labelStatus24hz.setLabel(fsconfig.status24hz)

        self.labelStatusAuto = Label('')
        self.placeControl(self.labelStatusAuto, 7, 11, columnspan=2, pad_y=11)
        self.labelStatusAuto.setLabel(fsconfig.statusAuto)

        self.labelStatusInfo = Label('')
        self.placeControl(self.labelStatusInfo, 8, 11, columnspan=2, pad_y=11)
        self.labelStatusInfo.setLabel(fsconfig.statusInfo)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 10, 6, columnspan=8, pad_y=11)
        
        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 11, 6, columnspan=8, pad_y=11)

        # connect buttons and actions to functions
        self.connect(self.radio60hz, self.clickRadio60hz)
        self.connect(self.radio50hz, self.clickRadio50hz)
        self.connect(self.radio30hz, self.clickRadio30hz)
        self.connect(self.radio25hz, self.clickRadio25hz)
        self.connect(self.radio24hz, self.clickRadio24hz)
        self.connect(self.radioAuto, self.clickRadioAuto)
        self.connect(self.radioInfo, self.clickRadioInfo)
        self.connect(self.buttonMap60hz, self.clickButtonMap60hz)
        self.connect(self.buttonMap50hz, self.clickButtonMap50hz)
        self.connect(self.buttonMap30hz, self.clickButtonMap30hz)
        self.connect(self.buttonMap25hz, self.clickButtonMap25hz)
        self.connect(self.buttonMap24hz, self.clickButtonMap24hz)
        self.connect(self.buttonMapAuto, self.clickButtonMapAuto)
        self.connect(self.buttonMapInfo, self.clickButtonMapInfo)
        self.connect(self.buttonMapKeysSave, self.clickMapKeysSave)
        self.connect(self.buttonMapKeysReset, self.clickMapKeysReset)       
        self.connect(ACTION_NAV_BACK, self.close)

        # set the enabled state of objects
        self.atSetup = True
        self.clickRadio60hz()
        self.clickRadio50hz()
        self.clickRadio30hz()
        self.clickRadio25hz()
        self.clickRadio24hz()
        self.clickRadioAuto()
        self.clickRadioInfo()
        self.atSetup = False

        # check current display mode setting
        currentOutputMode, currentAmlogicMode = fsutil.getDisplayMode()

        if currentOutputMode == 'unsupported':
            self.labelCurrentRes.setLabel('Unsupported resolution: ' + currentAmlogicMode)           
            self.disableAll()

        elif currentOutputMode == 'invalid':
            self.labelCurrentRes.setLabel('Error: ' + currentAmlogicMode)       
            self.disableAll()

        else:
            # get current resolution
            resSplit = currentOutputMode.find('-')
            self.currentRes = currentOutputMode[0:resSplit]
            self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes)       

            if self.currentRes == '720p':
                self.disable24hz()

            # check whether res has changed since KeyMap was last saved
            if (self.currentRes != fsconfig.keymapRes) and (fsconfig.keymapRes != ''):
                self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes + ' (active resolution was ' + fsconfig.keymapRes + ')')       
                self.clickMapKeysReset()

        # define key navigation (up-down)
        self.radio60hz.controlDown(self.radio50hz)
        self.radio50hz.controlUp(self.radio60hz)
        self.radio50hz.controlDown(self.radio30hz)
        self.radio30hz.controlUp(self.radio50hz)
        self.radio30hz.controlDown(self.radio25hz)
        self.radio25hz.controlUp(self.radio30hz)
        self.radio25hz.controlDown(self.radio24hz)
        self.radio24hz.controlUp(self.radio25hz)
        self.radio24hz.controlDown(self.radioAuto)
        self.radioAuto.controlUp(self.radio24hz)
        self.radioAuto.controlDown(self.radioInfo)
        self.radioInfo.controlUp(self.radioAuto)
        self.radioInfo.controlDown(self.buttonMapKeysSave)      
        self.buttonMapKeysSave.controlUp(self.radioInfo)
        self.buttonMapKeysSave.controlDown(self.buttonMapKeysReset)
        self.buttonMapKeysReset.controlUp(self.buttonMapKeysSave)

        self.buttonMap60hz.controlDown(self.buttonMap50hz)
        self.buttonMap50hz.controlUp(self.buttonMap60hz)
        self.buttonMap50hz.controlDown(self.buttonMap30hz)
        self.buttonMap30hz.controlUp(self.buttonMap50hz)
        self.buttonMap30hz.controlDown(self.buttonMap25hz)
        self.buttonMap25hz.controlUp(self.buttonMap30hz)
        self.buttonMap25hz.controlDown(self.buttonMap24hz)
        self.buttonMap24hz.controlUp(self.buttonMap50hz)
        self.buttonMap24hz.controlDown(self.buttonMapAuto)
        self.buttonMapAuto.controlUp(self.buttonMap24hz)
        self.buttonMapAuto.controlDown(self.buttonMapInfo)
        self.buttonMapInfo.controlUp(self.buttonMapAuto)
        self.buttonMapInfo.controlDown(self.buttonMapKeysSave)

        # define key navigation (left-right)
        self.radio60hz.controlRight(self.buttonMap60hz)
        self.buttonMap60hz.controlLeft(self.radio60hz)
        self.radio50hz.controlRight(self.buttonMap50hz)
        self.buttonMap50hz.controlLeft(self.radio50hz)
        self.radio30hz.controlRight(self.buttonMap30hz)
        self.buttonMap30hz.controlLeft(self.radio30hz)
        self.radio25hz.controlRight(self.buttonMap25hz)
        self.buttonMap25hz.controlLeft(self.radio25hz)
        self.radio24hz.controlRight(self.buttonMap24hz)
        self.buttonMap24hz.controlLeft(self.radio24hz)
        self.radioAuto.controlRight(self.buttonMapAuto)
        self.buttonMapAuto.controlLeft(self.radioAuto)
        self.radioInfo.controlRight(self.buttonMapInfo)
        self.buttonMapInfo.controlLeft(self.radioInfo)

        # set initial focus
        self.setFocus(self.radio60hz)

    def disable24hz(self):

        self.radio24hz.setEnabled(False)
        self.buttonMap24hz.setEnabled(False)
        self.labelKey24hz.setEnabled(False)

    def disableAll(self):

        self.radio60hz.setEnabled(False)
        self.buttonMap60hz.setEnabled(False)
        self.labelKey60hz.setEnabled(False)

        self.radio50hz.setEnabled(False)
        self.buttonMap50hz.setEnabled(False)
        self.labelKey50hz.setEnabled(False)

        self.radio30hz.setEnabled(False)
        self.buttonMap30hz.setEnabled(False)
        self.labelKey30hz.setEnabled(False)

        self.radio25hz.setEnabled(False)
        self.buttonMap25hz.setEnabled(False)
        self.labelKey25hz.setEnabled(False)

        self.radio24hz.setEnabled(False)
        self.buttonMap24hz.setEnabled(False)
        self.labelKey24hz.setEnabled(False)

        self.radioAuto.setEnabled(False)
        self.buttonMapAuto.setEnabled(False)
        self.labelKeyAuto.setEnabled(False)

        self.radioInfo.setEnabled(False)
        self.buttonMapInfo.setEnabled(False)
        self.labelKeyInfo.setEnabled(False)

        self.buttonMapKeysSave.setEnabled(False)
        self.buttonMapKeysReset.setEnabled(False)

        self.clickMapKeysReset()

    def clickRadio60hz(self):

        if self.radio60hz.isSelected():
            self.buttonMap60hz.setEnabled(True)
            self.labelKey60hz.setEnabled(True)
        else:
            self.buttonMap60hz.setEnabled(False)
            self.labelKey60hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadio50hz(self):

        if self.radio50hz.isSelected():
            self.buttonMap50hz.setEnabled(True)
            self.labelKey50hz.setEnabled(True)
        else:
            self.buttonMap50hz.setEnabled(False)
            self.labelKey50hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                            
    def clickRadio30hz(self):

        if self.radio30hz.isSelected():
            self.buttonMap30hz.setEnabled(True)
            self.labelKey30hz.setEnabled(True)
        else:
            self.buttonMap30hz.setEnabled(False)
            self.labelKey30hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadio25hz(self):

        if self.radio25hz.isSelected():
            self.buttonMap25hz.setEnabled(True)
            self.labelKey25hz.setEnabled(True)
        else:
            self.buttonMap25hz.setEnabled(False)
            self.labelKey25hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                            
    def clickRadio24hz(self):

        if self.radio24hz.isSelected():
            self.buttonMap24hz.setEnabled(True)
            self.labelKey24hz.setEnabled(True)
        else:
            self.buttonMap24hz.setEnabled(False)
            self.labelKey24hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                      
    def clickRadioAuto(self):

        if self.radioAuto.isSelected():
            self.buttonMapAuto.setEnabled(True)
            self.labelKeyAuto.setEnabled(True)
        else:
            self.buttonMapAuto.setEnabled(False)
            self.labelKeyAuto.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadioInfo(self):

        if self.radioInfo.isSelected():
            self.buttonMapInfo.setEnabled(True)
            self.labelKeyInfo.setEnabled(True)
        else:
            self.buttonMapInfo.setEnabled(False)
            self.labelKeyInfo.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickButtonMap60hz(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKey60hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '60hz')

    def clickButtonMap50hz(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKey50hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '50hz')

    def clickButtonMap30hz(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKey30hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '30hz')

    def clickButtonMap25hz(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKey25hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '25hz')

    def clickButtonMap24hz(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKey24hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '24hz')

    def clickButtonMapAuto(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKeyAuto.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, 'Auto')

    def clickButtonMapInfo(self):

        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()

        if keyPressed is not None:
            self.labelKeyInfo.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, 'Info')

    def removeDupeKey(self, keyPressed, mappedAction):

        if (self.labelKey60hz.getLabel() == keyPressed) and (mappedAction != '60hz'):
            self.labelKey60hz.setLabel('')

        if (self.labelKey50hz.getLabel() == keyPressed) and (mappedAction != '50hz'):
            self.labelKey50hz.setLabel('')

        if (self.labelKey30hz.getLabel() == keyPressed) and (mappedAction != '30hz'):
            self.labelKey30hz.setLabel('')

        if (self.labelKey25hz.getLabel() == keyPressed) and (mappedAction != '25hz'):
            self.labelKey25hz.setLabel('')

        if (self.labelKey24hz.getLabel() == keyPressed) and (mappedAction != '24hz'):
            self.labelKey24hz.setLabel('')

        if (self.labelKeyAuto.getLabel() == keyPressed) and (mappedAction != 'Auto'):
            self.labelKeyAuto.setLabel('')

        if (self.labelKeyInfo.getLabel() == keyPressed) and (mappedAction != 'Info'):
            self.labelKeyInfo.setLabel('')

    def clickMapKeysSave(self):

        self.labelInfoTitle.setLabel('Keys activating...')
        self.labelInfoText.setLabel('Saving settings...')
        xbmc.sleep(600)

        actionRes = self.currentRes

        keyMappings = []

        if self.radio60hz.isSelected():
            if self.labelKey60hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey60hz.getLabel(), actionRes + '-60hz'))
                self.labelStatus60hz.setLabel('Active')

        if self.radio50hz.isSelected():
            if self.labelKey50hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey50hz.getLabel(), actionRes + '-50hz'))
                self.labelStatus50hz.setLabel('Active')

        if self.radio30hz.isSelected():
            if self.labelKey30hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey30hz.getLabel(), actionRes + '-30hz'))
                self.labelStatus30hz.setLabel('Active')

        if self.radio25hz.isSelected():
            if self.labelKey25hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey25hz.getLabel(), actionRes + '-25hz'))
                self.labelStatus25hz.setLabel('Active')

        if self.radio24hz.isSelected() and (actionRes == '1080p'):
            if self.labelKey24hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey24hz.getLabel(), actionRes + '-24hz'))
                self.labelStatus24hz.setLabel('Active')

        if self.radioAuto.isSelected():
            if self.labelKeyAuto.getLabel() != '':
                keyMappings.insert(0, (self.labelKeyAuto.getLabel(), 'auto'))
                self.labelStatusAuto.setLabel('Active')

        if self.radioInfo.isSelected():
            if self.labelKeyInfo.getLabel() != '':
                keyMappings.insert(0, (self.labelKeyInfo.getLabel(), 'info'))
                self.labelStatusInfo.setLabel('Active')

        keyScope = 'global'

        if not keyMappings:
            mapKeyStatus = "No active keys defined" 
        else:
            mapKeyStatus = fsutil.mapKey(keyScope, keyMappings)
            self.buttonMapKeysReset.setEnabled(True)

        self.labelInfoTitle.setLabel(mapKeyStatus)
        xbmc.sleep(600)

        self.saveAllSettings()

    def clickMapKeysReset(self):

        if not fsutil.mapKeyActive():
            self.labelInfoTitle.setLabel('')
            self.labelInfoText.setLabel('')            
        else:
            self.labelInfoTitle.setLabel('Keys deactivating...')
            self.labelInfoText.setLabel('')
            xbmc.sleep(600)

            self.labelStatus60hz.setLabel('')
            self.labelStatus50hz.setLabel('')
            self.labelStatus30hz.setLabel('')
            self.labelStatus25hz.setLabel('')
            self.labelStatus24hz.setLabel('')
            self.labelStatusAuto.setLabel('')
            self.labelStatusInfo.setLabel('')

            mapKeyResetStatus = fsutil.mapKeyReset()

            self.labelInfoTitle.setLabel(mapKeyResetStatus)
            xbmc.sleep(600)

            self.saveStatusSettings()

            self.buttonMapKeysReset.setEnabled(False)

    def checkKeyMap(self):

        # check whether keymap has been deleted or renamed by another add-on (e.g Keymap Editor)
        if not fsutil.mapKeyActive():

            # reload key maps
            xbmc.executebuiltin('action(reloadkeymaps)')

            fsconfig.status60hz = ''
            fsconfig.status50hz = ''
            fsconfig.status30hz = ''
            fsconfig.status25hz = ''
            fsconfig.status24hz = ''
            fsconfig.statusAuto = ''
            fsconfig.statusInfo = ''
            fsconfig.keymapRes = ''

            saveSettingsStatus = fsconfigutil.saveSettings()

            self.buttonMapKeysReset.setEnabled(False)

    def saveStatusSettings(self):

        fsconfig.status60hz = self.labelStatus60hz.getLabel()
        fsconfig.status50hz = self.labelStatus50hz.getLabel()
        fsconfig.status30hz = self.labelStatus30hz.getLabel()
        fsconfig.status25hz = self.labelStatus25hz.getLabel()
        fsconfig.status24hz = self.labelStatus24hz.getLabel()
        fsconfig.statusAuto = self.labelStatusAuto.getLabel()
        fsconfig.statusInfo = self.labelStatusInfo.getLabel()
        fsconfig.keymapRes = ''

        saveSettingsStatus = fsconfigutil.saveSettings()

    def saveAllSettings(self):

        fsconfig.radio60hz = self.radio60hz.isSelected()
        fsconfig.radio50hz = self.radio50hz.isSelected()
        fsconfig.radio30hz = self.radio30hz.isSelected()
        fsconfig.radio25hz = self.radio25hz.isSelected()
        fsconfig.radio24hz = self.radio24hz.isSelected()
        fsconfig.radioAuto = self.radioAuto.isSelected()
        fsconfig.radioInfo = self.radioInfo.isSelected()
        fsconfig.key60hz = self.labelKey60hz.getLabel()
        fsconfig.key50hz = self.labelKey50hz.getLabel()
        fsconfig.key30hz = self.labelKey30hz.getLabel()
        fsconfig.key25hz = self.labelKey25hz.getLabel()
        fsconfig.key24hz = self.labelKey24hz.getLabel()
        fsconfig.keyAuto = self.labelKeyAuto.getLabel()
        fsconfig.keyInfo = self.labelKeyInfo.getLabel()
        fsconfig.status60hz = self.labelStatus60hz.getLabel()
        fsconfig.status50hz = self.labelStatus50hz.getLabel()
        fsconfig.status30hz = self.labelStatus30hz.getLabel()
        fsconfig.status25hz = self.labelStatus25hz.getLabel()
        fsconfig.status24hz = self.labelStatus24hz.getLabel()
        fsconfig.statusAuto = self.labelStatusAuto.getLabel()
        fsconfig.statusInfo = self.labelStatusInfo.getLabel()
        fsconfig.keymapRes = self.currentRes

        saveSettingsStatus = fsconfigutil.saveSettings()

        self.labelInfoText.setLabel(saveSettingsStatus)

class ConfigWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(ConfigWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 26)

        # create, place, then set objects
        self.radio60hz = RadioButton('60 hz')
        self.placeControl(self.radio60hz, 1, 2, columnspan=6)
        self.radio60hz.setSelected(fsconfig.radioAuto60hz)

        self.radio50hz = RadioButton('50 hz')
        self.placeControl(self.radio50hz, 2, 2, columnspan=6)
        self.radio50hz.setSelected(fsconfig.radioAuto50hz)

        self.radio30hz = RadioButton('30 hz')
        self.placeControl(self.radio30hz, 3, 2, columnspan=6)
        self.radio30hz.setSelected(fsconfig.radioAuto30hz)

        self.radio25hz = RadioButton('25 hz')
        self.placeControl(self.radio25hz, 4, 2, columnspan=6)
        self.radio25hz.setSelected(fsconfig.radioAuto25hz)

        self.radio24hz = RadioButton('24 hz')
        self.placeControl(self.radio24hz, 5, 2, columnspan=6)
        self.radio24hz.setSelected(fsconfig.radioAuto24hz)

        self.edit60hzFps1 = Edit('')
        self.placeControl(self.edit60hzFps1, 1, 9, columnspan=3, pad_y=11)
        self.edit60hzFps1.setText(fsconfig.edit60hzFps1)

        self.edit60hzFps2 = Edit('')
        self.placeControl(self.edit60hzFps2, 1, 13, columnspan=3, pad_y=11)
        self.edit60hzFps2.setText(fsconfig.edit60hzFps2)

        self.edit60hzFps3 = Edit('')
        self.placeControl(self.edit60hzFps3, 1, 17, columnspan=3, pad_y=11)
        self.edit60hzFps3.setText(fsconfig.edit60hzFps3)

        self.edit60hzFps4 = Edit('')
        self.placeControl(self.edit60hzFps4, 1, 21, columnspan=3, pad_y=11)
        self.edit60hzFps4.setText(fsconfig.edit60hzFps4)

        self.edit50hzFps1 = Edit('')
        self.placeControl(self.edit50hzFps1, 2, 9, columnspan=3, pad_y=11)
        self.edit50hzFps1.setText(fsconfig.edit50hzFps1)

        self.edit50hzFps2 = Edit('')
        self.placeControl(self.edit50hzFps2, 2, 13, columnspan=3, pad_y=11)
        self.edit50hzFps2.setText(fsconfig.edit50hzFps2)

        self.edit50hzFps3 = Edit('')
        self.placeControl(self.edit50hzFps3, 2, 17, columnspan=3, pad_y=11)
        self.edit50hzFps3.setText(fsconfig.edit50hzFps3)

        self.edit50hzFps4 = Edit('')
        self.placeControl(self.edit50hzFps4, 2, 21, columnspan=3, pad_y=11)
        self.edit50hzFps4.setText(fsconfig.edit50hzFps4)

        self.edit30hzFps1 = Edit('')
        self.placeControl(self.edit30hzFps1, 3, 9, columnspan=3, pad_y=11)
        self.edit30hzFps1.setText(fsconfig.edit30hzFps1)

        self.edit30hzFps2 = Edit('')
        self.placeControl(self.edit30hzFps2, 3, 13, columnspan=3, pad_y=11)
        self.edit30hzFps2.setText(fsconfig.edit30hzFps2)

        self.edit30hzFps3 = Edit('')
        self.placeControl(self.edit30hzFps3, 3, 17, columnspan=3, pad_y=11)
        self.edit30hzFps3.setText(fsconfig.edit30hzFps3)

        self.edit30hzFps4 = Edit('')
        self.placeControl(self.edit30hzFps4, 3, 21, columnspan=3, pad_y=11)
        self.edit30hzFps4.setText(fsconfig.edit30hzFps4)

        self.edit25hzFps1 = Edit('')
        self.placeControl(self.edit25hzFps1, 4, 9, columnspan=3, pad_y=11)
        self.edit25hzFps1.setText(fsconfig.edit25hzFps1)

        self.edit25hzFps2 = Edit('')
        self.placeControl(self.edit25hzFps2, 4, 13, columnspan=3, pad_y=11)
        self.edit25hzFps2.setText(fsconfig.edit25hzFps2)

        self.edit25hzFps3 = Edit('')
        self.placeControl(self.edit25hzFps3, 4, 17, columnspan=3, pad_y=11)
        self.edit25hzFps3.setText(fsconfig.edit25hzFps3)

        self.edit25hzFps4 = Edit('')
        self.placeControl(self.edit25hzFps4, 4, 21, columnspan=3, pad_y=11)
        self.edit25hzFps4.setText(fsconfig.edit25hzFps4)

        self.edit24hzFps1 = Edit('')
        self.placeControl(self.edit24hzFps1, 5, 9, columnspan=3, pad_y=11)
        self.edit24hzFps1.setText(fsconfig.edit24hzFps1)

        self.edit24hzFps2 = Edit('')
        self.placeControl(self.edit24hzFps2, 5, 13, columnspan=3, pad_y=11)
        self.edit24hzFps2.setText(fsconfig.edit24hzFps2)

        self.edit24hzFps3 = Edit('')
        self.placeControl(self.edit24hzFps3, 5, 17, columnspan=3, pad_y=11)
        self.edit24hzFps3.setText(fsconfig.edit24hzFps3)

        self.edit24hzFps4 = Edit('')
        self.placeControl(self.edit24hzFps4, 5, 21, columnspan=3, pad_y=11)
        self.edit24hzFps4.setText(fsconfig.edit24hzFps4)

        self.buttonConfigSave = Button('Save Configuration')
        self.placeControl(self.buttonConfigSave, 9, 2, columnspan=8)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 9, 12, columnspan=16, pad_y=11)

        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 10, 12, columnspan=16, pad_y=11)

        # connect buttons and actions to functions
        self.connect(self.radio60hz, self.clickRadio60hz)
        self.connect(self.radio50hz, self.clickRadio50hz)
        self.connect(self.radio30hz, self.clickRadio30hz)
        self.connect(self.radio25hz, self.clickRadio25hz)
        self.connect(self.radio24hz, self.clickRadio24hz)
        self.connect(self.buttonConfigSave, self.clickConfigSave)
        self.connect(ACTION_NAV_BACK, self.close)

        # set the enabled state of objects
        self.clickRadio60hz()
        self.clickRadio50hz()
        self.clickRadio30hz()
        self.clickRadio25hz()
        self.clickRadio24hz()

        # define key navigation (up-down)
        self.radio60hz.controlDown(self.radio50hz)
        self.radio50hz.controlUp(self.radio60hz)
        self.radio50hz.controlDown(self.radio30hz)
        self.radio30hz.controlUp(self.radio50hz)
        self.radio30hz.controlDown(self.radio25hz)
        self.radio25hz.controlUp(self.radio30hz)
        self.radio25hz.controlDown(self.radio24hz)
        self.radio24hz.controlUp(self.radio25hz)
        self.radio24hz.controlDown(self.buttonConfigSave)
        self.buttonConfigSave.controlUp(self.radio24hz)

        self.edit60hzFps1.controlDown(self.edit50hzFps1)
        self.edit50hzFps1.controlUp(self.edit60hzFps1)
        self.edit50hzFps1.controlDown(self.edit30hzFps1)
        self.edit30hzFps1.controlUp(self.edit50hzFps1)
        self.edit30hzFps1.controlDown(self.edit25hzFps1)
        self.edit25hzFps1.controlUp(self.edit30hzFps1)
        self.edit25hzFps1.controlDown(self.edit24hzFps1)
        self.edit24hzFps1.controlUp(self.edit25hzFps1)
        self.edit24hzFps1.controlDown(self.buttonConfigSave)

        self.edit60hzFps2.controlDown(self.edit50hzFps2)
        self.edit50hzFps2.controlUp(self.edit60hzFps2)
        self.edit50hzFps2.controlDown(self.edit30hzFps2)
        self.edit30hzFps2.controlUp(self.edit50hzFps2)
        self.edit30hzFps2.controlDown(self.edit25hzFps2)
        self.edit25hzFps2.controlUp(self.edit30hzFps2)
        self.edit25hzFps2.controlDown(self.edit24hzFps2)
        self.edit24hzFps2.controlUp(self.edit25hzFps2)
        self.edit24hzFps2.controlDown(self.buttonConfigSave)

        self.edit60hzFps3.controlDown(self.edit50hzFps3)
        self.edit50hzFps3.controlUp(self.edit60hzFps3)
        self.edit50hzFps3.controlDown(self.edit30hzFps3)
        self.edit30hzFps3.controlUp(self.edit50hzFps3)
        self.edit30hzFps3.controlDown(self.edit25hzFps3)
        self.edit25hzFps3.controlUp(self.edit30hzFps3)
        self.edit25hzFps3.controlDown(self.edit24hzFps3)
        self.edit24hzFps3.controlUp(self.edit25hzFps3)
        self.edit24hzFps3.controlDown(self.buttonConfigSave)

        self.edit60hzFps4.controlDown(self.edit50hzFps4)
        self.edit50hzFps4.controlUp(self.edit60hzFps4)
        self.edit50hzFps4.controlDown(self.edit30hzFps4)
        self.edit30hzFps4.controlUp(self.edit50hzFps4)
        self.edit30hzFps4.controlDown(self.edit25hzFps4)
        self.edit25hzFps4.controlUp(self.edit30hzFps4)
        self.edit25hzFps4.controlDown(self.edit24hzFps4)
        self.edit24hzFps4.controlUp(self.edit25hzFps4)
        self.edit24hzFps4.controlDown(self.buttonConfigSave)

        # define key navigation (left-right)
        self.radio60hz.controlRight(self.edit60hzFps1)
        self.edit60hzFps1.controlLeft(self.radio60hz)
        self.edit60hzFps1.controlRight(self.edit60hzFps2)
        self.edit60hzFps2.controlLeft(self.edit60hzFps1)
        self.edit60hzFps2.controlRight(self.edit60hzFps3)
        self.edit60hzFps3.controlLeft(self.edit60hzFps2)
        self.edit60hzFps3.controlRight(self.edit60hzFps4)
        self.edit60hzFps4.controlLeft(self.edit60hzFps3)

        self.radio50hz.controlRight(self.edit50hzFps1)
        self.edit50hzFps1.controlLeft(self.radio50hz)
        self.edit50hzFps1.controlRight(self.edit50hzFps2)
        self.edit50hzFps2.controlLeft(self.edit50hzFps1)
        self.edit50hzFps2.controlRight(self.edit50hzFps3)
        self.edit50hzFps3.controlLeft(self.edit50hzFps2)
        self.edit50hzFps3.controlRight(self.edit50hzFps4)
        self.edit50hzFps4.controlLeft(self.edit50hzFps3)

        self.radio30hz.controlRight(self.edit30hzFps1)
        self.edit30hzFps1.controlLeft(self.radio30hz)
        self.edit30hzFps1.controlRight(self.edit30hzFps2)
        self.edit30hzFps2.controlLeft(self.edit30hzFps1)
        self.edit30hzFps2.controlRight(self.edit30hzFps3)
        self.edit30hzFps3.controlLeft(self.edit30hzFps2)
        self.edit30hzFps3.controlRight(self.edit30hzFps4)
        self.edit30hzFps4.controlLeft(self.edit30hzFps3)

        self.radio25hz.controlRight(self.edit25hzFps1)
        self.edit25hzFps1.controlLeft(self.radio25hz)
        self.edit25hzFps1.controlRight(self.edit25hzFps2)
        self.edit25hzFps2.controlLeft(self.edit25hzFps1)
        self.edit25hzFps2.controlRight(self.edit25hzFps3)
        self.edit25hzFps3.controlLeft(self.edit25hzFps2)
        self.edit25hzFps3.controlRight(self.edit25hzFps4)
        self.edit25hzFps4.controlLeft(self.edit25hzFps3)

        self.radio24hz.controlRight(self.edit24hzFps1)
        self.edit24hzFps1.controlLeft(self.radio24hz)
        self.edit24hzFps1.controlRight(self.edit24hzFps2)
        self.edit24hzFps2.controlLeft(self.edit24hzFps1)
        self.edit24hzFps2.controlRight(self.edit24hzFps3)
        self.edit24hzFps3.controlLeft(self.edit24hzFps2)
        self.edit24hzFps3.controlRight(self.edit24hzFps4)
        self.edit24hzFps4.controlLeft(self.edit24hzFps3)

        # set initial focus
        self.setFocus(self.radio60hz)

    def clickRadio60hz(self):

        if self.radio60hz.isSelected():
            self.edit60hzFps1.setEnabled(True)
            self.edit60hzFps2.setEnabled(True)
            self.edit60hzFps3.setEnabled(True)
            self.edit60hzFps4.setEnabled(True)
        else:
            self.edit60hzFps1.setEnabled(False)
            self.edit60hzFps2.setEnabled(False)
            self.edit60hzFps3.setEnabled(False)
            self.edit60hzFps4.setEnabled(False)

    def clickRadio50hz(self):

        if self.radio50hz.isSelected():
            self.edit50hzFps1.setEnabled(True)
            self.edit50hzFps2.setEnabled(True)
            self.edit50hzFps3.setEnabled(True)
            self.edit50hzFps4.setEnabled(True)
        else:
            self.edit50hzFps1.setEnabled(False)
            self.edit50hzFps2.setEnabled(False)
            self.edit50hzFps3.setEnabled(False)
            self.edit50hzFps4.setEnabled(False)

    def clickRadio30hz(self):

        if self.radio30hz.isSelected():
            self.edit30hzFps1.setEnabled(True)
            self.edit30hzFps2.setEnabled(True)
            self.edit30hzFps3.setEnabled(True)
            self.edit30hzFps4.setEnabled(True)
        else:
            self.edit30hzFps1.setEnabled(False)
            self.edit30hzFps2.setEnabled(False)
            self.edit30hzFps3.setEnabled(False)
            self.edit30hzFps4.setEnabled(False)

    def clickRadio25hz(self):

        if self.radio25hz.isSelected():
            self.edit25hzFps1.setEnabled(True)
            self.edit25hzFps2.setEnabled(True)
            self.edit25hzFps3.setEnabled(True)
            self.edit25hzFps4.setEnabled(True)
        else:
            self.edit25hzFps1.setEnabled(False)
            self.edit25hzFps2.setEnabled(False)
            self.edit25hzFps3.setEnabled(False)
            self.edit25hzFps4.setEnabled(False)


    def clickRadio24hz(self):

        if self.radio24hz.isSelected():
            self.edit24hzFps1.setEnabled(True)
            self.edit24hzFps2.setEnabled(True)
            self.edit24hzFps3.setEnabled(True)
            self.edit24hzFps4.setEnabled(True)
        else:
            self.edit24hzFps1.setEnabled(False)
            self.edit24hzFps2.setEnabled(False)
            self.edit24hzFps3.setEnabled(False)
            self.edit24hzFps4.setEnabled(False)

    def clickConfigSave(self):

        self.labelInfoTitle.setLabel('Verifying settings...')
        self.labelInfoText.setLabel('')
        xbmc.sleep(600)

        fpsEditList = [self.edit60hzFps1,
                       self.edit60hzFps2,
                       self.edit60hzFps3,
                       self.edit60hzFps4,
                       self.edit50hzFps1,
                       self.edit50hzFps2,
                       self.edit50hzFps3,
                       self.edit50hzFps4,
                       self.edit30hzFps1,
                       self.edit30hzFps2,
                       self.edit30hzFps3,
                       self.edit30hzFps4,
                       self.edit25hzFps1,
                       self.edit25hzFps2,
                       self.edit25hzFps3,
                       self.edit25hzFps4,
                       self.edit24hzFps1,
                       self.edit24hzFps2,
                       self.edit24hzFps3,
                       self.edit24hzFps4]

        self.fpsList = []       # FPS list for duplicate checking

        fpsIsValid = True
        for (fpsEditItem) in fpsEditList:
            if fpsIsValid:
                fpsIsValid, fpsMsg = self.verifyFPS(fpsEditItem)

        if not fpsIsValid:
            self.labelInfoTitle.setLabel(fpsMsg)
            self.labelInfoText.setLabel('Settings not saved')
        else:
            self.labelInfoTitle.setLabel('Settings verified')
            self.labelInfoText.setLabel('Saving settings...')
            xbmc.sleep(600)

            self.saveFpsSettings()

    def verifyFPS(self, editFps):

        currentFps = editFps.getText()

        if currentFps == '':
            fpsIsValid = True
            fpsMsg = ''

        else:
            # check that edit field contains a number
            try:
                numCurrentFps = float(currentFps)
            # not a valid number - set field text to red
            except ValueError:
                fpsIsValid = False
                fpsMsg = 'Invalid FPS: ' + currentFps

            # is a valid number
            else:    

                # number is outside reasonable FPS range (1-70)
                if (numCurrentFps < 1) or (numCurrentFps > 70):
                    fpsIsValid = False
                    fpsMsg = 'Invalid FPS: ' + currentFps

                # number is within reasonable FPS range (1-70)
                else:

                    # truncate FPS to three decimal places
                    decSplit = currentFps.find('.') + 4
                    newFps = currentFps[0:decSplit]

                    # check fpsList for duplicates
                    dupeFpsFound = False
                    for (fpsItem) in self.fpsList:
                        if fpsItem == newFps:
                            dupeFpsFound = True
                            break

                    # duplicate FPS detected
                    if dupeFpsFound:
                        fpsIsValid = False
                        fpsMsg = 'Duplicate FPS: ' + currentFps

                    # no duplicate FPS detected
                    else:
                        fpsIsValid = True

                        if currentFps == newFps:
                            fpsMsg = 'OK - FPS verified.'
                        else:
                            editFps.setText(newFps)
                            fpsMsg = 'OK - FPS truncated: ' + currentFps

                        # add FPS to list for dupe checking
                        self.fpsList.insert(0, currentFps)

        return fpsIsValid, fpsMsg

    def saveFpsSettings(self):

        fsconfig.edit60hzFps1 = self.edit60hzFps1.getText() 
        fsconfig.edit60hzFps2 = self.edit60hzFps2.getText() 
        fsconfig.edit60hzFps3 = self.edit60hzFps3.getText() 
        fsconfig.edit60hzFps4 = self.edit60hzFps4.getText() 
        fsconfig.edit50hzFps1 = self.edit50hzFps1.getText() 
        fsconfig.edit50hzFps2 = self.edit50hzFps2.getText() 
        fsconfig.edit50hzFps3 = self.edit50hzFps3.getText() 
        fsconfig.edit50hzFps4 = self.edit50hzFps4.getText() 
        fsconfig.edit30hzFps1 = self.edit30hzFps1.getText() 
        fsconfig.edit30hzFps2 = self.edit30hzFps2.getText() 
        fsconfig.edit30hzFps3 = self.edit30hzFps3.getText() 
        fsconfig.edit30hzFps4 = self.edit30hzFps4.getText() 
        fsconfig.edit25hzFps1 = self.edit25hzFps1.getText() 
        fsconfig.edit25hzFps2 = self.edit25hzFps2.getText() 
        fsconfig.edit25hzFps3 = self.edit25hzFps3.getText() 
        fsconfig.edit25hzFps4 = self.edit25hzFps4.getText() 
        fsconfig.edit24hzFps1 = self.edit24hzFps1.getText() 
        fsconfig.edit24hzFps2 = self.edit24hzFps2.getText() 
        fsconfig.edit24hzFps3 = self.edit24hzFps3.getText() 
        fsconfig.edit24hzFps4 = self.edit24hzFps4.getText() 

        fsconfig.radioAuto60hz = self.radio60hz.isSelected()
        fsconfig.radioAuto50hz = self.radio50hz.isSelected()
        fsconfig.radioAuto30hz = self.radio30hz.isSelected()
        fsconfig.radioAuto25hz = self.radio25hz.isSelected()
        fsconfig.radioAuto24hz = self.radio24hz.isSelected()

        saveSettingsStatus = fsconfigutil.saveSettings()

        self.labelInfoText.setLabel(saveSettingsStatus)

class MapEventsWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MapEventsWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 26)

        # create, place, then set objects
        self.labelCurrentRes = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCurrentRes, 1, 2, columnspan=20, pad_y=11)    

        self.labelActiveService = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelActiveService, 2, 2, columnspan=20, pad_y=11)    

        self.radioOnPlayStart = RadioButton('Playback Starts')
        self.placeControl(self.radioOnPlayStart, 4, 2, columnspan=8)
        self.radioOnPlayStart.setSelected(fsconfig.radioOnPlayStart)

        self.labelOnPlayStart = Label('Auto-set HDMI mode on playback start', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStart, 4, 11, columnspan=14, pad_y=11)    

        self.radioOnPlayStop60 = RadioButton('Default 60 hz')
        self.placeControl(self.radioOnPlayStop60, 5, 2, columnspan=8)
        self.radioOnPlayStop60.setSelected(fsconfig.radioOnPlayStop60)

        self.labelOnPlayStop60 = Label('Set mode to 60 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop60, 5, 11, columnspan=14, pad_y=11)    

        self.radioOnPlayStop50 = RadioButton('Default 50 hz')
        self.placeControl(self.radioOnPlayStop50, 6, 2, columnspan=8)
        self.radioOnPlayStop50.setSelected(fsconfig.radioOnPlayStop50)

        self.labelOnPlayStop50 = Label('Set mode to 50 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop50, 6, 11, columnspan=14, pad_y=11)    

        self.radioNotifyOn = RadioButton('')
        self.placeControl(self.radioNotifyOn, 8, 2, columnspan=8)
        self.radioNotifyOn.setSelected(fsconfig.radioNotifyOn)

        self.buttonConfigSave = Button('Save Configuration')
        self.placeControl(self.buttonConfigSave, 10, 2, columnspan=8)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 10, 12, columnspan=16, pad_y=11)

#         self.labelInfoText = Label('', alignment=ALIGN_LEFT)
#         self.placeControl(self.labelInfoText, 11, 12, columnspan=16, pad_y=11)

        # check current display mode setting
        currentOutputMode, currentAmlogicMode = fsutil.getDisplayMode()

        if currentOutputMode == 'unsupported':
            self.labelCurrentRes.setLabel('Unsupported resolution: ' + currentAmlogicMode)           
            self.disableAll()

        elif currentOutputMode == 'invalid':
            self.labelCurrentRes.setLabel('Error: ' + currentAmlogicMode)       
            self.disableAll()

        else:
            # get current resolution
            resSplit = currentOutputMode.find('-')
            self.currentRes = currentOutputMode[0:resSplit]
            self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes)       

        # connect buttons and actions to functions
        self.connect(self.radioOnPlayStart, self.clickRadioOnPlayStart)
        self.connect(self.radioOnPlayStop60, self.clickRadioOnPlayStop60)
        self.connect(self.radioOnPlayStop50, self.clickRadioOnPlayStop50)
        self.connect(self.radioNotifyOn, self.clickRadioNotifyOn)
        self.connect(self.buttonConfigSave, self.clickConfigSave)
        self.connect(ACTION_NAV_BACK, self.close)

        # set the enabled state of objects
        self.checkIfActive()
        self.clickRadioOnPlayStop60()
        self.clickRadioOnPlayStop50()
        self.clickRadioNotifyOn()
        self.clickRadioOnPlayStart()

        # define key navigation (up-down)
        self.radioOnPlayStart.controlDown(self.radioOnPlayStop60)
        self.radioOnPlayStop60.controlUp(self.radioOnPlayStart)

        self.radioOnPlayStop60.controlDown(self.radioOnPlayStop50)
        self.radioOnPlayStop50.controlUp(self.radioOnPlayStop60)

        self.radioOnPlayStop50.controlDown(self.radioNotifyOn)
        self.radioNotifyOn.controlUp(self.radioOnPlayStop50)

        self.radioNotifyOn.controlDown(self.buttonConfigSave)
        self.buttonConfigSave.controlUp(self.radioNotifyOn)

        # set initial focus
        self.setFocus(self.radioOnPlayStart)

    def clickRadioOnPlayStart(self):
        if self.radioOnPlayStart.isSelected():
            self.labelOnPlayStart.setEnabled(True)
            self.radioOnPlayStop60.setEnabled(True)
            self.radioOnPlayStop50.setEnabled(True)
            self.clickRadioOnPlayStop60()
            self.clickRadioOnPlayStop50()
            self.radioNotifyOn.setEnabled(True)
        else:
            self.labelOnPlayStart.setEnabled(False)
            self.radioOnPlayStop60.setEnabled(False)
            self.radioOnPlayStop50.setEnabled(False)
            self.labelOnPlayStop60.setEnabled(False)
            self.labelOnPlayStop50.setEnabled(False)
            self.radioNotifyOn.setEnabled(False)

        self.checkIfActive()
            
    def clickRadioOnPlayStop60(self):
        if self.radioOnPlayStop60.isSelected():
            self.labelOnPlayStop60.setEnabled(True)
            self.radioOnPlayStop50.setSelected(False)
            self.labelOnPlayStop50.setEnabled(False)
        else:
            self.labelOnPlayStop60.setEnabled(False)

        self.checkIfActive()

    def clickRadioOnPlayStop50(self):
        if self.radioOnPlayStop50.isSelected():
            self.labelOnPlayStop50.setEnabled(True)
            self.radioOnPlayStop60.setSelected(False)
            self.labelOnPlayStop60.setEnabled(False)
        else:
            self.labelOnPlayStop50.setEnabled(False)

        self.checkIfActive()

    def checkIfActive(self):
        
        fsconfigutil.loadActiveServiceSetting()

        if fsconfig.activeService:
            if fsconfig.radioOnPlayStart:
                self.labelActiveService.setLabel('Service running')
            else:
                self.labelActiveService.setLabel('Service running - restart XBMC')

        else:
            if fsconfig.radioOnPlayStart:
                self.labelActiveService.setLabel('Service stopped - restart XBMC')
            else:
                self.labelActiveService.setLabel('Service stopped')

    def clickRadioNotifyOn(self):
        if self.radioNotifyOn.isSelected():
            self.radioNotifyOn.setLabel('Notifications On')
        else:
            self.radioNotifyOn.setLabel('Notifications Off')

        self.checkIfActive()

    def clickConfigSave(self):
        self.labelInfoTitle.setLabel('Saving settings...')
        xbmc.sleep(600)

        fsconfig.radioOnPlayStart = self.radioOnPlayStart.isSelected()
        fsconfig.radioOnPlayStop60 = self.radioOnPlayStop60.isSelected()
        fsconfig.radioOnPlayStop50 = self.radioOnPlayStop50.isSelected()
        fsconfig.radioNotifyOn = self.radioNotifyOn.isSelected()

        saveSettingsStatus = fsconfigutil.saveSettings()

        if not fsconfig.radioOnPlayStart:
            xbmc.sleep(4500)            

        self.labelInfoTitle.setLabel(saveSettingsStatus)

        self.checkIfActive()

    def disableAll(self):

        self.labelInfoTitle.setEnabled(False)
        self.labelActiveService.setEnabled(False)

        self.radioOnPlayStart.setEnabled(False)
        self.radioOnPlayStop60.setEnabled(False)
        self.radioOnPlayStop50.setEnabled(False)
        self.radioNotifyOn.setEnabled(False)
        self.buttonConfigSave.setEnabled(False)

        self.disableService()

    def disableService(self):

        self.radioOnPlayStart.setSelected(False)

        self.clickRadioOnPlayStart()

        self.clickConfigSave()

class MainWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MainWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 13)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 1, 1, columnspan=8)

        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 2, 1, columnspan=8)

        # create and place objects
        self.buttonWindowMapEvents = Button('Service')
        self.placeControl(self.buttonWindowMapEvents, 4, 1, columnspan=5)

        self.buttonWindowConfig = Button('Frame Rates')
        self.placeControl(self.buttonWindowConfig, 5, 1, columnspan=5)

        self.buttonWindowMapKeys = Button('Map Keys')
        self.placeControl(self.buttonWindowMapKeys, 6, 1, columnspan=5)

        self.buttonCleanup = Button('Clean Up')
        self.placeControl(self.buttonCleanup, 8, 1, columnspan=5)

        self.labelInfoStatus1 = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoStatus1, 4, 7, columnspan=8, pad_y=11)

        self.labelInfoStatus2 = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoStatus2, 6, 7, columnspan=8, pad_y=11)

        self.labelCleanupStatus = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCleanupStatus, 8, 7, columnspan=8, pad_y=11)
        # check platform type
        self.checkPlatformType()       
        self.checkDisplayModeFileStatus()
        self.checkStatus()

        # connect buttons and actions to functions
        self.connect(self.buttonWindowMapEvents, self.windowMapEvents)
        self.connect(self.buttonWindowConfig, self.windowConfig)
        self.connect(self.buttonWindowMapKeys, self.windowMapKeys)
        self.connect(self.buttonCleanup, self.cleanup)
        self.connect(ACTION_NAV_BACK, self.close)

        # define key navigation
        self.buttonWindowMapEvents.controlDown(self.buttonWindowConfig)
        self.buttonWindowConfig.controlUp(self.buttonWindowMapEvents)

        self.buttonWindowConfig.controlDown(self.buttonWindowMapKeys)
        self.buttonWindowMapKeys.controlUp(self.buttonWindowConfig)

        self.buttonWindowMapKeys.controlDown(self.buttonCleanup)
        self.buttonCleanup.controlUp(self.buttonWindowMapKeys)

        # set initial focus
        self.setFocus(self.buttonWindowMapEvents)

    def windowConfig(self):

        # create and show the Auto Sync configuration window
        fsConfigWindow = ConfigWindow('Refresh rate to frame rate synchronization')
        self.close()
        fsConfigWindow.doModal()
        self.doModal()

    def windowMapEvents(self):

        # create and show the Map Events configuration window
        fsMapEventsWindow = MapEventsWindow('Service configuration')
        self.close()

        fsMapEventsWindow.doModal()

        self.checkStatus()
        self.doModal()

    def windowMapKeys(self):

        # create and show the Map Keys configuration window
        fsMapKeysWindow = MapKeysWindow('Map keys')
        self.close()

        fsMapKeysWindow.doModal() 

        self.checkStatus()
        self.doModal()

    def checkPlatformType(self):

        self.labelInfoTitle.setLabel('Detecting platform...')
        xbmc.sleep(200)

        osPlatform, osVariant = fsutil.getPlatformType()

        if osPlatform is None:
            self.labelInfoTitle.setLabel('Failed to detect platform')
            fsconfig.osPlatform = 'unknown'
            self.disableAll()

        elif osVariant == 'Windows 7':
            self.labelInfoTitle.setLabel(osVariant + ' (testing only)')
            fsconfig.osPlatform = osVariant

        else:
            self.labelInfoTitle.setLabel(osVariant)
            fsconfig.osPlatform = osVariant

        fsconfigutil.saveSettings()

    def checkDisplayModeFileStatus(self):

        self.labelInfoText.setLabel('Checking display mode file...')
        xbmc.sleep(200)

        modeFile, fileStatus = fsutil.getDisplayModeFileStatus()

        if fileStatus is None:
            self.labelInfoText.setLabel('HDMI mode file check failed.')

        elif fileStatus[:2] == 'OK':
            self.labelInfoText.setLabel(fileStatus[4:])

        else:
            self.labelInfoText.setLabel(fileStatus)
            self.disableAll()

    def checkStatus(self):

        self.checkIfActive()
        self.checkIfKeysMapped() 

        # check for settings folder
        golbalSettingsFolder = fsconfigutil.settingsFolder()

        if (self.labelInfoStatus1.getLabel() != 'Service stopped') or (self.labelInfoStatus2.getLabel() == 'Keys activated') or (os.path.isdir(golbalSettingsFolder)):
            self.buttonCleanup.setEnabled(True)
        else:
            self.buttonCleanup.setEnabled(False)
            self.labelCleanupStatus.setLabel('Clean up complete')  

    def checkIfActive(self):

        fsconfigutil.loadActiveServiceSetting()

        if fsconfig.activeService:
            if fsconfig.radioOnPlayStart:
                self.labelInfoStatus1.setLabel('Service running')
            else:
                self.labelInfoStatus1.setLabel('Service running - restart XBMC')

        else:
            if fsconfig.radioOnPlayStart:
                self.labelInfoStatus1.setLabel('Service stopped - restart XBMC')
            else:
                self.labelInfoStatus1.setLabel('Service stopped')

    def checkIfKeysMapped(self):

        if fsutil.mapKeyActive():
            self.labelInfoStatus2.setLabel('Keys activated')

        else:
            self.labelInfoStatus2.setLabel('Keys deactivated')

    def disableAll(self):

        self.buttonWindowConfig.setEnabled(False)
        self.buttonWindowMapEvents.setEnabled(False)
        self.buttonWindowMapKeys.setEnabled(False)

    def cleanup(self):

        self.disableAll()

        if (self.labelInfoStatus1.getLabel() != 'Service stopped'):

            self.labelInfoStatus1.setLabel('Service stopping...') 

            fsconfig.radioOnPlayStart = False

            saveSettingsStatus = fsconfigutil.saveSettings()
            xbmc.sleep(4500)            

            self.checkIfActive()

        if (self.labelInfoStatus2.getLabel() == 'Keys activated'):

            self.labelInfoStatus2.setLabel('Keys deactivating...')
            xbmc.sleep(600)

            mapKeyResetStatus = fsutil.mapKeyReset()

            self.labelInfoStatus2.setLabel(mapKeyResetStatus)
            xbmc.sleep(600)

            self.checkIfKeysMapped()

        fsconfigutil.deleteAllSettingsFiles()

        self.checkStatus()

        if (self.labelCleanupStatus.getLabel() != 'Clean up complete'):
            self.labelCleanupStatus.setLabel('Clean up incomplete')  

        self.setFocus(self.buttonCleanup)

class InfoPanel():

    @staticmethod
    def showInfo():

        # get current window
        windowID = xbmcgui.getCurrentWindowId()

        # check for a valid window (10007 = system info, 12005 = full screen video)
#         if (windowID == 12005) or (windowID == 10007):
        if (windowID == 12005):
            currentWindow = xbmcgui.Window(windowID)

            # flag info panel as active
            fsconfig.activeInfo = True
            fsconfigutil.saveActiveInfoSetting()

            # create info panel objects

            # same height as codec info
#             panelTop = 19
            # under codec info
            panelTop = 158          

            panelBorder = 10
            panelLineTop = panelTop + panelBorder
            panelLineSpacing = 23
            panelLineCount = 3

            descHdmiMode = 'Output frequency:'
            descSourceFPS = 'Source framerate:'
            descCurrentFPS = 'Current framerate:'

            imageInfoPanel = xbmcgui.ControlImage(-200, panelTop, 1920, (panelBorder * 2) + (panelLineSpacing * panelLineCount), 'DialogBack2.png', colorDiffuse='0xBBBBBBBB')

            # Output Frequency ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelHdmiModeTitle = xbmcgui.ControlLabel(50, panelLineTop, 150, 20, descHdmiMode, font='font12')
            labelHdmiMode = xbmcgui.ControlLabel(200, panelLineTop, 100, 20, '', font='font12')

            # get current display mode setting
            currentOutputMode, currentAmlogicMode = fsutil.getDisplayMode()

            # get current frequency
            freqSplit = currentOutputMode.find('-') + 1
            currentFreq = currentOutputMode[freqSplit:len(currentOutputMode)-2]

            labelHdmiMode.setLabel(currentFreq + ' hz')

            # Source FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelSourceFpsTitle = xbmcgui.ControlLabel(50, panelLineTop + (panelLineSpacing * 1), 150, 20, descSourceFPS, font='font12')
            labelSourceFps = xbmcgui.ControlLabel(200, panelLineTop + (panelLineSpacing * 1), 100, 20, '', font='font12')

            # get FPS of currently playing video
            setModeStatus, statusType = fsutil.getCurrentFPS()

            if statusType == 'ok':
                labelSourceFps.setLabel(setModeStatus)
            else:
                labelSourceFps.setLabel('')

            # Current FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelCurrentFpsTitle = xbmcgui.ControlLabel(50, panelLineTop + (panelLineSpacing * 2), 150, 20, descCurrentFPS, font='font12')
            labelCurrentFps = xbmcgui.ControlLabel(200, panelLineTop + (panelLineSpacing * 2), 100, 20, '', font='font12')

            # get current rendered FPS
            currentFPS = xbmc.getInfoLabel('System.FPS')

            labelCurrentFps.setLabel(currentFPS)

            # ------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # build list of controls
            controlList = [imageInfoPanel, labelHdmiModeTitle, labelHdmiMode, labelSourceFpsTitle, labelSourceFps, labelCurrentFpsTitle, labelCurrentFps]

#             if fsconfig.radioAuto50hz:
#                 syncConfig.extend([(fsconfig.edit50hzFps1, mode50hz), 
#                                    (fsconfig.edit50hzFps2, mode50hz), 
#                                    (fsconfig.edit50hzFps3, mode50hz), 
#                                    (fsconfig.edit50hzFps4, mode50hz)])

#             autoSync.insert(0, (syncFPS, syncMode))

            # add info panel to window
            currentWindow.addControls(controlList) 

            refreshCounter = 0

            # check for configuration changes every 0.25 second
            while fsconfig.activeInfo:

                xbmc.sleep(250)

                refreshCounter = refreshCounter + 1

                # Every half second (update panel)
                if (refreshCounter == 2) or (refreshCounter == 4):

                    # Update Current FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    currentFPS = xbmc.getInfoLabel('System.FPS')
                    labelCurrentFps.setLabel(currentFPS)

                # Every second (update panel)
                if refreshCounter == 4:

                    # Update Source FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    setModeStatus, statusType = fsutil.getCurrentFPS()
                    if statusType == 'ok':
                        labelSourceFps.setLabel(setModeStatus)
                    else:
                        labelSourceFps.setLabel('')

                    # Update Output Frequency ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    currentOutputMode, currentAmlogicMode = fsutil.getDisplayMode()
                    freqSplit = currentOutputMode.find('-') + 1
                    currentFreq = currentOutputMode[freqSplit:len(currentOutputMode)-2]
                    labelHdmiMode.setLabel(currentFreq + ' hz')

                    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------

                # Every quarter second - reload settings, to allow info panel stop
                fsconfigutil.loadActiveInfoSetting()

                 # Every second (check and update panel status)
                if refreshCounter == 4:

                    # check that user has not deactivate in last 0.25 seconds
                    if fsconfig.activeInfo:

                        # check if window is still active
                        windowIDcheck = xbmcgui.getCurrentWindowId()       

                        # if window is not activate then disable info panel
                        if windowID != windowIDcheck:
                            fsconfig.activeInfo = False

                        # rewrite flag file (necessary even when active for detection of old flag file should XBMC exit unexpectedly)
                        fsconfigutil.saveActiveInfoSetting()

                    # reset refresh counter
                    refreshCounter = 0


            # remove info from window
            currentWindow.removeControls(controlList) 

