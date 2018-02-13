#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class AP:
    
    def __init__(self):
        self.message = 1
        self.replayCounter = 0
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EA'
        self.clconn = None
        self.cl = None


    def sendMessage1(self):
        self.message += 1
        self.ANonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        self.replayCounter += 1
        return tmp, self.ANonce

    def sendMessage3(self):
        self.message += 1
        tmp = self.replayCounter
        self.replayCounter += 1
        return 'message 3'

    def connect_to_client(self):
        self.clconn = rpyc.connect("localhost", 18813)
        self.cl = self.clconn.root
        self.message = 1
        return "Connection established, ready to start 4 way handshake"
        

# RPYC Server Stuff
class APService(rpyc.Service):

    def exposed_reqMessage1(self):
        time.sleep(3)
        return ap.sendMessage1()

    def exposed_reqMessage3(self):
        time.sleep(3)
        return ap.sendMessage3()

    def exposed_reqConnection(self):
        time.sleep(3)
        print("Connection established, ready to start 4 way handshake")
        return ap.connect_to_client()
        

# start the APserver
server = ThreadedServer(APService, port = 18812)
t = Thread(target = server.start)
t.daemon = True
t.start()

ap = AP()

jammed = False

while True:
    time.sleep(3)

    if (jammed == true):
        pass
    else:
        if(ap.message == 2):
            ap.message += 1
            print('waiting for message 2')
            m2 = ap.cl.exposed_reqMessage2()
            print(m2)
        if(ap.message == 4):
            ap.message += 1
            print('waiting for message 4')
            m4 = ap.cl.exposed_reqMessage4()
            print(m4)
            # if m4 'not received' request again
        if(ap.message == 5):
            ap.message += 1
            com1 = ap.cl.exposed_reqCom1()
            print('encrypted message 1:')
            print(com1)
        if(ap.message == 6):
            ap.message += 1
            com2 = ap.cl.exposed_reqCom2()
            print('encrypted message 2:')
            print(com2)
        

    
        
    

