from LCDInterface import lcd_show_text
from LCDModule import LCD
from RadioInterface import get_station_names
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

class StationView()

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

