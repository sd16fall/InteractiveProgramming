import sys
import pygame
import random


#pygame.display.init()
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



def snake(block_size, snakelist):

    if direction == "right":
        head = unicorn

    if direction == "left":
        head = pygame.transform.flip(unicorn, 1, 0)

    if direction == "up":
        head = pygame.transform.rotate(unicorn, 90)

    if direction == "down":
        head = pygame.transform.rotate(unicorn, 270)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size))
    randAppleY = round(random.randrange(0, display_height-block_size))
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace=-50)
            message_to_screen("Press C to play again or Q to quit",black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(sky_blue)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        
        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
		randAppleX = round(random.randrange(0, display_width-block_size))
                randAppleY = round(random.randrange(0, display_height-block_size))
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width-block_size))
                randAppleY = round(random.randrange(0, display_height-block_size))
                snakeLength += 1


        clock.tick(FPS)


gameLoop()

pygame.display.quit()
pygame.quit()

