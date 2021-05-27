from board import SCL, SDA
import busio, adafruit_ssd1306
from subprocess import Popen, PIPE
from time import strftime

I2C = busio.I2C(SCL, SDA)
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

class Oled:
    def __init__(self, height=128, width=64):
        self.height = height
        self.width = width
        padding = -2
        self.top = padding
        self.bottom = self.height - padding
        self.display = self.get_display()
    
    def get_uptime(self):
        process = Popen(['uptime', '-p'], stdout=PIPE, stderr=PIPE)
        uptime, uptime_err = process.communicate()
        uptime, uptime_err = uptime.decode('utf-8'), uptime_err.decode('utf-8')
        if uptime_err != '':
            return uptime_err
        else:
            return uptime.replace('\n', '')
    
    def get_display(self):
        display = adafruit_ssd1306.SSD1306_I2C(self.height, self.width, I2C)
        display.fill(0)
        display.show()  # Show cleared display
        return display

    def display_text(self, text):
        self.display.text(strftime('%Y-%m-%d %H:%M:%S'), x, self.top + 3, 1)
        self.display.text(self.get_uptime(), x, self.top + 11, 1)
        self.display.text(text, x, self.top + 25, 1)
        self.display.show()
