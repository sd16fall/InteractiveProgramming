import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
class Grid(object):
	def __init__(self):
		n = 10
		self.grid = []
		for row in range(10):
			# Add an empty array that will hold each cell
			# in this row
			self.grid.append([])
			for column in range(10):
				self.grid[row].append(0)  # Append a cell
		self.int_column = 0
		self.int_row = 9
		self.grid[self.int_row][self.int_column] = 1

class GridView(object):
	def __init__(self, model):
		self.model = model
		
	def draw(self, screen):
		for row in range(10):
			for column in range(10):
				color = WHITE
				if self.model.grid[row][column] == 1:
					color = GREEN
				pygame.draw.rect(screen,
								 color,
								 [(MARGIN + WIDTH) * column + MARGIN,
								  (MARGIN + HEIGHT) * row + MARGIN,
								  WIDTH,
								  HEIGHT])
	pass

class GridController(object):
	def __init__(self, model):
		self.model = model

	def grid_event(self, event):
		if event.type == pygame.KEYDOWN:       
			if event.key == pygame.K_UP and self.model.int_row != 0:
				row = self.model.int_row - 1
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.grid[row+1][column] = 0
			if event.key == pygame.K_RIGHT and self.model.int_column != 9:
				row = self.model.int_row
				column = self.model.int_column + 1
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.grid[row][column-1] = 0
			if event.key == pygame.K_LEFT and self.model.int_column != 0:
				row = self.model.int_row
				column = self.model.int_column - 1
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.grid[row][column+1] = 0
			if event.key == pygame.K_DOWN and self.model.int_row != 9:
				row = self.model.int_row + 1
				column = self.model.int_column
				self.model.grid[row][column] = 1
				self.model.int_row = row
				self.model.int_column = column
				self.model.grid[row-1][column] = 0

class Block(object):
	def __init__(self):
		#Initializes the block
		pass
	def win_condition(self):
		#When the block reaches a certain point on the grid, a win condition is applied
		pass
	def start_condition(self):
		#Defines where the block will begin
		pass
	def lose_condition(self):
		#Defines how the play will lose
		pass

class BlockView(object):
	#Defines all six views of the block in relation to each other
	pass

class BlockController(object):
	#Defines how player input and how pressing directional keys will rotate the block on its side
	pass

		
 
def main(): 
	# Initialize pygame
	pygame.init()
	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [255, 255]
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