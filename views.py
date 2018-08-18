from LCDInterface import lcd_show_text
from LCDModule import LCD
from RadioInterface import Radio
from buttons import Buttons

import datetime
import time
import functools
from copy import deepcopy

fp = functools.partial

stundengrenzen = [(2, "Aaldah, escht jetz"),
                  (5, "Guten Morgen"),
                  (12, "Einen Schoenen Mittwoch!"),
                  (17, "Guten Abend!")]
    
def begruessung(stunden, time):
    hours_24 = deepcopy(stunden)
    hours_24.append((24, stunden[0][1]))

    for index, zeit in enumerate(stunden):
        if(index == (len(stunden) - 1)):
            if(((zeit[0] <= time) and (time < hours_24[index+1][0])) or
               ((hours_24[index+1][0] > time) and (time < hours_24[0][0]))):
                return zeit[1]
        else:
            if((zeit[0] <= time) and (time < hours_24[index+1][0])):
                return zeit[1]
    return "Begruessungsfehler"


def get_shown_station_names(station_index, station_names, lines=4):
    shown_lines = []
    leng = len(station_names)
    if((station_index + lines) > leng):
        shown_lines = station_names[station_index:]
        additional = lines - (leng - station_index)
        shown_lines = shown_lines + station_names[0:additional]

    else:
        shown_lines = station_names[station_index:station_index+lines]
    return shown_lines

class StationView(object):
    def __init__(self, lcd_object):
        self.radio = Radio()
        self.active = False
        self.stationnames = self.radio.get_station_names()
        self.station_index = self.radio.current_station_index()
        self.lcd = lcd_object
        print("Current station index: %d" % self.station_index)
        

    def run_updates(self, btn_presses):
        if(self.active):
            if(btn_presses[0] == 1): # Enter 
                # Get Station Index
                self.play(self.station_index)
            if(btn_presses[1] == 1): # Center
                self.radio.stop()
            if(btn_presses[2] == 1): # Left
                # Get Station Index
                self.radio.dec_volume()
            if(btn_presses[3] == 1): # Right
                # Get Station Index
                self.radio.inc_volume()
            if(btn_presses[4] == 1): # Up
                # Increase station index, then modulo stations
                self.station_index = (self.station_index + 1) % len(self.stationnames)
                zeilen = get_shown_station_names(self.station_index, self.stationnames)
                lcd_show_text(self.lcd, zeilen)
            if(btn_presses[5] == 1): # Down
                self.station_index = (self.station_index - 1) % len(self.stationnames)
                zeilen = get_shown_station_names(self.station_index, self.stationnames)
                lcd_show_text(self.lcd, zeilen)
                
    def play(self, station_index):
        self.radio.play(station_index + 1)

            
    

def main():
    lcd = LCD()
    zeilen = ["", "", "", ""]
    zeilen[0] = datetime.datetime.now().strftime("%d.%b.%y %H:%M")
    t = int(datetime.datetime.now().strftime("%H"))
    aktuelle_begruessung = begruessung(stundengrenzen, t)
    zeilen[3] = aktuelle_begruessung
    lcd_show_text(lcd, zeilen)
    time.sleep(2)
    radio_view = StationView(lcd)
    btns = Buttons([10,15,17,27,24,9])
    radio_view.active = True
    try:
        while(True):
            time.sleep(0.05)
            radio_view.run_updates(btns.get_signals())
    except KeyboardInterrupt:
        exit

    
    
if __name__ == "__main__":
    main()

