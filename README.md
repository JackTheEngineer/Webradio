# Webradio
This is the software / 
setup package for the Raspberry Pi zero as a Webradio.

## Webradio Setup
### Use PWM Audio 
Please google  "adafruit raspberry pi zero audio output" 
and build the schematic.

### Add line to /boot/config.txt
dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4

	sudo reboot

	sudo apt-get update && sudo apt-get dist-upgrade
	sudo apt-get install python3-setuptools  python3-pip python-pip

	sudo pip install RPi.GPIO
	sudo apt-get install mpc mpd alsa-utils

### Audio Output
Here the output is being set to 1, which is the headphone jack
Setting the output to 2 switches to HDMI. 
The default setting is 0 which is automatic.

	amixer cset numid=3 1	

### test audio
	aplay /usr/share/sounds/alsa/Front_Center.wav

### for changing the volume
	alsamixer 
	
### backup /etc/mpd.conf by the file in the project
	
	sudo cp /etc/mpd.conf /etc/mpd.conf.backup

### Replace it by the mpd.conf file provided by the project

### If you edited the file your own way:
To fix "mpd error: Timeout":
In the file /etc/mpd.conf within the audio_output settings, change the mixer_type to "software".

### This depends on the configuratin of the mpd.conf file
If you copied the given file, create the folders:
	
	mkdir -p /home/pi/.mpd/playlists
	mkdir -p /home/pi/music
	mkdir -p /home/pi/.mpd/playlists

And copy your playlist into the folder playlists.

    	 cp /home/pi/Webradio/playlist.m3u /home/pi/.mpd/playlists


### Enable and start mpd service
	
	sudo systemctl enable mpd.service
	sudo systemctl start mpd.service

### Layout of GPIO numbers on my specific board:

	Button | GPIO Number
	------------
	enter  | 10
	center | 15 
	left   | 17
	right  | 27
	up     | 24
	down   | 9

