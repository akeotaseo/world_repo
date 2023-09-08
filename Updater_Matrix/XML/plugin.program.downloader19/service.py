# -*- coding: utf-8 -*-
import xbmc, xbmcgui
from updatervar import *
from resources.lib.modules import check


if __name__ == '__main__':
	if not setting('updaterversion') == 'false':
		dialog.notification(Dialog_welcome, Dialog_Update, icon_Build, sound=False)
		BG.create(Dialog_U8, Dialog_U6)
		xbmc.sleep(5000)
		BG.close()
		check.updater()
		check.notifyT()
		xbmc.sleep(5000)
		dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
		check.autoenable()
		check.var()
		check.setsetting()
		check.players()
		check.delete()
		check.zip1()
		check.zip2()
		check.zip3()
		check.zip4()
		check.zip5()
		check.pvr()
		check.installation()
		check.database()
		dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
		xbmc.sleep(10000)
		check.xmlskin()


		xbmc.sleep(20000)
		dialog.notification('[B][COLOR orange]Το build είναι ενημερωμένο![/COLOR][/B]', '[COLOR white]Καλή διασκέδαση...[/COLOR]', icon_ok, sound=False)
		check.UpdateAddonRepos()

	else:
		dialog.notification(Dialog_welcome, Dialog_not_Updater, icon_Build, sound=False)
		check.UpdateAddonRepos()
	xbmc.sleep(5000)
	dialog.notification('Check Updates', 'Ελεγχος για ενημερώσεις προσθέτων', icon_auto2, sound=False)



	monitor = xbmc.Monitor()

	while not monitor.abortRequested():
		if monitor.waitForAbort(2*60*60):#διάστημα 2ωρών μεταξύ των ενημερώσεων
			break
		xbmc.executebuiltin('UpdateAddonRepos()')
		dialog.notification('Υπηρεσία ενημέρωσης', 'Εκκίνηση ενημερώσεων προσθέτων', icon_auto, sound=False)
