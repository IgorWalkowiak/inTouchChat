import socket
import threading
import time
import logging
import signal
import sys

def dataListener(dataQueue, conn, name):
    while True:
        print("Refreshing ", name)
        dataQueue.append(conn.recv(255))

def newConnectionListener(connections, socket):
    while True:
        connections.append(socket.accept())
        print("New connection accepted")

HOST = '192.168.0.113'
PORT = 4444

dataQueue = []
conns = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    connectionListener = threading.Thread(target=newConnectionListener, args=(conns,socket))
    connectionListener.start()

    while True:
        if dataQueue:
            data = dataQueue.pop()
            print('Got message: ', data)
