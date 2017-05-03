"""Pain Train the Video Game, by Charlie Weiss and Diego Garcia"""
"""TODO:
- Obstacle placement
- Graphic design
- Interactive Start screen
- Interactive End screen
- Pain Train name"""

import pygame
import math

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
DIMGRAY = (105,105,105)
SLATEGRAY = (112,128,144)

"""Model classes"""
class Player(object):
	def __init__(self,x=0,y=0,width=50,height=50,dx=1,dy=0,shiftdx=0,jumpdy=-.75):
		# places player below and to the right of the coordinate given
		self.x = x
		self.y = y-height
		self.width = width
		self.height = height
		self.dx = dx
		self.dy = dy
		self.shiftdx = shiftdx
		self.jumpdy = jumpdy # variable dy is set to when controller jumps

	def train_wreck(self, train):
		return (train.x+train.width) > self.x

	def shift_world(self):
		return self.x > 350

	def go_back(self):
		return self.x < 130

	def hit_platform(self,platform):
		#if the player rectangle dimensions are ABCD
		#and the platform rectangle is abcd
		A = self.x
		B = self.x+self.width
		C = self.y
		D = self.y+self.height
		a = platform.x
		b = platform.x+platform.width
		c = platform.y
		d = platform.y+platform.height
		return ((A>a and A<b) or (B>a and B<b)) and ((C>c and C<d) or (D>c and D<d))

	def fall_to_death(self):
			return self.y > 480

	def on_platform(self,platform):
		return self.x < (platform.x+platform.width) and (self.x+self.width) > platform.x and (self.y+self.height)==platform.y

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
	def __init__(self, x=0,y=0,width = 150, height = 20, dx=0, shiftdx=-1):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx
		self.shiftdx = shiftdx

"""View classes"""
class PlayerView(object):
	def __init__(self, model,pic):
		self.model = model
		self.pic = pic

	def draw(self, surface):
		model = self.model
		surface.blit(self.pic,(model.x,model.y))

class PainTrainView(object):
	def __init__(self, model,pic):
		self.model = model
		self.pic = pic

	def draw(self, surface):
		model = self.model
		surface.blit(self.pic,(model.x,model.y))

class GroundView(object):
	def __init__(self, model,pic):
		self.model = model
		self.pic = pic

	def draw(self, surface):
		model = self.model
		surface.blit(self.pic,(model.x,model.y))

class ObstacleView(object):
	# can be used for any rectangular object
	def __init__(self,model,pic):
		self.model = model
		self.pic = pic

	def draw(self,surface):
		model = self.model
		surface.blit(self.pic,(model.x,model.y))

"""Controller classes"""
class Controller(object):
	def __init__(self,models):
		self.models = models
		self.player = models[0] # make sure this aligns with all_models in main

	def handle_event(self):
		# time passed isn't actually time based... based on while loop efficiency
		player = self.player
		models = self.models
		jump = False
		keys = pygame.key.get_pressed() # checking pressed keys
		for model in models:
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
			if model.y and player.on_platform(model):
				jump = True

		if keys[pygame.K_UP] and jump==True:
			player.dy = player.jumpdy

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))

	# Images
	gameover_pic = pygame.image.load('images/gameover1.bmp').convert()
	train_pic = pygame.image.load('images/train.bmp').convert()
	player_pic = pygame.image.load('images/player.bmp').convert()
	playerjump_pic = pygame.image.load('images/player_jump.bmp').convert()
	ground_pic = pygame.image.load('images/ground2.bmp').convert()
	platform_pic = pygame.image.load('images/platform.bmp').convert()

	# models
	# level models:
	# design for level 6000 wide
	ground1 = Ground(x=0,width=650)
	ground2 = Ground(x=850,width=1100) #jump dist: 200
	platform1 = Platform(x=1400,y=200)
	platform2 = Platform(x=1700,y=100)
	ground3 = Ground(x=2100,width=1100) #jump dist: 150
	ground4 = Ground(x=3350,width=1100) #jump dist: 150
	ground5 = Ground(x=4450,width=1100) #jump dist: 150
	ground6 = Ground(x=5550,width=650)
	platform3 = Platform(3000,200)
	platform4 = Platform(3500,200)
	platform5 = Platform(6300,300)
	# player/NPC models:
	player = Player(300,300,width=40)
	train = PainTrain(x=-300,y=300,width=400,height=300)
	#models = [train, player, ground, platform1]
	all_models = [player,train,ground1,ground2,platform1,platform2,ground3,ground4,ground5,ground6,platform3,platform4,platform5]
	collision_models = [ground1,ground2,platform1,platform2,ground3,ground4,ground5,ground6,platform3,platform4,platform5]

	#resize images for views
	new_train_pic = pygame.transform.scale(train_pic, (train.width,train.height))
	new_player_pic = pygame.transform.scale(player_pic, (player.width,player.height))
	new_playerjump_pic = pygame.transform.scale(playerjump_pic, (player.width,player.height))
	a_ground_pic = pygame.transform.scale(ground_pic, (ground1.width,ground1.height))
	b_ground_pic = pygame.transform.scale(ground_pic, (ground2.width,ground2.height))
	new_platform_pic = pygame.transform.scale(platform_pic, (platform1.width,platform1.height))
	t_platform_pic = pygame.transform.scale(platform_pic, (platform2.width,platform2.height))

	# views
	views = []
	views.append(PlayerView(player,new_player_pic))
	views.append(GroundView(ground1,a_ground_pic))
	views.append(GroundView(ground2,b_ground_pic))
	views.append(ObstacleView(platform1,new_platform_pic))
	views.append(ObstacleView(platform2,t_platform_pic))
	views.append(GroundView(ground3,b_ground_pic))
	views.append(GroundView(ground4,b_ground_pic))
	views.append(GroundView(ground5,b_ground_pic))
	views.append(GroundView(ground6,a_ground_pic))
	views.append(ObstacleView(platform3,new_platform_pic))
	views.append(ObstacleView(platform4,new_platform_pic))
	views.append(ObstacleView(platform5,new_platform_pic))
	views.append(PainTrainView(train,new_train_pic))

	# controller
	controller = Controller(all_models)
	running = True
	counter = 0

	# variable to make speed lower
	delta_speed = .00001 # good one is .00005
	train.constdx = .17
	quit_button = False
	player.jumpdy=-.65

	while running == True:
		counter += 1
		if counter%5 == 0: # adjust if it's running too slow. A little jank, sorry.
			controller.handle_event()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_button = True
				running = False

		if player.train_wreck(train) or player.fall_to_death():
			train.constdx = 0
			player.dx = 0
			running = False

		# keep train moving
		train.step()

		# code for player jumping
		player.y += player.dy
		# make player fall
		player.dy += 0.001 # if you lower this, also lower jumpdy in player class
		if player.dy > 0:
			views[0]=PlayerView(player,new_player_pic)
		else:
			views[0]=PlayerView(player,new_playerjump_pic)
		# make player's jump speed lower with time
		if player.jumpdy < -.05:
			player.jumpdy += delta_speed

		#handle collisions
		for model in collision_models:
			if player.hit_platform(model):
				if player.dy>0:
					if player.y+player.height<model.y+5:
						player.dy = 0
						player.y = model.y - player.height
					else:
						if player.x<model.x+model.width/2:
							player.x = model.x-player.width
						else:
							player.x = model.x+model.width
				elif player.dy<0:
					player.y = model.y+model.height
					player.dy = .001
			if not player.on_platform(model) and player.dy==0:
				player.dy = .001

		# decrease speed of player (and all things relative to it)
		for model in all_models:
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
	while running == True and quit_button==False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.blit(gameover_pic,(60,60))
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()
