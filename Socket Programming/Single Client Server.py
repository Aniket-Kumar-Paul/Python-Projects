from socket import *
from uuid import getnode

s = socket()
ip , port = 'localhost' , 9999
s.bind((ip,port))
s.listen(3)
servermac=':'.join(("%012X" % getnode())[i:i+2] for i in range(0, 12, 2))

while True:
    c , addr = s.accept()
    c.send(bytes(servermac,'utf-8'))
    name = c.recv(1024).decode()
    clientmac = c.recv(1024).decode()
    print('\nConnected with client of  :- \nIP address  : {}\nPort\t   : {}\nName\t : {}\nMAC address : {}\n'.format(addr[0],addr[1],name,clientmac))
    while True:
        msg = input('SERVER : ')
        c.send(bytes(msg,'utf-8'))
        received =  c.recv(1024).decode()
        print('CLIENT :', received)
        if(received=='Bye'):
            c.send(bytes('BaBye','utf-8'))
            break
    c.close()
