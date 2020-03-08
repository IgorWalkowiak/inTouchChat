
from threading import Thread

class ConnectionManager:

    def newConnectionHandler(self, newConnection):
        connectionListener = Thread(target=self.rxPacketListener, args=((self,newConnection),))
        connectionListener.start()
        a ,connectionInfo = newConnection
        print("new connection from address:",connectionInfo[0])


    def newConnectionListener(self,why):
        while True:
            newConnection = self.socket.accept()
            self.connections.append(newConnection)
            self.newConnectionHandler(newConnection)

    def rxPacketListener(self, connection):
        unpacked = connection[1]
        conn, addr = unpacked
        while True:
            data = conn.recv(1024)
            if data:
                self.queuedData.append((data,addr))
            else:
                print("Lost connection with", addr)
                break

            
    
    def __init__(self, socket):
        self.socket = socket
        self.connections = []
        self.queuedData = []
        connectionListener = Thread(target=self.newConnectionListener, args=(self,))
        connectionListener.start()

    

