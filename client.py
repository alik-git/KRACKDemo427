#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class CL:
    
    def __init__(self):
        self.replayCounter = None
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EB'
        self.apconn = None
        self.ap = None

    def sendMessage2(self):
        self.SNonce = random.randint(10000, 99999)
        tmp = self.replayCounter
        return tmp, self.SNonce
    
    def reqAPConnection(self):
        self.apconn = rpyc.connect("localhost", 18812)
        self.ap = self.apconn.root
        ap_response = self.ap.exposed_reqConnection()
        # time.sleep(3)
        print(ap_response)
        
    


# RPYC Server Stuff
class CLService(rpyc.Service):
    
    def exposed_sendMessage2(self):
        return cl.sendMessage2()
        
    
# start the CLserver
server = ThreadedServer(CLService, port = 18813)
t = Thread(target = server.start)
t.daemon = True
t.start()

cl = CL()

raw_input('Initiate 4-way handshake? (y/y)')
# try:
cl.reqAPConnection()
# except:
#    print('No AP found')
#   exit()

while True:
    time.sleep(3)
    



    
    
