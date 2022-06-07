import socket
from uuid import getnode
from datetime import datetime

print('\nNOTE :- Type CALCULATOR to access calculator and DISCONNECT to disconnect\n\n')
HEADER = 64
PORT = 5050
SERVER_IP = 'localhost'
addr = (SERVER_IP,PORT)
FORMAT = 'utf-8'
DISCONNECT_msg = 'DISCONNECT'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

name = input('\nEnter client name : ')
client.send(bytes(name,'utf-8'))
clientmac = ':'.join(("%012X" % getnode())[i:i+2] for i in range(0, 12, 2))
client.send(bytes(clientmac,'utf-8'))
servermac = client.recv(1024).decode()
print(f'\n[CONNECTED TO SERVER]\nTime of request : {str(datetime.now().time())[:8]}\nIP address  : {addr[0]}\nPort : {addr[1]}\nMAC address: {servermac}\n')

def send(msg):
    message = msg.encode(FORMAT)
    send_length = str(len(message)).encode(FORMAT)
    send_length+=b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if(msg=='CALCULATOR'):
        while True:
            servermg = client.recv(2048).decode(FORMAT)
            print(servermg)
            mg = input(f'[{addr} {str(datetime.now().time())[:8]}] : ')
            client.send(mg.encode(FORMAT))
            if(mg=='N' or mg=='No'):
                break
while True:
    mes = input(f'[{addr} {str(datetime.now().time())[:8]}] : ')
    send(mes)
    servermsg = client.recv(2048).decode(FORMAT)
    print(f'[SERVER] : {servermsg}')
    if mes == DISCONNECT_msg:
        break

client.close()
