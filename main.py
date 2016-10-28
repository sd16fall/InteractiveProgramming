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
	def __init__(self,x=0,y=0,width=50,height=50,dx = 0):
		# places player centered above the coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.dx = dx

	def train_wreck(self, train):
		return (train.x+train.width) > self.x

	def shift_world(self):
		return self.x > 450

class PainTrain(object):
	def __init__(self,x=0,y=0,width=200,height=200,dx=0):
		# places train centered above coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.dx = dx

	def step(self):
		self.x += self.dx

# classes for level objects
class Ground(object):
	def __init__(self, x = 0, y = 300, width = 600, height = 180,dx=-10):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx

class Platform(object):
	def __init__(self, x=0,y=0,width = 100, height = 20, dx=-10):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx

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

	def handle_event(self,event):
		if event.type == pygame.KEYDOWN:
			for model in self.models:
				if event.key == pygame.K_LEFT:
					print model
					print "I'm here! %d,%d" % (model.x,model.dx)
					model.x -= model.dx
					print "Now I'm here! %d,%d" % (model.x,model.dx)
				if event.key == pygame.K_RIGHT:
					print model
					print "I'm here! %d,%d" % (model.x,model.dx)
					model.x += model.dx
					print "Now I'm here! %d,%d" % (model.x,model.dx)

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
	controlled_models = [ground, platform1, player]

	# views
	views = []
	views.append(GroundView(ground))
	views.append(ObstacleView(platform1))
	views.append(PlayerView(player))
	views.append(PainTrainView(train))

	# TODO: Add controller
	controller = Controller(controlled_models)
	running = True
	while running == True:
		for event in pygame.event.get():
			controller.handle_event(event)
			if event.type == pygame.QUIT:
				running = False

		# some events:
		"""if player.shift_world():
			player.dx = 0
			for model in level_models:
				model.dx = -20
		else:
			player.dx = 20
			for model in level_models:
				model.dx = 0"""

		if player.train_wreck(train):
			train.dx = 0
			print "Game over!"
			running = False

		#for model in models:
		#	model.step()

		train.step()

		screen.fill(WHITE)
		for view in views:
			view.draw(screen)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()