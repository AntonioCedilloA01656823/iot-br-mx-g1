#pip install tk
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
        self.connect["command"] = self.connect_function
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
        self.update["command"] = self.update_function
        self.update.pack()

    def connect_function(self):
        brokerIP = self.brokerIP.get()
        brokerPort = self.brokerPort.get()
        print(brokerIP+":"+brokerPort)

    def sel(self):
        selection = "You selected the option " + str(var.get())
        print(selection)

    def update_function(self):
        print(1)

root = Tk()
var = IntVar()
Application(root)
root.mainloop()
