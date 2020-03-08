import socket
from ConnectionManager import ConnectionManager


HOST = '192.168.0.113'
PORT = 2555

dataQueue = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    connManager = ConnectionManager(socket)

    while True:
        if connManager.queuedData:
            data, addr = connManager.queuedData.pop()
            data = data.decode("utf-8") 
            print(f'Received {data} from {addr[0]}')
