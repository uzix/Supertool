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
        screen.addstr(3, 4,  "a - Kolla systemets loggar", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
       	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
		execute_cmd("cat /var/log/messages | less")
                execute_cmd("cat /var/log/dmesg | less")
                execute_cmd("cat /var/log/syslog | less")
                execute_cmd("cat /var/log/boot.log | less")
                execute_cmd("cat /var/log/dpkg.log | less")
                execute_cmd("cat /var/log/bootstrap.log | less")
                execute_cmd("cat /var/log/alternatives.log | less")
                execute_cmd("cat /var/log/auth.log | less")

curses.endwin()

