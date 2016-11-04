import pygame
import sys
import random
import time
from pygame.locals import *

window_width = 1200
window_height = 1200
p1_wins = 0
p2_wins = 0

class Pikachu(pygame.sprite.Sprite): #making the Pikachu act as a Paddle

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.scale(self.image, (150,200)) #resizing Pikachu
        self.rect = self.image.get_rect() #converting the image into a rectangle for rect attributes
        self.pikac = self.rect
        self.pikac.centery = window_height / 2.0 
        
    def move_pika(self,key):
        if 150 < self.rect.bottom < window_height: #parameters for where pikachu can move
            if key[pygame.K_x]:
                self.rect.centery += 25 #moves pikachu down 
            elif key[pygame.K_s]:
                self.rect.centery -= 25 #moves pikachu up

        elif self.rect.bottom >= window_height: #if pikachu hits the bottom 
            self.rect.centery -= 25
        elif self.rect.bottom <= 150: #if pikachu hits the top 
            self.rect.centery += 25

class PongBall(pygame.sprite.Sprite):
    def __init__(self, pika_one, pika_two):
        pygame.sprite.Sprite.__init__(self)
        pika = Pikachu()
        pika2 = Pikachu2()
        self.pika = pika_one
        self.pika2 = pika_two
        self.image = pygame.image.load('pokeball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,80)) #code to resize the ball image
        self.rect = self.image.get_rect() 
        self.ball = self.rect #making ball a rectangle to get rect attributes
        self.ball.centery = window_height / 2.0 #ball starts at center of screen
        self.ball.centerx = window_width / 2.0
        self.dx = -22
        self.dy = 5

    def set_ball(self): #ball action at beginning of game
        if self.ball.left > 0 or self.ball.right < window_width:
            self.ball.move_ip(self.dx, self.dy)

    def collision_wall(self):
         #instances if ball hits a wall
        if self.ball.top <= 0:
            self.dy = -1*self.dy
        elif self.ball.bottom >= window_height:
            self.dy = -1*self.dy
        elif self.ball.right >= window_width:
            p1_score()
            self.ball.center = (600,600)
            self.dx = -1*self.dx
        elif self.rect.left <= 0:
            p2_score()
            self.ball.center = (600,600)
            self.dx = -1*self.dx

class Pikachu2(Pikachu):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,200)) #code to resize pikachu 2
        self.rect = self.image.get_rect() 
        self.pikac = self.rect
        self.pikac.centery = window_height / 2.0 #setting starting location
        self.pikac.right = window_width

    def move_pika2(self,key):
        if 150 < self.rect.bottom < window_height:
            if key[pygame.K_DOWN]:
                self.rect.centery += 25
            elif key[pygame.K_UP]:
                self.rect.centery -= 25

        elif self.rect.bottom >= window_height:
            self.rect.centery -= 25
        elif self.rect.bottom <= 150:
            self.rect.centery += 25

'''Scoring'''
def p1_score():
    global p1_wins
    p1_wins += 1
    win_game()

def p2_score():
    global p2_wins
    p2_wins += 1
    win_game()

def win_game():
    global p1_wins, p2_wins
    if p1_wins == 5:
        p1_wins = 0
        p2_wins = 0
        p1_wins_text = win_text.render('Player 1 wins!', 1, (255,255,255))
        screen.blit(p1_wins_text, (300,600))
        pygame.display.flip()
        pygame.display.update()
        time.sleep(2)
        reset_game()
    elif p2_wins == 5:
        p1_wins = 0
        p2_wins = 0
        p2_wins_text = win_text.render('Player 2 wins!', 1, (255,255,255))
        screen.blit(p2_wins_text, (300,600))
        pygame.display.flip()
        pygame.display.update()
        time.sleep(2)
        reset_game()

def reset_game():
    global pika, pika2 #resets pikachu locations when someone wins the game
    pika.pikac.centery = window_height / 2.0
    pika2.pikac.centery = window_height / 2.0

'''main'''
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pokemon Pong')
pika = Pikachu()
pika2 = Pikachu2()
pongball = PongBall(pika, pika2)
running = True

while running == True:
    pika.move_pika(pygame.key.get_pressed())
    pika2.move_pika2(pygame.key.get_pressed())
    #calling functions
    pongball.set_ball()
    pongball.collision_wall()
    if pygame.sprite.collide_rect(pongball, pika) or pygame.sprite.collide_rect(pongball, pika2):
        pongball.dx = -1*pongball.dx
        pongball.dy = random.randint(0,20)
    '''text'''
    text = pygame.font.SysFont("Arial", 60)
    win_text = pygame.font.SysFont("Arial", 100)
    p1_render = text.render(str(p1_wins), 1, (255,255,255))
    p2_render = text.render(str(p2_wins), 1, (255,255,255))
    '''image stuff'''
    background = pygame.image.load('grass.png')
    background = pygame.transform.smoothscale(background, (window_width, window_height))
    screen.blit(background, (0,0))
    screen.blit(pika.image, pika.rect)
    screen.blit(pongball.image, pongball.rect)
    screen.blit(pika2.image, pika2.rect)
    screen.blit(p1_render, (50,10))
    screen.blit(p2_render, (1100,10))
    pygame.display.flip()
    pygame.display.update()
    '''quit event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
