import socket

PORT = 12345
ADDRESS = '127.0.1.1'
FORMAT = 'utf-8'

socket = socket.socket()

socket.connect((ADDRESS, PORT))
print(socket.recv(2024).decode(FORMAT))
socket.close()