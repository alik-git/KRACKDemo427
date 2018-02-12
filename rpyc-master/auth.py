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
        self.c = None

    def sendMessage2(self):
        self.SNonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        self.replayCounter += 1
        return tmp, self.SNonce


    def connect_to_client(self):
        conn = rpyc.connect("localhost", 18813)
        self.c = conn.root
        self.c.exposed_sendMessage1();
        

# RPYC Server Stuff
class APService(rpyc.Service):

    def exposed_sendMessage2(self):
        return ap.sendMessage2()


    def exposed_client_connect(self):
        ap.connect_to_client()
        

        

# start the server
server = ThreadedServer(APService, port = 18812)
t = Thread(target = server.start)
t.daemon = True
t.start()

ap = AP()

while True:
    time.sleep(3)



    
    

