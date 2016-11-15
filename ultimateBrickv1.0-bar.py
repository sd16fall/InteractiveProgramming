import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
x_position=0
xx_position=780
y_position=580
yy_position=600
x_move = 0
x2_move = 0
x2_position=650
y2_position=0
xx2_position=0
yy2_position=-150
gamerun = True
clock = pygame.time.Clock()
screen.fill((255,255,255))
pygame.draw.rect(screen,(0,0,0),[x_position,y_position,150,20])
upperslide = pygame.Surface((780,580))
upperslide.fill((255,255,255))
pygame.draw.rect(upperslide,(0,0,0),[x2_position,y2_position,150,20])
screen.blit(upperslide,(0,0))
while gamerun == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_move = -10
            if event.key == pygame.K_RIGHT:
                x_move = 10
            if event.key == pygame.K_q:
                x2_move = -10
            if event.key == pygame.K_e:
                x2_move = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_move = 0
            if event.key == pygame.K_RIGHT:
                x_move = 0
            if event.key == pygame.K_q:
                x2_move = 0
            if event.key == pygame.K_e:
                x2_move = 0
    x_position += x_move
    x2_position += x2_move
    if x_position >800 and x_position <1280:
        screen.fill((255,255,255))
        yy_position -= x_move
        pygame.draw.rect(screen,(0,0,0),[xx_position,yy_position,20,150])
    if x_position >=650 and x_position <=800:
        screen.fill((255,255,255))
        yy_position -= x_move
        pygame.draw.rect(screen,(0,0,0),[xx_position,yy_position,20,150])
        pygame.draw.rect(screen,(0,0,0),[x_position,y_position,150,20])
    if x_position < 650 and x_position > 0:
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(0,0,0),[x_position,y_position,150,20])
        yy_position = 600
    if x_position < 0:
        x_position = 0
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(0,0,0),[x_position,y_position,150,20])
    if x_position >1280:
        screen.fill((255,255,255))
        yy_position = 0
        x_position = 1281
        pygame.draw.rect(screen,(0,0,0),[xx_position,yy_position,20,150])
    if x2_position >=-580 and x2_position <-150:
        upperslide.fill((255,255,255))
        yy2_position -= x2_move
        pygame.draw.rect(upperslide,(0,0,0),[xx2_position,yy2_position,20,150])
    if x2_position >=-150 and x2_position <=0:
        upperslide.fill((255,255,255))
        yy2_position -= x2_move
        pygame.draw.rect(upperslide,(0,0,0),[xx2_position,yy2_position,20,150])
        pygame.draw.rect(upperslide,(0,0,0),[x2_position,y2_position,150,20])
    if x2_position <= 630 and x2_position > 0:
        upperslide.fill((255,255,255))
        pygame.draw.rect(upperslide,(0,0,0),[x2_position,y2_position,150,20])
        yy2_position = -150
    if x2_position > 630:
        x2_position = 630
        upperslide.fill((255,255,255))
        pygame.draw.rect(upperslide,(0,0,0),[x2_position,y2_position,150,20])
    if x2_position <-580:
        upperslide.fill((255,255,255))
        yy2_position = 430
        x2_position = -581
        pygame.draw.rect(upperslide,(0,0,0),[xx2_position,yy2_position,20,150])
    screen.blit(upperslide,(0,0))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
