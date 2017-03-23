# "Pain Train" the Video Game
### by Charlie Weiss and Diego Garcia

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
Now this function is the thing that pulls the whole game together, and thus, it is probably the most confusing. Here's what it does:

- Initializes pygame and the screen
- defines objects and their views and puts them in appropriate arrays
- defines controller
- Runs main while loop, which updates object positions, draws the corresponding views, and checks for events. This stops running if the player dies or closes the window.
- If the player dies, it runs another while loop which displays the losing screen.

And that's it!

## So how do I play?
## Other questions
####It's running to slow, what can I do to fix it?
####Why do I always lose?
## License/Attribution
