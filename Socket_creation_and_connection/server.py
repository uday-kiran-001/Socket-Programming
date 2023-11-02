import socket

PORT = 8000
ADDRESS = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

print(ADDRESS)

socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.bind((ADDRESS, PORT))
socket.listen(2)

while True:
    new_conn, addr  = socket.accept()
    print(f"[NEW CONNECTION] {addr}")
    new_conn.send('[SUCCESSFULLY CONNECTED]'.encode(FORMAT))
    new_conn.close()
    break
    