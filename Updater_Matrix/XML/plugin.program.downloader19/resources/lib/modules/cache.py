# -*- coding: utf-8 -*-

'''
    Tulip routine libraries, based on lambda's lamlib
    Author Twilight0

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re, hashlib, time, xbmcgui, xbmc

try:
    from sqlite3 import dbapi2 as database
except:
    # noinspection PyUnresolvedReferences
    from pysqlite2 import dbapi2 as database

from resources.lib.modules import control
from updatervar import *



def get(definition, time_out, *args, **table):
    try:
        response = None

        f = repr(definition)
        f = re.sub('.+\smethod\s|.+function\s|\sat\s.+|\sof\s.+', '', f)

        a = hashlib.md5()
        for i in args: a.update(str(i))
        a = str(a.hexdigest())
    except:
        pass

    try:
        table = table['table']
    except:
        table = 'rel_list'

    try:
        control.makeFile(control.dataPath)
        dbcon = database.connect(control.cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("SELECT * FROM %s WHERE func = '%s' AND args = '%s'" % (table, f, a))
        match = dbcur.fetchone()

        response = eval(match[2].encode('utf-8'))

        t1 = int(match[3])
        t2 = int(time.time())
        update = (abs(t2 - t1) / 3600) >= int(time_out)
        if not update:
            return response
    except:
        pass

    try:
        r = definition(*args)
        if (r is None or r == []) and response is not None:
            return response
        elif r is None or r == []:
            return r
    except:
        return

    try:
        r = repr(r)
        t = int(time.time())
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s (""func TEXT, ""args TEXT, ""response TEXT, ""added TEXT, ""UNIQUE(func, args)"");" % table)
        dbcur.execute("DELETE FROM %s WHERE func = '%s' AND args = '%s'" % (table, f, a))
        dbcur.execute("INSERT INTO %s Values (?, ?, ?, ?)" % table, (f, a, r, t))
        dbcon.commit()
    except:
        pass

    try:
        return eval(r.encode('utf-8'))
    except:
        pass


def timeout(definition, *args, **table):

    try:
        response = None

        f = repr(definition)
        f = re.sub('.+\smethod\s|.+function\s|\sat\s.+|\sof\s.+', '', f)

        a = hashlib.md5()
        for i in args: a.update(str(i))
        a = str(a.hexdigest())
    except:
        pass

    try:
        table = table['table']
    except:
        table = 'rel_list'

    try:
        control.makeFile(control.dataPath)
        dbcon = database.connect(control.cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("SELECT * FROM %s WHERE func = '%s' AND args = '%s'" % (table, f, a))
        match = dbcur.fetchone()
        return int(match[3])
    except:
        return


def clear(table=None, withyes=True):

    try:
        control.idle()

        if table is None:
            table = ['rel_list', 'rel_lib']
        elif not type(table) == list:
            table = [table]

        if withyes:

            yes = control.yesnoDialog(control.lang(30401).encode('utf-8'), '', '')

            if not yes:
                return

        else:

            pass

        dbcon = database.connect(control.cacheFile)
        dbcur = dbcon.cursor()

        for t in table:
            try:
                dbcur.execute("DROP TABLE IF EXISTS %s" % t)
                dbcur.execute("VACUUM")
                dbcon.commit()
            except:
                pass

        control.infoDialog(control.lang(32013).encode('utf-8'))
    except:
        pass


def delete(dbfile=control.cacheFile, withyes=True):
    if withyes:
        yes = control.yesnoDialog(control.lang(30401).encode('utf-8'), '', '')
        if not yes:
            return

    else:
        pass

    control.deleteFile(dbfile)
    control.infoDialog(control.lang(32023).encode('utf-8'))



homelander  = control.provider_homelander
scrubsv2    = control.provider_scrubsv2
thecrew     = control.provider_thecrew
shadow      = control.provider_shadow
blacklodge  = control.provider_blacklodge ##  World Build ##
quicksilver = control.provider_quicksilver ##  World Build ##

def clear_provider():
    try:
        control.idle()

        control.makeFile(control.dataPath)

        dbcon = database.connect(homelander)
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

        dbcon = database.connect(scrubsv2)
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

        dbcon = database.connect(thecrew)
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

        dbcon = database.connect(shadow)
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

        dbcon = database.connect(blacklodge) ##  World Build ##
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

        dbcon = database.connect(quicksilver) ##  World Build ##
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS rel_src")
        dbcur.execute("DROP TABLE IF EXISTS rel_url")
        dbcur.execute("VACUUM")
        dbcon.commit()

    except:
        pass
    xbmc.sleep(1000)
    xbmcgui.Dialog().ok(addon_name, '[COLOR lime]Πραγματοποιήθηκε καθαρισμός παρόχων:[/COLOR][CR] homelander, scrubsv2[CR] thecrew, shadow[CR] blacklodge, quicksilver, sealteam6')

