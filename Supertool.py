#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Licens:GNU General Public License
# Written by Uzi juni 2011

from os import system
import curses
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Kommando utfört"
	else:
		print "Kommandot kunde ej verkställas, programvara saknas"
	raw_input("Tryck Enter")
	print ""

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
        screen.addstr(3, 4,  "0 - Användaralternativ", curses.color_pair(2) )
        screen.addstr(4, 4,  "1 - Kör supertool i rootläge", curses.color_pair(2) )
	screen.addstr(5, 4,  "2 - Användarhantering samt grupphantering", curses.color_pair(2) )
	screen.addstr(6, 4,  "3 - Logghantering", curses.color_pair(2) )
	screen.addstr(7, 4,  "4 - Egna installationer samt tweaks", curses.color_pair(2) )
        screen.addstr(8, 4,  "5 - Hantera processer", curses.color_pair(2) )
        screen.addstr(9, 4,  "6 - Pakethantering", curses.color_pair(2) )
        screen.addstr(10, 4, "7 - Hantera starttjänster", curses.color_pair(2) )
        screen.addstr(11, 4, "8 - System", curses.color_pair(2) )
        screen.addstr(12, 4, "9 - Hantera nätverk", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Avsluta", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

        if x == ord('0'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Custom.py")
        if x == ord('1'):
                curses.endwin()
		execute_cmd("sudo /usr/local/bin/Supertool.py")
	if x == ord('2'):
		curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/python/User.py")
	if x == ord('3'):
		curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/python/Log.py")
	if x == ord('4'):
		curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/python/Install.py")
        if x == ord('5'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Ps.py")
        if x == ord('6'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Packet.py")
        if x == ord('7'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Start.py")
        if x == ord('8'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/System.py")
        if x == ord('9'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Network.py")

curses.endwin()

