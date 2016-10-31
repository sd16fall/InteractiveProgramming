""" UNFOLDED
RULES:
	The player begins at the red space indicated on the grid, which represents the position of a 6 sided, 1X1 cube. Moving on the grid rotates and unfolds the cube,
	meaning that once the player has rolled onto a face of the cube, it cannot be used again. The objective is to reach the blue space on the grid. Green 
	spaces indicate locations that can still be moved to.

For every direcion rolled on the grid, the game keeps track of the position of the face relative to every other face on the cube, and tracks which ones have already
been used.

"""

import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5


 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
def shift(l,n): #Shifts a list l to the right (negative n) or left (positive n) the number of times indicated by n
		return l[n:] + l[:n]

def options(xroll, used, model, n): #Lights up green squares on the grid to indicate where the player can move to next
		for i in range(n): #Returns green squares from the previous turn back to white for the next turn
			for j in range(n):
				if model.grid[i][j] == 2:
					model.grid[i][j] = 0
		for i in xroll: #The faces in xroll always correspond to the potential moves the player can make, so we sort through the list
			if i not in used: #Checks to see if the face the player could rotate onto has been used yet. If so, the space does not turn green
				if i == xroll[0] and model.int_column != 0: #Sets the left space green
					model.grid[model.int_row][model.int_column - 1] = 2
				if i == xroll[1] and model.int_row != (n-1): #Sets the down space green
					model.grid[model.int_row + 1][model.int_column] = 2
				if i == xroll[2] and model.int_column != (n-1): #Sets the right space green
					model.grid[model.int_row][model.int_column + 1] = 2
				if i == xroll[3] and model.int_row != 0: #Sets the up space green
					model.grid[model.int_row - 1][model.int_column] = 2

def random_ending(model): #Defines a list of potential end objective locations in the form [row, column] and randomly chooses one from the list
	objectives = [[2,1], [1,2], [1,6], [2,7], [6,1], [7,2], [7,6], [6,7]]
	return random.choice(objectives)
	

class Grid(object):
	""" Represents a 2D grid
	
	attributes: grid, int_column, int_row, xroll, yroll, used, temp
	"""


	def __init__(self):
		# Create a n by n 2 dimensional array. A two dimensional
		# array is simply a list of lists.
		n = 9
		self.grid = []
		for row in range(n):
			# Add an empty array that will hold each cell
			# in this row
			self.grid.append([])
			for column in range(n):
				self.grid[row].append(0)  # Append a cell
		self.int_column = 4
		self.int_row = 4
		self.grid[self.int_row][self.int_column] = 1 #Set initial position of on the grid to red
		self.xroll = ['L', 'F', 'R', 'B'] #Sets the initial orientation of the block along the x axis (rotating the block to the left or right)
		self.yroll = ['D', 'F', 'U', 'B'] #Sets the initial orientation of the block along the y axis (rotating the block up or down)
		self.used = ['D'] #The block starts on this face, so it is added to the list of used faces from the very beginning. We cannot use it again.
		self.temp = []

class GridView(object):
	""" Draws a 2D grid
	"""

	def __init__(self, model):
		self.model = model
		
	def draw(self, screen):
		n = 9
		for row in range(n): #Set all the grid spaces to white and changes the color of a space when it is assigned a value of 1, 2, or 3
			for column in range(n):
				color = WHITE
				if self.model.grid[row][column] == 1:
					color = RED
				if self.model.grid[row][column] == 2:
					color = GREEN
				if self.model.grid[row][column] == 3:
					color = BLUE
				pygame.draw.rect(screen,
								 color,
								 [(MARGIN + WIDTH) * column + MARGIN,
								  (MARGIN + HEIGHT) * row + MARGIN,
								  WIDTH,
								  HEIGHT])

class GridController(object):
	"""Controls movement around a 2D grid

	attributes: objective
	"""

	def __init__(self, model):
		self.model = model
		objective = random_ending(self.model) #Chooses a random position from objectives, assigns it to objective, and sets that position to blue
		self.objective = objective
		model.grid[objective[0]][objective[1]] = 3


	def grid_event(self, event):
		n = 9
		options(self.model.xroll, self.model.used, self.model, n) #Lights up potential movement options before play has started
		if self.model.int_row == self.objective[0] and self.model.int_column == self.objective[1]:
			print 'You win!'
			for row in range(n):
				for column in range(n): #Removes green squares upon reaching objective to end gameplay
					if self.model.grid[row][column] == 2:
						self.model.grid[row][column] = 0
		if event.type == pygame.KEYDOWN:      
			if event.key == pygame.K_UP and self.model.int_row != 0 and self.model.grid[self.model.int_row - 1][self.model.int_column] != 1 \
			and self.model.grid[self.model.int_row - 1][self.model.int_column] != 0: #Checks that that the player is not along the top wall and that the square they are moving toward is not red or white
				self.model.xroll[1] = self.model.yroll[0] #Shifts xroll and yroll to maintain relationships between sides of the cube
				self.model.xroll[3] = self.model.yroll[2]
				self.model.yroll = shift(self.model.yroll, -1)
				row = self.model.int_row - 1 #Updates the grid position
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0]) #Adds the face that was rolled onto to the used list
				
			if event.key == pygame.K_RIGHT and self.model.int_column != (n-1) and self.model.grid[self.model.int_row][self.model.int_column + 1] != 1 \
			and self.model.grid[self.model.int_row][self.model.int_column + 1] != 0:
				temp = self.model.xroll
				self.model.xroll = self.model.yroll
				self.model.yroll = [temp[2], temp[1], temp[0], temp[3]]
				row = self.model.int_row
				column = self.model.int_column + 1
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0])

			if event.key == pygame.K_LEFT and self.model.int_column != 0 and self.model.grid[self.model.int_row][self.model.int_column - 1] != 1 \
			and self.model.grid[self.model.int_row][self.model.int_column - 1] != 0:
				temp = self.model.yroll
				self.model.yroll = self.model.xroll
				self.model.xroll = [temp[2], temp[1], temp[0], temp[3]]
				row = self.model.int_row
				column = self.model.int_column - 1
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0])

			if event.key == pygame.K_DOWN and self.model.int_row != (n-1) and self.model.grid[self.model.int_row + 1][self.model.int_column] != 1 \
			and self.model.grid[self.model.int_row + 1][self.model.int_column] != 0:
				self.model.xroll[1] = self.model.yroll[2]
				self.model.xroll[3] = self.model.yroll[0]
				self.model.yroll = shift(self.model.yroll, 1)
				row = self.model.int_row + 1
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0])
 
def main(): 
	# Initialize pygame
	pygame.init()
	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [230, 230]
	screen = pygame.display.set_mode(WINDOW_SIZE)
	 
	# Set title of screen
	pygame.display.set_caption("Array Backed Grid")
	 
	# Loop until the user clicks the close button.
	done = False
	 
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	grid_obj = Grid()
	model = grid_obj
	view = GridView(model)
	controller = GridController(model)
	 
	# -------- Main Program Loop -----------

	while not done:
		for event in pygame.event.get():  # User did something
			controller.grid_event(event)
			if event.type == pygame.QUIT:  # If user clicked close
				done = True  # Flag that we are done so we exit this loop
	 
		# Set the screen background
		screen.fill(BLACK)
		view.draw(screen) 
		# Limit to 60 frames per second
		clock.tick(60)
	 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	 
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()