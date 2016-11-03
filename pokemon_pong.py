import pygame
import sys
import random
from pygame.locals import *

window_width = 1200
window_height = 1200


class Pikachu(pygame.sprite.Sprite): #making the Pikachu act as a Paddle

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.scale(self.image, (150,200)) #code to resize the Pikachu
        self.rect = self.image.get_rect() #pygame rect function converts the image into a rectangle object
        self.pikac = self.rect
        self.pikac.centery = window_height / 2.0 #rect object in pygame has many built in attributes including values for centery, centerx, top, bottom, left, right etc
                                                 #this code starts the Pikachu in the middle left side of the screen
        #self.pika_rect = self.pikac.move(x,y)

    def move_pika(self,key):
        if 150 < self.rect.bottom < window_height:
            if key[pygame.K_DOWN]:
                self.rect.centery += 15
                print "pika: " + str(self.rect.bottom)
            elif key[pygame.K_UP]:
                self.rect.centery -= 15

        elif self.rect.bottom >= window_height:
            self.rect.centery -= 15
        elif self.rect.bottom <= 150:
            self.rect.centery += 15

class PongBall(pygame.sprite.Sprite):
    def __init__(self, this_pika, pika_two):
        pygame.sprite.Sprite.__init__(self)
        pika = Pikachu()
        pika2 = AIPikachu()
        self.pika = this_pika
        self.pika2 = pika_two
        self.image = pygame.image.load('pokeball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,80)) #code to resize the ball image
        self.rect = self.image.get_rect()
        self.ball = self.rect
        self.ball.centery = window_height / 2.0 #taking the total window dimensions and dividing by 2 to get the ball in the center of the screen to start
        self.ball.centerx = window_width / 2.0
        self.dx = -12
        self.dy = 5

    def set_ball(self): #,dx = -12, dy =0):
        #if the ball is at position 0, then make it go left until it collides or hits the wall
        if self.ball.left > 0 or self.ball.right < window_width:
            self.ball.move_ip(self.dx, self.dy)

    def collision_pikachu(self):
        if self.pika.rect.right >= self.ball.left:
            if (self.ball.bottom >= self.pika.rect.top and self.ball.bottom <= self.pika.rect.bottom) or  (self.ball.top <= self.pika.rect.top and self.ball.top >= self.pika.rect.bottom):
                print "hi"
                self.dx = -1*self.dx

    def collision_pikachu2(self):
        if self.ball.right >= self.pika2.rect.left:
            print "pika bottom", self.pika2.rect.bottom, 'pika top', self.pika2.rect.top, 'ball top', self.ball.top, 'ball bottom', self.ball.bottom
            if (self.ball.bottom >= self.pika2.rect.top and self.ball.bottom <= self.pika2.rect.bottom) or  (self.ball.top <= self.pika2.rect.top and self.ball.top >= self.pika2.rect.bottom):
                print "hi"
                self.dx = -1*self.dx

    def collision_wall(self):
         #instances if ball hits a wall
        if self.ball.top <= 0:
            self.dy = -1*self.dy
        elif self.ball.bottom >= window_height:
            self.dy = -1*self.dy
        elif self.ball.right >= window_width:
            self.ball.center = (600,600)
            self.dx = -1*self.dx
        elif self.rect.left <= 0:
            self.ball.center = (600,600)
            self.dx = -1*self.dx

    """def check_collision_wall(self):
         #instances if ball hits a wall
        if self.ball.top <= 0:
            return True
        elif self.ball.bottom >= window_height:
            return True
        elif self.ball.right >= window_width:
            self.ball.center = (600,600)
            return True
        elif self.rect.left <= 0:
            self.ball.center = (600, 600)
            return True
        return False"""

class AIPikachu(Pikachu):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,200)) #code to resize the Pikachu
        self.rect = self.image.get_rect() #pygame rect function converts the image into a rectangle object
        self.pikac = self.rect
        self.pikac.centery = window_height / 2.0 #rect object in pygame has many built in attributes including values for centery, centerx, top, bottom, left, right etc
                                            #this code starts the Pikachu in the middle left side of the screen
        self.pikac.right = window_width
        self.direction = 'down'

    def move_AI(self,key):
        if 150 < self.rect.bottom < window_height:
            if key[pygame.K_x]:
                self.rect.centery += 15
                print "pika: " + str(self.rect.bottom)
            elif key[pygame.K_s]:
                self.rect.centery -= 15

        elif self.rect.bottom >= window_height:
            self.rect.centery -= 15
        elif self.rect.bottom <= 150:
            self.rect.centery += 15

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pokemon Pong')
pika = Pikachu()
pika2 = AIPikachu()
pongball = PongBall(pika, pika2)

running = True
while running == True:
    pika.move_pika(pygame.key.get_pressed())
    pika2.move_AI(pygame.key.get_pressed())
    pongball.set_ball()
    pongball.collision_pikachu()
    pongball.collision_pikachu2()
    pongball.collision_wall()

    '''image stuff'''
    background = pygame.image.load('grass.png')
    background = pygame.transform.smoothscale(background, (window_width, window_height))
    screen.blit(background, (0,0))
    screen.blit(pika.image, pika.rect)
    screen.blit(pongball.image, pongball.rect)
    screen.blit(pika2.image, pika2.rect)
    pygame.display.flip()
    pygame.display.update()
    '''quit event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
