import socket
from time import sleep


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.184.111"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            # return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        print("client sending", data)
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)

    def recv(self):
        print("client recieving", end=" ")
        try:
            data = self.client.recv(2048).decode()
            print(data)
            return data
        except socket.error as e:
            print(e)
