#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class MIM:
    
    def __init__(self):
        self.messagesent = 0
        self.intercepted = False
        self.replayCounter = None
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EB'
        self.apconn = None
        self.ap = None

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

    def sendMessage2(self):
        self.messagesent = 2
        self.SNonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        return tmp, self.SNonce

    def sendMessage4(self):
        self.messagesent = 4
        return '4-way handshake complete'

    def sendCom1(self):
        self.messagesent = 5
        tmp = self.replayCounter
        return 'c7041f44d10f1801d4e081c61dee4cbf32090d0f90f5420cc554'

    def sendCom2(self):
        self.messagesent = 6
        tmp = self.replayCounter
        if (self.intercepted == False):
            return '3315ed233f9899c261290d436107a2b73dd834517c1540044f3c'

        return 'c7041f44d10f1801cff98bc054e21fa43b05054adff40c55c744'

    def reinstallKey(self):
        self.intercepted = True
        return None
    
    def jamComs(self):
        self.jammed = True
        return 'correct string'
    
    def reqAPConnection(self):
        self.apconn = rpyc.connect("localhost", 18812)
        self.ap = self.apconn.root
        ap_response = self.ap.exposed_reqConnection()
        # time.sleep(3)
        print(ap_response)


# RPYC Server Stuff
class CLService(rpyc.Service):
    
    def exposed_reqMessage2(self):
        time.sleep(3)
        return cl.sendMessage2()

    def exposed_reqMessage4(self):
        time.sleep(3)
        return cl.sendMessage4()

    def exposed_reqCom1(self):
        time.sleep(3)
        return cl.sendNextCom()

    def exposed_reqCom2(self):
        time.sleep(3)
        return cl.sendNextCom()

    def exposed_reinstallKey(self):
        return cl.reinstallKey()

    def exposed_jamComs(self):
        return cl.jamComs()

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
        
    
# start the CLserver
server = ThreadedServer(CLService, port = 18814)
t = Thread(target = server.start)
t.daemon = True
t.start()

mim = MIM()

input('Hijack all connections? (y/y)')
cl.reqAPConnection()

print('waiting for message 1')
m1 = cl.ap.exposed_reqMessage1()
print(m1)

while True:
    time.sleep(3)
    


    
    
