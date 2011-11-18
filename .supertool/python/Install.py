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
        screen.addstr(3, 4,  "a - Installera standardprogramvara", curses.color_pair(2) )
       	screen.addstr(4, 4,  "b - Installera startscript, tweaks samt egna konfigurationsfiler", curses.color_pair(2) )
 	screen.addstr(5, 4,  "c - Bygg en chrootad test-server", curses.color_pair(2) )
	screen.addstr(6, 4,  "d - Förändra root-lösenord test-server", curses.color_pair(2) )
        screen.addstr(7, 4,  "e - Lägg till användare test-server", curses.color_pair(2) )
        screen.addstr(8, 4,  "f - Förändra standardport för ssh-inloggningar, samt stäng av root-inloggning test-server", curses.color_pair(2) )
       	screen.addstr(9, 4,  "g - Förändra teckenupsättning på test-server, 379 sv_SE.UTF-8 för svenska tecken", curses.color_pair(2) )
	screen.addstr(10, 4, "h - Ta bort användare test-server", curses.color_pair(2) )
        screen.addstr(11, 4, "i - Kolla om ssh-tjänsten är igång och på vilken port", curses.color_pair(2) )
        screen.addstr(12, 4, "j - Lägg till spotify i ditt befintliga repo samt installera det", curses.color_pair(2) )
        screen.addstr(13, 4, "k - Ställ in så det fungerar att kolla temperaturen på hårdvaran, svara ja på alla frågor", curses.color_pair(2) )
        screen.addstr(14, 4, "l - Förändra display i bash.bashrc om du installerat mina tweaks och konfiguration, för att tillåta grafisk ssh", curses.color_pair(2) )
        screen.addstr(15, 4, "m - Förändra din prompt, om det står T-Server efter @ till valfritt namn", curses.color_pair(2) )
        screen.addstr(16, 4, "n - Förändra din prompt, nya namet som står efter @ till valfritt namn", curses.color_pair(2) )
        screen.addstr(17, 4, "o - Installera lubuntu-specifika tweaks, samt modifiera systemet efter egna behov, uzi användare", curses.color_pair(2) )
        screen.addstr(18, 4, "p - Skapa en skräddarsydd Ubuntu-Debian-remaster", curses.color_pair(2) )
        screen.addstr(19, 4, "r - Ta backup på systemet", curses.color_pair(2) )
        screen.addstr(20, 4, "s - Återställ backup", curses.color_pair(2) )
        screen.addstr(21, 4, "t - Modifiera din skräddarsydda Ubuntu-Debian-remaster", curses.color_pair(2) )
        screen.addstr(22, 4, "y - Installera repository för spel i ubuntu", curses.color_pair(2) )	
        screen.addstr(23, 4, "v - Installera mediabuntus repository i ubuntu", curses.color_pair(2) )
        screen.addstr(24, 4, "w - Ta backup på Pidgin, firefox samt thunderbird", curses.color_pair(2) )
        screen.addstr(25, 4, "x - Installera samt konfigurera metasploit", curses.color_pair(2) )
	screen.addstr(26, 4, "q - Huvudmeny", curses.color_pair(1) )
	screen.refresh()

	x = screen.getch()

	if x == ord('a'):
		curses.endwin()
                execute_cmd_silent("apt-get update")
                execute_cmd("apt-get install fbreader gpm python-tk python-easygui git-core git-gui git-doc youtube-dl ffmpeg lame whois squashfs-tools genisoimage unetbootin outguess kompozer avidemux gparted gimp xchat gftp  build-essential firefox linux-headers-generic gcc make thunderbird smartmontools tor polipo vidalia nmap kismet dchroot debootstrap lm-sensors growisofs dvd+rw-tools ntpdate aumix lsof less sensors-applet wine eclipse rkhunter")
        if x == ord('b'):
                curses.endwin()
                execute_cmd_silent("chattr +i /etc/bash.bashrc")
                execute_cmd_silent("cp -R -L /usr/local/bin/.supertool/etc /")
                StartScript = raw_input("Vill du aktivera scripten automatiskt vid nästa systemstart ja/nej ")
                if StartScript == ('ja'):
			execute_cmd_silent("update-rc.d hostname.sh start 02 S .")
			execute_cmd_silent("update-rc.d hostname-rewrite-files start 36 S .")
			execute_cmd_silent("update-rc.d Chroot-Debian defaults")
			execute_cmd_silent("update-rc.d Custom-Script defaults")
			execute_cmd("update-rc.d android-adb-server defaults")
		if StartScript == ('nej'):
			execute_cmd(" ")
                Bashrc = raw_input("Varning, vill du använda min /etc/bash.bashrc")
                if Bashrc == ('ja'):
                        execute_cmd_silent("chattr -i /etc/bash.bashrc")
                        execute_cmd_silent("cp -R -L /usr/local/bin/.supertool/etc/bash.bashrc /etc")
                if Bashrc == ('nej'):
                        execute_cmd("chattr -i /etc/bash.bashrc")
        if x == ord('c'):
                curses.endwin()
                execute_cmd_silent("mkdir -p /var/chroot/Debian")
		execute_cmd_silent("debootstrap --variant=buildd --arch i386 squeeze /var/chroot/Debian/ http://ftp.se.debian.org/debian")
		execute_cmd_silent("mkdir -p /var/chroot/Debian")
		execute_cmd_silent("mount -t proc proc /var/chroot/Debian/proc")
		execute_cmd_silent("mount -t devpts devpts /var/chroot/Debian/dev/pts")
		execute_cmd_silent("CHROOT=/var/chroot/Debian")
                execute_cmd_silent("chroot  $CHROOT apt-get update")
 		execute_cmd_silent("chroot  $CHROOT apt-get install -y nano locales mysql-server mysql-client apache2 php5 libapache2-mod-php5 phpmyadmin perl libapache2-mod-perl2 python libapache2-mod-python ssh")		
		execute_cmd_silent("chroot  $CHROOT rm /etc/locales.gen")
		execute_cmd_silent("cp -L -R /usr/local/bin/.supertool/var/chroot/Debian /var/chroot/Debian/")
		execute_cmd_silent("chroot  $CHROOT /usr/sbin/locale-gen")
		execute_cmd_silent("chroot  $CHROOT apt-get upgrade")
		execute_cmd_silent("chroot  $CHROOT apt-get dist-upgrade")
		execute_cmd_silent("cp -L /usr/local/bin/.supertool/etc/init.d/Chroot-Debian /etc/init.d")
		execute_cmd_silent("/etc/init.d/Chroot-Debian start")
		execute_cmd("update-rc.d Chroot-Debian defaults")
        if x == ord('d'):
                curses.endwin()
                execute_cmd("chroot  $CHROOT passwd root")
        if x == ord('e'):
		User = get_param("Välj användare du vill skapa")
                curses.endwin()
                execute_cmd("chroot  $CHROOT adduser " + User)
        if x == ord('f'):
		From = get_param("Ändra nuvarande port från,exempelvis port 22")
                To = get_param("Till följande port")
                curses.endwin()
                execute_cmd("sed 's/PermitRootLogin yes/PermitRootLogin no/g' /var/chroot/Debian/etc/ssh/sshd_config > /tmp/tmp-sshd_config")
		execute_cmd("mv /tmp/tmp-sshd_config /var/chroot/Debian/etc/ssh/sshd_config")
		execute_cmd("sed 's/Port " + From + "/Port " + To + "/g' /var/chroot/Debian/etc/ssh/sshd_config > /tmp/tmp-sshd_config")
		execute_cmd("mv /tmp/tmp-sshd_config /var/chroot/Debian/etc/ssh/sshd_config")
		execute_cmd("chroot  $CHROOT /etc/init.d/ssh restart")
        if x == ord('g'):
                curses.endwin()
                execute_cmd("chroot  $CHROOT dpkg-reconfigure locales")
        if x == ord('h'):
                User = get_param("Välj användarnamn")
                curses.endwin()
                execute_cmd("chroot  $CHROOT deluser " + User)
        if x == ord('i'):
                curses.endwin()
                execute_cmd("lsof -i | grep sshd")
        if x == ord('j'):
                curses.endwin()
                execute_cmd_silent("sed '$ a deb http://repository.spotify.com stable non-free' /etc/apt/sources.list > /tmp/tmp-spotify")
                execute_cmd_silent("mv /tmp/tmp-spotify /etc/apt/sources.list")
                execute_cmd_silent("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4E9CFF4E")               
		execute_cmd_silent("apt-get update")
                execute_cmd("apt-get install spotify-client-qt spotify-client-gnome-support")
        if x == ord('k'):
                curses.endwin()
                execute_cmd("sensors-detect")
        if x == ord('l'):
                curses.endwin()
                execute_cmd("sed 's/export DISPLAY=:0.0/export DISPLAY/g' /etc/bash.bashrc > /tmp/tmp-display")
                execute_cmd("mv /tmp/tmp-display /etc/bash.bashrc")
		execute_cmd("sed '$ a xhost +' /etc/bash.bashrc > /tmp/tmp-display")
                execute_cmd("mv /tmp/tmp-display /etc/bash.bashrc")
        if x == ord('m'):
		Prompt = get_param("Välj ditt nya prompt namn")
                curses.endwin()
                execute_cmd("sed 's/T-Server/" + Prompt + "/g' /etc/bash.bashrc > /tmp/tmp-display")
                execute_cmd("mv /tmp/tmp-display /etc/bash.bashrc")
        if x == ord('n'):
		From = get_param("Skriv in ditt gamla prompt namn, namnet efter @")
                To = get_param("Välj ditt nya prompt namn")
                curses.endwin()
                execute_cmd("sed 's/" + From + "/" + To + "/g' /etc/bash.bashrc > /tmp/tmp-display")
                execute_cmd("mv /tmp/tmp-display /etc/bash.bashrc")
        if x == ord('o'):
                curses.endwin()
                execute_cmd("apt-get install xscreensaver-data-extra xscreensaver-gl-extra  aircrack-ng lubuntu-restricted-addons lubuntu-restricted-extras")
		Wifi = raw_input("Installera wlan ja/nej ")
                if Wifi == ('ja'):
                	execute_cmd_silent("cd /home/uzi/Wireless")
                	execute_cmd_silent("make")
                	execute_cmd_silent("make install")
			execute_cmd_silent("make unload")
			execute_cmd_silent("modprobe ath9k")	
			execute_cmd("modinfo ath9k")
		if Wifi == ('nej'):
			execute_cmd_silent(" ")
        if x == ord('p'):
		Custom = get_param("Välj vad du ska döpa din remaster till")
		Based = get_param("Välj kodnamnet för den distribution din remaster baseras på, exempelvis natty")
                curses.endwin()
		# Coded after reading, guide at https://help.ubuntu.com/community/LiveCDCustomizationFromScratch
                execute_cmd_silent("mkdir -p /var/chroot/" + Custom)
                execute_cmd_silent("debootstrap --arch=i386 " + Based + " /var/chroot/" + Custom )
	       	execute_cmd_silent("mount --bind /dev /var/chroot/" + Custom + "/dev ")
		execute_cmd_silent("cp /etc/hosts /var/chroot/" + Custom + "/etc/hosts")
                execute_cmd_silent("cp /etc/resolv.conf /var/chroot/" + Custom + "/etc")
                execute_cmd_silent("cp /etc/apt/sources.list /var/chroot/" + Custom + "/etc/apt")
 		execute_cmd_silent("Chrootlive=/var/chroot/" + Custom)
                execute_cmd_silent("chroot $Chrootlive mount none -t proc /proc")
                execute_cmd_silent("chroot $Chrootlive mount none -t sysfs /sys")
                execute_cmd_silent("chroot $Chrootlive mount none -t devpts /dev/pts")
#               execute_cmd("chroot $Chrootlive export HOME=/root")
#               execute_cmd("chroot $Chrootlive export LC_ALL=C")
		execute_cmd_silent("chroot $Chrootlive apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3E5C1192")
		execute_cmd_silent("chroot $Chrootlive apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4E9CFF4E")
		execute_cmd_silent("chroot $Chrootlive apt-get update")
	        execute_cmd_silent("chroot $Chrootlive apt-get install --yes dbus")
                execute_cmd_silent("chroot $Chrootlive dbus-uuidgen > /var/lib/dbus/machine-id")
		execute_cmd_silent("chroot $Chrootlive dpkg-divert --local --rename --add /sbin/initctl")
                execute_cmd_silent("chroot $Chrootlive apt-get install --yes locales language-pack-sv language-pack-sv-base firefox-locale-sv")
                execute_cmd_silent("cp /usr/local/bin/.supertool/var/chroot/Debian/etc/locale.gen /var/chroot/" + Custom + "/etc/")
                execute_cmd_silent("chroot $Chrootlive /usr/sbin/locale-gen")
#               execute_cmd("chroot $Chrootlive dpkg-reconfigure locales")
                execute_cmd_silent("chroot $Chrootlive apt-get --yes upgrade")
		execute_cmd_silent("chroot $Chrootlive apt-get install --yes ubuntu-standard casper lupin-casper discover laptop-detect os-prober linux-generic grub2 plymouth-x11 ubiquity-frontend-debconf")
                Version = raw_input("Vilken version av ubuntu vill du ha lubuntu/ubuntu/kubuntu/xubuntu ")
                if Version == ('lubuntu'):
			execute_cmd_silent("chroot $Chrootlive apt-get install --yes squashfs-tools genisoimage unetbootin outguess kompozer avidemux gparted gimp xchat gftp  build-essential firefox linux-headers-generic gcc make thunderbird smartmontools tor polipo vidalia nmap kismet dchroot debootstrap lm-sensors growisofs dvd+rw-tools ntpdate aumix lsof less sensors-applet wine eclipse rkhunter aircrack-ng lubuntu-restricted-addons lubuntu-restricted-extras lubuntu-default-settings lubuntu-desktop lubuntu-icon-theme lubuntu-artwork spotify-client-qt spotify-client-gnome-support")
		if Version == ('ubuntu'):
			execute_cmd_silent("chroot $Chrootlive apt-get install --yes squashfs-tools genisoimage unetbootin outguess kompozer avidemux gparted gimp xchat gftp  build-essential firefox linux-headers-generic gcc make thunderbird smartmontools tor polipo vidalia nmap kismet dchroot debootstrap lm-sensors growisofs dvd+rw-tools ntpdate aumix lsof less sensors-applet wine eclipse rkhunter aircrack-ng ubuntu-restricted-addons ubuntu-restricted-extras ubuntu-default-settings ubuntu-desktop ubuntu-icon-theme ubuntu-artwork spotify-client-qt spotify-client-gnome-support")
#		if Version == ('kubuntu')
#			execute_cmd_silent("chroot $Chrootlive apt-get install --yes squashfs-tools genisoimage unetbootin outguess kompozer avidemux gparted gimp xchat gftp  build-essential firefox linux-headers-generic gcc make thunderbird smartmontools tor polipo vidalia nmap kismet dchroot debootstrap lm-sensors growisofs dvd+rw-tools ntpdate aumix lsof less sensors-applet wine eclipse rkhunter aircrack-ng kubuntu-restricted-addons kubuntu-restricted-extras kubuntu-default-settings kubuntu-desktop kubuntu-icon-theme kubuntu-artwork spotify-client-qt spotify-client-gnome-support")
#		if Version == ('xubuntu')
#			execute_cmd_silent("chroot $Chrootlive apt-get install --yes squashfs-tools genisoimage unetbootin outguess kompozer avidemux gparted gimp xchat gftp  build-essential firefox linux-headers-generic gcc make thunderbird smartmontools tor polipo vidalia nmap kismet dchroot debootstrap lm-sensors growisofs dvd+rw-tools ntpdate aumix lsof less sensors-applet wine eclipse rkhunter aircrack-ng xubuntu-restricted-addons xubuntu-restricted-extras xubuntu-default-settings xubuntu-desktop xubuntu-icon-theme xubuntu-artwork spotify-client-qt spotify-client-gnome-support")
                execute_cmd_silent("cp -R -L /usr/local/bin/.supertool $Chrootlive/usr/local/bin")
                execute_cmd_silent("cp -R -L /usr/local/bin/Supertool.py $Chrootlive/usr/local/bin")
                execute_cmd_silent("chroot $Chrootlive Supertool.py")
                execute_cmd_silent("chroot $Chrootlive rm /var/lib/dbus/machine-id")
                execute_cmd_silent("chroot $Chrootlive rm /sbin/initctl")
                execute_cmd_silent("chroot $Chrootlive dpkg-divert --rename --remove /sbin/initctl")
                execute_cmd_silent("chroot $Chrootlive apt-get clean")
                execute_cmd_silent("chroot $Chrootlive rm -rf /tmp/*")
                execute_cmd_silent("chroot $Chrootlive rm /etc/resolv.conf")
                execute_cmd_silent("chroot $Chrootlive umount -lf /proc")
                execute_cmd_silent("chroot $Chrootlive umount -lf /sys")
                execute_cmd_silent("chroot $Chrootlive umount -lf /dev/pts")
                execute_cmd_silent("umount $Chrootlive/dev")
		execute_cmd_silent("apt-get install syslinux squashfs-tools genisoimage sbm netpbm")
                execute_cmd_silent("mkdir -p /opt/image/{casper,isolinux,install}")
		execute_cmd_silent("cp $Chrootlive/boot/vmlinuz-2.6.**-**-generic /opt/image/casper/vmlinuz")
 		execute_cmd_silent("cp $Chrootlive/boot/initrd.img-2.6.**-**-generic /opt/image/casper/initrd.gz ")
		execute_cmd_silent("cp /usr/lib/syslinux/isolinux.bin /opt/image/isolinux/")
                execute_cmd_silent("cp /boot/memtest86+.bin /opt/image/install/memtest")
                execute_cmd_silent("cp /boot/sbm.img /opt/image/install/")
                execute_cmd_silent("cp /usr/local/bin/.supertool/opt/image/isolinux/isolinux.txt /opt/image/isolinux/")
                execute_cmd_silent("cp /usr/local/bin/.supertool/opt/image/isolinux/isolinux.cfg /opt/image/isolinux/")
                execute_cmd_silent("chroot $Chrootlive dpkg-query -W --showformat='${Package} ${Version}\n' | tee /opt/image/casper/filesystem.manifest")
                execute_cmd_silent("cp -v /opt/image/casper/filesystem.manifest /opt/image/casper/filesystem.manifest-desktop")
                execute_cmd_silent("/usr/local/bin/.supertool/bash/Remove")
                execute_cmd_silent("mksquashfs $Chrootlive /opt/image/casper/filesystem.squashfs")
                execute_cmd_silent("printf $(sudo du -sx --block-size=1 chroot | cut -f1) > /opt/image/casper/filesystem.size")
                execute_cmd_silent("cp /usr/local/bin/.supertool/opt/image/README.diskdefines /opt/image")
                execute_cmd_silent("mkdir /opt/image/.disk")
                execute_cmd_silent("/usr/local/bin/.supertool/bash/ubuntu-remaster")
                execute_cmd_silent("/usr/local/bin/.supertool/bash/ubuntu-remaster-md5")
		execute_cmd("/usr/local/bin/.supertool/bash/make-ubuntu-remaster")
        if x == ord('r'):
                curses.endwin()
                execute_cmd_silent("cp -R -L /home/uzi/.android /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.eclipse /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.gftp /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.local /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.mozilla /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.Skype /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.thunderbird /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.uplink /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/.xchat2 /home/uzi/Extended/Backup/home/uzi")
                execute_cmd_silent("cp -R -L /home/uzi/.ssh /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/Bilder /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/Dokument /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/IDEOS /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/scripts /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/Xbox /home/uzi/Extended/Backup/home/uzi")
                execute_cmd_silent("cp -R -L /home/uzi/Supertool /home/uzi/Extended/Backup/home/uzi")
		execute_cmd_silent("cp -R -L /home/uzi/Wireless /home/uzi/Extended/Backup/home/uzi")
                execute_cmd_silent("cp -R -L /home/uzi/Video /home/uzi/Extended/Backup/home/uzi")
                execute_cmd_silent("cp -R -L /home/uzi/Hämtningar /home/uzi/Extended/Backup/home/uzi")
                execute_cmd_silent("cp -R -L /usr/local/bin /home/uzi/Extended/Backup/usr/local")
                execute_cmd_silent("cp -R -L /etc/fstab /home/uzi/Extended/Backup/etc")
                execute_cmd_silent("cp -R -L /android /home/uzi/Extended/Backup")
		execute_cmd_silent("cp -R -L /var/chroot/Debian/var/www /home/uzi/Extended/Backup/var/chroot/Debian/var/www")
                execute_cmd("chown -R uzi /home/uzi")
        if x == ord('s'):
                curses.endwin()
                execute_cmd_silent("cp -L /home/uzi/Extended/Backup/usr/share/backgrounds/spiderweb.jpg /usr/share/backgrounds")
                execute_cmd_silent("cp -L /home/uzi/Extended/Backup/usr/share/lubuntu/images/uzi.png /usr/share/lubuntu/images")
                execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/home/uzi /home")
                execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/home/uzi/.bashrc /root")
		execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/android /")
                execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/usr /")
                execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/var /")
                execute_cmd_silent("cp -R -L /home/uzi/Extended/Backup/opt /")
                execute_cmd("chown -R uzi /home/uzi")
        if x == ord('t'):
                curses.endwin()
                execute_cmd("/usr/local/bin/.supertool/python/Remaster.py")
        if x == ord('y'):
                curses.endwin()
		UbuntuVersion = raw_input("Vilken version av ubuntu vill du installera spel för, exempelvis maverick/lucid/natty ")
                execute_cmd_silent("sed '$ a deb http://archive.getdeb.net/ubuntu " + UbuntuVersion + "-getdeb games' /etc/apt/sources.list > /tmp/tmp-spel")
                execute_cmd_silent("mv /tmp/tmp-spel /etc/apt/sources.list")
                execute_cmd("wget -q -O- http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -")
        if x == ord('v'):
                curses.endwin()
		UbuntuVersion = raw_input("Vilken version av ubuntu vill du installera mediubuntu för, exempelvis maverick/lucid/natty ")
                execute_cmd_silent("sed '$ a deb http://packages.medibuntu.org/ " + UbuntuVersion + " free non-free' /etc/apt/sources.list > /tmp/tmp-mediubuntu")
                execute_cmd_silent("mv /tmp/tmp-mediubuntu /etc/apt/sources.list")
                execute_cmd("wget -q -O- http://packages.medibuntu.org/medibuntu-key.gpg | sudo apt-key add -")
        if x == ord('w'):
                curses.endwin()
		execute_cmd_silent("cp -R -L /home/uzi/.mozilla /home/uzi/Extended/Backup/home/uzi")                
                execute_cmd_silent("cp -R -L /home/uzi/.purple /home/uzi/Extended/Backup/home/uzi")
                execute_cmd("cp -R -L /home/uzi/.thunderbird /home/uzi/Extended/Backup/home/uzi")
        if x == ord('x'):
                curses.endwin() # Info about installation on https://community.rapid7.com/docs/DOC-1296
                execute_cmd("apt-get install apt-get install ruby libopenssl-ruby libyaml-ruby libdl-ruby libiconv-ruby libreadline-ruby irb ri rubygems subversion build-essential ruby-dev libpcap-dev")
                execute_cmd_silent("wget -P /tmp http://downloads.metasploit.com/data/releases/framework-latest.tar.bz2")
                execute_cmd_silent("mv /tmp/framework-latest.tar.bz2 /opt")
                execute_cmd_silent("tar -xvf /opt/framework-latest.tar.bz2")               
                execute_cmd_silent("chown root:root -R /opt/msf")
                execute_cmd_silent("ln -sf /opt/msf/msf* /usr/local/bin/")

curses.endwin()
