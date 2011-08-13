#!/bin/bash

	cp -L Supertool.py /usr/local/bin/
	cp -R -L .supertool/ /usr/local/bin/
        cp -L Supertool.py /var/chroot/Debian/usr/local/bin/
        cp -R -L .supertool/ /var/chroot/Debian/usr/local/bin/

	cp -L Supertool.py /mnt/Debian/usr/local/bin/
	cp -R -L .supertool/ /mnt/Debian/usr/local/bin/
        cp -L Supertool.py /mnt/Debian//var/chroot/Debian/usr/local/bin/
        cp -R -L .supertool/ /mnt/Debian//var/chroot/Debian/usr/local/bin/

	cp -L Supertool.py /mnt/kubuntu/usr/local/bin/
	cp -R -L .supertool/ /mnt/kubuntu/usr/local/bin/
        cp -L Supertool.py /mnt/kubuntu/var/chroot/Debian/usr/local/bin/
        cp -R -L .supertool/ /mnt/kubuntu/var/chroot/Debian/usr/local/bin/

        cp -L Supertool.py /mnt/lubuntu-SD/usr/local/bin/
        cp -R -L .supertool/ /mnt/lubuntu-SD/usr/local/bin/

