# Raspberry Pi Security Alarm
This program will monitor a [normally closed magnetic reed switch](https://www.explainthatstuff.com/howreedswitcheswork.html) attached to a door or window and sound a buzzer/alarm(or multiple) if the switch is opened.

I plan to impliment this code in MicroPython or CurcuitPython to run on a Raspberry Pi PICO soon. Currently being developed on the Raspberry Pi Zero W.

TODO impliment an email alert that the alarm has been set off, and a picture taken at that time.

## Hardware Components used
* Raspberry Pi - Any model, lower power consumption the better
* Minimum of two LEDs, red and green
* At least one buzzer, I will be using two for the alarm
    * If multiple are used an alternating patterns could be configured
* OLED screen such as [this one](https://www.amazon.com/UCTRONICS-SSD1306-Self-Luminous-Display-Raspberry/dp/B072Q2X2LL/ref=sr_1_12?dchild=1&keywords=oled+screen+raspberry+pi&qid=1622034762&sr=8-12)
* 4x4 Matrix key pad such as [these membrane pads](https://www.amazon.com/Matrix-Membrane-Switch-Keyboard-Arduino/dp/B07THCLGCZ/ref=sr_1_4?dchild=1&keywords=4x4+matrix+keypad&qid=1622034846&sr=8-4) or [this more durable pad](https://www.adafruit.com/product/3844) - I'll be using the latter in my final build
* A durable metal case with a lock and a backup battery UPS inside the case is ideal to prevent someone from disonnecting power to stop the alarm
* NOT YET ADDED - Raspberry Pi Camera V1 or V2 - once I learn how to use the camera without blacklisting the I2C drivers this will be added