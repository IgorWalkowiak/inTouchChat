import socket
import threading

HOST = 'XXX'  # The server's hostname or IP address
PORT = 2553        # The port used by the server


class ConnectionManager:
    def __init__(self, responsHandler):
        self.responsHandler = responsHandler
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.waitForConnection()
        listener = threading.Thread(target=self.rxPacketListener)
        listener.start()
    def waitForConnection(self):
        self.soc.connect((HOST, PORT))

    def send(self, data):
        self.soc.send(data.encode())

    def rxPacketListener(self):
        print(self.soc)
        while True:
            data = self.soc.recv(1024)
            if data:
                self.responsHandler(data.decode("utf-8"))
            else:
                print("Lost connection with", addr)
                break
