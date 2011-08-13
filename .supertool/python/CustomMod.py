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
      	screen = curses.initscr()
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

def execute_cmd_silent(cmd_string):
        a = system(cmd_string)
        print ""
        if a == 0:
                print " "
        else:
                print " "
        print ""

