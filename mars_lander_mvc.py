"""Framework for MVC mars lander game"""

import pygame
import math

WindowWidth = 640 # width of the program's window, in pixels
WindowHeight = 480 # height in pixels

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

class LanderView(pygame.sprite.Sprite):
	"""Handles display of lander"""
	def __init__(self, model):
		self.model = model

		pygame.sprite.Sprite.__init__(self)

		#Load an imgae from a file
		self.image.load('lander.png')
		self.image = pygame.transform.rotate(self.image, model.Rotation)

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()

		def update(self, model):
			model = self.model
			self.rect.center = (model.X, model.Y)
			pygame.draw

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
	screen = pygame.display.set_mode((WindowWidth, WindowHeight))

	lander = Lander()

	lander_view = LanderView(lander)
	lander_sprite = pygame.sprite.Group(lander_view)
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

		lander_sprite.clear(screen,background)
		lander_sprite.update()
		lander_sprite.draw(screen)

		gauge.draw(background)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()
