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


# layout = [[pg.Button('r1','center',visible=True)]]
# window = pg.Window('layout',layout)
# while True:
#   event , values = window.read()
#   if event == 'ok' or event == pg.WIN_CLOSED:
#     break
# window.close() 


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255,255,255))
    # pygame.draw.circle(screen,(255,255,0),(250,250),75)
pygame.display.set_caption('image')

imp = pygame.image.load(r'./assets/board.png').convert_alpha()
r1 = pygame.image.load(r'./assets/button_r (1).png').convert_alpha()
r2 = pygame.image.load(r'./assets/button_r (2).png')
r3 = pygame.image.load(r'./assets/button_r (3).png')
r4 = pygame.image.load(r'./assets/button_r (4).png')
r5 = pygame.image.load(r'./assets/button_r (5).png')
r6 = pygame.image.load(r'./assets/button_r (6).png')
r7 = pygame.image.load(r'./assets/button_r (9).png')
class Button():
      def __init__(self,image,x,y):
          self.image = image
          self.x = x
          self.y = y
          
      def draw(self):
       pos = pygame.mouse.get_pos()
       if self.image.collide_point(pos) == 1:
        #checking if pointer is clicking on the image
        if pygame.mouse.get_pressed()[0] == 1:
         running = False
       screen.bilt(self.image , (self.x,self.y))

sc = Button(imp,288 , 139)
b1 =Button(r1,325 , 50)
running = True
while running:
    sc.draw()
    b1.draw()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    
    
screen.blit(imp, (288, 139))
#     screen.blit(r1, (325, 50))
#     screen.blit(r2, (430, 50))
#     screen.blit(r3, (535, 50))
#     screen.blit(r4, (640, 50))
#     screen.blit(r5, (745, 50))
#     screen.blit(r6, (850, 50))
#     screen.blit(r7, (955, 50))
pygame.display.flip()
pygame.quit()

