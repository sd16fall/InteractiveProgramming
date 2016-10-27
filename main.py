import sys
import pygame
import random


pygame.display.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0,0 )
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brick = (144, 69, 53)
sky_blue= (52, 152, 219)

display_width = 1200
display_height = 1200
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Unicorn Squad')

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    gameDisplay.fill(sky_blue)
    unicorn = pygame.image.load('unicorn.png')
    unicorn = pygame.transform.scale(unicorn, (50, 50))
    rainbow = pygame.image.load('rainbow.png')
    rainbow = pygame.transform.scale(rainbow, (50, 50))
    food = pygame.image.load('food.png')
    food = pygame.transform.scale(food, (50, 50))

clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

font = pygame.font.SysFont(None, 25)

clock.tick(FPS)


gameLoop()

pygame.display.quit()
pygame.quit()
