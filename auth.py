#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class AP:
    
    def __init__(self):
        self.replayCounter = 0
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EA'
        self.clconn = None
        self.cl = None


    def sendMessage1(self):
        self.SNonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        self.replayCounter += 1
        return tmp, self.ANonce


    def connect_to_client(self):
        self.clconn = rpyc.connect("localhost", 18813)
        self.cl = self.clconn.root
        return "Connection established, ready to start 4 way handshake"
        

# RPYC Server Stuff
class APService(rpyc.Service):

    def exposed_reqMessage1(self):
        return ap.sendMessage1()


    def exposed_reqConnection(self):
        time.sleep(3)
        return ap.connect_to_client()
        

# start the APserver
server = ThreadedServer(APService, port = 18812)
t = Thread(target = server.start)
t.daemon = True
t.start()

ap = AP()

while True:
    time.sleep(3)



    
    

