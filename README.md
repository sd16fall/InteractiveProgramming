# "Pain Train" the Video Game
### by Charlie Weiss and Diego Garcia

## What is this?
This is a video game created using Python's pygame library and an MVP (model-viewer-player) framework. It is a platform game with a player, a chaser, and some obstacles. The player loses by either being overtaken by the chaser, or by falling to their death.

## How does it work?
The code is split into three collections of classes: The Model classes, the View classes, and the Controller classes. The functions in these classes are called by the main function (found at the bottom of the file), which runs the game with a while loop. Here's some more detail about those sections:

### Model Classes
These contain the definition of the models of each type of object in the game, and their interactions with other objects or events. Each class defines things such as an object's postion, height, width, and distance traveled per loop. Here's an example of a model class:

```class PainTrain(object):
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

### View Classes
### Controller Classes
### Main Function

## How do I play?
## Other questions
## License/Attribution
