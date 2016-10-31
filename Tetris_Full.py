import pygame, sys, random
from pygame.locals import *

'''Generating Pieces'''
class Piece:

    t_block = (((0,0,0,0,0),(0,0,1,0,0),(0,0,1,1,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(0,1,1,1,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,0,0),(0,1,1,0,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,0,0),(0,1,1,1,0),(0,0,0,0,0),(0,0,0,0,0)))

    s_block = (((0,0,0,0,0),(0,0,1,0,0),(0,0,1,1,0),(0,0,0,1,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(0,0,1,1,0),(0,1,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,1,0,0,0),(0,1,1,0,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,1,0),(0,1,1,0,0),(0,0,0,0,0),(0,0,0,0,0)))

    z_block = (((0,0,0,0,0),(0,0,0,1,0),(0,0,1,1,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(0,1,1,0,0),(0,0,1,1,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,0,0),(0,1,1,0,0),(0,1,0,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,1,1,0,0),(0,0,1,1,0),(0,0,0,0,0),(0,0,0,0,0)))

    i_block = (((0,0,0,0,0),(0,0,0,0,0),(0,1,1,1,1),(0,0,0,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,1,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(1,1,1,1,0),(0,0,0,0,0),(0,0,0,0,0)),
                 ((0,0,1,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,0,0,0)))

    l_block = (((0,0,0,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,1,1,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(0,1,1,1,0),(0,1,0,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,1,1,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,1,0),(0,1,1,1,0),(0,0,0,0,0),(0,0,0,0,0)))

    j_block = (((0,0,0,0,0),(0,0,1,0,0),(0,0,1,0,0),(0,1,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,1,0,0,0),(0,1,1,1,0),(0,0,0,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,1,1,0),(0,0,1,0,0),(0,0,1,0,0),(0,0,0,0,0)),
                 ((0,0,0,0,0),(0,0,0,0,0),(0,1,1,1,0),(0,0,0,1,0),(0,0,0,0,0)))

    o_block = (((0,0,0,0,0),(0,0,0,0,0),(0,0,1,1,0),(0,0,1,1,0),(0,0,0,0,0)),)*4

    pieces = {'t': t_block, 's': s_block, 'z': z_block, 'i': i_block, 'l': l_block, 'j': j_block, 'o': o_block}

    def __init__(self, piece_type = None):
        if piece_type: #if there is already currently a piece, use the piece
            self.piece_type = piece_type
        else:
            random_piece = random.choice(Piece.pieces.keys()) #if there isn't a piece then generate a piece
            self.piece_type = random_piece
        self.rotate = 0
        self.piece_array = Piece.pieces[self.piece_type][self.rotate] #specific piece and rotation of the piece

    def rotater(self, clockwise = True):
        if clockwise:
            if self.rotate == 3: #if piece is at rotation position 3, resets back to original position
                self.rotate = 0
            else:
                self.rotate +=1
        else: #if counter clockwise
            if self.rotate == 0:
                self.rotate = 3
            else:
                self.rotate -=1
        self.piece_array = Piece.pieces[self.piece_type][self.rotate]

"""    def color():
        For i in range(len[cells]):
    	Row = cells[i]
    	For j in range(len[cells]):
        Color = row[j]"""

'''Generating Board'''
class Board:
    def __init__(self,screen):
        self.screen = screen
        self.block_size = 20 #multiplier for pixels to represent a block
        self.board_height = 20
        self.board_width = 10
        self.board_pix_height = self.board_height * self.block_size #translates the board dimension into pixels
        self.board_pix_width = self.board_width * self.block_size
        self.board = []
        for i in range(self.board_width):
            row = []*self.board_height
            self.board.append(row)
        self.generate_piece()

    def generate_piece(self): #sets position on board for where piece shows up
        self.piece = Piece()
        self.x_piece = 4
        self.y_piece = 0

    def block_error(self, x, y): #checks if block is not colliding with the board
        if x >= self.board_width: #collides with right wall
            return True
        elif y >= self.board_height: #collides with bottom
            return True
        elif x < 0: #collides with left wall
            return True
        elif self.board[y][x]: #overlaps
            return True
        return False

    def piece_hits_board(self, dx, dy):
        for y in range(len(self.piece.piece_type)): #looks at the y value for the array of a piece
            for x in range(len(self.piece.piece_type[y])): #looks at the x value for every row of the array
                if self.piece.piece_type[y][x]:
                    error = self.block_error(x=x+dx, y=y+dy)
                    if error:
                        return error

    def can_move(self, dx, dy):
        new_dx = self.x_piece + dx #takes the current position of the piece and determines whether the proposed action is acceptable
        new_dy = self.y_piece + dy
        if self.piece_hits_board(dx = new_dx, dy = new_dy):
            return False
        return True

    def attach_piece(self):
        for y in range(len(self.piece)):
            for x in range(len(self.piece[y])):
                if self.piece[y][x]:
                    self.piece[y][x] = self.board[y+self.y_piece][x+self.x_piece] #adds values of new piece joining existing piece
        self.generate_piece()

    def rotate_piece(self, clockwise = True):
        self.piece.rotater(clockwise)
        #what do we do if the piece cannot rotate?'''

    def move(self, dx, dy): #checks if the proposed action is acceptable and then moves the piece
        if self.can_move(dx,dy):
            self.x_piece += dx
            self.y_piece += dy

    def piece_falls(self): #moves the piece drop down if it is able to, otherwise either attach the piece or delete the line
        if(self.can_move(dx = 0, dy = 1)):
            self.move(dx = 0, dy = 1)
        else:
            self.attach_piece()
            self.delete_lines()

    def hard_drop(self): #drops the piece all the way to the bottom
        while self.can_move(dx = 0, dy = 1):
            self.piece_falls()
        self.piece_falls()

    def delete_line(self, y): #checks if entire row is filled and if so, deletes a line and pushes everything else down one row
        while y>=1:
            self.board[y] = list(self.board[y-1])
            y -= 1

    def delete_multiple_lines(self):
        if range(len(self.piece[y])) == True:
            delete = y in range(len(self.piece)) #sets delete to the number of rows filled
            for y in delete:
                self.delete_line(y)

    def draw_blocks(self, color=(0,0,255), offset_x = 4, offset_y = 0):
        for r in range(0,5):
            for c in range(0,5):
                block = self.piece.piece_array[r][c]
                if block == 1:
                    x = self.block_size*r + offset_x
                    y = self.block_size*c + offset_y
                    pygame.draw.rect(self.screen, (0,0,225), (x, y, self.block_size, self.block_size))

    def game_over(self):
        return sum(self.board[0]) > 0 or sum(self.board[1]) > 0 #if the pieces reach the top of the board then game is over

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((200,400))
        self.board = Board(self.screen)

    def pause_game(self):
        continuing = True
        while continuing:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuing = False

    def key_controls(self, key):
        if key == K_LEFT:
            self.board.move(dx=-1, dy=0)
        elif key == K_RIGHT:
            self.board.move(dx=1, dy=0)
        elif key == K_DOWN:
            self.board.piece_falls()
        elif key == K_SPACE:
            self.board.hard_drop()
        elif key == K_UP:
            self.board.rotate_piece()
        elif key == K_ESCAPE:
            self.pause()

    def run_game(self):
        pygame.init()
        while True:
            if self.board.game_over():
                print 'Game Over' #place holder, replace with picture
                pygame.quit()
                sys.exit()
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.key_controls(event.key)
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.board.draw_blocks(self, offset_x = 4, offset_y = 0)
            pygame.display.update()

if __name__ == "__main__":
    Game().run_game()
