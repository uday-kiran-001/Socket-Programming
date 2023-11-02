import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5670
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
DISCONNECT = 0

def receive():
    global connected
    while connected:
        try:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")
        except:
            print("CONNECTION CLOSED")
            break
    client.close()

def send_msg():
    global connected
    while connected:
        msg = input("> ")
        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
            DISCONNECT = 1
            client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] {IP}: {PORT}")

connected = True

receive_thread = threading.Thread(target = receive, args=())
receive_thread.start()
print(f"Recieve thread started : {receive_thread}")

send_thread = threading.Thread(target=send_msg, args = ())
send_thread.start()
print(f"Send thread started : {send_thread}")