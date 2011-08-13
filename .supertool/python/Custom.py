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
        screen.addstr(3, 4,  "a - Testa xbox360 iso", curses.color_pair(2) )
        screen.addstr(4, 4,  "b - Bränn xbox360 iso", curses.color_pair(2) )
	screen.addstr(5, 4,  "c - Chroot test-server", curses.color_pair(2) )
	screen.addstr(6, 4,  "d - Chroot pc-linux-os", curses.color_pair(2) )
	screen.addstr(7, 4,  "e - Chroot lmde", curses.color_pair(2) )
        screen.addstr(8, 4,  "f - Chroot Ubuntu", curses.color_pair(2) )
        screen.addstr(9, 4,  "g - Montera iso", curses.color_pair(2) )
        screen.addstr(10, 4, "h - Avmontera iso", curses.color_pair(2) )
        screen.addstr(11, 4, "i - Kör WifiCrack", curses.color_pair(2) )
        screen.addstr(12, 4, "j - Kör Swissknife", curses.color_pair(2) )
        screen.addstr(13, 4, "k - Förändra Prompt", curses.color_pair(2) )
	screen.addstr(14, 4, "l - Starta igång egna initscript", curses.color_pair(2) )
        screen.addstr(15, 4, "m - Göm textfil inne i bildfil, uzis inställning", curses.color_pair(2) )
        screen.addstr(16, 4, "n - Tryck om du vill öppna textfil inne i bildfil, uzis inställning", curses.color_pair(2) )
        screen.addstr(17, 4, "o - Kolla en fils attribut", curses.color_pair(2) )
        screen.addstr(18, 4, "p - Modifiera, grub lägg till en bildfil", curses.color_pair(2) )
        screen.addstr(19, 4, "r - Läs pythondokumentation", curses.color_pair(2) )
        screen.addstr(20, 4, "s - Ladda ner en youtubefilm och gör om den till en mp3-fil", curses.color_pair(2) )
        screen.addstr(21, 4, "t - Stäng av splash bootskärm, samt inaktivera uppgraderingar av grubs-config", curses.color_pair(2) )
        screen.addstr(22, 4, "y - Aktivera splash bootskärm, samt aktivera uppgraderinga av grubs-config", curses.color_pair(2) )
	screen.addstr(25, 4, "q - Huvudmenyn", curses.color_pair(1))
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		ISO = get_param("Välj isofil")
		curses.endwin()
		execute_cmd("abgx360 -af3 " + ISO)
	if x == ord('b'):
		ISO = get_param("Välj isofil")
		curses.endwin()
		execute_cmd("growisofs -use-the-force-luke=dao -use-the-force-luke=break:1913760  -dvd-compat -speed=4 -Z /dev/scd0=" + ISO)
	if x == ord('c'):	
		curses.endwin()
		execute_cmd("ssh uzi@localhost -p 8522")
        if x == ord('d'):
                curses.endwin()
                execute_cmd("rm /mnt/pc-linux-os/etc/resolv.conf")
		execute_cmd("cp -L /etc/resolv.conf /mnt/pc-linux-os/etc/resolv.conf")
                execute_cmd("mount -t devpts devpts /mnt/pc-linux-os/dev/pts")
        	execute_cmd("mount -t proc proc /mnt/pc-linux-os/proc")
		execute_cmd("chroot /mnt/pc-linux-os /bin/bash")
	if x == ord('e'):
		curses.endwin()
                execute_cmd("rm /mnt/debian/etc/resolv.conf")
                execute_cmd("cp -L /etc/resolv.conf /mnt/debian/etc/resolv.conf")
                execute_cmd("mount -t devpts devpts /mnt/debian/dev/pts")
                execute_cmd("mount -t proc proc /mnt/debian/proc")
                execute_cmd("chroot /mnt/debian /bin/bash")
        if x == ord('f'):
                curses.endwin()
                execute_cmd("rm /mnt/ubuntu/etc/resolv.conf")
                execute_cmd("cp -L /etc/resolv.conf /mnt/ubuntu/etc/resolv.conf")
                execute_cmd("mount -t devpts devpts /mnt/ubuntu/dev/pts")
                execute_cmd("mount -t proc proc /mnt/ubuntu/proc")
                execute_cmd("chroot /mnt/ubuntu /bin/bash")
        if x == ord('g'):
                Fil = get_param("Välj isofil du vill montera")
		Katalog = get_param("Välj katalog där du vill montera ison")
		curses.endwin()
                execute_cmd("mount -o loop -t iso9660 " + Fil + " " + Katalog)
        if x == ord('h'):
		Katalog = get_param("Välj katalog som du vill avmontera")
                curses.endwin()
                execute_cmd("umount -f " + Katalog)
  	if x == ord('i'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/bash/Wifi-Crack")
        if x == ord('j'):
		curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/python/Swissknife.py")
        if x == ord('k'):
               	From = get_param("Ange namnet efter @ i prompten, ex T-Server eller U-11.04")
		To = get_param("Ange ditt nya namn")
		curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/perl/prompt")
        if x == ord('l'):
	        curses.endwin()
	        execute_cmd("/etc/init.d/android-adb-server")
		execute_cmd("/etc/init.d/Custom-Script")
		execute_cmd("/etc/init.d/Chroot-Debian")
		execute_cmd("/etc/init.d/hostname.sh")
		execute_cmd("/etc/init.d/hostname-rewrite-files")
        if x == ord('m'):
		Passw = get_param("Ange ditt nya lösenord, observera du kommer ej bekräfta lösen!")
                curses.endwin()
                execute_cmd("outguess -k " + Passw + " -d /home/uzi/Bilder/noter.txt /home/uzi/Bilder/Stalker.jpg  /home/uzi/Bilder/Forever-Stalker.jpg")
		execute_cmd("rm /home/uzi/Bilder/noter.txt")
		execute_cmd("chattr +i /home/uzi/Bilder/Forever-Stalker.jpg")
	        execute_cmd("chown -R uzi /home/uzi/Bilder")
        if x == ord('n'):
		Passworld = get_param("Ange lösenord")
                curses.endwin()
		execute_cmd("chattr -i /home/uzi/Bilder/Forever-Stalker.jpg")
                execute_cmd("outguess -k " + Passworld + " -r /home/uzi/Bilder/Forever-Stalker.jpg /home/uzi/Bilder/noter.txt")
                execute_cmd("mv /home/uzi/Bilder/Forever-Stalker.jpg /home/uzi/Bilder/Stalker.jpg")
		execute_cmd("nano /home/uzi/Bilder/noter.txt")
		execute_cmd("chown -R uzi /home/uzi/Bilder")
        if x == ord('o'):
                CheckFile = get_param("Vilkens fils attribut vill du se")
                curses.endwin()
                execute_cmd("lsattr " + CheckFile)
        if x == ord('p'):
                File = get_param("Vilkens bildfil vill du använda?")
                curses.endwin()
                execute_cmd("cp " + File + " /boot/grub")
        if x == ord('r'):
                Docs = get_param("Välj programbibliotek du vill läsa om")
                curses.endwin()
                execute_cmd("pydoc " + Docs)
        if x == ord('s'):
                curses.endwin()
		execute_cmd("/usr/local/bin/.supertool/bash/youtube2mp3")
        if x == ord('t'):
		curses.endwin()
               	execute_cmd("sed 's/quiet splash/quiet/g' /boot/grub/grub.cfg > /tmp/tmp-grub.cfg")
		execute_cmd("mv /tmp/tmp-grub.cfg /boot/grub/grub.cfg")
                execute_cmd("chattr +i /boot/grub/grub.cfg")
        if x == ord('y'):
		curses.endwin()
                execute_cmd("chattr -i boot/grub/grub.cfg")
                execute_cmd("update-grub2")

curses.endwin()

