import socket

HOST = '192.168.0.113'  # The server's hostname or IP address
PORT = 2555        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:

    name = input("Type your nickname: ")
    socket.connect((HOST, PORT))
    while True:
        text = input(":")
        socket.send((name + "::" + text).encode())
        #data = socket.recv(1024)
        

print('Received', repr(data))

