import machine
import time
import network
from umqtt.simple import MQTTClient

SSID = 'Lukijan Musicki'
PASSWORD = 'ZF87zeYk'

MQTT_SERVER = 'broker.hivemq.com'  
MQTT_PORT = 1883
MQTT_TOPIC = 'hellou1'  


button_pin = 15 
mq9_pin = 35     

# Setup the button pin (button connected to GND)
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Setup the MQ-9 sensor pin (ADC)
mq9_adc = machine.ADC(machine.Pin(mq9_pin))  # Create ADC object on pin 35
mq9_adc.atten(machine.ADC.ATTN_11DB)  # Set attenuation for 0-3.3V range

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(0.5)
    print('Connected to WiFi:', wlan.ifconfig())

# Connect to MQTT broker (without authentication)
def connect_mqtt():
    client = MQTTClient('ESP32', MQTT_SERVER, port=MQTT_PORT)
    client.connect()
    return client

# Read the MQ-9 sensor value (raw ADC value)
def read_mq9():
    return mq9_adc.read()

# Main loop
def main():
    connect_wifi()  # Connect to Wi-Fi
    client = connect_mqtt()  # Connect to the MQTT broker

    button_pressed = False  # Flag to track button state

    while True:
        if button.value() == 0:  # Button pressed (active LOW)
            if not button_pressed:  # Only read and send once per press
                button_pressed = True
                
                # Read sensor value
                sensor_value = read_mq9()
                print("MQ-9 Sensor Value:", sensor_value)

                # Send the sensor data to the MQTT broker
                message = "CO Concentration: {}".format(sensor_value)
                client.publish(MQTT_TOPIC, message)

                # Small delay after sending message
                time.sleep(0.5)

        else:
            button_pressed = False  # Reset button pressed state when released
        
        time.sleep(0.1)  # Small delay for stability

# Start the main loop
if __name__ == '__main__':
    main()
