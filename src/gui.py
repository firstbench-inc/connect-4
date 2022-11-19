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


class Button:
    def __init__(self, img_path: str, pos: (int, int)):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        return


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


def place_coin(surface, col_no: int, row_no: int, board_pos: (int, int), player: int):
    pos_x = board_pos[0] + 71 + 106 * (col_no)
    pos_y = board_pos[1] + 51 + 77 * (row_no)
    if player == 1:
        return pygame.draw.circle(surface, (125, 24, 28), (pos_x, pos_y), 37)
    if player == 2:
        return pygame.draw.circle(surface, (40, 95, 71), (pos_x, pos_y), 37)


# ------------ pygame init -------------
pygame.init()

# running = True
screen = pygame.display.set_mode((1366, 780))
# # screen.fill((255, 255, 255))
# clock = pygame.time.Clock()

board = pygame.image.load(r"./assets/board2.png")
bg = pygame.image.load(r"./assets/bg1.jpg")

board = pygame.image.load(r"assets/board2.png")

board_pos = get_board_cord(screen.get_width(), screen.get_height())
vid = Video("./assets/intro1.mp4")
vid.set_size((1366, 780))


def intro():
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("meow")
                vid.__del__()
                print("meow deleted")
                main_game()
                return


def main_game():
    running = True

    clock = pygame.time.Clock()
    # ----------- game init -----------------
    game_state = game.Game()
    coins = []

    # ------------ columns ------------------
    columns = []
    start_point = board_pos[0] + 32
    for i in range(1, 8):
        columns.append(
            Button(f"assets/button_r ({i}).png", (start_point + 106 * (i - 1), 50))
        )
        pass

    # ------------ game loop ----------------

    screen.blit(bg, (0, 0))
    screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
    screen.blit(board, board_pos)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for col_no, col in enumerate(columns):
                    if col.rect.collidepoint(mouse_pos):
                        # user has pressed a column button
                        print(f"col {col_no + 1} was pressed!")
                        row_no = game_state.add_coin(col_no)
                        if row_no is None:
                            continue
                        row_no = 5 - row_no
                        print(row_no)
                        # create a coin and add it to the list
                        coins.append(
                            # updates the game_state
                            place_coin(
                                screen,
                                col_no,
                                row_no,
                                board_pos,
                                game_state.player_turn,
                            )
                        )
                        # check for win
                        win = game_state.check_win()
                        if win:
                            print(f"player {win} won!")
                            running = False
                    pass
                pass
        # intro()
        pygame.display.update()
        clock.tick(60)
        pass


intro()
