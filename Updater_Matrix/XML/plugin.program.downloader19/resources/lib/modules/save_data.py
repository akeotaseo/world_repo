import os, xbmc, shutil
from updatervar import *


user_path = xbmcvfs.translatePath('special://userdata/')
data_path = os.path.join(user_path, 'addon_data/')

def backup(path, file):
    if os.path.exists(os.path.join(path, file)):
        try:
            if os.path.isfile(os.path.join(path, file)):
                xbmcvfs.copy(os.path.join(path, file), os.path.join(packages, file))
            elif os.path.isdir(os.path.join(path, file)):
                shutil.copytree(os.path.join(path, file), os.path.join(packages, file), dirs_exist_ok=True)
        except Exception as e:
            xbmc.log('Failed to backup %s. Reason: %s' % (os.path.join(packages, file), e), xbmc.LOGINFO)

def restore(path, file):
    if os.path.exists(os.path.join(packages, file)):
        try:
            if os.path.isfile(os.path.join(packages, file)):
                if os.path.exists(os.path.join(user_path, file)):
                    os.unlink(os.path.join(path, file))
                shutil.move(os.path.join(packages, file), os.path.join(path, file))
            elif os.path.isdir(os.path.join(packages, file)):
                shutil.copytree(os.path.join(packages, file), os.path.join(path, file), dirs_exist_ok=True)
        except Exception as e:
            xbmc.log('Failed to restore %s. Reason: %s' % (os.path.join(path, file), e), xbmc.LOGINFO)

def save_menu():
	save_items = []
	choices = ["Favourites", "Sources", "Debrid - Resolve URL", "OpenSubtitles Settings", "Disney Settings", "Netflix Settings", "Pvr Stalker Settings", "Advanced Settings", "Api Key YouTube", "MyPreferences Settings (Folders)"]
	dialog = xbmcgui.Dialog()
	save_select = dialog.multiselect("Επιλέξτε στοιχεία που επιθυμείτε να διατηρηθούν",choices, preselect=[])
	
	if save_select == None:
		return
	else:
		for index in save_select:
			save_items.append(choices[index])
	if 'Favourites' in save_items:
		setting_set('savefavs','true')
	else:
		setting_set('savefavs','false')
	if 'Sources' in save_items:
		setting_set('savesources', 'true')
	else:
		setting_set('savesources', 'false')
	if 'Debrid - Resolve URL' in save_items:
		setting_set('savedebrid','true')
	else:
		setting_set('savedebrid','false')
	if 'OpenSubtitles Settings' in save_items:
		setting_set('saveopensubtitles','true')
	else:
		setting_set('saveopensubtitles','false')
	if 'Disney Settings' in save_items:
		setting_set('savedisney','true')
	else:
		setting_set('savedisney','false')
	if 'Netflix Settings' in save_items:
		setting_set('savenetflix','true')
	else:
		setting_set('savenetflix','false')
	if 'Pvr Stalker Settings' in save_items:
		setting_set('savepvrstalker','true')
	else:
		setting_set('savepvrstalker','false')
	if 'Advanced Settings' in save_items:
		setting_set('saveadvanced','true')
	else:
		setting_set('saveadvanced','false')
	if 'Api Key YouTube' in save_items:
		setting_set('saveapikey','true')
	else:
		setting_set('saveapikey','false')
	if 'MyPreferences Settings (Folders)' in save_items:
		setting_set('savemypreferences','true')
	else:
		setting_set('savemypreferences','false')

	setting_set('firstrunSave', 'true')
	return

def save_check():
	if setting('savefavs')=='true':
		EXCLUDES.append('favourites.xml')
	if setting('savesources')=='true':
		EXCLUDES.append('sources.xml')
	if setting('savedebrid')=='true':
		EXCLUDES.append('script.module.resolveurl')
	if setting('saveopensubtitles')=='true':
		EXCLUDES.append('service.subtitles.opensubtitles')
	if setting('savedisney')=='true':
		EXCLUDES.append('slyguy.disney.plus')
	if setting('savenetflix')=='true':
		EXCLUDES.append('plugin.video.netflix')
	if setting('savepvrstalker')=='true':
		EXCLUDES.append('pvr.stalker')
	if setting('saveadvanced')=='true':
		EXCLUDES.append('advancedsettings.xml')
	if setting('saveapikey')=='true':
		EXCLUDES.append('plugin.video.youtube')
	if setting('savemypreferences')=='true':
		EXCLUDES.append('plugin.program.mypreferences')
	return EXCLUDES

def save_backup():
	backup(user_path, addon_id)
	if setting('savefavs')=='true':
		try:backup(user_path, 'favourites.xml')
		except: pass
	if setting('savesources')=='true':
		try: backup(user_path, 'sources.xml')
		except: pass
	if setting('savedebrid')=='true':
		try: backup(data_path, 'script.module.resolveurl')
		except: pass
	if setting('saveopensubtitles')=='true':
		try: backup(data_path, 'service.subtitles.opensubtitles')
		except: pass
	if setting('savedisney')=='true':
		try: backup(data_path, 'slyguy.disney.plus')
		except: pass
	if setting('savenetflix')=='true':
		try: backup(data_path, 'plugin.video.netflix')
		except: pass
	if setting('savepvrstalker')=='true':
		try: backup(data_path, 'pvr.stalker')
		except: pass
	if setting('saveadvanced')=='true':
		try: backup(user_path, 'advancedsettings.xml')
		except: pass
	if setting('saveapikey')=='true':
		try: backup(data_path, 'plugin.video.youtube')
		except: pass
	if setting('savemypreferences')=='true':
		try: backup(data_path, 'plugin.program.mypreferences')
		except: pass

def save_restore():
	restore(user_path, addon_id)
	if setting('savefavs')=='true':
		try: restore(user_path, 'favourites.xml')
		except: pass
	if setting('savesources')=='true':
		try: restore(user_path, 'sources.xml')
		except: pass
	if setting('savedebrid')=='true':
		try: restore(data_path, 'script.module.resolveurl')
		except: pass
	if setting('saveopensubtitles')=='true':
		try: restore(data_path, 'service.subtitles.opensubtitles')
		except: pass
	if setting('savedisney')=='true':
		try: restore(data_path, 'slyguy.disney.plus')
		except: pass
	if setting('savenetflix')=='true':
		try: restore(data_path, 'plugin.video.netflix')
		except: pass
	if setting('savepvrstalker')=='true':
		try: restore(data_path, 'pvr.stalker')
		except: pass
	if setting('saveadvanced')=='true':
		try: restore(user_path, 'advancedsettings.xml')
		except: pass
	if setting('saveapikey')=='true':
		try: restore(data_path, 'plugin.video.youtube')
		except: pass
	if setting('savemypreferences')=='true':
		try: restore(data_path, 'plugin.program.mypreferences')
		except: pass
#	shutil.rmtree(packages)