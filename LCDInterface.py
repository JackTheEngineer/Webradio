from LCDModule import LCD
import time

def lcd_show_text(lcd, strings, alle_shifts=(0, 0, 0, 0)):
    lcd.clear()

    newstrings = []
    for i in range(4 - len(strings)):
        strings.append("")

    # Uber jede Zeile 
    for zeilen_idx in range(4):

        aktuelle_zeile = strings[zeilen_idx]
        zeilenlaenge = len(aktuelle_zeile)
        zeile_shift = alle_shifts[zeilen_idx]

        newstring = aktuelle_zeile[zeile_shift :  16+zeile_shift]
        newstring = (newstring + " "*(16 - zeilenlaenge))
        newstrings.append(newstring)
    
    firstline = "".join([newstrings[0], newstrings[2]])
    secondline = "".join([newstrings[1], newstrings[3]])

    lcd.message(firstline)
    lcd.message("\n")
    lcd.message(secondline)



def main():
    four_strings = ["Guten Morgen", "Julia", "und Jakov"]
    lcd = LCD()
    lcd_show_text(lcd, four_strings, (0,0,0,0))
    time.sleep(2)
    four_strings = ["Guten Morgen ihr sportskanonen",
                    "Julia mein lieber Schatz",
                    "und Jakov der programmierer",
                    "Ich wunsche euch einen tollen Tag !!!"]
    lcd_show_text(lcd, four_strings, (0,0,0,0))
    time.sleep(2)

    for i in range(len(four_strings[3]) - 15):
        lcd_show_text(lcd, four_strings, (2,4,2,i))
        time.sleep(0.1)

if __name__ == "__main__":
    main()
