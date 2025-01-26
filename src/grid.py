from math import sqrt

class Grid:
    def __init__(self, grid_size: int=9):
        self.__size = grid_size
        self.data = [Cell(i, self.__size) for i in range(self.__size**2)]
    
    @property
    def size(self):
        return self.__size

class Row:
    def __init__(self, grid: Grid, row_id: int=0):
        self.__size = grid.size
        self.row_id = row_id
        self.data = [grid.data[i] for i in range(len(grid.data)) if i >= (row_id * self.__size) and i < (row_id+1)*(self.__size)]

    @property
    def get_size(self):
        return self.__size

class Column(Grid):
    def __init__(self, grid: Grid, column_id: int=0):
        self.__size = grid.size
        self.column_id = column_id
        self.data = [grid.data[i] for i in range(len(grid.data)) if i % self.get_size == self.column_id]

    @property
    def get_size(self):
        return self.__size

class Area(Grid):
    # Only used when grid.size is a square number
    # create a isSquareNumber function?
    def __init__(self, grid: Grid, area_id: int=0):
        self.__size = grid.size
        self.area_id = area_id
        row = int(self.area_id // sqrt(grid.size))
        column = int(self.area_id % sqrt(grid.size))
        row_start = (int(sqrt(grid.size)) * grid.size * row)
        row_and_column_start = row_start + (3 * column)
        self.data = [grid.data[i:i+3] + grid.data[i+self.size:i+self.size+3] + grid.data[i+(2*self.size):i+(2*self.size)+3] for i in range(len(grid.data)) if i == row_and_column_start][0]

    @property
    def size(self):
        return self.__size


class Cell:
    def __init__(self, cell_id: int, grid_size: int, solution: str|None=None):
        self.__cell_id = cell_id
        self.__row_id = cell_id//grid_size
        self.__column_id = cell_id%grid_size
        # To be figured out later
        self.__area_id = None
        self.__solution = solution
        self.__potentials = [str(i+1) for i in range(grid_size)] if solution == None else [solution]

    @property
    def cell_id(self):
        return self.__cell_id
    
    @cell_id.setter
    def cell_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Cell ID must be an integer")
        elif value < 0:
            raise ValueError("Cell ID should not be negative")
        else:
            self.__cell_id = value
    
    @property
    def row_id(self):
        return self.__row_id
    
    @property
    def column_id(self):
        return self.__column_id
    
    @property
    def area_id(self):
        return self.__area_id
    
    @property
    def solution(self):
        return self.__solution
    
    @property
    def potentials(self):
        return self.__potentials

    @potentials.setter
    def potentials(self, potentials_list: list):
        self.__potentials = potentials_list
    
    def reduce_potentials(self):
        # Util function of some descript
        # Another one
        # Each take in area, column, row and potential
        # each return a reduced potential?
        # or one master util takes in arguments then returns potentials once several functions have been applied?
        # reassign self.__potentials
        pass

    def solve(self):
        if len(self.potentials) == 1:
            self.__solution = self.potentials[0]

