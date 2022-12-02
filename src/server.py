import os 
import sys 
import socket
from _thread import *

server = '192.168.1.108'
port = 5555
y = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #af_inet is for ipv4 and sock_stream is tcp


try:
    y.bind((server,port))
except socket.error as i:
    str(i)

y.listen()
print('waiting for connections')
def threading(connection):
    while True:
        inp = connection.recv(1500)
        out = connection.decode('UTF-8')
        if not inp:
            print('no connection')
            break
        else:
            print(out)
            connection.sendall(str.encode(out))

while True:
    connection , addr = y.accept()
    print('connected to: ',addr)
    start_new_thread(threading , (connection,))
