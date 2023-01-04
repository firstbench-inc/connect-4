import socket
from _thread import *
import sys
from game import Game


def start_server(game_state: Game):
    server = "192.168.144.111"
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    def send_msg(conn, data):
        while True:
            try:
                conn.sendall(str.encode(data))

            except:
                break

    def recv(conn):
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")
                return reply

                if not data:
                    print("Disconnected")
                    break
            except:
                break

    def threaded_client(conn, data):
        conn.send(str.encode("Connected"))
        reply = ""
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")

                if not data:
                    print("Disconnected")
                    break
                else:
                    print("Received: ", reply)
                    print("Sending : ", reply)

                conn.sendall(str.encode(data))

            except:
                break

        print("Lost connection")
        conn.close()

    prev_data = None
    data = None
    while True:
        print("Cat")
        conn, addr = s.accept()
        data = "meowmeow"
        data = game_state.last_move()
        # if data == prev_data:
        #     continue
        # blocking function that returns data
        print("Connected to:", addr)

        # start_new_thread(send_msg, (conn, data))

        # get msg from client
        data = recv(conn)
        data = data.decode("utf-8")
        data = data.split("#")
        game_state.add_coin(data[1])
