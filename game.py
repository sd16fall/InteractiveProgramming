import sys
import pygame
import random

class GameManager(object): #*args, **kwargs
    def __init__(self, **kwargs):
        # Initliizlies PyGame Window & Gameover Font
        pygame.display.init()
        pygame.font.init()

        # Defineing Color RGB Values for GUI elements
        self.white = (255, 255, 255)
        self.black = (0, 0,0 )
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.brick = (144, 69, 53)
        self.sky_blue= (52, 152, 219)

        self.display_width = kwargs.pop('display_width')
        self.display_height = kwargs.pop('display_height')

        self.game_display = pygame.display.set_mode((self.display_width,self.display_height))
        self.game_display.fill(self.sky_blue)
        if 'caption' in kwargs:    
            pygame.display.set_caption(caption)
        else:
            pygame.display.set_caption('Unicorn Squad')

        self.clock = pygame.time.Clock()
        if 'FPS' in kwargs:    
            self.FPS = kwargs.pop('FPS')
        else:
            self.FPS = 10
        
        self.font = pygame.font.SysFont(None, 55)

    def game_did_quit(self):
        gameExit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        return gameExit

    def add_icon(self,icon,location):
        self.game_display.blit(icon,location)

    def get_center(self):
        return (self.display_width/2, self.display_height/2)

    def did_collide(self,obj1, obj2):
        if obj1.x > obj2.x and obj1.x < obj2.x + obj2.image_width or obj1.x + obj1.image_width > obj2.x and obj1.x + obj1.image_width < obj2.x + obj2.image_width:
            if obj1.y > obj2.y and obj1.y < obj2.y + obj2.image_height:
                return True
            elif obj1.y + obj1.image_height > obj2.y and obj1.y + obj1.image_height < obj2.y + obj2.image_height:
                return True
        return False

#display_width,display_height, caption='Unicorn Squad', FPS=10

class SnakeGame(GameManager):
    def __init__(self,**kwargs):
        super(SnakeGame,self).__init__(**kwargs)

    def is_game_over(self,snake):
        if snake.x >= self.display_width or snake.x < 0 or snake.y >= self.display_height or snake.y < 0:
            return True
        return False

    def fill_blue(self):
        self.game_display.fill(self.sky_blue)

    # Initliazes text object
    def text_objects(self, text, color):
        textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    # Defines  display message with color variable
    def message_to_screen(self, msg, color, y_displace=0):
        textSurf, textRect = self.text_objects(msg,color)
        textRect.center = (self.display_width / 2), (self.display_height / 2) + y_displace
        self.game_display.blit(textSurf, textRect)

    def score_to_screen(self, msg, color):
        textSurf, textRect = self.text_objects(msg, color)
        textRect = (self.display_width - 50), (self.display_height - 50)
        self.game_display.blit(textSurf, textRect)

class Image(object):
    def __init__(self,**kwargs):
        self.start_pos = kwargs.pop('start_pos') #(x,y)
        self.icon = pygame.image.load(kwargs.pop('icon'))
        self.icon = pygame.transform.scale(self.icon, (kwargs.pop('image_width'), kwargs.pop('image_height')))
        self.x = self.start_pos[0]
        self.y = self.start_pos[1]
        if 'image_width' in kwargs:  
            self.image_width = kwargs.pop('image_width')
        else:
            self.image_width = 50 
        if 'image_height' in kwargs:  
            self.image_height = kwargs.pop('image_height')
        else:
            self.image_height = 50


#start_pos=(0,0),icon='food.png', image_width=50, image_height=50

class Carrot(Image):
    def __init__(self,**kwargs):
        super(Carrot,self).__init__(**kwargs)
    
    def set_random_location(self,display_width,display_height):
        self.x = round(random.randrange(0, display_width-self.image_width))
        self.y = round(random.randrange(0, display_height-self.image_height))
        self.start_pos = (self.x,self.y)

class Rainbow(Image):
    def __init__(self, **kwargs):
        super(Rainbow,self).__init__(**kwargs)

class Snake(Image):
    def __init__(self,**kwargs):
        super(Snake,self).__init__(**kwargs)
        self.tail_list = []
        self.tail_size = 1
        self.direction = "right"
        self.delta_y = 0
        self.delta_x = 40

    def add_to_tail(self):
        gameOver = False
        snake_head = []
        snake_head.append(self.x)
        snake_head.append(self.y)

        self.tail_list.append(snake_head)

        if len(self.tail_list) > self.tail_size:
            del self.tail_list[0]

        for eachSegment in self.tail_list[:-1]:
            if eachSegment == snake_head:
                gameOver = True
        
        return gameOver

    def handle_tail(self):
        if self.direction == "right":
            head = self.icon

        if self.direction == "left":
            head = pygame.transform.flip(self.icon, 1, 0)

        if self.direction == "up":
            head = pygame.transform.rotate(self.icon, 90)

        if self.direction == "down":
            head = pygame.transform.rotate(self.icon, 270)
        
        return head
        

    def process_move(self):
        gameExit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = "left"
                    self.delta_x = -self.image_width
                    self.delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    self.direction = "right"
                    self.delta_x = self.image_width
                    self.delta_y = 0
                elif event.key == pygame.K_UP:
                    self.direction = "up"
                    self.delta_y = -self.image_height
                    self.delta_x = 0
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"
                    self.delta_y = self.image_height
                    self.delta_x = 0
        return gameExit

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        # self.delta_x = 0
        # self.delta_y = 0

class Player:
    def __init__(self):
        self.player_score = 0

    def set_score(self,score):
        self.player_score = score
    
    def increase_score(self):
        self.player_score += 1
    
    def decrease_score(self):
        self.player_score -= 1
    
    def reset_score(self):
        self.player_score = 0    

def run_game(display_width,display_height):
    gameExit = False # HItting the close button (closing Window)
    gameOver = False # Internal game over view (Hitting the walls or your own tail)
    game = SnakeGame(display_width=display_width,display_height=display_height)
    player = Player()

    snake = Snake(start_pos=game.get_center(),image_height=50,image_width=50, icon="unicorn.png")

    carrot = Carrot(icon='food.png',image_height=50,image_width=50, start_pos=(0,0))
    carrot.set_random_location(display_width,display_height)

    while not gameExit:
        while gameOver:
            game.game_display.fill(game.white)
            game.message_to_screen("Game Over!", game.red, -50)
            game.message_to_screen("Press C to play again, or Q to quit", game.black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                # Maps keboard strokes to close game and redo game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                        exit()
                    if event.key == pygame.K_c:
                        run_game(display_width,display_height)
        
        gameExit = snake.process_move()

        
        snake.move()

        gameOver = game.is_game_over(snake)
        

        #fill blue
        game.fill_blue()

        game.add_icon(carrot.icon,(carrot.x,carrot.y))
        
        gameOver2 = snake.add_to_tail()
        if not gameOver:
            gameOver = gameOver2
        head = snake.handle_tail() #drawing snake

        # defines movement of snake tail
        game.game_display.blit(head, (snake.tail_list[-1][0], snake.tail_list[-1][1]))

        #  defines adding of rainbow image to user sprite
        for XnY in snake.tail_list[:-1]:
            rainbow = Rainbow(icon="rainbow.png", image_height=50, image_width=50, start_pos=(0,0)).icon
            game.game_display.blit(rainbow,(XnY[0], XnY[1]))

        game.score_to_screen(str(player.player_score), game.white)

        pygame.display.update()

        if (game.did_collide(snake,carrot)):
            carrot.set_random_location(display_width,display_height)
            snake.tail_size += 1
            player.increase_score()
        
        game.clock.tick(game.FPS)


    pygame.display.quit(str())
    pygame.quit()

run_game(800,600)