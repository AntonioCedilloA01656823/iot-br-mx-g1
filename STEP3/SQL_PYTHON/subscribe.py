import random
from paho.mqtt import client as mqtt_client
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=13306,
    user="root",
    passwd="iotbrmx1", #"T0n1tO#313", 
    database="eq1Events"

)

print("Connection to database sucessful!")
myCursor = db.cursor()
# myCursor.execute("CREATE DATABASE eq1Events") Database for the project created
#myCursor.execute("CREATE TABLE Events (ipAdress VARCHAR(20), clientId VARCHAR(20), severity VARCHAR(10),latitude float,altitude float,   ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")
#myCursor.execute("DESCRIBE Events")



broker = '20.196.200.98' #change with ur virtual machine IP adress
port = 1882
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
        latdata = float(latstr)

        altstr = data[5]
        altdata = float(altstr)
        myCursor.execute(f"INSERT INTO Events(ipAdress,clientId,severity,latitude,altitude) VALUES('{broker}', '{client_id}', '{svdata}', {latdata}, {altdata});")
        db.commit()
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

run()
