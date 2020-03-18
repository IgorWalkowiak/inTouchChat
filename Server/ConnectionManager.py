
from threading import Thread
import DataReceiver
import DataExtractor
import socket

HOST = '192.168.0.3'
PORT = 2553

def createAndBindSocket(host, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))
    soc.listen()
    return soc

class ConnectionManager:
    _dataReceiver : DataReceiver
    socket = createAndBindSocket(HOST, PORT)

    def registerReceiver(self, dataReceiver: DataReceiver):
        print("OK ZAREJESTROWALEM")
        self._dataReceiver = dataReceiver

    def newConnectionHandler(self, newTcpConnection):
        connection = (newTcpConnection, self._nextConnectionId)
        self.connections.append(connection)
        connectionListener = Thread(target=self.rxPacketListener, args=((self,connection),))
        connectionListener.start()
        a ,connectionInfo = newTcpConnection
        print("new connection from address:",connectionInfo[0])

    def newConnectionListener(self,why):
        while True:
            newConnection = self.socket.accept()
            self.newConnectionHandler(newConnection)

    def rxPacketListener(self, handledConnection):
        connection, connectionID = handledConnection[1]
        conn, addr = connection
        while True:
            data = conn.recv(1024)
            if data:
                self._dataReceiver.handleData(data.decode("utf-8"))
            else:
                print("Lost connection with", addr)
                break


    def __init__(self):
        self._nextConnectionId = 0
        self.connections = []
        connectionListener = Thread(target=self.newConnectionListener, args=(self,))
        connectionListener.start()

connManager = ConnectionManager()