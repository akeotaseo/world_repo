import os, glob, xbmc, xbmcgui, xbmcvfs, xbmcaddon, shutil
from updatervar import *
#from resources.lib.modules.delete_addons import del_dir
from resources.lib.GUIcontrol import txt_updater
from resources.lib.modules import db, addonsEnable
from resources.lib.modules.addonsEnable import enable_addons
#from resources.lib.modules.installer_addons import installAddon
#from resources.lib.GUIcontrol.txt_updater import get_skinshortcutsversion


#exists = os.path.exists
#skinshortcuts_version = get_skinshortcutsversion()

Database_Addons33 = [('repository.World', 'repository.World')]

addon_list = ['plugin.video.live.test', 'plugin.video.testt']


         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα ή τα αρχεία που επιθυμείς να αφαιρέσεις [  ] ###

delete_addons = ['repository.test', 'repository.testt']



def Updater_Matrix():
    BG.create('Αναμονή για ολοκλήρωση...', Dialog_U2)
    xbmc.sleep(3000)

    del_dir()
    installAddon()



    BG.update(25, 'Αναμονή για ολοκλήρωση...', 'Έλεγχος...')
    xbmc.sleep(5000)


                                        #KODI-Intro-Video.mp4
    if os.path.exists(UpdaterMatrix_path4): xbmcvfs.delete(UpdaterMatrix_path4), xbmc.sleep(1000)



    if not os.path.exists(UpdaterMatrix_path4):
        xbmc.sleep(5000)
        BG.update(52, Dialog_U1, 'KODI-Intro-Video.mp4') 
        xbmc.sleep(5000)
        xbmc.executebuiltin(UpdaterMatrix_4)
        xbmc.sleep(7000)
        BG.update(54, Dialog_U1, Dialog_U6)
        xbmcvfs.delete('special://home/media/Bamako.mp4')

###########################################################################
        xbmc.executebuiltin('!Skin.HasSetting(HideKodiIntro)')


    BG.update(55, 'Αναμονή για ολοκλήρωση...', 'Παρακαλώ περιμένετε....')
    xbmc.sleep(5000)
    BG.update(100, Dialog_U4, 'ok!')
    xbmc.sleep(5000)
###########################################################################


    BG.close()

        
def installAddon():
    for addon_id in addon_list:
      xbmc.executebuiltin('InstallAddon(%s)' % (addon_id))
      xbmc.sleep(100)
      xbmc.executebuiltin('SendClick(11)')
      xbmc.sleep(100)


def del_dir():
    for ad in addons_data_path:
     for rr in delete_addons:
       dir_list = glob.iglob(os.path.join(ad, rr))
       for path in dir_list:
           if os.path.isdir(path):
               shutil.rmtree(path)
           if os.path.isfile(path):
              os.remove(path)


def enable_addons():
	conn =db_lib.connect(os.path.join(xbmc.translatePath('special://profile/Database'),'Addons33.db'))
	conn.text_factory = str
	conn.executemany('update installed set enabled=1 where addonID = (?)',((val,) for val in os.listdir(xbmc.translatePath(os.path.join('special://home','addons')))))
	conn.commit()
	xbmc.executebuiltin('UpdateLocalAddons')
	xbmc.executebuiltin('UpdateAddonRepos')


     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoplayer.stretch43","value":0}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":1}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"GUI.SetFullscreen","id":1,"params":{"fullscreen":"toggle"}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ExecuteAction","id":1,"params":{"action":"togglefullscreen"}}')




#        choice = xbmcgui.Dialog().yesno('[B][COLOR orange]TechNEWSology[/COLOR][/B]', '[COLOR white]      Επιθυμείτε την απενεργοποίηση των ενημερώσεων [CR]                        του TechNEWSology Updater ?[/COLOR]',
#                                        nolabel='[COLOR lime]Ενεργοποίηση[/COLOR]',yeslabel='[COLOR orange]Απενεργοποίηση[/COLOR]')
#        if choice == 1: [xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":false}}'), xbmcgui.Dialog().ok("[COLOR lime]TechNEWSology Updater-Tools[/COLOR]", "[COLOR orange]Απενεργοποήθηκαν οι αυτόματες ενημερώσεις         του TechNEWSology Updater.[/COLOR]")]
#        else:
#            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":true}}')

Updater_Matrix()
