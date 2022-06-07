import socket
import threading
from uuid import getnode
from datetime import datetime

HEADER = 64
PORT = 5050
# SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_IP = '127.0.0.1'
ADDR = (SERVER_IP,PORT)
FORMAT = 'utf-8'
DISCONNECT_msg = 'DISCONNECT'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servermac = ':'.join(("%012X" % getnode())[i:i+2] for i in range(0, 12, 2))
server.bind(ADDR)

def handle_client(conn,addr):
    conn.send(bytes(servermac,'utf-8'))
    name = conn.recv(1024).decode()
    clientmac = conn.recv(1024).decode()
    print(f'\n[NEW CONNECTION]\nTime of request : {str(datetime.now().time())[:8]}\nIP address  : {addr[0]}\nPort : {addr[1]}\nName : {name}\nMAC address: {clientmac}\n')
    while True:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        if msg_length:
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f'[{addr} {str(datetime.now().time())[:8]}] : {msg}')
            if msg == DISCONNECT_msg:
                conn.send("\n| DISCONNECTED |".encode(FORMAT))
                break
            servermsg = input('[SERVER] : ')
            conn.send(servermsg.encode(FORMAT))
    conn.close()

def start_server():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'\n[ACTIVE CONNECTIONS] {threading.activeCount()-1}')

print("[STARTING SERVER] Server is starting...")
start_server()