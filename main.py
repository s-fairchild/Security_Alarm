from threading import Thread, Event
from door import DoorMonitor
from pad import get_keypad
from oled import Oled
from time import sleep
from alarm import Alarm
from yaml import safe_load

def parse_config(config_file):
    try:
        print("Reading fand.yaml.")
        with open(config_file, 'r') as file:
            config = safe_load(file)
        print("Successfully read fand.yaml.")
        if len(config) != 0:
            return config
        else:
            raise Exception("config file loaded with 0 length, somethings wrong.")
    except Exception as e:
        print(f"Could not read fand.yaml, {e}")

if __name__ == "__main__":
    stop_event, val, config = Event(), False, parse_config('alarm.yaml')
    alarm = Alarm(Oled(height=config['oled']['height'], width=config['oled']['width']), 
            get_keypad(config['keypad']['matrix']), 
            config['secret'])
    door = DoorMonitor(alarm.disarm_alarm)
    th_doormon = Thread(target=door.monitor, args=[stop_event], daemon=True)

    while True:
        while val is False:
            val = alarm.arm_alarm()
            
        th_doormon.start()
        val = False

        while val is False:
            val = alarm.disarm_alarm("ALARM IS ARMED\nPRESS '#' TO DISARM AND ENTER PASSCODE")
            if val:
                stop_event.set()
                
        th_doormon.join()
        stop_event.clear()
