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
        screen.addstr(3, 4,  "a - Kolla hårdvara, kärnmoduler samt kärna", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Kolla system meddelanden", curses.color_pair(2) )
        screen.addstr(5, 4,  "c - Kolla hur mycket minne systemet använder", curses.color_pair(2) )
        screen.addstr(6, 4,  "d - Kolla hårddiskars status", curses.color_pair(2) )
        screen.addstr(7, 4,  "e - Kolla temperaturer", curses.color_pair(2) )
        screen.addstr(8, 4,  "f - Aktivera Brandvägg", curses.color_pair(2) )
        screen.addstr(9, 4,  "g - Avaktivera Brandvägg", curses.color_pair(2) )
        screen.addstr(10, 4, "h - Port att öppna i brandvägg", curses.color_pair(2) )
    	screen.addstr(11, 4, "i - Port att stänga i brandvägg", curses.color_pair(2) )
        screen.addstr(12, 4, "j - Kolla status på brandvägg", curses.color_pair(2) )
       	screen.addstr(13, 4, "k - Kolla hur mycket utrymme en katalog tar", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
                execute_cmd("lspci -k | less")
                execute_cmd("dmidecode | less")
                execute_cmd("uname -a")
        if x == ord('b'):
                curses.endwin()
                execute_cmd("dmesg | less")
        if x == ord('c'):
                curses.endwin()
                execute_cmd("free -m")
		execute_cmd("df -m")
        if x == ord('d'):
		Harddrive = get_param("Välj hårdisk, exempelvis /dev/sda eller /dev/sdb")
                curses.endwin()
                execute_cmd("smartctl -a " + Harddrive + " | less")
        if x == ord('e'):
                curses.endwin()
                execute_cmd("sensors")
        if x == ord('f'):
                curses.endwin()
		execute_cmd("ufw default deny")
                execute_cmd("ufw enable")
        if x == ord('g'):
                curses.endwin()
                execute_cmd("ufw disable")
        if x == ord('h'):
		Port = get_param("Välj port att öppna")
                curses.endwin()
                execute_cmd("ufw allow " + Port)
        if x == ord('i'):
                Port = get_param("Välj port att stänga")
                curses.endwin()
                execute_cmd("ufw deny " + Port)
        if x == ord('j'):
                curses.endwin()
                execute_cmd("ufw status")
        if x == ord('l'):
                Katalog = get_param("Välj katalog, exempelvis /usr/bin")
                curses.endwin()
                execute_cmd("du -h " + Katalog)

curses.endwin()

