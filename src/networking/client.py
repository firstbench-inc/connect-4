import socket


class network:
    def __init__(self):
        self.check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(1500).decode()

    def traffic(self, data):
        self.client.send(str.encode(data))
        return self.client.recv(1500).decode()


a = network()
