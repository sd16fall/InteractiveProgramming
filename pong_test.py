import pygame
import sys
import random
from pygame.locals import *

window_width = 800
window_height = 1200
class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image.png')
        self.image = self.image.get_rect()
        self.image.y = window_height / 2.0

    def can_move(self, dy):
        new_dy = self.image.y + dy
        if new_dy == window_height:
            return False
        elif new_dy == 0:
            return False
        return True

    def movement(self, key):
        if key == K_DOWN:
            self.image.y -= 50
        elif key == K_UP:
            self.image.y += 50

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    paddle = Paddle()
    key = pygame.key.get_pressed()
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
