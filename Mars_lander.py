"""MVC mars lander game
Land dragon on Mars with arrow keys"""

import pygame
import math

WindowWidth = 1366  # width of the program's window, in pixels
WindowHeight = 768  # height of the program's window, in pixels

class Lander(object):
   """Model of Lander, with attributes, X,Y,Rotation,Fuel,dX, and dY
   and methods gravity_update ,roll, and fire_thrusters"""
   def __init__(self):
      self.X = 100  #Lander X coordinate in Pixels
      self.Y = 100 #Lander Y coordinate in Pixels
      self.Rotation = 0 #Lander vertical axis orientation in degrees (from -180 to 180)
      self.Fuel = 1200 #Lander fuel in milliseconds of thruster time
      self.Dx = 100 #Lander velocity in pixels/second to the right
      self.Dy = 0 #Lander velocity in pixels/second up
   def thruster_fire_right(self,duration):
      "Given a duration since last tick in ms and itself, translates right"
      #Checks if there is fuel, if there is translates and updates remaining fuel
      if self.Fuel >= 0:
          self.Dx += 1000/duration
          self.Fuel -= duration
   def thruster_fire_left(self,duration):
      "Given a duration since last tick in ms and itself, translates left"
      #Checks if there is fuel, if there is translates and updates remaining fuel
      if self.Fuel >= 0:
          self.Dx -= 1000/duration
          self.Fuel -= duration
   def thruster_fire_up(self,duration):
       "Given a duration since last tick in ms and itself, translates up"
       #Checks if there is fuel, if there is translates and updates remaining fuel
       if self.Fuel >= 0:
          self.Dy -= 1000/duration
          self.Fuel -= duration
   def update(self,duration):
      self.Dy += 1 * duration #Updates Dy to Account for gravity
      self.X += self.Dx * duration/1000 #Updates X according to Dx
      self.Y += self.Dy * duration/1000 #Updates Y according to DY
   def reset(self):
      " resets lander position and velocity to initial settings"
      self.X = 100  #Lander X coordinate in Pixels
      self.Y = 100 #Lander Y coordinate in Pixels
      self.Rotation = 0 #Lander vertical axis orientation in degrees (from -180 to 180)
      self.Fuel = 1200 #Lander fuel in milliseconds of thruster time
      self.Dx = 100 #Lander velocity in pixels/second to the right
      self.Dy = 0 #Lander velocity in pixels/second up
     
class LanderView(pygame.sprite.Sprite):
   """Handles display of lander"""
   def __init__(self, model, surface):
      self.surface = surface #surface to display sprite on 
      self.model = model #model that the sprite should display
      pygame.sprite.Sprite.__init__(self)
      #Load an image from a file and set the Sprite's rect attribute to the size of the image
      self.image = pygame.image.load('lander.png')
      self.image = self.image.convert_alpha()
      self.rect = self.image.get_rect()
   def update(self):
      """Update the position of this sprite by setting the values of rect.center.x and rect.center.y"""
      self.rect.center = (self.model.X, self.model.Y)
   def reset(self, outcome):
     "Takes input of the outcome ('WIN' or 'LOSE' strings) and then flashes screen color to outcome state (red for lose, green for win)"
     surface = self.surface
     if outcome == 'WIN':
        #If win, fill screen green, update display, and wait a second so user can see green box
        pygame.draw.line(surface, (0,255,0), (WindowWidth/2, WindowHeight), (WindowWidth/2, 0), 1366)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)
     elif outcome == 'LOSE':
        #If lose, fill screen red, update display, and wait a second so user can see green box
        pygame.draw.line(surface, (255,0,0), (WindowWidth/2, WindowHeight), (WindowWidth/2 ,0), 1366)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)


class Gauge(object):
  """handles display of fuel gauge"""
  def __init__(self, model,surface):
     """sets model and view attributes based on model and view that is passed in"""
     self.model = model
     self.surface = surface 
  def draw(self):
     """draws gauge"""
     model = self.model
     surface = self.surface
     #draws a red line for the fuel guage , arbitrarily scaled
     pygame.draw.line(surface, (255,0,0), (35, (WindowHeight - 50)), (35, (WindowHeight - 50) - int(model.Fuel * .2)), 20) 
  

class LanderController(object):
   """Controls key-presses to rotate lander and fire thrusters
        (calls lander methods)"""
   def __init__(self,model,view):
      """sets model and view attributes based on model and view that is passed in"""
      self.model = model
      self.view = view
   def handle_update(self,duration):
      """controls model based on key presses,detects collison with the ground and commands "WIN" or "LOSE" reset"""
      model = self.model
      view = self.view
      #On contact with ground, check velocity
      if model.Y >= (WindowHeight - 90) and model.Dx <= 200 and model.Dy <= 200 and model.Dx >= -200 and model.Dy >= -10:
        #if velocity is low enough, flash screen green and reset
        view.reset("WIN")
        model.reset()
      elif model.Y >= (WindowHeight - 90):
        #otherwise, flash screen red and reset
        view.reset("LOSE")
        model.reset()
      else:
        #if no contact with the ground,
        keys=pygame.key.get_pressed()
        #if A pressed, fire left
        if keys[pygame.K_a]: 
           model.thruster_fire_left(duration)
        #if D pressed, fire right
        if keys[pygame.K_d]:
           model.thruster_fire_right(duration)
        #if W pressed, fire up
        if keys[pygame.K_w]:
           model.thruster_fire_up(duration)
        model.update(duration)

def main():
   """Main function for the code"""
   pygame.init() #start pygame
   screen = pygame.display.set_mode((WindowWidth, WindowHeight)) #make screen of proper window size
   lander = Lander() #initialize lander class
   lander_view = LanderView(lander,screen) #initialize lander view with lander class
   lander_sprite = pygame.sprite.Group(lander_view)  #initialize lander sprite with lander view
   gauge = Gauge(lander,screen)  #initialize gauge object
   controller = LanderController(lander,lander_view)#initialize controller object
   clock = pygame.time.Clock() #start pygame clock to keep track of frame duration and framerate
   background = pygame.image.load('background.jpg')
   background = pygame.transform.smoothscale(background, (WindowWidth, WindowHeight)) # Use smoothscale() to stretch the background image to fit the entire window
   running = True
   while running == True:
      clock.tick(50) #sets framerate to 50 fps
      #handle pygame quit
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      controller.handle_update(20) #call controller update with duration of 20 ms (50 FPS)
      #Draw game and update display
      screen.blit(background,(0,0))
      lander_sprite.clear(screen,background)
      lander_sprite.update()
      lander_sprite.draw(screen)
      gauge.draw()
      pygame.display.flip()
      pygame.display.update()
   pygame.quit()


if __name__ == '__main__':
   main()
