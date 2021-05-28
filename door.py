from gpiozero import LED, Button, Buzzer
from signal import pause
from time import sleep, strftime
from threading import currentThread

class DoorMonitor:
    def __init__(self, use_oled=False):
        self.red = LED(17)
        self.green = LED(27)
        self.button = Button(18)
        self.button.hold_time = 1
        self.buzzer = Buzzer(22)
        self.buzzer.off()
        self.count = 0
        self.use_oled = use_oled
    
    def sound_alarm(self):
        self.buzzer.on()
        print(f"Alarm started at {strftime('%m-%d-%Y %H:%M:%S')}")
        while True:
            self.red.toggle()
            sleep(0.1)
        self.buzzer.off()
        self.red.off()
        print(f"Alarm ended at {strftime('%m-%d-%Y %H:%M:%S')}")

    def monitor(self, stop_event):
        try:
            while stop_event is False:
                self.red.on()
                if self.button.is_pressed is False:
                    sleep(0.1)
                else:
                    self.button.when_held = self.sound_alarm
        finally:
            self.buzzer.off()
            self.red.off()
            self.green.on()