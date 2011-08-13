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
        screen.addstr(3, 4,  "a - Lägg till användare", curses.color_pair(2) )
        screen.addstr(4, 4,  "b - Ta bort användare", curses.color_pair(2) )
	screen.addstr(5, 4,  "c - Förändra ägare av fil", curses.color_pair(2) )
	screen.addstr(6, 4,  "d - Förändra ägare av filer", curses.color_pair(2) )
	screen.addstr(7, 4,  "e - Modifiera befintlig användare", curses.color_pair(2) )
        screen.addstr(8, 4,  "f - Skapa grupp", curses.color_pair(2) )
        screen.addstr(9, 4,  "g - Förändra ägare av filer för grupp", curses.color_pair(2) )
        screen.addstr(10, 4, "h - Ta bort grupp", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		username = get_param("Välj användarnamn")
		homedir = get_param("Välj hemkatalog, exempelvis /home/valfri")
		groups = get_param("Välj komma-separerade grupper, exempelvis adm,dialout,cdrom")
		shell = get_param("Välj skal, exempelvis /bin/bash:")
		curses.endwin()
		execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
		execute_cmd("passwd " + username)
	if x == ord('b'):
		User = get_param("Välj användarnamn")
		curses.endwin()
		execute_cmd("deluser -r " + User)
	if x == ord('c'):
                User = get_param("Välj användarnamn")
		Katalog = get_param("Välj katalog")	
		curses.endwin()
		execute_cmd("chown " + User + " " + Katalog)
        if x == ord('d'):
                User = get_param("Välj användarnamn")
                Katalog = get_param("Välj katalog")
                curses.endwin()
                execute_cmd("chown -R " + User + " " + Katalog)
        if x == ord('e'):
		User = get_param("Välj användarnamn")
                Parameter = get_param("Välj åtgärd,lås konto -L,Lås upp konto -U,ändra standardskal -s följt av mellanslag samt skal, exempelvis /bin/ash")
		curses.endwin()
                execute_cmd("usermod " + Parameter + " " + User)
        if x == ord('f'):
                Group = get_param("Välj gruppnamn")
                curses.endwin()
                execute_cmd("groupadd " + Group)
        if x == ord('g'):
                Group = get_param("Välj gruppnamn")
                Katalog = get_param("Välj katalog")
		curses.endwin()
                execute_cmd("chgrp " + Group + " " +Katalog)
        if x == ord('h'):
                Group = get_param("Välj gruppnamn")
		curses.endwin()
                execute_cmd("groupdel " + Group)

curses.endwin()

