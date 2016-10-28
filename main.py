import sys
import pygame
import random

# Initliizlies PyGame Window & Gameover Font
pygame.display.init()
pygame.font.init()

# Defineing Color RGB Values for GUI elements
white = (255, 255, 255)
black = (0, 0,0 )
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brick = (144, 69, 53)
sky_blue= (52, 152, 219)

# Sets size of display
display_width = 1200
display_height = 1200

# Sets Top of game Windoe Caption
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Unicorn Squad')

image_pixels = 50
# Defines close of game (Ends program)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Linking color values to GUI elements & Imports iimages and reduces size to 50 by 50px
    gameDisplay.fill(sky_blue)
    unicorn = pygame.image.load('static/unicorn.png')
    unicorn = pygame.transform.scale(unicorn, (image_pixels, image_pixels))
    rainbow = pygame.image.load('static/rainbow.png')
    rainbow = pygame.transform.scale(rainbow, (image_pixels, image_pixels))
    food = pygame.image.load('static/food.png')
    food = pygame.transform.scale(food, (image_pixels, image_pixels))

    clock = pygame.time.Clock()


# The higher the FPS the fasted the sprite moves. We fid that 15 is a good balance for gameplay
FPS = 10

# Initial directio of character sprite
direction = "right"

# Aiisgns font & font size 25 pixels
font = pygame.font.SysFont(None, 55)


# Initlizes up down left right actions
def snake(image_pixels, snakelist):

    if direction == "right":
        head = unicorn

    if direction == "left":
        head = pygame.transform.flip(unicorn, 1, 0)

    if direction == "up":
        head = pygame.transform.rotate(unicorn, 90)

    if direction == "down":
        head = pygame.transform.rotate(unicorn, 270)

    # deifnes movement of snake tail
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    #  defines adding of rainbow image to user sprite
    for XnY in snakelist[:-1]:
        gameDisplay.blit(rainbow,(XnY[0], XnY[1]) )

# Initliazes text object
def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Defines  display message with color variable
def message_to_screen(msg,color, y_displace=0):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

# Sets counnt positoin
def score_to_screen(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (display_width -50), (display_height -50)
    gameDisplay.blit(textSurf, textRect)



# Main game engine -
def gameLoop():
    global direction
    # Sets game exit variblaes to false
    gameExit = False # HItting the close button (closing Window)
    gameOver = False # Internal game over view (HItting the walls or your own tail)

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    # Snake size array
    snakeList = []
    # Sets inital snake length (Snake head counts as 1)
    snakeLength = 1
    player_score = 0


    # Randomly places next block
    randAppleX = round(random.randrange(0, display_width-image_pixels))
    randAppleY = round(random.randrange(0, display_height-image_pixels))

    #  View
    while not gameExit:
        # Game over viwe
        while gameOver == True:
            # Sets window to white
            gameDisplay.fill(white)
            # Sets message text, color, and positoin
            message_to_screen("Game over", red, y_displace=-50)
            message_to_screen("Press C to play again or Q to quit",black, 50)
            pygame.display.update()

            # Maps user close window actio to close og game window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                # Maps keboard strokes to close game and redo game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameLoop()

        # While game in progress (Maps keyboard actions to sprike movements) Controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -image_pixels
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = image_pixels
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -image_pixels
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = image_pixels
                    lead_x_change = 0

        # If you go outside game area horizontlal or vertically
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        # Change player coordinates based on user action
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Defines game ares as skyblue
        gameDisplay.fill(sky_blue)


        # Sets carroat ad player treat and sets random x y coordinates
        # Sets square thickness
        
        gameDisplay.blit(food, (randAppleX,randAppleY))


        unicorn
        # Defines snake head as an empty deict
        snakeHead = []
        # Appends  Initial X and Y coordinates to the snake head
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        # Adds snake head to sake body. Snkae body is an empty dict
        snakeList.append(snakeHead)




        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Runs through each segment of the snake list and checks if the x y corrsoidate of the snake segment equalis the x y coordinates of the snake head
        # ie the snake is overlapping itslef and it runs the game over sequensce
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        # Initlizes the snakeList
        snake(image_pixels, snakeList)

        score_to_screen(str(player_score), white)

        # Updates the screen screen with new movement
        pygame.display.update()

        # Defiens the paraemnts necuasey for player spriite to pick up Apple and add length to snake list
        if lead_x > randAppleX and lead_x < randAppleX + image_pixels or lead_x + image_pixels > randAppleX and lead_x + image_pixels < randAppleX + image_pixels:

            if lead_y > randAppleY and lead_y < randAppleY + image_pixels:
		randAppleX = round(random.randrange(0, display_width-image_pixels))
                randAppleY = round(random.randrange(0, display_height-image_pixels))
                snakeLength += 1
                player_score += 1


            elif lead_y + image_pixels > randAppleY and lead_y + image_pixels < randAppleY + image_pixels:
                randAppleX = round(random.randrange(0, display_width-image_pixels))
                randAppleY = round(random.randrange(0, display_height-image_pixels))
                snakeLength += 1
                # Updates player score as well as as snake lenth
                player_score += 1





        # Rate of referesh
        clock.tick(FPS)


gameLoop()

pygame.display.quit()
pygame.quit()
