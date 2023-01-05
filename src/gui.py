"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at 
  as it was on development.runtime
Give us this day our daily output.
And forgive us our code duplication,
    as we forgive those who
  duplicate code against us.
And lead us not into frustration;
  but deliver us from GOTOs.
    For thine is algorithm,
the computation, and the solution,
    looping forever and ever.
          Return;
"""

import pygame
import game
from pyvidplayer import Video
from time import *
from networking import server
from networking.client import Network
import threading

winner = 0
loser = 0
class Button:
    def __init__(self, img_path: str, pos: (int, int)):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        return


class NewButton:
    # a and b are co-ordinates.
    def __init__(self, a, b, image, image1):
        self.image = image
        self.image1 = image1
        self.rect = self.image.get_rect()
        self.rect.topleft = (a, b)
        self.clicked = False

    def draw(self):
        act = False
        pos = pygame.mouse.get_pos()
        on_button = self.rect.collidepoint(pos)
        if on_button:
            screen.blit(self.image1, self.image1.get_rect(center=self.rect.center))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else:
            screen.blit(self.image, self.image.get_rect(center=self.rect.center))
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            self.clicked = False
            act = True
        # screen.blit(self.image, (self.rect.topleft[0],self.rect.topleft[1]))
        return act


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


def place_coin(surface, col_no: int, row_no: int, board_pos: (int, int), player: int):
    pos_x = 71 + 106 * (col_no)
    pos_y = 51 + 77 * (row_no)
    if player == 1:
        return pygame.draw.circle(surface, (125, 24, 28), (pos_x, pos_y), 37)
    if player == 2:
        return pygame.draw.circle(surface, (40, 95, 71), (pos_x, pos_y), 37)


def place_timer(surface, player: int, time: int):
    font = pygame.font.Font("freesansbold.ttf", 32)
    if player == 1:
        timer = font.render("player 1: " + str(time), True, (125, 24, 28))
        surface.blit(timer, (100, 5))
    if player == 2:
        timer = font.render("player 2: " + str(time), True, (40, 95, 71))
        surface.blit(timer, (1100, 5))
    return


def place_coin_row(surface, player: int, posx: int):
    if player == 1:
        pygame.draw.circle(surface, (125, 24, 28), (posx, 50), 37)
    if player == 2:
        pygame.draw.circle(surface, (40, 95, 71), (posx, 50), 37)
    return


# ------------ pygame init -------------
pygame.init()

# running = True
screen = pygame.display.set_mode((1366, 780))
# # screen.fill((255, 255, 255))
# clock = pygame.time.Clock()
start_img = pygame.image.load("./assets/button_(3).png").convert_alpha()
end_image = pygame.image.load("./assets/button_(2).png").convert_alpha()
start1_img = pygame.image.load("./assets/button.png").convert_alpha()
end1_img = pygame.image.load("./assets/button_(1).png").convert_alpha()
join_img = pygame.image.load("assets/join_blue.png").convert_alpha()
join_img1 = pygame.image.load("assets/join_purple.png").convert_alpha()
host_img = pygame.image.load("assets/host_blue.png").convert_alpha()
host_img1 = pygame.image.load("assets/host_purple.png").convert_alpha()

board = pygame.image.load(r"./assets/board2.png")
bg = pygame.image.load(r"./assets/bg1.jpg")

board_pos = get_board_cord(screen.get_width(), screen.get_height())
vid = Video("./assets/INTRO3.mp4")
vid.set_size((1366, 780))
start_b = NewButton(590, 372, start_img, start1_img)
end_b = NewButton(625, 442, end_image, end1_img)
server_b = NewButton(580, 272, host_img, host_img1)
client_b = NewButton(580, 172, join_img, join_img1)


clock = pygame.time.Clock()
# ----------- game init -----------------
game_state = game.Game()
coins = []

# ------------ columns ------------------
columns = []
start_point = board_pos[0] + 32
# for i in range(1, 8):
#     columns.append((start_point + 106 * (i - 1), 50))
#     # Button(f"assets/button_r ({i}).png", (start_point + 106 * (i - 1), 50))
#     pass
for i in range(6):
    columns.append((106 * i + 53))

# ------------ game loop ----------------

screen.blit(bg, (0, 0))
# screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
screen.blit(board, board_pos)

coin_tray = pygame.Surface([1366, 74], pygame.SRCALPHA, 32)
coin_tray.convert_alpha()
# coin_tray.fill((255, 0, 0))
screen.blit(coin_tray, (0, 13))
cl_sr = None


def intro():
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                vid.__del__()
                start_window(game_state)
                return


def start_window(game_state):
    global cl_sr
    run = True
    while run:
        screen.fill((237, 197, 128))

        if start_b.draw() == True:
            return main_game()
        if end_b.draw():
            run = False
        if server_b.draw() == True:
            cl_sr = ("server", None)
            server_thread = threading.Thread(
                target=server.start_server, args=(game_state,)
            )
            server_thread.start()
            return main_game(True)
            # server.start_server(game_state)
            pass
        if client_b.draw() == True:
            meow = Network()
            print("cat")
            cl_sr = ("client", meow)
            # game_state.player_turn = 2
            return main_game(True)
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


def main_game(multiplayer: bool = False):
        running = True
        # timer = time_ns()
        move_played = True
        prev_move = None
        screen.blit(bg, (0, 0))
        screen.blit(coin_tray, (0, 13))
        screen.blit(board, board_pos)
        pygame.display.update()
    #while True:
        # my_dog = pygame.Surface([1366, 780])
        # screen.blit(my_dog, (0, 0))
        while running:
            coin_added = False
            # screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            screen.blit(coin_tray, (0, 13))

            # screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
            if multiplayer and cl_sr[0] == "client":
                # if multiplayer and turn 2 and current computer is
                # client then wait for server response
                if game_state.player_turn == 1:
                    move = cl_sr[1].recv()
                    if move is None or len(move.split("#")) <= 1:
                        continue
                    row_no = game_state.add_coin(int(move.split("#")[1]))
                    if row_no is None:
                        continue
                    row_no = 5 - row_no
                    # create a coin and add it to the list
                    coins.append(
                        # updates the game_state
                        place_coin(
                            board,
                            int(move.split("#")[1]),
                            row_no,
                            board_pos,
                            1,
                        )
                    )
                    coin_added = True
                    prev_move = game_state.last_move()
                    move_played = True
                    # check for win
                    win = game_state.check_win()
                    if win:
                        print(f"player {win} won!")
                        running = False
                    pass
                    continue

            if multiplayer and cl_sr[0] == "server":
                # if multiplayer and turn 1, computer is server
                # wait for client response
                if game_state.player_turn == 2:
                    if game_state.multiplayer_moved == True:
                        col_no = game_state.last_move()[1]
                        row_no = game_state.last_move()[0]
                        coins.append(
                            # updates the game_state
                            place_coin(
                                board,
                                col_no,
                                5 - row_no,
                                board_pos,
                                2,
                            )
                        )
                        coin_added = True
                        prev_move = game_state.last_move()
                        move_played = True
                        game_state.player_turn = 1
                        # check for win
                        win = game_state.check_win()
                        if win:
                            print(f"player {win} won!")
                            running = False
                        pass

                        pass
                    else:
                        continue
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    coin_tray.fill((0, 0, 0, 0))
                    # screen.blit(my_cat, (0, 13))
                    # screen.blit(bg, (0, 0))
                    # pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if posx < 295:
                        posx = 295
                    if posx > 1072:
                        posx = 1072
                    if game_state.player_turn == 1:
                        pygame.draw.circle(coin_tray, (125, 24, 28), (posx, 37), 37)
                    if game_state.player_turn == 2:
                        pygame.draw.circle(coin_tray, (40, 95, 71), (posx, 37), 37)
                    # place_coin_row(screen, game_state.player_turn, posx)
                # pygame.display.update()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if multiplayer and move_played:
                    #     continue

                    mouse_pos = event.pos
                    posx = mouse_pos[0]
                    if posx < 295:
                        posx = 295
                    if posx > 1072:
                        posx = 1072
                    if posx < 295 + 71 + 53:
                        print(posx - 295 - 71)
                        col_no = 0
                    elif posx > 1072 - (71 + 53):
                        col_no = 6
                    else:
                        posx = posx - 295 - 71
                        col_no = 0
                        prev = 0
                        for j, i in enumerate(columns):
                            if prev < posx < i:
                                col_no = j
                                break
                            else:
                                prev = i

                        # if col_no
                    print(col_no)

                    # user has pressed a column button
                    print(f"col {col_no + 1} was pressed!")
                    player = game_state.player_turn
                    row_no = game_state.add_coin(col_no)
                    if row_no is None:
                        continue
                    row_no = 5 - row_no
                    print(row_no)
                    # create a coin and add it to the list
                    coins.append(
                        # updates the game_state
                        place_coin(
                            board,
                            col_no,
                            row_no,
                            board_pos,
                            player,
                        )
                    )
                    coin_added = True
                    prev_move = game_state.last_move()
                    move_played = True
                    if multiplayer:
                        if game_state.player_turn == 2:
                            game_state.multiplayer_moved = False
                            pass
                        else:
                            cl_sr[1].send(str(5 - row_no) + "#" + str(col_no))
                    # check for win
                    win = game_state.check_win()
                    if win:
                        print(f"player {win} won!")
                        running = False
                        global winner
                        winner = win
                        global loser
                        loser = 1 if win == 2 else 2                                                    
                    pass
                pass
            pass

            # if not coin_added:
            #     time_left = (time_ns() - timer) // (10**9)
            #     if time_left > 15:
            #         print(game_state.player_turn)
            #         game_state.player_turn = 1 if game_state.player_turn == 2 else 2
            #         print("player change", game_state.player_turn)
            #         timer = time_ns()
            #         place_timer(screen, game_state.player_turn, 15)
            #     else:
            #         place_timer(screen, game_state.player_turn, 15 - time_left)
            # else:
            #     timer = time_ns()
            #     place_timer(screen, game_state.player_turn, 15)
            #     pass
            screen.blit(board, board_pos)
            pygame.display.update()
            clock.tick(30)
            pass

def outro(win):
        if winner:
            screen.fill((237, 197, 128))
            pygame.display.update()
            green = (151, 195, 116)
            font = pygame.font.Font("freesansbold.ttf", 60)
            text = font.render(f"Player {win} won", True, green)
            textRect = text.get_rect()
            screen.blit(text, (500, 350) )
            pygame.display.update()
            pygame.time.wait(10000)
        elif loser:
            screen.fill((237, 197, 128))
            pygame.display.update()
            green = (151, 195, 116)
            font = pygame.font.Font("freesansbold.ttf", 60)
            text = font.render(f"Player {win} won", True, green)
            textRect = text.get_rect()
            screen.blit(text, (500, 350) )
            pygame.display.update()
            pygame.time.wait(10000)


intro()
outro(winner)
# main_game()
