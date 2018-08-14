#!/bin/python3

from subprocess import call
from subprocess import check_output
import subprocess
import re

class Radio(object):
    def __init__(self):
        pass

    def _get_stations_from_file(self):
        stations = []
        with open("/home/alarm/.mpd/playlists/playlist.m3u",'r') as datei:
            lines = datei.readlines()
            for i in range(len(lines)):
                if i%2 == 1:
                    line = lines[i]
                    name = line.split(",")[-1]
                    stations.append(name)
        return stations

    def _get_stations_from_cmd(self):
        string = check_output(['mpc', 'playlist']).decode('utf-8')
        liste = string.splitlines()
        return liste

    def play(self, number):
        self.stop()
        call(['mpc', 'play', str(number)])
        
    ### ATTENTION ### THE PLAYLISTNAME IS HARDCODED!!    
    def update_playlist(self):
        call(['mpc', 'clear'])
        call(['mpc', 'load', 'playlist'])

    def stop(self):
        call(['mpc', 'stop'])

    def get_station_names(self):
        try:
            stations = self._get_stations_from_cmd()
        except subprocess.CalledProcessError:
            stations = self._get_stations_from_file()
        return stations
        
    def dec_volume(self):
        call(['mpc', 'volume', '-10'])

    def inc_volume(self):
        call(['mpc', 'volume', '+10'])

    def current_station_index(self):
        cmd_output_string = check_output(['mpc']).decode('utf-8')
        # The index in mpc is handled from  1- end
        match = re.search('\[playing\] \#(\d+)\/\d+', cmd_output_string)
        # The index in the above radio module is handled from 0 - (end -1)
        return int(match.group(1)) - 1

if __name__ == '__main__':
    rad = Radio()
    for station in rad.get_list():
        print(station)
