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


class Button:
    def __init__(self, img_path: str, pos: (int, int)):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        return


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


pygame.init()
screen = pygame.display.set_mode((1366 , 780))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
board = pygame.image.load(r"./assets/board.png")
board_pos = get_board_cord(screen.get_width(), screen.get_height())

# ------------ columns ------------------
columns = [
    Button("assets/button_r (1).png", (325, 50)),
    Button("assets/button_r (2).png", (430, 50)),
    Button("assets/button_r (3).png", (535, 50)),
    Button("assets/button_r (4).png", (640, 50)),
    Button("assets/button_r (5).png", (745, 50)),
    Button("assets/button_r (6).png", (850, 50)),
    Button("assets/button_r (7).png", (955, 50)),
]

# ------------ game loop ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for col_no, col in enumerate(columns):
                if col.rect.collidepoint(mouse_pos):
                    print(f"{col_no + 1} was pressed!")
                pass
            pass

    screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
    screen.blit(board, board_pos)
    pygame.display.update()
    clock.tick(60)
    pass
