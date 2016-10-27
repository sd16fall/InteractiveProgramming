import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second
screen = pygame.display.set_mode((800, 600))
screen.fill(0,0,0)
pygame.display.set_caption('Tetris')
while event == True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
            pygame.display.update()
