import pygame
import sys
import random
from pygame.locals import *

window_width = 1200
window_height = 1200
p_wins = 0
AI_wins = 0

class Pikachu(pygame.sprite.Sprite): #making the Pikachu act as a Paddle

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pikachu.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.scale(self.image, (150,200)) #code to resize the Pikachu
        self.rect = self.image.get_rect() #pygame rect function converts the image into a rectangle object
        self.pikac = self.rect
        self.pikac.centery = window_height / 2.0 #rect object in pygame has many built in attributes including values for centery, centerx, top, bottom, left, right etc
                                                 #this code starts the Pikachu in the middle left side of the screen
        self.pika_rect = self.pikac.move(x,y)

    def move_pika(self,key):
        if 150 < self.rect.bottom < window_height:
            if key[pygame.K_DOWN]:
                self.rect.centery += 15
            elif key[pygame.K_UP]:
                self.rect.centery -= 15
        elif self.rect.bottom >= window_height:
            self.rect.centery -= 15
        elif self.rect.bottom <= 150:
            self.rect.centery += 15

class PongBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pika = Pikachu(0,0)
        self.pika = (pika.pika_rect)
        self.image = pygame.image.load('pokeball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,80)) #code to resize the ball image
        self.rect = self.image.get_rect()
        self.ball = self.rect
        self.ball.centery = window_height / 2.0 #taking the total window dimensions and dividing by 2 to get the ball in the center of the screen to start
        self.ball.centerx = window_width / 2.0

    def set_ball(self):
        #if the ball is at position 0, then make it go left until it collides or hits the wall
        if self.ball.left > 0:
            self.ball.move_ip(-10,0)

    """def collision_pikachu(self,target):
        print self.ball.colliderect(target)
        return self.ball.colliderect(target)
        collide = False
        print self.pika.right
        print self.ball.left
        if self.pika.right <= self.ball.left:
            collide = True
        return collide"""

    def collision_wall(self):
         #instances if ball hits a wall
        if self.ball.top <= 0:
            pass
        elif self.ball.bottom >= window_height:
            pass
        elif self.ball.right >= window_width:
            self.ball.center = (600,600)
            player_score()
            return self.set_ball()
        elif self.rect.left <= 0:
            self.ball.center = (600, 600)
            AI_score()
            return self.set_ball()

    # def check_collision_wall(self):
    #      #instances if ball hits a wall
    #     if self.ball.top <= 0:
    #         return True
    #     elif self.ball.bottom >= window_height:
    #         return True
    #     elif self.ball.right >= window_width:
    #         self.ball.center = (600,600)
    #         return True
    #     elif self.rect.left <= 0:
    #         self.ball.center = (600, 600)
    #         return True
    #     return False

#     def collision_pikas(self):
#         if pygame.sprite.spritecollide(Pikachu, PongBall, True):
            

class AIPikachu(pygame.sprite.Sprite):
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

    def move_AI(self): #if pikachu hits a wall, move in the opposite direction
        if self.direction == 'down':
            self.pikac.centery +=15
            if self.pikac.bottom >= window_height:
                self.direction = 'up'
        elif self.direction == 'up':
            self.pikac.centery -=15
            if 150 > self.pikac.bottom:
                self.direction = 'down'
                
def player_score():
    global p_wins
    p_wins += 1
    win_game

def AI_score():
    global AI_wins
    AI_wins += 1
    win_game()

def win_game():
    global p_wins, AI_wins
    if p_wins == 5:
        p_wins = 0
        AI_wins = 0
        #p_wins_text = text.render('You win!', 1, (255,0,0))
        reset_game()
    elif AI_wins == 5:
        p_wins = 0
        AI_wins = 0
        #AI_wins_text = text.render('You lose!',1 (255,0,0))
        reset_game()

def reset_game():
    global pika
    pika.pikac.centery = window_height / 2.0

'''main'''
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pokemon Pong')
pika = Pikachu(0,0)
pongball = PongBall()
pika2 = AIPikachu()
running = True
while running == True:
    pika.move_pika(pygame.key.get_pressed())
    pika2.move_AI()
    pongball.set_ball()
    pongball.collision_wall()
    #pongball.collision(pika)
    # pongball.collision_pikas()

    """if pygame.sprite.collide_rect(pika, pongball):
        pongball.ball.centery -= 50
        pongball.ball.centerx -= 0
        pongball.ball.move_ip(-15,-10)"""

    #pongball.collision_pad()
    #pongball.score()
    # pongball.random_move()
    # '''moving Pikachu'''
    # if 150 < pikachu.pika.bottom < window_height:
    #     if key[pygame.K_DOWN]:
    #         pikachu.pika.centery += 15
    #     elif key[pygame.K_UP]:
    #         pikachu.pika.centery -= 15
    # elif pikachu.pika.bottom >= window_height:
    #     pikachu.pika.centery -= 15
    # elif pikachu.pika.bottom <= 150:
    #     pikachu.pika.centery += 15
    '''text'''
    text = pygame.font.SysFont("Arial", 60)
    win_text = pygame.font.SysFont("Arial", 200)
    p_render = text.render(str(p_wins), 1, (255,0,0))
    AI_render = text.render(str(AI_wins), 1, (255,0,0))
    '''image stuff'''
    background = pygame.image.load('grass.png')
    background = pygame.transform.smoothscale(background, (window_width, window_height))
    screen.blit(background, (0,0))
    screen.blit(pika.image, pika.rect)
    screen.blit(pongball.image, pongball.rect)
    screen.blit(pika2.image, pika2.rect)
    screen.blit(p_render, (50,10))
    screen.blit(AI_render, (1100,10))
    #screen.blit(p_wins_text, (600,600))
    #screen.blit(AI_wins_text, (600,600))
    pygame.display.flip()
    pygame.display.update()
    '''quit event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

