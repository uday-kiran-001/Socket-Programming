import socket 
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5670
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def listen_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")

    connected = True
    while connected:
        try:
            msg = conn.recv(SIZE).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            
            print(f"[{addr}] {msg}")

            msg = f"[ MSG RECIEVED ]: {msg}"
            conn.send(msg.encode(FORMAT))
        except : 
            print(f"{addr} [ CONNECTION CLOSED SUCCESSFULLY ]")
            del clients[addr[1]]
            break

    conn.close

def send_client():
    global clients
    while True:
        print("[ CLIENTS ] : ")
        for i in clients.keys():
            print(i)
        client = int(input("[ WHICH CLIENT YOU WANT TO MSG ]:"))
        if client not in clients.keys():
            print("[ UNAVAILABLE ]")
            continue
        message = input("[ ENTER MESSAGE ] : ")
        clients[client].send(message.encode(FORMAT))

def main():
    server.listen()
    print(f"[ SERVER LISTENING ] {IP}:{PORT}")
    flag = True
    global clients

    while True:
        conn, addr = server.accept()
        receive_thread = threading.Thread(target=listen_client, args = (conn, addr))
        receive_thread.start()
        print(f"Recieve thread started : {receive_thread}")
        clients[addr[1]] = conn


        if flag:
            send_thread = threading.Thread(target = send_client, args = ())
            send_thread.start()
            print(f"Send thread started : {send_thread}")
            flag = False
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")


print("[ SERVER STARTED ]")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = {}
main ()