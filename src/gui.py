"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at runtime
  as it was on development.
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


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


pygame.init()
screen = pygame.display.set_mode()
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
board = pygame.image.load(r"./assets/board.png")
board_pos = get_board_cord(screen.get_width(), screen.get_height())

# ------------ columns ------------------
columns = [
    pygame.image.load("assets/button_r (1).png").convert_alpha(),
    pygame.image.load("assets/button_r (2).png").convert_alpha(),
    pygame.image.load("assets/button_r (3).png").convert_alpha(),
    pygame.image.load("assets/button_r (4).png").convert_alpha(),
    pygame.image.load("assets/button_r (5).png").convert_alpha(),
    pygame.image.load("assets/button_r (6).png").convert_alpha(),
    pygame.image.load("assets/button_r (7).png").convert_alpha(),
]

col_coords = [100, 200, 300, 400, 500, 600, 700]

col_rects = [
    col.get_rect(topleft=(col_coords[cno], 50)) for cno, col in enumerate(columns)
]

# ------------ game loop ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for col_no, col in enumerate(col_rects):
                if col.collidepoint(mouse_pos):
                    print(f"{col_no + 1} was pressed!")
                pass
            pass

    screen.blits(((col, (col_coords[i], 50)) for i, col in enumerate(columns)))
    screen.blit(board, board_pos)
    pygame.display.update()
    clock.tick(60)
    pass
