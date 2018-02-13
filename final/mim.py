#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class MIM:
    
    def __init__(self):
        self.message = 0
        self.replayCounter = None
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EB'
        self.clconn = None
        self.cl = None 
        self.jobdone = False

    def getMessage2(self, mnum, message):
        self.m2 = message
        self.message = mnum
        print(self.m2)

    def getMessage4(self, mnum, message):
        self.m4 = message
        self.message = 4
        print(self.m4)

    def getMessage5(self, mnum, message):
        print('Encrypted communication 1:')
        print(message)

    def getMessage6(self, mnum, message):
        print('Encrypted communication 2:')
        print(message)
        self.jobdone = True

    def connect_to_client(self):
        print('connecting')
        self.clconn = rpyc.connect("localhost", 18813)
        self.cl = self.clconn.root
        return "Connection established, ready to start 4 way handshake"


# RPYC Server Stuff
class MIMService(rpyc.Service):

    def exposed_sendMessage2(self, mnum, message):
        return mim.getMessage2(mnum, message)

    def exposed_sendMessage4(self, mnum, message):
        return mim.getMessage4(mnum, message)

    def exposed_sendMessage5(self, mnum, message):
        return mim.getMessage5(mnum, message)

    def exposed_sendMessage6(self, mnum, message):
        return mim.getMessage6(mnum, message)

    def exposed_reqConnection(self):
        mim.connect_to_client()
        

# start the MIMserver
server = ThreadedServer(MIMService, port = 18814)
t = Thread(target = server.start)
t.daemon = True
t.start()

mim = MIM()

#self.cl.exposed_sendMessage1('message')

while True:
    time.sleep(1)
    if(mim.message == 4):
        if (mim.jobdone == True):
            print('done')
            break

    
    
