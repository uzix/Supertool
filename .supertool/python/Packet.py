#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Licens:GNU General Public License
# Written by Uzi juni 2011

from os import system
import curses
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
from CustomMod import*

x = 0

while x != ord('q'):
      	system("reset")
	screen = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Välj...", curses.color_pair(1) )
        screen.addstr(3, 4,  "a - Ladda hem samt installera systemuppdateringar", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Kolla vilka paket som är installerade", curses.color_pair(2) )
        screen.addstr(5, 4,  "c - Sök paket", curses.color_pair(2) )
      	screen.addstr(6, 4,  "d - Installera paket", curses.color_pair(2) )
        screen.addstr(7, 4,  "e - Uppdatera Metasploit", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
                execute_cmd_silent("apt-get update")
                execute_cmd_silent("apt-get upgrade")
                execute_cmd("apt-get dist-upgrade")
        if x == ord('b'):
                curses.endwin()
                execute_cmd("dpkg -l | less")
        if x == ord('c'):
		Packet = get_param("Sök paket namn")
                curses.endwin()
                execute_cmd("apt-cache search " + Packet)
        if x == ord('d'):
                Packet = get_param("Installera ett eller flera paket, om fler skilj dem åt med mellanslag")
                curses.endwin()
                execute_cmd("apt-get install " + Packet)
        if x == ord('e'):
                curses.endwin()
                execute_cmd("svn update /opt/msf/msf")

curses.endwin()

