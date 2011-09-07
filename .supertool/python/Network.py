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
        screen.addstr(3, 4,  "a - Kolla vilka ipadresser systemet har", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Portscanna hela ditt lokala nätverk", curses.color_pair(2) )
        screen.addstr(5, 4,  "c - Kolla vilka internettjänster som körs", curses.color_pair(2) )
        screen.addstr(6, 4,  "d - Analysera omkringliggande nätverk", curses.color_pair(2) )
        screen.addstr(7, 4,  "e - Analysera nätverksaktiviter", curses.color_pair(2) )
        screen.addstr(8, 4,  "f - Kringgå brandvägg delvis, starta en krypterad sshtunnel. Inställningar program 127.0.0.1:Porten", curses.color_pair(2) )
        screen.addstr(9, 4,  "g - Kringgå brandvägg helt, starta en krypterad omvänd sshtunnel", curses.color_pair(2) )
        screen.addstr(10, 4, "h - Kolla upp en servers ipadress", curses.color_pair(2) )
        screen.addstr(11, 4, "i - Kolla upp en ipadress", curses.color_pair(2) )
        screen.addstr(12, 4, "j - Ladda ner en fil", curses.color_pair(2) )
        screen.addstr(13, 4, "k - Ladda ner en hel hemsida, inklusive undersidor", curses.color_pair(2) )
        screen.addstr(14, 4, "l - Ladda upp en fil til en ftp-server", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
                execute_cmd("ifconfig -a")
        if x == ord('b'):
             	Lokalip = get_param("Ange ditt ip nummers serie, exempelvis 192.168.0 eller 192.168.1")
                curses.endwin()
                execute_cmd("nmap " + Lokalip +".*")
        if x == ord('c'):
                curses.endwin()
                execute_cmd("lsof -i | less")
        if x == ord('d'):
                curses.endwin()
                execute_cmd("kismet")
        if x == ord('e'):
                curses.endwin()
                execute_cmd("iptraf | less")
		execute_cmd("netstat | less")
 		execute_cmd("wireshark")
        if x == ord('f'):
		#Kodat efter att ha läst denna guide http://wiki.linuxportalen.se/index.php/SSH_genom_brandvägg
                Port = get_param("Ange den port du vill använda")
                User = get_param("Ange användare som ska logga in på ssh-servern")
                Host = get_param("Ange ipnummer eller värdadress till ssh-servern")
                curses.endwin()
                execute_cmd("ssh -N -D " + Port +" " + User + "@" + Host)
        if x == ord('g'):
		#Kodat efter att ha läst denna guide http://wiki.linuxportalen.se/index.php/SSH_genom_brandvägg
                Remoteport = get_param("Ange fjärrport du vill använda")
		Localport = get_param("Ange lokal port du vill kringgå")
                User = get_param("Ange användare som ska logga in på ssh-servern")
                Host = get_param("Ange ipnummer eller värdadress till ssh-servern")
                curses.endwin()
                execute_cmd("ssh -R " + Remoteport + ":localhost:" + Localport + " " + User + "@" + Host + " /usr/local/bin/.supertool/bash/kick.sh")
        if x == ord('h'):
                Url = get_param("Ange Url till servern, exempel www.exempel.com")
                curses.endwin()
                execute_cmd("nslookup " + Url)
        if x == ord('i'):
                Ip = get_param("Ange ipadressen du vill kolla upp")
                curses.endwin()
                execute_cmd("whois " + Url)
        if x == ord('j'):
                File = get_param("Ange url till filen du vill ladda ner")
                curses.endwin()
                execute_cmd("wget " + File)
        if x == ord('k'):
                Homepage = get_param("Ange hemside adress")
                curses.endwin()
                execute_cmd("wget -r " + Homepage)
        if x == ord('l'):
                User = get_param("Ange ditt användarnamn")
                Passworld = get_param("Ange ditt lösenord")
                Server = get_param("Ange vilken ftp-server du vill ladda upp en fil till")
		Fil = get_param("Ange vilken fil du vill ladda upp")
                curses.endwin()
                execute_cmd(" ")

curses.endwin()

