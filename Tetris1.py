import pygame, sys
from pygame.locals import *

'''Color Definitions'''
Purple = (80, 0.0, 120)
Red = (240, 0.0, 0.0)
Green = (0.0, 240, 0.0)
Aqua = (0.0, 240, 240)
Orange = (240, 160, 0.0)
Blue = (0.0, 0.0, 240)
Yellow = (240, 240, 0.0)
Black = (0.0,0.0,0.0)
White = (255, 255, 255)


'''Dimensions for Screen and Tetris Board'''
block_size = 20 #multiplier for pixels to represent a block
board_height = 20
board_width = 10
board_pix_height = board_height * block_size
board_pix_width = board_width * block_size
screen_height = 480
screen_width = 640
left_margin = 220
top_margin = 80

def main():
    pygame.init()

    FPS = 30 #frames per second
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(Black)
    pygame.display.set_caption('Tetris')
    drawBoard(screen)
    #while event == True: #main game loop
    #    for event in pygame.event.get():
    #        if event.type == QUIT:
    #            pygame.quit()
    #            sys.exit
    pygame.display.update()
