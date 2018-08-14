import time

class Buttons(object):
    def __init__(self, btn_list, GPIO=None):
        self.btn_list = btn_list
        self.last_pressed = [0] * len(btn_list)
        self.pressed = [0] * len(btn_list)
        

        if not GPIO:
            import RPi.GPIO as GPIO
            GPIO.setwarnings(False)
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)

        for btn in btn_list:
            self.GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def get_signals(self):
        current = []

        # A "not x" operation can be implemented as (x-1)**2
        # I used this, because the switch was pressed all the time, and released
        # whenever the button was pressed 
        current.append((self.GPIO.input(self.btn_list[0]) - 1)**2)
        
        for i, btn in enumerate(self.btn_list[1:]):
            current.append(self.GPIO.input(btn))

        for i, press in enumerate(current):
            if((self.last_pressed[i] == 0) and (press==1)):
                self.pressed[i] = 1
            else:
                self.pressed[i] = 0
            self.last_pressed[i] = press

        return self.pressed

def main():
    btns = Buttons([10,15,17,27,24,9])
    try:
        while(True):
            time.sleep(0.05)
            print(btns.get_signals())
    except KeyboardInterrupt:
        exit


            
if __name__ ==  "__main__":
    main()
