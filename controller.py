class Controller(object):
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
