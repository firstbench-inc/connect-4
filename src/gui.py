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

pygame.init()
screen = pygame.display.set_mode()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    # pygame.draw.circle(screen,(255,255,0),(250,250),75)
    pygame.display.set_caption('image')
 
    imp = pygame.image.load('C:\\Users\\Yash\\Pictures\\board.png')
    screen.blit(imp, (288, 139))
    pygame.display.flip()
pygame.quit()

