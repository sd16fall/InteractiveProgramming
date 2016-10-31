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
	def __init__(self,x=0,y=0,width=200,height=200,constdx=.01,dx=0,shiftdx=-1):
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
	def __init__(self, x = 0, y = 300, width = 600, height = 180,dx=0,shiftdx=-1):
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
		self.player = models[2] # make sure this aligns with controlled_models in main
		self.groundtest = models[1]

	def handle_event(self):
		# time passed isn't actually time based... based on while loop efficiency
		player = self.player
		models = self.models
		groundtest = self.groundtest
		#print groundtest.x,player.x,time_passed
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
	# player/NPC models:
	player = Player(300,300)
	train = PainTrain(0,300)
	#models = [train, player, ground, platform1]
	controlled_models = [ground, platform1, player,train]
	level_models = [ground,platform1]

	# views
	views = []
	views.append(GroundView(ground))
	views.append(ObstacleView(platform1))
	views.append(PlayerView(player))
	views.append(PainTrainView(train))

	# TODO: Add controller
	controller = Controller(controlled_models)
	running = True
	counter = 0

	# variable to make speed lower
	delta_speed = .0005 # good one is .00005

	while running == True:
		# Pretty awful way to slow player down.
		counter += 1 # adjust this if it's running to slow. Sorry.
		if counter%5 == 0:
			controller.handle_event()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if player.train_wreck(train):
			train.dx = 0
			print "Game over!"
			running = False

		train.step()

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

	pygame.quit()

if __name__ == '__main__':
	main()