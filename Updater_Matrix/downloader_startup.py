import os, glob, xbmc, xbmcgui, xbmcvfs, xbmcaddon, shutil
from updatervar import *
#from resources.lib.modules.delete_addons import del_dir
from resources.lib.GUIcontrol import txt_updater
from resources.lib.modules import db, addonsEnable
from resources.lib.modules.addonsEnable import enable_addons
#from resources.lib.modules.installer_addons import installAddon
from resources.lib.GUIcontrol.txt_updater import get_skinshortcutsversion

skinshortcuts_version = get_skinshortcutsversion()

Database_Addons33 = [('plugin.video.fmoviesto', 'repository.mbebe'),
                     ('plugin.video.subsmovies', 'repository.mbebe'),
                     ('plugin.program.downloader19', 'repository.World'),
                     ('script.extendedinfo', 'repository.World'),
                     ('plugin.image.World', 'repository.World'),
                     ('plugin.program.super.favourites', 'repository.World'),
                     ('plugin.program.installelementum', 'repository.World'),
                     ('plugin.video.hdtrailers_net.reloaded', 'repository.World'),
                     ('plugin.video.cartoonsgr', 'repository.gkobu'),
                     ('plugin.video.tvone', 'repository.gkobu'),
                     ('plugin.video.tvone11', 'repository.gkobu'),
                     ('plugin.video.tvone111', 'repository.gkobu'),
                     ('plugin.video.tvone1111', 'repository.gkobu'),
                     ('plugin.video.shadow', 'repository.gkobu'),
                     ('plugin.video.last_played', 'repository.gkobu'),
                     ('plugin.video.f4mTester', 'repository.gkobu'),
                     ('script.skinshortcuts', 'repository.gkobu'),
                     ('plugin.video.microjen', 'repository.gkobu'),
                     ('repository.gkobu', 'repository.gkobu'),
                     ('script.gkobu.pairwith', 'repository.gkobu'),
                     ('service.subtitles.localsubtitle', 'repository.gkobu'),
                     ('plugin.video.themoviedb.helper', 'repository.jurialmunkey'),
                     ('repository.arrownegra', 'repository.arrownegra'),
                     ('vkkodi.repo', 'vkkodi.repo')]


def Updater_Matrix():
    BG.create(Dialog_U1, Dialog_U2)
    xbmc.sleep(500)
    BG.update(5, Dialog_U1, Dialog_U6)
    xbmc.sleep(5000)
    BG.update(25, Dialog_U1, Dialog_U6)

    xbmc.sleep(5000)
    db.addon_database(Database_Addons33, 1, True)
    xbmc.sleep(7000)
    BG.update(30, Dialog_U1, 'Εισαγωγή αποθετηρίων στο Database/Addons33...')

### Το ενεργοποιείς όταν θέλεις να περάσεις πρόσθετα ###
    installAddon()
    xbmc.sleep(8000)


###########################################################################



    if not os.path.exists(UpdaterMatrix_path):
       xbmc.sleep(1000)
       xbmc.executebuiltin(UpdaterMatrix_1)
       xbmc.sleep(5000)
       BG.update(33, Dialog_U1, Dialog_U6)

    if not os.path.exists(UpdaterMatrix_path2):
       xbmc.sleep(1000)
       xbmc.executebuiltin(UpdaterMatrix_2)
       xbmc.sleep(5000)
       BG.update(36, Dialog_U1, Dialog_U6)

    if not os.path.exists(UpdaterMatrix_path3):
        xbmc.sleep(1000)
        xbmc.executebuiltin(UpdaterMatrix_3)
        xbmc.sleep(5000)
        BG.update(33, Dialog_U1, Dialog_U6)
 
 #   if not os.path.exists(UpdaterMatrix_path4):
 #       xbmc.sleep(1000)
 #       xbmc.executebuiltin(UpdaterMatrix_4)
 #       xbmc.sleep(5000)
 #       BG.update(33, Dialog_U1, Dialog_U6)
 
 #   if not os.path.exists(UpdaterMatrix_path5):
 #       xbmc.sleep(1000)
 #       xbmc.executebuiltin(UpdaterMatrix_5)
 #       xbmc.sleep(5000)
 #       BG.update(33, Dialog_U1, Dialog_U6)
 
 #   if not os.path.exists(UpdaterMatrix_path6):
 #       xbmc.sleep(1000)
 #       xbmc.executebuiltin(UpdaterMatrix_6)
 #       xbmc.sleep(5000)
 #       BG.update(33, Dialog_U1, Dialog_U6)



###########################################################################

#    xbmc.sleep(5000)
#    BG.update(40, Dialog_U1, 'Διαγραφή αχρείαστων αρχείων...')
#    del_dir()                                     ### delete addons ands files ###

#    if os.path.exists(UpdaterMatrix_path3): xbmcvfs.delete(UpdaterMatrix_path3), xbmc.sleep(1000)
#    if os.path.exists(UpdaterMatrix_path4): xbmcvfs.delete(UpdaterMatrix_path4), xbmc.sleep(1000)


    BG.update(50, Dialog_U1, Dialog_U2)

    xbmc.sleep(5000)
#    addonsEnable.enable_addons()
#    BG.update(75, Dialog_U1, 'Ενεργοποίηση πρόσθετων...')
    xbmc.sleep(8000)
    BG.update(80, Dialog_U1, Dialog_U6)

    if skinshortcuts_version > int(setting('skinshortcutsversion')):
        xbmc.executebuiltin(skinshortcuts_menu)
        xbmc.sleep(8000)
        BG.update(96, Dialog_U1, 'Ενημέρωση στο μενού του skin...')
        setting_set('skinshortcutsversion', str(skinshortcuts_version))
        xbmc.sleep(5000)
        BG.update(100, Dialog_U4, 'Θα ακολουθήσει... επαναφόρτωση του προφίλ')
        xbmc.sleep(5000)
        BG.update(100, Dialog_U4, 'Θα ακολουθήσει... και πάγωμα της εικόνας')
        xbmc.sleep(8000)
        BG.update(100, Dialog_U4, Dialog_U5)
        xbmc.executebuiltin("LoadProfile(Master user)")
    xbmc.sleep(5000)
    BG.update(100, Dialog_U4, Dialog_U5)
    xbmc.sleep(5000)
    BG.update(100, Dialog_U4, Dialog_U5)

    BG.close()
    xbmcvfs.delete(downloader_startup_delete)

def installAddon():
    for addon_id in addon_list:
      xbmc.executebuiltin('InstallAddon(%s)' % (addon_id))
      xbmc.sleep(100)
      xbmc.executebuiltin('SendClick(11)')
      xbmc.sleep(100)

                         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα που επιθυμείς [  ] ###

addon_list = ['plugin.video.live.streamspro', 'plugin.program.downloader19', 'plugin.video.sporthdme', 'repository.arrownegra', 'plugin.program.autowidget',
              'plugin.video.cartoonsgr']


def del_dir():
    for ad in addons_data_path:
     for rr in delete_addons:
       dir_list = glob.iglob(os.path.join(ad, rr))
       for path in dir_list:
           if os.path.isdir(path):
               shutil.rmtree(path)
           if os.path.isfile(path):
              os.remove(path)
              
         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα ή τα αρχεία που επιθυμείς να αφαιρέσεις [  ] ###

delete_addons = ['plugin.video.TEST', 'addon/main.py']


Updater_Matrix()
