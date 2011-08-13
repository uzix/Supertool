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
        screen.addstr(3, 4,  "a - Lista tjänster", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Lägg till startjänst", curses.color_pair(2) )
        screen.addstr(5, 4,  "c - Ta bort startjänst", curses.color_pair(2) )
        screen.addstr(6, 4,  "d - Starta, stoppa, boota om tjänst", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
                execute_cmd("ls /etc/init.d | less")
        if x == ord('b'):
		Service = get_param("Lägg till starttjänst")
                curses.endwin()
                execute_cmd("update-rc.d " + Service + " defaults")
        if x == ord('c'):
		Service = get_param("Ta bort starttjänst")
                curses.endwin()
                execute_cmd("update-rc.d " + Service + " remove")
        if x == ord('d'):
                Service = get_param("Välj tjänst")
		Action = get_param("Välj start,stop eller restart")
                curses.endwin()
                execute_cmd("/etc/init.d/" + Service + " " + Action)

curses.endwin()

