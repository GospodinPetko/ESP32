import machine
import time

red_led = machine.Pin(16, machine.Pin.OUT)
yellow_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(18, machine.Pin.OUT)

button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

def traffic_light_sequence():
    red_led.on()       
    yellow_led.off()   
    green_led.off()   
    time.sleep(1)     
    
    red_led.off()      
    yellow_led.on()    
    green_led.off()    
    time.sleep(0.5)    
    
    yellow_led.off()   
    green_led.on()     
    time.sleep(2)      
    
    red_led.off()      
    yellow_led.off()
    green_led.off()

while True:
    if button.value() == 0:  
        traffic_light_sequence()  
        time.sleep(0.1)  
    else:
       
        red_led.off()
        yellow_led.off()
        green_led.off()
        time.sleep(0.1)  