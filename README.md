# Webradio with the Raspberry Pi / Raspberry Pi Zero
# Preliminary Description

This is the Setup description for the Raspberry Pi zero as a Webradio.
It uses Six buttons and one 4 line LCD display.
You can also use it for any other Raspberry Pi,
just leave out the part with the `dtoverlay=...`, and use any
desired audio output.


## Webradio Setup
## Clone the project with the Raspberry by:
If you want to use all preconfigured files, do clone the project into `/home/pi`
   
   cd /home/pi
   git clone git@github.com:JackTheEngineer/Webradio.git

### Use PWM Audio 
Please google  "adafruit raspberry pi zero audio output" 
and build the schematic. 

### Add line to /boot/config.txt,
This is done to map the Audio output to
HEADER pin 33(GPIO 13)and HEADER pin 12(GPIO 18), using PWM.

    dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4

To make this change active, reboot the system:

   sudo reboot

The Audio quality is not the very Best, but it is adequate.
My Raspberry pi sometimes makes a little buzz sound, when the load is high.
If you expect something better, you should get some Audio-HAT, and see
for yourself how to configure it.
If you wish, open an issue, so i could help you. 

### Install all required packages 

	sudo apt-get update && sudo apt-get dist-upgrade
	sudo apt-get install python3-setuptools  python3-pip python-pip

	sudo pip install RPi.GPIO
	sudo apt-get install mpc mpd alsa-utils

### Audio Output
Here the output is being set to 1, which is the headphone jack/PWM output
Setting the output to 2 switches to HDMI. 
The default setting is 0 which is automatic. (You probably don't want to use that,
but i haven't tried)

	amixer cset numid=3 1	

### test audio
	aplay /usr/share/sounds/alsa/Front_Center.wav

### for changing the volume, run
	alsamixer 
	
### backup /etc/mpd.conf by the file in the project

    sudo cp /etc/mpd.conf /etc/mpd.conf.backup

### Replace it by the mpd.conf file provided by the project

### If you edited the file your own way:
To fix "mpd error: Timeout":
In the file /etc/mpd.conf within the audio_output settings, change the mixer_type to "software".

### Important Assumption:
From here on i assume that you have cloned your project to the folder `/home/pi`

### This now depends on the configuratin of the mpd.conf file
If you copied the given file here, create the folders:
	
	mkdir -p /home/pi/music
	mkdir -p /home/pi/.mpd/playlists

And copy your playlist into the folder playlists.

    	 cp /home/pi/Webradio/playlist.m3u /home/pi/.mpd/playlists

### Enable and start mpd service
	
	sudo systemctl enable mpd.service
	sudo systemctl start mpd.service

### Test that mpc working

    mpc load playlist
    mpc play 1

This should play, depending on the contents of the playlist.m3u, BBC Radio 1 or something similar
	
### Run the Program:
Currently it is a rather simplish program that views the Radio Stations, and if you click the button,
it switches.

    python3 view.py


### Enable autostartup of the webradio python script by adding a new service:
I again provided the ready to go webradio.service file, but this will only work
if you have cloned the directory to `/home/pi`.


   	 cp /home/pi/Webradio/webradio.service /etc/systemd/system/
	 sudo systemctl enable webradio.service

### Layout of GPIO numbers on my specific board:

	Button |  HEADER Pin | GPIO Number |
	-----------------------------------
	enter  |   19	     |	10
	center |   10	     |	15 
	left   |   11	     |	17
	right  |   13	     |	27
	up     |   18	     |	24
	down   |   21	     |	9

