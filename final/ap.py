#!/usr/bin/env python

import time
import random

import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread


# Actual Access Point Logic
class AP:
    
    def __init__(self):
        self.message = 0
        self.replayCounter = 0
        self.ANonce = None
        self.SNonce = None
        self.MAC = '34-25-B8-1C-17-EA'
        self.clconn = None
        self.cl = None
        self.jammed = False
        self.m2 = None
        self.m4 = None
        self.m3sent = False


    def getMessage2(self, mnum, message):
        self.m2 = message
        self.message = mnum + 2
        print('Recieved Message 2:')
        print(self.m2)

    def getMessage4(self, mnum, message):
        self.m4 = message
        self.message = 4
        print('Recieved Message 4:')
        print(self.m4)

    def getMessage5(self, mnum, message):
        print('Encrypted message 1:')
        print(message)

    def getMessage6(self, mnum, message):
        print('Encrypted message 2:')
        print(message)

    def connect_to_client(self):
        print('connecting')
        self.clconn = rpyc.connect("localhost", 18813)
        self.cl = self.clconn.root
        self.message = 1
        return "Connection established, ready to start 4 way handshake"


# RPYC Server Stuff
class APService(rpyc.Service):

    def exposed_sendMessage2(self, mnum, message):
        return ap.getMessage2(mnum, message)

    def exposed_sendMessage4(self, mnum, message):
        return ap.getMessage4(mnum, message)

    def exposed_sendMessage5(self, mnum, message):
        return ap.getMessage5(mnum, message)

    def exposed_sendMessage6(self, mnum, message):
        return ap.getMessage6(mnum, message)

    def exposed_reqConnection(self):
        ap.connect_to_client()
        

# start the APserver
server = ThreadedServer(APService, port = 18812)
t = Thread(target = server.start)
t.daemon = True
t.start()

ap = AP()

#self.cl.exposed_sendMessage1('message')

while True:
    time.sleep(1)
    #print(ap.message)
    if(ap.message == 1):
        print('sending message 1')
        time.sleep(3)
        ap.cl.exposed_sendMessage1(ap.message, 'ANonce: 1235571')
        print('message 1 sent')
        time.sleep(3)
    if(ap.message == 3):
        if (ap.m3sent == False):
            print('sending message 3')
            time.sleep(3)
            ap.cl.exposed_sendMessage3(ap.message, 'GTK: 8569285, MIAC: 5468778')
            print('message 3 sent')
            time.sleep(3)
        else:
            print('sending message 3 again...')
            time.sleep(3)
            ap.cl.exposed_sendMessage3(ap.message, 'GTK: 8569285, MIAC: 5468778')
            print('message 3 sent again....')
            time.sleep(3)
    if(ap.message == 4):
        pass
        #wait for messages

