***Model***
Import pygame


#Defining colors
Purple = (80, 0.0, 120)
Red = (240, 0.0, 0.0)
Green = (0.0, 240, 0.0)
Aqua = (0.0, 240, 240)
Orange = (240, 160, 0.0)
Blue = (0.0, 0.0, 240)
Yellow = (240, 240, 0.0)


class Point(object):
    def __init__(self):
    self.x = x
    self.y = y


class Block(object):
    def __init__(self):
        self.length = side_length
class t(block):
    Pass


class s(block):
    Pass


class z(block):
    Pass


class i(block):
Pass


class l(block):
    Pass


class j(block):
    Pass


class o(block):
    Pass


class board(object):
    def __init__(self):
        self.width = width
        self.length = length




***View***
Class blockController(object):
    def __init__(self, models):
        self. models = models
    
    def rotate(): #if the input is up arrow or down arrow, rotate the piece 90 degrees


    def hardDrop(): #if the input is space bar, then place block in available space below


    def stop(): #lock the piece into place when lays on top of another piece


def start_game():
    #start screen with text, click any button to start game


def view_board():
    #creates the Tetris board


def addTextToScreen():
    #add start screen and rules, end game screen


def countAndDeleteLine():
    #remove completed line
    line += 1
return line


def score(line):
    #calculate game score


def generatePiece():
    #randomly generate piece
    return piece


def addPieceToBoard(piece):
    #adds the piece to the board based on user’s actions


def showNextPiece(piece):
    #displays the next piece coming up in the game


def speedUpPiece():
    #speeds up the falling of the piece as lines completed increases




***Controller***
def main():
pygame.init()


FPS = 30 #frames per second
screen = pygame.display.set_mode((800, 600))
screen.fill(0,0,0)
pygame.display.set_caption('Tetris')
    while event == True : #main game loop
            for event in pygame.event.get():


    #add music code here
    pygame.mixer.music.load(mp3 file here)
    pygame.mixer.music.play(-1 ,0.0)
    pygame.mixer.music.stop()
            
pygame.quit()
               pygame.display.update()


