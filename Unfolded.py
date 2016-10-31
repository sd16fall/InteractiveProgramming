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
def shift(l,n):
		return l[n:] + l[:n]

def options(xroll, used, model, n):
		#check if things in xroll are in used
		#check that we arxen't along a wall
		#apply positions and color grid accordingly
		for i in range(n):
			for j in range(n):
				if model.grid[i][j] == 2:
					model.grid[i][j] = 0
		for i in xroll:
			if i not in used:
				if i == xroll[0] and model.int_column != 0:
					model.grid[model.int_row][model.int_column - 1] = 2
				if i == xroll[1] and model.int_row != (n-1):
					model.grid[model.int_row + 1][model.int_column] = 2
				if i == xroll[2] and model.int_column != (n-1):
					model.grid[model.int_row][model.int_column + 1] = 2
				if i == xroll[3] and model.int_row != 0:
					model.grid[model.int_row - 1][model.int_column] = 2

def random_ending(model):
	objectives = [[2,1], [1,2], [1,6], [2,7], [6,1], [7,2], [7,6], [6,7]]
	return random.choice(objectives)
	

class Grid(object):
	def __init__(self):
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
		self.grid[self.int_row][self.int_column] = 1
		self.xroll = ['L', 'F', 'R', 'B']
		self.yroll = ['D', 'F', 'U', 'B']
		self.used = ['D']
		self.temp = []
		#thing = [[3, 5], [4, 6], [7, 8]]
		#return random.choice(thing)

		#end = function
		#grid[f[0]][f[1]]

class GridView(object):
	def __init__(self, model):
		self.model = model
		
	def draw(self, screen):
		n = 9
		for row in range(n):
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
	def __init__(self, model):
		self.model = model
		random_ending(self.model)
		objective = random_ending(self.model)
		self.objective = objective
		model.grid[objective[0]][objective[1]] = 3


	def grid_event(self, event):
		n = 9
		play_again = 1
		options(self.model.xroll, self.model.used, self.model, n)
		if self.model.int_row == self.objective[0] and self.model.int_column == self.objective[1]:
			print 'boo yah'
		if event.type == pygame.KEYDOWN:       
			if event.key == pygame.K_UP and self.model.int_row != 0 and self.model.grid[self.model.int_row - 1][self.model.int_column] != 1 and self.model.grid[self.model.int_row - 1][self.model.int_column] != 0:
				self.model.xroll[1] = self.model.yroll[0]
				self.model.xroll[3] = self.model.yroll[2]
				self.model.yroll = shift(self.model.yroll, -1)
				row = self.model.int_row - 1
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0])
				options(self.model.xroll, self.model.used, self.model, n)
				
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
				options(self.model.xroll, self.model.used, self.model, n)

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
				options(self.model.xroll, self.model.used, self.model, n)

			if event.key == pygame.K_DOWN and self.model.int_row != (n-1) and self.model.grid[self.model.int_row + 1][self.model.int_column] != 1 and self.model.grid[self.model.int_row + 1][self.model.int_column] != 0:
				self.model.xroll[1] = self.model.yroll[2]
				self.model.xroll[3] = self.model.yroll[0]
				self.model.yroll = shift(self.model.yroll, 1)
				row = self.model.int_row + 1
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.used.append(self.model.yroll[0])
				options(self.model.xroll, self.model.used, self.model, n)
 
def main(): 
	# Initialize pygame
	pygame.init()
	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [230, 300]
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