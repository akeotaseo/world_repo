
import xbmc
from updatervar import *
from resources.lib.GUIcontrol import notify
from resources.lib.GUIcontrol.notify import get_notifyversion
from resources.lib.GUIcontrol.txt_updater import get_addonsrepos, get_updaterversion, get_xmlskin, get_players, get_set_setting, get_var, get_pvr
from resources.lib.GUIcontrol.txt_updater import get_addons_list_installation, get_delete_files, get_zip1, get_zip2, get_zip3, get_zip4, get_zip5
from resources.lib.modules import addonsEnable

addons_list_installation_version = get_addons_list_installation()
notify_version       = get_notifyversion()
addons_repos_version = get_addonsrepos()
updater_version      = get_updaterversion()
xmlskin_version      = get_xmlskin()
players_version      = get_players()
set_setting_version  = get_set_setting()
delete_files_version = get_delete_files()
var_version          = get_var()
zip1_version         = get_zip1()
zip2_version         = get_zip2()
zip3_version         = get_zip3()
zip4_version         = get_zip4()
zip5_version         = get_zip5()
pvr_version          = get_pvr()


def autoenable():
    if setting('autoenable') == 'true':
        addonsEnable.enable_addons()
        setting_set('autoenable','false')
        dialog.notification(Dialog_enable_on, Dialog_enable, icon_Build, sound=False)


def var():
    if var_version > int(setting('varversion')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Var_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('varversion', str(var_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def players():
    if players_version > int(setting('playersversion')):
        BG.create(Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(5, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_Players)
        xbmc.executebuiltin(Players_startup)
        xbmc.sleep(1500)
        BG.update(25, Dialog_U12, Dialog_Players)
        xbmc.sleep(500)
        setting_set('playersversion', str(players_version))
        BG.update(55, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def delete():
    if delete_files_version > int(setting('deleteversion')):
        xbmc.executebuiltin(Delete_startup)
        BG.create(Dialog_U2, Dialog_U11)
        xbmc.sleep(7000)
        BG.update(33, Dialog_U2, Dialog_U11)
        xbmc.sleep(5000)
        BG.update(63, Dialog_U2, Dialog_U11)
        xbmc.sleep(7000)
        BG.update(96, Dialog_U2, Dialog_U10)
        xbmc.sleep(7000)
        xbmc.executebuiltin(del_startup)
        BG.update(100, '[B]Η διαγραφή των στοιχείων[/B]', Dialog_U4)
        xbmc.sleep(1000)
        setting_set('deleteversion', str(delete_files_version))
        BG.close()


def zip1():
    if zip1_version > int(setting('zip1version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip1_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip1version', str(zip1_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip2():
    if zip2_version > int(setting('zip2version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip2_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip2version', str(zip2_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip3():
    if zip3_version > int(setting('zip3version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip3_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip3version', str(zip3_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip4():
    if zip4_version > int(setting('zip4version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip4_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip4version', str(zip4_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip5():
    if zip5_version > int(setting('zip5version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip5_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip5version', str(zip5_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def pvr():
    if pvr_version > int(setting('pvrversion')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Pvr_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('pvrversion', str(pvr_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def installation():
    if addons_list_installation_version > int(setting('installationversion')):
        xbmc.executebuiltin(Installation_startup)
        BG.create(Dialog_U12, Dialog_U6)
        xbmc.sleep(5000)
        BG.update(33, Dialog_U12, Dialog_U2)
        xbmc.sleep(5000)
        BG.update(63, Dialog_U12, 'Έλεγχος εγκατάστασης νέων πρόσθετων...')
        xbmc.sleep(5000)
        BG.update(96, Dialog_U12, 'Έλεγχος εγκατάστασης νέων πρόσθετων...')
        xbmc.sleep(3000)
        xbmc.executebuiltin(install_startup)
        BG.update(100, Dialog_U1, Dialog_U4)
        xbmc.sleep(1000)
        setting_set('installationversion', str(addons_list_installation_version))
        BG.close()


def updater():
    if updater_version > int(setting('updaterversion')):
        xbmc.executebuiltin(Updater_startup)
        xbmc.sleep(15000)
        xbmc.executebuiltin(downloader_startup)
        setting_set('updaterversion', str(updater_version))
    else:
        if os.path.exists (downloader_startup_tk):
            xbmc.sleep(5000)
            xbmc.executebuiltin(downloader_startup)


def setsetting():
    if set_setting_version > int(setting('setsettingversion')):
        xbmc.executebuiltin(SetSetting_startup)
        xbmc.sleep(18000)
        xbmc.executebuiltin(set_setting_startup)
        xbmc.sleep(1000)
        setting_set('setsettingversion', str(set_setting_version))
        xbmc.sleep(1000)


def database():
    if addons_repos_version > int(setting('addonsreposversion')):
        xbmc.executebuiltin(AddonsRepos_startup)
        BG.create(Dialog_U6, Dialog_Database)
        xbmc.sleep(5000)
        BG.update(33, Dialog_U6, Dialog_Database)
        xbmc.sleep(5000)
        BG.update(63, Dialog_U12, Dialog_Database)
        xbmc.sleep(5000)
        BG.update(96, Dialog_U12, Dialog_Database)
        xbmc.sleep(3000)
        xbmc.executebuiltin(database_startup)
        xbmc.sleep(1000)
        setting_set('addonsreposversion', str(addons_repos_version))
        BG.update(100, Dialog_U12, Dialog_U4)
        xbmc.sleep(7000)
        addonsEnable.enable_addons()
        xbmc.sleep(5000)
        BG.close()


def xmlskin():
    if not setting('xmlskinversion') == 'false':
        if xmlskin_version > int(setting('xmlskinversion')):
            BG.create(Dialog_U12, Dialog_Xml_Skin)
            BG.update(5, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(15, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            xbmc.executebuiltin(XmlSkin_startup)
            xbmc.sleep(1000)
            BG.update(25, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(500)
            setting_set('xmlskinversion', str(xmlskin_version))
            BG.update(55, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(75, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(80, Dialog_U12, Dialog_U9)
            xbmc.sleep(1000)
            BG.update(90, Dialog_U1, 'Ενημέρωση μενού skin.')
            xbmc.sleep(5000)
            BG.update(95, Dialog_U4, 'Θα ακολουθήσει... επαναφόρτωση του προφίλ')
            xbmc.sleep(3000)
            xbmcgui.Dialog().notification("[B][COLOR orange]Reload Profile[/COLOR][/B]", "[COLOR white]Παρακαλώ περιμένετε...[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/reloadprofile.png')
            xbmc.sleep(500)
            BG.update(100, Dialog_U4, 'Θα ακολουθήσει... και πάγωμα της εικόνας')
            xbmc.sleep(2000)
            xbmc.executebuiltin("LoadProfile(Master user)")
            BG.close()

def UpdateAddonRepos():
        xbmc.executebuiltin('UpdateLocalAddons')
        xbmc.executebuiltin('UpdateAddonRepos')


def notifyT():
    if not setting('firstrunNotify')=='false':
        if notify_version > int(setting('notifyversion')):
            setting_set('notifyversion', str(notify_version))
            d=notify.notify()
            d.doModal()
            del d

