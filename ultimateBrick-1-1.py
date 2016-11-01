""" Version 1.1 Ultimate Brick
Anderson Ang Wei Jian and Qingyun Liu

Uses trivial graphical tiles to create a game environment -
the objective is to spawn an environment with tiles and sprites using non-trivial
code (without interaction elements)

Changelog: (since Version 1.0)
    -

To do: (Total hours: 32 hours minimum, 40 hours maximum)
- Version 1.1 (estimated 13 hours )
    - Sound support (bgm, interactive) - not implemented -
    - Enable keyboard interaction - done -
    - Maps fixed keys, flash screen before starting game  - not implemented -
    - Collusion detection - done -
    - Edge detection - done -
    - Sprite motion (ball & bar) - done -

- Version 1.2 (est. 6 hours)
    - Add scoring system - not implemented -
    - Reform code grid into Model-View-Controller format - in progress -

- Version 2.0 (est. 9 hours)
    - Non-trivial graphics (using tilemaps) - cancelled -
    - Multi-face playablility - done -

-------------- Cut-off : Part II ----------------

- Version 2.1 (est. 4 hours)
    - Support 2P gaming (multiplayer) - done -
    - Develop competitive elements (inter-player sprite interaction) - not implemented -

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
    direction = 200.0

    # Size of the ball - note: ball's dimensions should match the pixel update rate
    width = 10
    height = 10
    radius = 5

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

    def bounce(self, diff):
        """ Creates a function that ensures the bounce mechanism works on
            horizontal surfaces """
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        """ Update the position of the ball. """
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)

        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

        # Do we bounce off the top of the screen?
        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1

        # Did we fall off the bottom edge of the screen?
        if self.y > 600:
            return True
        else:
            return False

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

        self.rect.x = 180.0
        self.rect.y = self.screenheight-self.height

    def update(self):
        """ Update the player position. """
        # Get where the mouse is
        pos = pygame.mouse.get_pos()
        # Set the left side of the player bar to the mouse position
        self.rect.x = pos[0]
        # Make sure we don't push the player paddle
        # off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width

### Pre-initalization Block ###
def main():

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
            # changes the color each time a block is printed (black and dark colors are avoided )
            rest = (random.randint(0,200),random.randint(0,180),random.randint(0,210))
            # spawns block actual (color, x, y)
            block = Block(rest, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)

        # Starts on the next rows
        top += block_height + 3

    # Sets game framerate
    clock = pygame.time.Clock()

    # Creates a universal exit parameter
    exit = False

    # Creates a standard exit parameter
    game_over = False

    # Directional difference
    diff = 40.0

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
                pygame.display.quit();

        # Update the ball and player position as long
        # as the game is not over.
        if not game_over:
            # Update the player and ball positions
            player.update()
            game_over = ball.update()

        # If we are done, print game over
        if game_over:
            text = font.render("Game Over", True, white)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)

        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player, balls, False):
            # Diff decides if the ball bounces to the left/right on collision
            diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)

        # Set the ball's y position in case
        # we hit the ball on the edge of the paddle
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)

        # Check for collisions between the ball and the blocks
        deadblocks = pygame.sprite.spritecollide(ball, blocks, True)

        # If we actually hit a block, bounce the ball
        if len(deadblocks) > 0:
            ball.bounce(0)

        # Game ends if all the blocks are gone
        if len(blocks) == 0:
            game_over = True

        ## Creation segment ##
        # Draw everything into frame
        allsprites.draw(screen)

        # Displays screen
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
