class Model(object):
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
