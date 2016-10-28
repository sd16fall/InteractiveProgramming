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
	def __init__(self,x=0,y=0,width=25,height=25):
		# places player centered above the coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height

	def step(self):
		# TODO: ?? Something something integrate with controller input
		pass

	def train_wreck(self, train):
		return (train.x+train.width) > self.x

class PainTrain(object):
	def __init__(self,x=0,y=0,width=200,height=200,dx=.01):
		# places train centered above coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.dx = dx

	def step(self):
		self.x += self.dx

class Level(object):
	def __init__(self, width = 640, height = 180):
		self.width = width
		self.height = height

	def step(self):
		pass

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

class LevelView(object):
	def __init__(self, model):
		self.model = model

	def draw(self, surface):
		model = self.model
		# this takes (x,y,width,height)
		pygame.draw.rect(surface,DIMGRAY,(0,480-model.height,model.width,model.height))

"""Controller classes"""
class PlayerController(object):
	def __init__(self,models):
		self.models = models

	def handle_event(self,event):
		if event.type == pygame.KEYDOWN:
			for model in self.models:
				if event.key == pygame.K_LEFT:
					model.x -= 10
        		if event.key == pygame.K_RIGHT:
					model.x += 10

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))

	# models
	level = Level()
	player = Player(320,300)
	train = PainTrain(50,300)
	models = [level, player, train]

	# views
	views = []
	views.append(LevelView(level))
	views.append(PlayerView(player))
	views.append(PainTrainView(train))

	# TODO: Add controller
	controller = PlayerController([player])
	running = True
	while running == True:
		for event in pygame.event.get():
			controller.handle_event(event)
			if event.type == pygame.QUIT:
				running = False

		if player.train_wreck(train):
			train.dx = 0
			print "Game over!"
			running = False

		for model in models:
			model.step()

		screen.fill(WHITE)
		for view in views:
			view.draw(screen)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()
