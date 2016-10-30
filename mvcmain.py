import sys
import pygame
import random

# Sets size of display
display_width = 1200
display_height = 1200
image_pixels = 50
# Randomly places next block
randAppleX = round(random.randrange(0, display_width-image_pixels))
randAppleY = round(random.randrange(0, display_height-image_pixels))


class viewer(object):
	def __init__(self):
		# Initliizlies PyGame Window & Gameover Font
		pygame.display.init()
		pygame.font.init()

		# Defineing Color RGB Values for GUI elements
		self.white = (255, 255, 255)
		self.sky_blue= (52, 152, 219)

		# Sets Top of game Window Caption
		self.gameDisplay = pygame.display.set_mode((display_width,display_height))
		pygame.display.set_caption('Unicorn Squad')



		# Linking color values to GUI elements & Imports iimages and reduces size to 50 by 50px
		self.gameDisplay.fill(self.sky_blue)
		self.unicorn = pygame.image.load('unicorn.png')
		self.unicorn = pygame.transform.scale(self.unicorn, (image_pixels, image_pixels))
		self.rainbow = pygame.image.load('rainbow.png')
		self.rainbow = pygame.transform.scale(self.rainbow, (image_pixels, image_pixels))
		self.food = pygame.image.load('food.png')
		self.food = pygame.transform.scale(self.food, (image_pixels, image_pixels))

		self.clock = pygame.time.Clock()


		# The higher the FPS the fasted the sprite moves. We fid that 15 is a good balance for gameplay
		self.FPS = 10

		# Aiisgns font & font size 25 pixels
		font = pygame.font.SysFont(None, 55)

	def drawapple(self):
		self.gameDisplay.blit(self.food, (randAppleX,randAppleY))


	# Initlizes up down left right actions
	def snake(self, image_pixels, snakelist, direction):
		head = self.unicorn

		if direction == "left":
			head = pygame.transform.flip(self.unicorn, 1, 0)

		if direction == "up":
			head = pygame.transform.rotate(self.unicorn, 90)

		if direction == "down":
			head = pygame.transform.rotate(self.unicorn, 270)

		# deifnes movement of snake tail
		gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

		#  defines adding of rainbow image to user sprite
		for XnY in snakelist[:-1]:
			gameDisplay.blit(rainbow,(XnY[0], XnY[1]) )

	# Initliazes text object
	def text_objects(self, text,color):
		textSurface = font.render(text, True, color)
		return textSurface, textSurface.get_rect()

	# Defines  display message with color variable
	def message_to_screen(self, msg,color, y_displace=0):
		textSurf, textRect = text_objects(msg,color)
		textRect.center = (display_width / 2), (display_height / 2)+y_displace
		self.gameDisplay.blit(textSurf, textRect)

	# Sets counnt positoin
	def score_to_screen(self, msg, color):
		textSurf, textRect = text_objects(msg,color)
		textRect = (display_width -50), (display_height -50)
		self.gameDisplay.blit(textSurf, textRect)

	def gameover(self):
		# Sets window to white
			self.gameDisplay.fill(self.white)
			# Sets message text, color, and positoin
			self.message_to_screen("Game over", red, y_displace=-50)
			self.message_to_screen("Press C to play again or Q to quit",black, 50)
			pygame.display.update()

class model(object):
	def __init__(self):
		self.lead_x = display_width/2
		self.lead_y = display_height/2

		self.lead_x_change = 10
	 	self.lead_y_change = 0

		# Snake size array
		self.snakeList = []
		# Sets inital snake length (Snake head counts as 1)
	   	self.snakeLength = 1
	   	self.player_score = 0

	# Initial direction of character sprite
		self.direction = "right"

	 # If you go outside game area horizontlal or vertically

	def snakemodel(self):
		# Change player coordinates based on user action
		lead_x += lead_x_change
		lead_y += lead_y_change

		if self.lead_x >= display_width or self.lead_x < 0 or self.lead_y >= display_height or self.lead_y < 0:
			gameOver = True

		self.unicorn
		# Defines snake head as an empty deict
		snakeHead = []
		# Appends  Initial X and Y coordinates to the snake head
		snakeHead.append(self.lead_x)
		snakeHead.append(self.lead_y)
		# Adds snake head to sake body. Snkae body is an empty dict
		snakeList.append(snakeHead)


		if len(snakeList) > snakeLength:
			del snakeList[0]

		# Runs through each segment of the snake list and checks if the x y corrsoidate of the snake segment equalis the x y coordinates of the snake head
		# ie the snake is overlapping itslef and it runs the game over sequensce
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True

		# Initlizes the snakeList
		snake(image_pixels, snakeList, direction)

		score_to_screen(str(player_score), self.white)

		# Updates the screen screen with new movement
		pygame.display.update()

		# Defiens the paraemnts necuasey for player spriite to pick up Apple and add length to snake list
		if self.lead_x > randAppleX and self.lead_x < randAppleX + image_pixels or self.lead_x + image_pixels > randAppleX and lead_x + image_pixels < randAppleX + image_pixels:

			if self.lead_y > randAppleY and self.lead_y < randAppleY + image_pixels:
				randAppleX = round(random.randrange(0, display_width-image_pixels))
				randAppleY = round(random.randrange(0, display_height-image_pixels))
				snakeLength += 1
				player_score += 1


			elif self.lead_y + image_pixels > randAppleY and self.lead_y + image_pixels < randAppleY + image_pixels:
				randAppleX = round(random.randrange(0, display_width-image_pixels))
				randAppleY = round(random.randrange(0, display_height-image_pixels))
				snakeLength += 1
				# Updates player score as well as as snake lenth
				player_score += 1

class controller(object):
	def gameovercontrol(self):
	# Maps user close window actio to close og game window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = False
				gameExit = True
				return gameOver, gameExit

				# Maps keboard strokes to close game and redo game
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = False
					gameExit = True
					return gameOver, gameExit

				if event.key == pygame.K_c:
					gameLoop()

	def movement(self, gamemodel):
		# While game in progress (Maps keyboard actions to sprike movements) Controller
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				return gameExit

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					gamemodel.direction = "left"
					gamemodel.lead_x_change = -image_pixels
					gamemodel.lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					gamemodel.direction = "right"
					gamemodel.lead_x_change = image_pixels
					gamemodel.lead_y_change = 0
				elif event.key == pygame.K_UP:
					gamemodel.direction = "up"
					gamemodel. lead_y_change = -image_pixels
					gamemodel.lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					gamemodel.direction = "down"
					gamemodel.lead_y_change = image_pixels
					gamemodel.lead_x_change = 0
				return False


# Main game engine -
def gameLoop():
	drawer = viewer()
	game = model()
	control = controller()
	# global direction
	# # Defines game ares as skyblue
	#
	#
	# # Sets game exit varibles to false
	gameExit = False # HItting the close button (closing Window)
	gameOver = False # Internal game over view (Hitting the walls or your own tail)

	#  View
	while not gameExit:
		print 'not exit game'
		# Game over viwe
		while gameOver == True:
			print 'game over'
			drawer.gameover()
		control.gameovercontrol()
		gameExit = control.movement(game)



		# Rate of referesh
		drawer.clock.tick(drawer.FPS)


gameLoop()

pygame.display.quit()
pygame.quit()
