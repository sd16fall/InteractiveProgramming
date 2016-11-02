import pygame
import sys
import random
from pygame.locals import *

window_width = 1200
window_height = 1200
class Paddle(pygame.sprite.Sprite): #making the Pikachu act as a Paddle

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.scale(self.image, (150,200)) #code to resize the Pikachu
        self.rect = self.image.get_rect() #pygame rect function converts the image into a rectangle object
        self.pad = self.rect
        self.pad.centery = window_height / 2.0 #rect object in pygame has many built in attributes including values for centery, centerx, top, bottom, left, right etc
                                                #this code starts the Pikachu in the middle left side of the screen

class PongBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pokeball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,80)) #code to resize the ball image
        self.rect = self.image.get_rect()
        self.ball = self.rect
        self.ball.centery = window_height / 2.0 #taking the total window dimensions and dividing by 2 to get the ball in the center of the screen to start
        self.ball.centerx = window_width / 2.0

    def set_ball(self):
        #if the ball is at position 0, then make it go left until it collides or hits the wall
        if self.ball.left > 0:
            self.ball.move_ip(-12,0)
            #  return self.random_move()
            #  print self.ball.center
    #
    # def random_move(self):
    #     rand = random.uniform(-1.0, 1.0)
    #     rand2 = random.uniform (-1.0, 1.0)
    #     print rand, rand2
    #     self.ball.move_ip(rand,rand2)
    #     return self.ball.move_ip(rand, rand2)


    def collision_wall(self):
         #instances if ball hits a wall
         if self.ball.top <= 0:
             pass#self.movement()
         elif self.ball.bottom >= window_height:
             pass#self.movement()
         elif self.ball.right >= window_width:
             self.ball.center = (600,600)
             return self.set_ball()
         elif self.rect.left <= 0:
             self.ball.center = (600, 600)
             return self.set_ball()

    # def collision_pad(self):
    #     if self.ball.left == self.paddle.pad.right:
    #         self.ball.move_ip(10,1)
    # def score(self):
    #     #if ball hits x == 0 or x == 1200, then iterate the score and reset ball to start position
    #     if self.ball.left <= 0: #if the ball hits the left wall, restart it at the center of the screen
    #         self.ball.center = (600,600)
    #         return self.set_ball()

# def movement(self):
#         pass
#     things to do/think about:
#     creating the cpu, printing the score, making a win screen, making the balls speed go faster

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Pokemon Pong')
    paddle = Paddle()
    pongball = PongBall()
    running = True

    while running == True:
        pongball.set_ball()
        pongball.collision_wall()
        #pongball.collision_pad()
        #pongball.score()
        # pongball.random_move()
        key = pygame.key.get_pressed()
        if 140 < paddle.pad.bottom < window_height:
            if key[pygame.K_DOWN]:
                paddle.pad.centery += 15
            elif key[pygame.K_UP]:
                paddle.pad.centery -= 15
        elif paddle.pad.bottom >= window_height:
            paddle.pad.centery -= 15
        elif paddle.pad.bottom <= 140:
            paddle.pad.centery += 15
        '''image stuff'''
        background = pygame.image.load('grass.png')
        background = pygame.transform.smoothscale(background, (window_width, window_height))
        screen.blit(background, (0,0))
        screen.blit(paddle.image, paddle.rect)
        screen.blit(pongball.image, pongball.rect)
        pygame.display.flip()
        pygame.display.update()
        '''quit event'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == "__main__":
    main()
