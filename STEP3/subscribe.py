import random
from paho.mqtt import client as mqtt_client
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="T0n1tO#313",
    database="eq1Events"

)

print("Connection to database sucessful!")
myCursor = db.cursor()
# myCursor.execute("CREATE DATABASE eq1Events") Database for the project created
#myCursor.execute("CREATE TABLE Requests (ipAdress VARCHAR(20), clientId VARCHAR(20) PRIMARY KEY, severity VARCHAR(10),latitude int,altitude int )")
#myCursor.execute("DESCRIBE Requests")



broker = '20.196.200.98' #change with ur virtual machine IP adress
port = 1883
topic = "srv/severity"
client_id = f'appmqtt-eq1-{random.randint(0, 100)}'
username = 's2'
password = 's2987654321' #Change with ur mosquitto password and user


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        a = msg.payload.decode()
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #add sql part, split
        data = a.split()
        svdata = data[1]

        latstr = data[3]
        latdata = int(latstr)

        altstr = data[5]
        altdata = int(altstr)

        myCursor.execute("INSERT INTO Events(ipAdress,clientId,severity,latitude,altitude) VALUES(%s,%s,%s,%s,%s),(broker, client_id, svdata, latdata, altdata)")


    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

run()

