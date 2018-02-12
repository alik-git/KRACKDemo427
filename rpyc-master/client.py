#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class CL:
    
    def __init__(self):
        self.replayCounter = 0
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EB'

    def sendMessage1(self):
        self.ANonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        self.replayCounter += 1
        return tmp, self.ANonce


# RPYC Server Stuff
class CLService(rpyc.Service):
    
    def exposed_sendMessage1(self):
        return cl.sendMessage1()
        
    
# start the server
server = ThreadedServer(CLService, port = 18813)
t = Thread(target = server.start)
t.daemon = True
t.start()

cl = CL()

input('Initiate 4-way handshake? (y/y)')
try:
    conn = rpyc.connect("localhost", 18812)
    c = conn.root
    print('4-way handshake initiated')
    c.exposed_client_connect()
except:
    print('No AP found')
    exit()

while True:
    time.sleep(3)
    



    
    
