
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

    def sendTo(self, portTarget, data):
        conn, addr = self.connections[portTarget]
        conn.send(data.encode())

    def registerReceiver(self, dataReceiver: DataReceiver):
        self._dataReceiver = dataReceiver

    def newConnectionHandler(self, newTcpConnection):
        self.connections[self._nextConnectionId] = newTcpConnection
        connectionListener = Thread(target=self.rxPacketListener, args=(newTcpConnection, self._nextConnectionId))
        connectionListener.start()
        a ,connectionInfo = newTcpConnection
        self._nextConnectionId = self._nextConnectionId+1

    def newConnectionListener(self, why):
        while True:
            newConnection = self.socket.accept()
            self.newConnectionHandler(newConnection)

    def rxPacketListener(self, tcpConnection, connId):
        conn, addr = tcpConnection
        print(connId)
        while True:
            data = conn.recv(1024)
            if data:
                self._dataReceiver.handleData(connId, data.decode("utf-8"))
            else:
                print("Lost connection with", addr)
                break

    def __init__(self):
        self._nextConnectionId = 0
        self.connections = {}
        connectionListener = Thread(target=self.newConnectionListener, args=(self,))
        connectionListener.start()

connManager = ConnectionManager()