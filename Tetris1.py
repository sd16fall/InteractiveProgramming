import pygame, sys, random
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

colors = [Purple, Red, Green, Aqua, Orange, Blue, Yellow]

'''Dimensions for Screen and Tetris Board'''
block_size = 20 #multiplier for pixels to represent a block
board_height = 20
board_width = 10
board_pix_height = board_height * block_size
board_pix_width = board_width * block_size
screen_height = 480
screen_width = 640
left_margin = 220
top_margin = 70

'''Tetris Pieces'''
t_block = ['OOOOO',
    	'OOOOO',
    	'OOXOO',
    	'OXXXO',
    	'OOOOO']

s_block = ['OOOOO',
    	'OOOOO',
    	'OOXXO',
    	'OXXOO',
    	'OOOOO']

z_block = ['OOOOO',
    	'OOOOO',
    	'OXXOO',
    	'OOXXO',
    	'OOOOO']

i_block = ['OOOOO',
    	'OOOOO',
    	'XXXXO',
    	'OOOOO',
    	'OOOOO']

l_block = [‘OOOOO’,
    	‘OOOXO’,
    	‘XXXXO’,
    	‘OOOOO’,
    	‘OOOOO’]

j_block = [‘OOOOO’,
    	‘OXOOO’,
    	‘OXXXX’,
    	‘OOOOO’,
    	‘OOOOO’]

o_block = [‘OOOOO’,
    	‘OOOOO’,
    	‘OXXOO’,
    	‘OXXOO’,
    	‘OOOOO’]

pieces = [t_block, s_block, z_block, i_block, l_block, j_block, o_block]

def main():
    global screen
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

def addBoard():
    board = []
    for i in range(board_width):
        row = []*board_height
        board.append(row)
    return board

def drawBoard(board):
    pygame.draw.rect(screen, White, (left_margin, top_margin, board_pix_width, board_pix_height), 5)

def makeNewPiece():
    block = random.choice(pieces) #randomly chooses one of the seven pieces
    chosen_color = random.choice(colors)
    new_block = [block,chosen_color]
    return new_block

def draw_box(row, col, new_block, xpixel, ypixel):
    xpix = left_margin + (xpixel * block_size)
    ypix = top_margin + (ypixel * block_size)
    pygame.draw.rect(screen,new_block[1], xpix, ypix, block_size, block_size)

    

if __name__ == '__main__':
    main()
