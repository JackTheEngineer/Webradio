from LCDInterface import lcd_show_text
from LCDModule import LCD
from RadioInterface import get_station_names
import datetime

def main():
    lcd = LCD()
    zeilen = []
    cleanlist = get_station_names()
    zeilen = cleanlist[0:3]
    zeilen.append(datetime.datetime.now().strftime("%d.%b.%y %H:%M"))
    lcd_show_text(lcd, zeilen)
    
if __name__ == "__main__":
    main()
