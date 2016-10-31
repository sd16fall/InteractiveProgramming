"""main.py

objects: screen, player, follower

TODO:
- train constant speed
- player slows down
- lose on collision
- flat level

DONE:
- simple objects for player sprite"""

import pygame
import math

# Images
gameover = pygame.image.load('gameover1.bmp')

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
DIMGRAY = (105,105,105)
SLATEGRAY = (112,128,144)

"""Model classes"""
class Player(object):
	def __init__(self,x=0,y=0,width=50,height=50,dx=1,shiftdx=0):
		# places player centered above the coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.dx = dx
		self.shiftdx = shiftdx

	def train_wreck(self, train):
		return (train.x+train.width) > self.x

	def shift_world(self):
		return self.x > 350

	def go_back(self):
		return self.x < 130

class PainTrain(object):
	def __init__(self,x=0,y=0,width=200,height=200,constdx=.05,dx=0,shiftdx=-1):
		# places train centered above coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.constdx = constdx
		self.dx = dx
		self.shiftdx = shiftdx

	def step(self):
		self.x += self.constdx

# classes for level objects
class Ground(object):
	def __init__(self, x = 0, y = 300, width = 2400, height = 180,dx=0,shiftdx=-1):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx
		self.shiftdx = shiftdx

class Platform(object):
	def __init__(self, x=0,y=0,width = 100, height = 20, dx=0, shiftdx=-1):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx
		self.shiftdx = shiftdx

"""View classes"""
class PlayerView(object):
	def __init__(self, model):
		self.model = model

	def draw(self, surface):
		model = self.model
		# this takes (x,y,width,height)
		pygame.draw.rect(surface,SLATEGRAY,(model.x,model.y,model.width,model.height))

class PainTrainView(object):
	def __init__(self, model):
		self.model = model

	def draw(self, surface):
		model = self.model
		# this takes (x,y,width,height)
		pygame.draw.rect(surface,BLACK,(model.x,model.y,model.width,model.height))

class GroundView(object):
	def __init__(self, model):
		self.model = model

	def draw(self, surface):
		model = self.model
		# this takes (x,y,width,height)
		pygame.draw.rect(surface,DIMGRAY,(model.x,model.y,model.width,model.height))

class ObstacleView(object):
	# can be used for any rectangular object
	def __init__(self,model):
		self.model = model

	def draw(self,surface):
		model = self.model
		pygame.draw.rect(surface,BLACK,(model.x,model.y,model.width,model.height))

"""Controller classes"""
class Controller(object):
	def __init__(self,models):
		self.models = models
		self.player = models[0] # make sure this aligns with controlled_models in main

	def handle_event(self):
		# time passed isn't actually time based... based on while loop efficiency
		player = self.player
		models = self.models
		for model in models:
			keys = pygame.key.get_pressed() # checking pressed keys
			if keys[pygame.K_LEFT]:
				if player.go_back():
					model.x -= model.shiftdx
				else:
					model.x -= model.dx
			if keys[pygame.K_RIGHT]:
				if player.shift_world():
					model.x += model.shiftdx
				else:
					model.x += model.dx

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))

	# models
	# level models:
	ground = Ground()
	platform1 = Platform(10,10)
	platform2 = Platform(800,10)
	platform3 = Platform(1600,10)
	platform4 = Platform(2000,10)
	platform5 = Platform(2400,10)
	# player/NPC models:
	player = Player(300,300)
	train = PainTrain(0,300)
	#models = [train, player, ground, platform1]
	controlled_models = [player,train,ground,platform1,platform2,platform3,platform4,platform5]
	level_models = [ground,platform1]

	# views
	views = []
	views.append(PlayerView(player))
	views.append(PainTrainView(train))
	views.append(GroundView(ground))
	views.append(ObstacleView(platform1))
	views.append(ObstacleView(platform2))
	views.append(ObstacleView(platform3))
	views.append(ObstacleView(platform4))
	views.append(ObstacleView(platform5))

	# TODO: Add controller
	controller = Controller(controlled_models)
	running = True
	counter = 0

	# variable to make speed lower
	delta_speed = .00005 # good one is .00005

	while running == True:
		# Pretty awful way to slow player down.
		counter += 1 # adjust this if it's running to slow. Sorry.
		if counter%5 == 0:
			controller.handle_event()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if player.train_wreck(train):
			train.constdx = 0
			player.dx = 0
			running = False

		# keep train moving
		train.step()

		# decrease speed of player (and all things relative to it)
		for model in controlled_models:
			# good delta speed is .00005
			if model.dx > .01:
				model.dx -= delta_speed
			elif model.dx < -.01:
				model.dx += delta_speed
			if model.shiftdx > .01:
				model.shiftdx -= delta_speed
			elif model.shiftdx < -.01:
				model.shiftdx += delta_speed

		screen.fill(WHITE)
		for view in views:
			view.draw(screen)

		pygame.display.update()

	running = True
	while running == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.blit(gameover,(60,60))
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()