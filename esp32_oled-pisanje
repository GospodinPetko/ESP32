from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0,scl=Pin(4),sda=Pin(0), freq=400000)
oled_width = 128
oled_height = 64
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3C)
oled.text('hello world',0,0,1)
oled.fill(0)
oled.show()