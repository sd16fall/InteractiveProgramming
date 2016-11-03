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
            if self.rotate == 3:
                self.rotate = 0
            else:
                self.rotate +=1
        else: #if counter clockwise
            if self.rotate == 0:
                self.rotate = 3
            else:
                self.rotate -=1
        self.piece_array = Piece.pieces[self.piece_type][self.rotate]

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
        for i in range(self.board_height):
            row = [0]*self.board_width
            self.board.append(row)
        self.generate_piece()

    def generate_piece(self): #sets position on board for where piece shows up
        self.piece = Piece()
        self.x_piece = 3
        self.y_piece = 0

    def collision(self, x, y): #checks if block is not colliding with the board
        """if x >= self.board_width: #collides with right wall
            return True
        elif y >= self.board_height: #collides with bottom
            return True
        elif x < 0: #collides with left wall
            return True
        elif self.board[y][x]: #overlaps
            return True
        return False"""

        #collides with bottom
        bottom_of_piece = self.piece.piece_array[len(self.piece.piece_array)-2]
        #print bottom_of_piece
        for r in bottom_of_piece:
            if r == 1:
                if self.y_piece >= 15:
                    return True
        return False

    def piece_hits_board(self, dx, dy): #checks if any square of the piece hits the board
        for y in range(len(self.piece.piece_array)):
            for x in range(len(self.piece.piece_array[y])):
                if self.piece.piece_array[y][x]:
                    error = self.collision(x = x + dx, y = y + dy)
                    if error:
                        return error

    def can_move(self, dx, dy):
        new_dx = self.x_piece + dx
        new_dy = self.y_piece + dy
        if self.piece_hits_board(dx = new_dx, dy = new_dy):
            return False
        return True

    def absorb_piece(self): #stop when there is a 1 below any 1 in the piece or if it hits the board
        for y in range(len(self.piece.piece_array)):
            for x in range(len(self.piece.piece_array[y])):
                if self.piece.piece_array[y][x]==1:
                    #print 'piece', self.piece.piece_array[y][x], 'board', self.board[y+1][x]
                    print self.piece.piece_array[len(self.piece.piece_array)-2]
                    if self.piece.piece_array[y][x] == self.board[y+1][x] or self.collision(x,y):
                        self.board[y][x] = self.piece.piece_array[y][x]
                        self.draw_board((0,0,225))
        self.generate_piece()

    def rotate_piece(self, clockwise = True):
        self.piece.rotater(clockwise)
        #what do we do if the piece cannot rotate?'''

    def move(self, dx, dy):
        if self.can_move(dx,dy):
            self.x_piece += dx
            self.y_piece += dy

    def piece_falls(self):
        if(self.can_move(dx = 0, dy = 1)):
            self.move(dx = 0, dy = 1)
        else:
            self.absorb_piece()
            self.delete_multiple_lines()

    def hard_drop(self):
        while self.can_move(dx = 0, dy = 1):
            self.piece_falls()
        self.piece_falls()

    def delete_line(self, y):
        """while y>=1:
            self.board[y] = list(self.board[y-1])
            y -= 1"""

    def delete_multiple_lines(self):
        """if range(len(self.piece.piece_array[y])) == True:
            delete = y in range(len(self.piece))
            for y in delete:
                self.delete_line(y)"""
        pass

    def draw_blocks(self, color=(0,0,255), offset_x = 3, offset_y = 0):
        for r in range(0,5):
            for c in range(0,5):
                block = self.piece.piece_array[r][c]
                if block == 1:
                    x = self.block_size*(r+self.x_piece) + offset_x
                    y = self.block_size*(c+self.y_piece) + offset_y
                    pygame.draw.rect(self.screen, (0,0,225), (x, y, self.block_size, self.block_size))

    def draw_board(self, color =(0,0,225)):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                cell = self.board[r][c]
                if cell == 1:
                    x = self.block_size*(r + self.x_piece)
                    y = self.block_size*(c + self.y_piece)
                    #print 'r', r, 'c',c
                    pygame.draw.rect(self.screen, (0,0,225), (x, y, self.block_size, self.block_size))

    def game_over(self):
        pass #return sum(self.board[0]) > 0 or sum(self.board[1]) > 0

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
            self.board.draw_blocks(self, offset_x = 3, offset_y = 0)
            self.board.draw_board(self)
            pygame.display.update()

if __name__ == "__main__":
    Game().run_game()
