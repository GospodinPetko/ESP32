from machine import Pin
import time
import mqtt_2 as mqtt  


BUTTON_PIN = 15  
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def main():
    print("Press the button to trigger MQTT!")
    while True:
        if not button.value():  
            print("Button was pressed! Triggering MQTT...")
            
            mqtt.mqtt_publish(mqtt.mqtt_broker, mqtt.mqtt_topic, mqtt.poruka)  
            time.sleep(0.2)

if __name__ == "__main__":
    main()
