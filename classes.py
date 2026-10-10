from helpers import *
from CONSTANTS import *

def valid_square_params(file, rank, colour):
    return file in files and rank in ranks and colour in colours

class Csquare:
    def __init__(self, file, rank, colour):
        if not valid_square_params(file, rank, colour):
            raise ValueError("one of the paramaters passed into the square __init__ function was an invalid parameter")

        self.file = file
        self.rank = rank
        self.colour = colour
        self.index = (files.index(file) * 8 + rank) - 1
        self.piece = None
        
    def __repr__(self):
        return (f"the properties of this square are\nfile = {self.file}\nrank = {self.rank}\ncolour = {self.colour}\nindex = {self.index}\npiece = {self.piece}")

class pawn:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the pawn __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self

        if self.colour:
            self.rep = "white-pawn.png"
        else:
            self.rep = "black-pawn.png"

class knight:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the knight __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self
        
        if self.colour:
            self.rep = "white-knight.png"
        else:
            self.rep = "black-knight.png"

class bishop:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the bishop __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self

        if self.colour:
            self.rep = "white-bishop.png"
        else:
            self.rep = "black-bishop.png"

class rook:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the rook __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self

        if self.colour:
            self.rep = "white-rook.png"
        else:
            self.rep = "black-rook.png"


class king:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the king __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self

        if self.colour:
            self.rep = "white-king.png"
        else:
            self.rep = "black-king.png"

class queen:
    def __init__(self, colour, square):
        if colour not in colours or not isinstance(square, Csquare):
            raise ValueError("one of the parameters passed into the queen __init__ function was an invalid parameter")

        self.colour = colour
        self.square = square
        square.piece = self

        if self.colour:
            self.rep = "white-queen.png"
        else:
            self.rep = "black-queen.png"

def fill_board(board):
    order = [rook, bishop, knight, queen, king, bishop, knight, rook]

    for f in files:
        board[sq2i(f, 1)].piece = order[files.index(f)](0, board[sq2i(f, 1)])
    for f in files:
        board[sq2i(f, 2)].piece = pawn(0, board[sq2i(f, 2)])
    for f in files:
        board[sq2i(f, 8)].piece = order[files.index(f)](1, board[sq2i(f, 8)])
    for f in files:
        board[sq2i(f, 7)].piece = pawn(1, board[sq2i(f, 7)])

    return board

def generate_board():
    board = []
    for f in files:
        for r in ranks:
            board.append(Csquare(f, r, ord(f)%2 == r%2))
    return board

board = fill_board(generate_board())

for i in board:
    print(i)
