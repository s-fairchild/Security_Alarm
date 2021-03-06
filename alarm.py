from time import sleep, strftime
from os import popen

class Alarm:
    def __init__(self, display, keypad, secret, use_oled=False):
        self.display = display
        self.fails = 0
        self.keypad = keypad
        self.secret = secret
        self.use_oled = use_oled
    
    def make_hash(self, passcode):
        cmd = f"echo \"{passcode}\" | sha256sum"
        stream = popen(cmd)
        output = stream.readline()
        return output.replace(' ', '').replace('\n', '').replace('-', '')
    
    def check_code(self, keys):
        passcode = ""
        for key in keys:
            passcode += str(key)

        if self.secret == self.make_hash(passcode):
            return True
        else:
            if self.use_oled:
                self.display.display_text('INCORRECT PASSCODE ENTERED, TRY AGAIN.')
            sleep(2)
            self.fails += 1
            print(f"Incorrect passcode entered at {strftime('%m-%d-%Y %H:%M:%S')}")
            print(f"Incorrect passcodes total: {self.fails}")
            return False
        
    def disarm_alarm(self, text=""):
        keys = []
        #Wait for disarming code.
        self.display.self.display_text(text)
        while '#' not in keys:
            keys = self.keypad.pressed_keys
            sleep(0.1)
        keys.clear()
        while '*' not in keys:
            if self.use_oled:
                self.display.self.display_text(f"Press * for enter\nPASSCODE: {len(keys) * '*'}")
            keys = self.keypad.pressed_keys
            sleep(0.1)
        
        return self.check_code(keys)

    def arm_alarm(self):
        keys = []
        if self.use_oled:
            self.display.display_text("Press \"#\" key to arm alarm.")
        while '#' not in keys:
            keys = self.keypad.pressed_keys
            sleep(0.1)

        return self.check_code(keys)