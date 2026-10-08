files = [chr(ord("A") + i) for i in range(8)]
ranks = [i+1 for i in range(8)]
colours = [0,1]
# 0 represents a dark square
# 1 represents a light square

def valid_square_params(file, rank, colour):
    return file in files and rank in ranks and colour in colours

class square:
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
