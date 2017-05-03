# "Pain Train" the Video Game
### by Charlie Weiss and Diego Garcia

Also, be sure to check out my [project website](charlievweiss.github.io).

## What is this?
This is a video game created using Python's pygame library and an MVP (model-viewer-player) framework. It is a platform game with a player, a chaser, and some obstacles. The player loses by either being overtaken by the chaser, or by falling to their death.

## How does it work?
The code is split into three collections of classes: The Model classes, the View classes, and the Controller classes. The functions in these classes are called by the main function (found at the bottom of the file), which runs the game with a while loop. Here's some more detail about those sections:

### Model Classes
These contain the definition of the models of each type of object in the game, and their interactions with other objects or events. Each class defines things such as an object's postion, height, width, and distance traveled per loop. Here's an example of the chaser model class, named PainTrain:

```
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
```

The classes you will find here are
- Player
- PainTrain
- Ground
- Platform

### Viewer Classes
These classes project the information contained in the model classes onto your screen. Each contains an initial function to define the class, and a draw function that says what the object should look like. For consistency's sake, here's the example of the PainTrain's Viewer class:

```
class PainTrainView(object):
	def __init__(self, model):
		self.model = model

	def draw(self, surface):
		model = self.model
		# this takes (x,y,width,height)
		pygame.draw.rect(surface,BLACK,(model.x,model.y,model.width,model.height))
```

The classes you will find here are
- PlayerView
- PainTrainView
- GroundView
- ObstacleView

### Controller Classes
This is actually one class called the Controller class. It has an initial function to define it, and a handle_event function. This class interacts with the main function, which passes it an event. The handle_event function then determines which event it is (i.e., which key has been pressed), and says what to do in that case. Here's the class:

```
class Controller(object):
	def __init__(self,models):
		self.models = models
		self.player = models[0] # make sure this aligns with controlled_models in main

	def handle_event(self):
		# time passed isn't actually time based... based on while loop efficiency
		player = self.player
		models = self.models
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

		if keys[pygame.K_UP] and player.dy == 0:
			player.dy = player.jumpdy
```

The class you will find here is 
- Controller

### Main Function
Now this function is the thing that pulls the whole game together, and thus, it is probably the most confusing. It begins by doing some set up, and then running a while loop that essentially runs the game. Here are the set up steps in order:

- initializes pygame and the screen
- loads object images
- defines objects puts them in appropriate arrays
- resizes images to fit object sizes
- defines views with objects and images and appends them to the views array
- defines controller

And here's what the main while loop does:
- checks for events such as key presses, and sends them to the controller class
- checks for trainwreck or player death, which ends the loop
- moves the train forward
- handles player jumping
- handles collisions
- decreases the speed of player and all things relative to it
- draws all the views on the screen, and finally
- updates the display, making this all look like a continuous game!

And one last thing-- if the player dies, it runs another while loop that displays the end screen!
And that's it!

## So how do I play?
Assuming you're working in Linux, it's really as simple as installing Pygame, cloning this repository, and calling playfile.py in Python using your terminal. This is what this will look like in your command window:

First,
```
$ pip install pygame
```
Next, navigate to where you want to clone the repository. Hit clone or download on this page and copy the url. In your command window, type:
```
$ git clone *copied url*
```
Last, type
```
$ python playfile.py
```
And look out, because now you're playing!

If you run into some issues installing Pygame or even Python, [this is a nice guide to refer to](https://www.pygame.org/wiki/GettingStarted).

## Other questions

#### It's running too slow, what can I do to fix it?
Try lowering the mod on the counter in the first if statement of the main while loop. For example, try turning this:

```
while running == True:
		counter += 1
		if counter%5 == 0: # adjust this
			controller.handle_event()
```
into this:
```
while running == True:
		counter += 1
		if counter%2 == 0: # adjust this
			controller.handle_event()
```
Beyond that, this really isn't the most efficient thing in the world right now... sorry about that.

#### Why do I always lose?
Life isn't fair, buddy. Neither is this.

## License
Hmm.
