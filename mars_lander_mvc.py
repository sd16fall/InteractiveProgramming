"""Framework for MVC mars lander game
"""

import pygame

class Lander(object):
"""Model of Lander, with attributes, X,Y,Rotation,Fuel,dX, and dY
   and methods gravity_update ,roll, and fire_thrusters"""

class LanderView(object):
   """Handles display of lander"""

class Gauge(object):
   """handles display of fuel, altitude, and velocity guages"""

class LanderController(object):
   """Controls key-presses to rotate lander and fire thrusters
      (calls lander methods)"""


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

   """Main function for the code"""


if __name__ == '__main__':
    main()
