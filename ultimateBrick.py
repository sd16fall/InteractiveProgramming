""" Version 1.0 Ultimate Brick
Anderson Ang Wei Jian and Qingyun Liu

Uses trivial graphical tiles to create a game environment -
the objective is to spawn an environment with tiles and sprites using non-trivial
code (without interaction elements)

To do: (Total hours: 32 hours minimum, 40 hours maximum)
- Version 1.1 (estimated 13 hours )
    - Sound support (bgm, interactive)
    - Enable keyboard interaction
    - Maps fixed keys, flash screen before starting game
    - Collusion detection
    - Edge detection

- Version 1.2 (est. 6 hours)
    - Add scoring system
    - Reform code grid into Model-View-Controller format

- Version 2.0 (est. 9 hours)
    - Non-trivial graphics (using tilemaps)
    - Multi-face playablility

-------------- Cut-off : Part II ----------------

- Version 2.1 (est. 4 hours)
    - Support 2P gaming (multiplayer)
    - Develop competitive elements (inter-player sprite interaction)

-------------- M.V.P (Minimum Viable) : Part III ---------

- Stretch goal: Version 3.0 (est. 4 + 4 hours)
    - Voice-based control
    - Multiple game modes (Time attack, Classic, Point Rush)

------------ Game complete! -------------------------

"""

# Libraries
import pygame
import math
import random


### Global variables ###
## Sprites - Block size
block_width = 23
block_height = 15

# Block color
black = (0,0,0)
white = (255,255,255)
# first initalization
rest = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


# Classes
class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by pinballs """

    def __init__(self, color, x, y):
        """ Constructor. Passes in the color of the block,
            and its x and y position. """

        # Calls the parent class (Sprite) constructor
        super(Block,self).__init__()

        # Create the image of the block of appropriate size
        # The width and height is set as a list (single parameter)
        self.image = pygame.Surface([block_width, block_height])

        # Fill the image with the appropriate color
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y.
        # This is where our block will appear
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    """ This class represents the pinball which will be spawned and moveable"""

    # Floating point representation of where the ball is
    x = 0.0
    y = 180.0

    # Speed in pixels per update
    speed = 10.0

    # Direction of ball (in degrees)
    direction = 200

    # Size of the ball - note: ball's dimensions should match the pixel update rate
    width = 10
    height = 10

    def __init__(self):
        """Constructor function to create the image of the ball"""
        # Call the parent class (Sprite) constructor
        super(Ball,self).__init__()

        # Create the image of the ball
        self.image = pygame.Surface([self.width, self.height])

        # Color the ball
        self.image.fill(white)

        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()

        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

class Bar(pygame.sprite.Sprite):
    """ This class represents the player's bar, which both players control"""

    def __init__(self):
        """ Constructor for Player. """
        # Call the parent's constructor
        super(Bar,self).__init__()

        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = self.screenheight-self.height

### Pre-initalization Block ###

# Initializes the py.game module
pygame.init()

# Creates a screen of 800 x 600 size
screen = pygame.display.set_mode([800,600])

# Gives the program a title
pygame.display.set_caption('Ultimate Brick')

# Declares a font to draw text on screen
font = pygame.font.Font(None, 36)

# Creates background/surface for drawing
background = pygame.Surface(screen.get_size())

# Create lists for grouping Sprites
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

# Spawns the ball in the game
ball = Ball()
balls.add(ball)
allsprites.add(ball)

# Spawns the player's bar (single player)
player = Bar()
allsprites.add(player)

## Spawns the blocks
# Declare the top stack limit of the block (vertical-y position)
top = 80

# Number of blocks to spawn
block_count = 28

# Varies the number of rows
row_count = random.randint(2,7)

# Range controls the number of rows
for row in range(row_count):
    # block_count determines the number of columns
    # random creates an assymmetric stacking of blocks
    for column in range(random.randint(2,8), block_count - random.randint(0,4)):
        # spawns block actual (color, x, y)
        block = Block(rest, column * (block_width + 2) + 1, top)
        blocks.add(block)
        allsprites.add(block)
        # changes the color each time a block is printed (black and dark colors are avoided )
        rest = (random.randint(0,200),random.randint(0,180),random.randint(0,210))

    # Starts on the next rows
    top += block_height + 3

# Sets game framerate
clock = pygame.time.Clock()

# Creates an exit parameter
exit = False

# Main Program Loop
while not exit:

    # Limit the game framerate to 30 fps
    clock.tick(30)

    # Clear the screen
    screen.fill(black)

    ## Event segment ##

    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    ## Creation segment ##
    # Draw everything into frame
    allsprites.draw(screen)

    # Displays screen
    pygame.display.flip()

pygame.quit()
