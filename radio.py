from copy import deepcopy
import buttons as btns
        

class Controller(object):
    def __init__(self, views):
        self.buttons = btns.Buttons([10,15,17,27,24,9])
        self.views = views

    def run_updates(self):
        signals = self.buttons.get_signals()
        for view in views:
            if(view.active):
                view.run_updates(signals)

    def disable_all_views():
        for view in views
            view.active = False

def main():
    lcd = LCD()
    zeilen = []
    cleanlist = get_station_names()
    print(cleanlist)
    zeilen = cleanlist[0:3]
    zeilen.append(datetime.datetime.now().strftime("%d.%b.%y %H:%M"))
    t = int(datetime.datetime.now().strftime("%H"))
    aktuelle_begruessung = begruessung(stundengrenzen, t)
    zeilen[3] = aktuelle_begruessung
    lcd_show_text(lcd, zeilen)
    
if __name__ == "__main__":
    main()
