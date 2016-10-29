"""Framework for MVC mars lander game
"""

import pygame
import math


class Lander(object):
"""Model of Lander, with attributes, X,Y,Rotation,Fuel,dX, and dY
   and methods gravity_update ,roll, and fire_thrusters"""
   def __init__(self):
      self.X = 600 #Lander X coordinate in Pixels
      self.Y = 400 #Lander Y coordinate in Pixels
      self.Rotation = 0 #Lander vertical axis orientation in degrees (from -180 to 180)
      self.Fuel = 1200 #Lander fuel in milliseconds of thruster time
      self.Dx = 0 #Lander velocity in pixels/second to the right
      self.Dy = 0 #Lander velocity in pixels/second up
   def roll_right(self,duration):
      "Given a duration since last tick in ms and itself, rolls right"
      self.Rotation += 1 *duration/1000 #change this value to tune rollrate
   def roll_left(self,duration):
      "Given a duration since last tick in ms and itself, rolls left"
      self.Rotation -= 1 * duration/1000 #change this value to tune rollrate
   def thruster_fire(self,duration):
      "Fire thrusters to update lander velocity"
      if self.Fuel >= 0:
         self.Dx += math.sin(math.radians(self.Rotation))* 100
         self.Dy += math.cos(math.radians(self.Rotation)) * 100
         self.Fuel -= duration
   def update(self,duration):
      self.Dy -= 10 * duration #Accounts for gravity
      self.X += Dx * duration/1000
      self.Y += Dy * duration/1000      
      
class LanderView(object):
   """Handles display of lander"""

class Gauge(object):
   """handles display of fuel, altitude, and velocity guages"""

class LanderController(object):
   """Controls key-presses to rotate lander and fire thrusters
      (calls lander methods)"""
   def __init__(self,models):
      self.models = models
   def handle_update(self):
      keys=pygame.key.get_pressed()
      if keys[K_LEFT]:
         for model in self.models:
            model.roll_left()
      if keys[K_RIGHT]:
         for model in self.models:
            model.roll_left()
      if keys[K_UP]:
         for model in self.models:
            model.thruster_fire()
      for model in self.models:
         model.update()



def main():
    """Main function for the code"""
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

   if __name__ == '__main__':
    main()
