"""Framework for MVC mars lander game"""

import pygame
import math

WindowWidth = 1366  # width of the program's window, in pixels
WindowHeight = 768  # ehight of the program's window, in pixels

class Lander(object):
   """Model of Lander, with attributes, X,Y,Rotation,Fuel,dX, and dY
   and methods gravity_update ,roll, and fire_thrusters"""
   def __init__(self):
      self.X = 100  #Lander X coordinate in Pixels
      self.Y = 100 #Lander Y coordinate in Pixels
      self.Rotation = 0 #Lander vertical axis orientation in degrees (from -180 to 180)
      self.Fuel = 1200 #Lander fuel in milliseconds of thruster time
      self.Dx = 0 #Lander velocity in pixels/second to the right
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
      self.Dy += 1 * duration #Accounts for gravity
      self.X += self.Dx * duration/1000
      self.Y += self.Dy * duration/1000
   def reset(self):
      " resets lander position and velocity to initial settings"
      self.X = 100  #Lander X coordinate in Pixels
      self.Y = 100 #Lander Y coordinate in Pixels
      self.Rotation = 0 #Lander vertical axis orientation in degrees (from -180 to 180)
      self.Fuel = 1200 #Lander fuel in milliseconds of thruster time
      self.Dx = 0 #Lander velocity in pixels/second to the right
      self.Dy = 0 #Lander velocity in pixels/second up
     
class LanderView(pygame.sprite.Sprite):
   """Handles display of lander"""
   def __init__(self, model, surface):
      self.surface = surface
      self.model = model
      pygame.sprite.Sprite.__init__(self)
      #Load an image from a file
      self.image = pygame.image.load('lander.png')
      self.image = self.image.convert_alpha()
      self.rect = self.image.get_rect()
   def update(self):
      #Update the position of this object by setting the values of rect.x and rect.y
      self.rect.center = (self.model.X, self.model.Y)
   def reset(self, outcome):
     "takes input of the outcome ('WIN' or 'LOSE' strings) and then changes screen color to outcome state (red for lose, green for win)"
     surface = self.surface
     if outcome == 'WIN':
        pygame.draw.line(surface, (0,255,0), (WindowWidth/2, WindowHeight), (WindowWidth/2, 0), 1366)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)
     elif outcome == 'LOSE':
        pygame.draw.line(surface, (255,0,0), (WindowWidth/2, WindowHeight), (WindowWidth/2 ,0), 1366)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)


class Gauge(object):
  """handles display of fuel, altitude, and velocity guages"""
  def __init__(self, model,surface):
     self.model = model
     self.surface = surface
  def draw(self):
     model = self.model
     surface = self.surface
     pygame.draw.line(surface, (255,0,0), (35, (WindowHeight - 50)), (35, (WindowHeight - 50) - int(model.Fuel * .2)), 20) #draws a red line for the fuel guage , arbitrarily scaled
  

class LanderController(object):
   """Controls key-presses to rotate lander and fire thrusters
        (calls lander methods)"""
   def __init__(self,model,view):
      self.model = model
      self.view = view
   def handle_update(self,duration):
      model = self.model
      view = self.view
      if model.Y >= (WindowHeight - 90) and model.Dx <= 10 and model.Dy <= 10 and model.Dx >= -10 and model.Dy >= -10:
        view.reset("WIN")
        model.reset()
      elif model.Y >= (WindowHeight - 90):
        view.reset("LOSE")
        model.reset()
      else:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
           model.thruster_fire_left(duration)
        if keys[pygame.K_d]:
           model.thruster_fire_right(duration)
        if keys[pygame.K_w]:
           model.thruster_fire_up(duration)
        model.update(duration)

def main():
   """Main function for the code"""
   pygame.init()
   screen = pygame.display.set_mode((WindowWidth, WindowHeight))
   lander = Lander()
   lander_view = LanderView(lander,screen)
   lander_sprite = pygame.sprite.Group(lander_view)
   gauge = Gauge(lander,screen)
   controller = LanderController(lander,lander_view)
   clock = pygame.time.Clock()
   background = pygame.image.load('background.jpg')
   background = pygame.transform.smoothscale(background, (WindowWidth, WindowHeight)) # Use smoothscale() to stretch the background image to fit the entire window
   running = True
   while running == True:
      clock.tick(50)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      controller.handle_update(20)
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
