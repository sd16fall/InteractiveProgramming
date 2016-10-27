import pygame, sys
from pygame.locals import *

Purple = (80, 0.0, 120)
Red = (240, 0.0, 0.0)
Green = (0.0, 240, 0.0)
Aqua = (0.0, 240, 240)
Orange = (240, 160, 0.0)
Blue = (0.0, 0.0, 240)
Yellow = (240, 240, 0.0)
Black = (0.0,0.0,0.0)
White = (255, 255, 255)

board_height = 20
board_width = 10

def main():
    pygame.init()

    FPS = 30 #frames per second
    screen = pygame.display.set_mode((800, 600))
    screen.fill(Black)
    pygame.display.set_caption('Tetris')
    drawBoard(screen)
    #while event == True: #main game loop
    #    for event in pygame.event.get():
    #        if event.type == QUIT:
    #            pygame.quit()
    #            sys.exit
    pygame.display.update()


def drawBoard(screen):
    board = []
    for i in range(board_width):
        row = [None]*board_height
        board.append(row)
        return board

    pygame.draw.rect(screen, White, (150,20, 250, 500), 5)

if __name__ == '__main__':
    main()
