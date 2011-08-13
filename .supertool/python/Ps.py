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
        screen.addstr(3, 4,  "a - Kolla vilka processer som körs", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Kolla vilka processer som är mest krävande", curses.color_pair(2) )
        screen.addstr(5, 4,  "c - Döda processnummer", curses.color_pair(2) )
      	screen.addstr(6, 4,  "d - Döda processnamn", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
		execute_cmd("ps -a | less")
        if x == ord('b'):
                curses.endwin()
                execute_cmd("top")
        if x == ord('c'):
		Process = get_param("Döda processnummer")
                curses.endwin()
                execute_cmd("kill -9 " + Process)
        if x == ord('d'):
                Process = get_param("Döda processnamn")
                curses.endwin()
                execute_cmd("killall -9 " + Process)

curses.endwin()

