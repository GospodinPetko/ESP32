import machine
import ssd1306
import time


i2c = machine.SoftI2C(scl=machine.Pin(4), sda=machine.Pin(0), freq=400000)


oled = ssd1306.SSD1306_I2C(128, 64, i2c)


button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)


def blink_oled():
    oled.fill(1) 
    oled.show()
    time.sleep(0.5) 
    oled.fill(0) 
    oled.show()
    time.sleep(0.5)  

while True:
    if button.value() == 0: 
        blink_oled()
        time.sleep(0.1)  
    else:
        time.sleep(0.1)  