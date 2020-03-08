import socket

HOST = '192.168.0.113'  # The server's hostname or IP address
PORT = 4444        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    
    socket.connect((HOST, PORT))
    while True:
        name = input(":")
        socket.send(name.encode())
        #data = socket.recv(1024)
        

print('Received', repr(data))

