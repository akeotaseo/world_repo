import os, glob, xbmc, xbmcgui, xbmcvfs, xbmcaddon, shutil
from updatervar import *
from resources.lib.GUIcontrol import txt_updater
from resources.lib.modules import db, addonsEnable
from resources.lib.modules.addonsEnable import enable_addons
from resources.lib.GUIcontrol.txt_updater import get_skinshortcutsversion, get_addonsrepos


exists = os.path.exists
skinshortcuts_version = get_skinshortcutsversion()

Database_Addons33 = [('plugin.video.vidembed', 'repository.World'),
                     ('script.module.parrot', 'repository.World'),
                     ('plugin.video.parrot', 'repository.World')]

                         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα που επιθυμείς [  ] ###

#addon_list = ['plugin.video.live.test', 'repository.Worldolympic', 'plugin.video.themoviedb.helper', 'repository.plexkodiconnect', 'plugin.program.jewpair', 'script.module.grs', 'plugin.video.testt']


         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα ή τα αρχεία που επιθυμείς να αφαιρέσεις [  ] ###

#delete_addons = ['repository.test', 'repository.gsource', 'repository.testt']



def Updater_Matrix():
    BG.create('Γίνεται εγκατάσταση', Dialog_U2)
    xbmc.sleep(3000)



                                 #Εγκατάσταση νέων repository'
    if exists(UpdaterMatrix_path15): xbmcvfs.delete(UpdaterMatrix_path15), xbmc.sleep(1000)



###########################################################################


    if not exists(UpdaterMatrix_path15):
        xbmc.sleep(1000)
        BG.update(50, 'Εγκατάσταση', 'The Anonymous Portal')
        xbmc.sleep(5000)
        xbmc.executebuiltin(UpdaterMatrix_15)
        xbmc.sleep(10000)
        xbmc.sleep(1000)
        addonsEnable.enable_addons()


        BG.update(100, 'Αυτό ήταν...', 'ok!')
        xbmc.sleep(1000)
###########################################################################


        BG.close()
        xbmcvfs.delete(downloader_startup_delete)

        xbmc.sleep(1000)
        addonsEnable.enable_addons()


        xbmc.sleep(1000)
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.autowidget/folders/py/TheAnonymousPortal/TheAnonymousPortal.py")')


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
