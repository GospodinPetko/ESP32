import time
from umqttsimple import MQTTClient
import ubinascii
import micropython
import network
import esp
import machine



ssid = 'Lukijan Musicki' 
password = 'ZF87zeYk'  

mqtt_broker = "broker.hivemq.com"  
mqtt_topic = 'hellou1'
poruka = "cas krece uskoro"


def connect_wifi(ssid, pw):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    
    station.disconnect()
    time.sleep(1)
    
    station.connect(ssid, pw)
    
    max_retries = 10  
    retry_count = 0
    
 
    while not station.isconnected() and retry_count < max_retries:
        print(f"Connecting to WiFi... Attempt {retry_count + 1}/{max_retries}")
        time.sleep(2)  
        retry_count += 1
    
    if station.isconnected():
        print("Connected to WiFi")
        print(f"ESP32 IP Address: {station.ifconfig()[0]}")
    else:
        print("Failed to connect to WiFi after several attempts")


def disconnect_wifi():
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    print("Disconnected from WiFi")

def mqtt_publish(broker, topic, msg):

    
    client = MQTTClient(ubinascii.hexlify(machine.unique_id()), broker)
    
    try:
        print("Connecting to MQTT Broker...")
        client.connect()  
        print("Connected to MQTT Broker")
        
        
        client.publish(topic, msg)
        print(f"Message sent to {topic}: {msg}")
        
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return False  
    
    
    try:
        print("Disconnecting from MQTT Broker...")
        client.disconnect()  
        print("Disconnected from MQTT Broker")
    except Exception as e:
        print(f"Error while disconnecting from MQTT broker: {e}")

    return True 


def main():

    connect_wifi(ssid, password)
    

    if network.WLAN(network.STA_IF).isconnected():
        mqtt_publish(mqtt_broker, mqtt_topic, poruka)
    

    disconnect_wifi()



if __name__ == "__main__":
    main()