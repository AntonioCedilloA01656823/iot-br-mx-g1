#udpated, DEFINITIVE VERSION, only issue is that the app might crash sometimes. 

import random
import time

from paho.mqtt import client as mqtt_client
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer.pack()

        self.forthContainer = Frame(master)
        self.forthContainer["pady"] = 20
        self.forthContainer.pack()

        self.fiftContainer = Frame(master)
        self.fiftContainer["pady"] = 10
        self.fiftContainer.pack()

        self.sixContainer = Frame(master)
        self.sixContainer["pady"] = 20
        self.sixContainer.pack()

        self.sevenContainer = Frame(master)
        self.sevenContainer["pady"] = 20
        self.sevenContainer.pack()

        self.tittle = Label(self.firstContainer, text="Broker Information")
        self.tittle["font"] = ("Arial", "10", "bold")
        self.tittle.pack()

        self.brokerIPLabel = Label(self.secondContainer, text="Broker IP", font=self.fontePadrao)
        self.brokerIPLabel.pack(side=LEFT)

        self.brokerIP = Entry(self.secondContainer)
        self.brokerIP["width"] = 30
        self.brokerIP["font"] = self.fontePadrao
        self.brokerIP.pack(side=LEFT)

        self.brokerPortLabel = Label(self.thirdContainer, text="Broker Port", font=self.fontePadrao)
        self.brokerPortLabel.pack(side=LEFT)

        self.brokerPort = Entry(self.thirdContainer)
        self.brokerPort["width"] = 30
        self.brokerPort["font"] = self.fontePadrao
        self.brokerPort.pack(side=LEFT)

        self.connect = Button(self.forthContainer)
        self.connect["text"] = "Connect"
        self.connect["bg"] = "lime"

        self.connect["font"] = ("Calibri", "8")
        self.connect["width"] = 12
        self.connect["command"] = self.connect_function #call connect to change to return a client
        self.connect.pack()

        self.mensagem = Label(self.forthContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.tittle = Label(self.fiftContainer, text="Severity")
        self.tittle["font"] = ("Arial", "10", "bold")
        self.tittle.pack()


        self.r1 = Radiobutton(self.sixContainer, text="Low", variable=var, value=1,command=self.sel)
        self.r1.pack(side=LEFT)

        self.r2 = Radiobutton(self.sixContainer, text="Middle", variable=var, value=2,command=self.sel)
        self.r2.pack(side=LEFT)

        self.r3 = Radiobutton(self.sixContainer, text="High", variable=var, value=3,command=self.sel)
        self.r3.pack(side=RIGHT)

        self.update = Button(self.sevenContainer)
        self.update["text"] = "Update"
        self.update["font"] = ("Calibri", "8")
        self.update["width"] = 12
        self.update["command"] = self.update_function #publish
        self.update.pack()

    def connect_function(self):
        brokerIP = self.brokerIP.get()
        brokerPort = self.brokerPort.get()
        brokerPort = int(brokerPort)
        print(brokerIP)
        print(brokerPort)

        self.client_id = f'python-client-{random.randint(0, 1000)}'

        def on_connect(client, userdata, flags, rc):
                if rc == 0:
                    print("Connected to MQTT Broker!")
                else:
                    print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        # client.username_pw_set(username, password)
        self.client.on_connect = on_connect
        self.client.connect(brokerIP, brokerPort)
        self.client.loop_start()


    def sel(self):
        selection = "You selected the option " + str(var.get())
        self.severity = var.get() # 1 to 3
        print(selection)
        if self.severity == 1:
            self.severityText = "Low"
        elif self.severity == 2:
            self.severityText = "Medium"
        elif self.severity == 3:
            self.severityText = "High"
        else:
            self.severityText = "None"


    def update_function(self):
        print(1)
        msg_count = 0
        topic = "srv/severity"
        latitude = random.randint(16, 19)
        altitude = random.randint(96, 99)
        while True:
            time.sleep(1)
            msg = f"{self.client_id}:{self.severityText}:{latitude}:{altitude}"
            result = self.client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1

root = Tk()
var = IntVar()
Application(root)
root.mainloop()
