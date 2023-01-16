from time import sleep
import socket
from _thread import *
import sys

from game import Game

# from  import Game


def start_server(game_state: Game):
    # def start_server():
    server = "192.168.118.111"
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    def send_msg(conn, data):
        print("sending")
        conn.sendall(str.encode(data))

    def recv(conn):
        print("receiving")
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
    conn, addr = s.accept()
    print("Connected to:", addr)
    while True:
        # conn, addr = s.accept()
        # print("Cat")
        data = game_state.last_move()
        # blocking function that returns data
        if data == prev_data:
            continue
        print("sending", data)
        send_msg(conn, str(data[0]) + "#" + str(data[1]))
        prev_data = data
        print(prev_data, data)

        # start_new_thread(send_msg, (conn, data))

        # get msg from client
        data = recv(conn)
        print("recieved", data)
        coord = data.split("#")
        game_state.add_coin(int(coord[1]))
        prev_data = game_state.last_move()
        game_state.multiplayer_moved = True
        game_state.player_turn = 2
