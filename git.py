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

screen = curses.initscr()

Kommentar = get_param("Lägg kommentar, exempelvis datum 2011-06-26, 1600")
system("git add .")	
system("git commit -m '" + Kommentar + "'")
system("git remote add origin git@github.com:uzix/Supertool.git")
system("git push origin master")
system("reset")
