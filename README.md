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
### Main Function

## How do I play?
## Other questions
## License/Attribution
