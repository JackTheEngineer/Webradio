from LCDInterface import lcd_show_text
from LCDModule import LCD
from RadioInterface import Radio
import datetime
import time
import functools

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


def get_shown_station_names(station_index, station_names):
    
    
    

class StationView(object):
    def __init__(self, lcd_object):
        self.radio = Radio()
        self.active = False
        self.stationnames = get_station_names()
        self.station_index = self.radio.current_station_index()

    def run_updates(self, btn_presses):
        if(self.active):
            if(btn_presses[0] == 1): # Enter 
                # Get Station Index
                self.radio.play(self.station_index + 1)
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
                self.station_index = (self.station_index + 1) % len(self.station_names)
                zeilen = get_shown_station_names(self.station_index, self.station_names)
                lcd_show_text(lcd, zeilen)
            if(btn_presses[5] == 1): # Down
                self.station_index = (self.station_index - 1) % len(self.station_names)
                zeilen = get_shown_station_names(self.station_index, self.station_names)
                lcd_show_text(lcd, zeilen)
                
    def play(self, station_index):
        self.radio.play(station_index + 1)

            
    

def main():
    lcd = LCD()
    zeilen = []
    cleanlist = get_station_names()
    zeilen = cleanlist[0:3]
    zeilen.append(datetime.datetime.now().strftime("%d.%b.%y %H:%M"))
#    t = int(datetime.datetime.now().strftime("%H"))
#    aktuelle_begruessung = begruessung(stundengrenzen, t)
#    zeilen[3] = aktuelle_begruessung
    lcd_show_text(lcd, zeilen)
    
if __name__ == "__main__":
    main()

