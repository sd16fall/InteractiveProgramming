class Viewer(objects):
    def message_to_screen(msg,color, y_displace=0):
        textSurf, textRect = text_objects(msg,color)
        textRect.center = (display_width / 2), (display_height / 2)+y_displace
        gameDisplay.blit(textSurf, textRect)
    def text_objects(text,color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
        
    if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

        if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
    randAppleX = round(random.randrange(0, display_width-block_size))
            randAppleY = round(random.randrange(0, display_height-block_size))
            snakeLength += 1

        elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
            randAppleX = round(random.randrange(0, display_width-block_size))
            randAppleY = round(random.randrange(0, display_height-block_size))
            snakeLength += 1
