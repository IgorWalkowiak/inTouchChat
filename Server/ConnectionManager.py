class ConnectionManager:

    def newConnectionListener(socket):
        while True:
            self.conncetions.append(socket.accept())
            print("New connection accepted")

    def __init__(self, socket):
        self.connections = []
        connectionListener = threading.Thread(target=newConnectionListener, args=(connections,socket))
        connectionListener.start()
        
        
    
