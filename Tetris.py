import pygame, sys
from pygame.locals import *

Score_P1 = 0
Score_P2 = 0
pygame.init()

FPS = 30 #frames per second
Surf = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tetris')
    while Score_P1 < 3 or Score_P2 < 3: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
        pygame.display.update()
