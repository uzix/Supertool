#Settings set by Uzi below, other distributions then ubuntu use /etc/profile
	BL="\[\033[0;34m\]"
	txtblk='\e[0;30m' # Black - Regular
	txtblu='\e[0;34m' # Blue
	bldwht='\e[1;37m' # White
	bldylw='\e[1;33m' # Yellow
	bldblk='\e[1;30m' # Black - Bold
	txtcyn='\e[0;36m' # Cyan
	txtgrn='\e[0;32m' # Green
	txtred='\e[0;31m' # Red
	HISTCONTROL=ignoredups:ignorespace
	HISTSIZE=1000
	HISTFILESIZE=2000
	[ -z "$PS1" ] && return
	shopt -s histappend
	shopt -s checkwinsize
	[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
	export DISPLAY=:0.0
       	export PS1="\[$txtblu\u@T-Server\]\[$bldwht \w\]\[$txtgrn \A\]\n "
	export PATH=$PATH:/android/android-sdk-linux_x86/platform-tools:/android/android-sdk-linux_x86/tools
	export CHROOT=/var/chroot/Debian
	export LFS=/var/chroot/lfs
	export ISO=/home/uzi/Extended/iso
#Alias
alias android-shell-root='/etc/init.d/android-adb-server start && /android/android-sdk-linux_x86/platform-tools/adb shell'
	alias android-shell='/android/android-sdk-linux_x86/platform-tools/adb shell'
	alias android-shell-script='/android/android-sdk-linux_x86/platform-tools/adb shell am'
	alias android-copy-to='/android/android-sdk-linux_x86/platform-tools/adb push'
	alias android-copy-from='/android/android-sdk-linux_x86/platform-tools/adb pull'
	alias ls='ls --color=auto'
	alias N900='ssh -X root@192.168.2.15 -p 8256'
	alias Test-Server='ssh uzi@localhost -p 8522'
#Strange syntax errors from time to time! 
