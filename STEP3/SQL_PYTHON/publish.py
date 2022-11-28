import random
import time
import math
from paho.mqtt import client as mqtt_client
from faker import Faker
fake = Faker()
Faker.seed(0)


broker = '20.196.200.98'
port = 1883
topic = "srv/severity"
client_id = f'python-mqtt-sql-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
   # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(0.1)
        severity = math.ceil(random.randint(1, 3))
        fake_local_latlng = fake.local_latlng(country_code='BR')
        fake_lat = float(fake_local_latlng[0])
        fake_lng = float(fake_local_latlng[1])

        msg = f"Severity: {severity} Latitude: {fake_lat} Longitude: {fake_lng}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

run()
