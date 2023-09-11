import copy
import sys
import random

sys.setrecursionlimit(5000)

all_shapes = {}

class Shape:
    def __init__(self, shape):
        self.shape = shape
        self.rows = len(self.shape)
        self.cols = len(self.shape[0])

    def add(self, board, x, y):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    board[x + i][y + j] = 1
    
    def get_height(self):
        return int(self.rows)
    
    def get_width(self):
        return int(self.cols)
    
    def rotate_shape(self):
        rotated = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                rotated[j][self.rows - i - 1] = self.shape[i][j]

        return Shape(rotated)
    
    def flip(self):
        return Shape(self.shape[::-1])
            
    
    def add_to_dict(self, my_dict, val):
        key = 'shape' + str(val)
        my_dict[key] = [self]
        for _ in range(3):
            self = self.rotate_shape()
            if self not in my_dict[key]:
                my_dict[key].append(self)
        self = self.flip()
        for _ in range(3):
            self = self.rotate_shape()
            if self not in my_dict[key]:
                my_dict[key].append(self)
    
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.shape)

class Board:
    def __init__(self, board):
        self.board = board
    
    def __str__(self) -> str:
        board_str = ""
        for row in self.board:
            board_str += " ".join(map(str, row)) + "\n"
        return board_str
    
    def get_height(self):
        return int(len(self.board))
    
    def get_width(self):
        return int(len(self.board[0]))

layout = [
    [0, 0, 0, 0, 0, 0, '.'],
    [0, 0, 0, 0, 0, 0, '.'],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, '.', '.', '.', '.']
]

my_board = Board(layout)

first = Shape([[0, 0, 0, 1], 
               [1, 1, 1, 1]
               ])
second = Shape([[1, 1, 1],
                [1, 0, 1]
                ])
third = Shape([[1, 1, 1],
               [1, 1, 1]])
fourth = Shape([[0, 1, 1, 1],
                [1, 1, 0, 0]
                ])
fifth = Shape([[0, 0, 1],
               [1, 1, 1],
               [1, 0, 0]
               ])
sixth = Shape([[1, 1, 1],
               [1, 0, 0],
               [1, 0, 0]
               ])
seventh = Shape([[0, 1, 0, 0],
                 [1, 1, 1, 1]
                 ])
eighth = Shape([[1,1,1],
                [1,1,0]
                ])
shapes = [first, second, third, fourth, fifth, sixth, seventh,eighth]

n = 1
for shape in shapes:
    shape.add_to_dict(all_shapes, n)
    n += 1

def is_valid_placement(board, shape, x, y):
    """Checks if given shape can be placed

    Args:
        board (Board): object storing the current puzzle board
        shape (Shape): object storing shape layout
        x (int): position
        y (int): position

    Returns:
        Bool: True if shape can be placed, False otherwise
    """
    for i in range(shape.get_height()):
        for j in range(shape.get_width()):
            if (
                shape.shape[i][j] == 1
                and (
                    x + i < 0
                    or x + i >= board.get_height()
                    or y + j < 0
                    or y + j >= board.get_width()
                    or board.board[x + i][y + j] != 0
                )
            ):
                return False
    return True

def place_shape(board, shape, x, y,n):
    """Places shape on voard

    Args:
        board (Board): object storing puzzle boars
        shape (Shape): object storing shape layout
        x (int): position
        y (int): position
        n (int): value to place
    """
    for i in range(shape.get_height()):
        for j in range(shape.get_width()):
            if shape.shape[i][j] == 1:
                board.board[x + i][y + j] = n

def get_random_shape(my_dict, temp_used):
    """Returns random shape from those not in temp_used

    Args:
        my_dict (dictionary): stores all shapes and their rotations
        temp_used (list): stores shapes already tried in given cell

    Returns:
        Shape: random shape
    """
    random_shape = random.choice(list(my_dict.keys()))
    while random_shape in temp_used:
        random_shape = random.choice(list(my_dict.keys()))
        
    return random_shape

def get_all_rotation(my_dict,used_shapes):
    """Returns all rotations that should be tried

    Args:
        my_dict (dictionary): stores all rotations in format my_dict[shape] = [rotation1,rotation2,...]
        used_shapes (list): stores all previously placed shapes

    Returns:
        list(shape,rotation): contains all rotations left to try
    """
    ans =[]
    n = len(my_dict.keys())-len(used_shapes)
    temp_used = copy.deepcopy(used_shapes)
    for _ in range(n):
        shape = get_random_shape(my_dict,temp_used)
        temp_used.append(shape)
        for rotation in my_dict[shape]:
            ans.append((shape,rotation))
    
    return ans

def all_cells_not_0(board):
    """Checks if the entire board is filled

    Args:
        board (Board): stores the puzzle board

    Returns:
        Bool: True if entire board filled, False otherwise
    """
    for rows in range(board.get_height()):
        for cols in range(board.get_width()):
            if board.board[rows][cols] == 0:
                return False
    return True

#declaring what date should be solved
my_board.board[1][2] = '.'
my_board.board[3][3] = '.'

def master(my_dict,board, used_shapes,default,n):
    """Places a random shape/rotation in the first free cell on the board, if none possible restarts the puzzle

    Args:
        my_dict (dictionary): stores all shapes and their rotations
        board (Board): object storing puzzle board
        used_shapes (list): stores shapes previously placed on board
        default (2d_array): array that stores the default puzzle board layout
        n (int): value to keep track of the shape placed on board

    Returns:
        Bool: True once entire board is filled, otherwise returns variables for next iteration
    """
    print(used_shapes)
    for rows in range(board.get_height()):
        for cols in range(board.get_width()): 
            if board.board[rows][cols] == 0:
                for shape,rotation in get_all_rotation(my_dict,used_shapes):
                    print('h')
                    if is_valid_placement(board, rotation, rows, cols):
                        place_shape(board, rotation, rows, cols,n)
                        n+=1
                        used_shapes.append(shape)
                        return board,used_shapes,n
                return Board(copy.deepcopy(default)),[],1
    return True

working_dict = copy.deepcopy(all_shapes)
b = Board(copy.deepcopy(my_board.board))
working_used_shapes = []
n=1
while not all_cells_not_0(b):
    b_old = Board(copy.deepcopy(b.board))
    used_shapes_old = copy.deepcopy(working_used_shapes)
    b,working_used_shapes,n = master(working_dict, b, working_used_shapes, layout,n)

print(b)