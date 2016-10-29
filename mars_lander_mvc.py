"""Framework for MVC mars lander game
"""

import pygame
import math

WindowWidth = 640 # width of the program's window, in pixels
WindowHeight = 480 # height in pixels

class Lander(object):
    """Model of Lander, with attributes, X,Y,Rotation,Fuel,dX, and dY"""

class LanderView(object):
   """Handles display of lander"""
    def __init__(self, model):
        self.model = model

    def draw(self, model):
        model = self.model
        pygame.draw

class LanderSprite(pygame.sprite.Sprite):
    def __init__(self, model):
        self.model = model

        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((0,255,0))
        pygame.draw.circle(self.image,(255,0,0),(25,25),25,0)
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.center =

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image.load('lander.png')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

class Gauge(object):
   """handles display of fuel, altitude, and velocity guages"""

class LanderController(object):
   """Controls key-presses to rotate lander and fire thrusters"""

def main():
    pygame.init()
    screen = pygame.display.set_mode((WindowWidth, WindowHeight))

   """Main function for the code"""

    lander = Lander()

    lander_view = LanderView(lander)
    gauge = Gauge(lander)

    lander = LanderController([lander])

    running = True
    while running == True:
        for event in pygame.event.get():
            controller.handle_event(event)
            if event.type == pygame.QUIT:
                running = False

        lander.step()
        background = pygame.image.load('background.jpg')
        # Use smoothscale() to stretch the background image to fit the entire window:
        background = pygame.transform.smoothscale(background, (WindowWidth, WindowHeight))
        screen.blit(background,(0,0))

        lander_view.draw(background)
        gauge.draw(background)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
