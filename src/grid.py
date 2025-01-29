from math import sqrt
# from src.utils import isSquareNumber

class Grid:
    def __init__(self, grid_size: int=9):
        self._size = grid_size
        self.data = [Cell(i, self.size) for i in range(self.size**2)]
    
    @property
    def size(self):
        return self._size

    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value



class Row(Grid):
    def __init__(self, grid: Grid, row_id: int=0):
        self._size = grid.size
        self._row_id = row_id
        self._data = [grid.data[i] for i in range(len(grid.data)) if i >= (self.row_id * self.size) and i < (self.row_id+1)*(self.size)]

    def __str__(self):
        return str([self.data[i].solution for i in range(self.size)])
    
    @property
    def size(self):
        return self._size
    
    @property
    def row_id(self):
        return self._row_id
    
    @property
    def data(self):
        return self._data

class Column(Grid):
    def __init__(self, grid: Grid, column_id: int=0):
        self._size = grid.size
        self._column_id = column_id
        self._data = [grid.data[i] for i in range(len(grid.data)) if i % self.size == self.column_id]

    @property
    def size(self):
        return self._size
    
    @property
    def column_id(self):
        return self._column_id
    
    @property
    def data(self):
        return self._data

class Area(Grid):
    # Only used when grid.size is a square number
    # create a isSquareNumber function?
    def __init__(self, grid: Grid, area_id: int=0):
        self._size = grid.size
        self._area_id = area_id
        row = int(self.area_id // sqrt(self.size))
        column = int(self.area_id % sqrt(self.size))
        row_start = (int(sqrt(self.size)) * self.size * row)
        row_and_column_start = row_start + (self.size * column)
        self._data = [grid.data[i:i+self.size] + grid.data[i+self.size:i+self.size+self.size] + grid.data[i+(2*self.size):i+(2*self.size)+self.size] for i in range(len(grid.data)) if i == row_and_column_start][0]

    @property
    def size(self):
        return self._size
    
    @property
    def area_id(self):
        return self._area_id
    
    @property
    def data(self):
        return self._data

class Cell:
    def __init__(self, cell_id: int, grid_size: int, solution: str|None=None):
        self._cell_id = cell_id
        self._row_id = cell_id//grid_size
        self._column_id = cell_id%grid_size
        self._area_id = (sqrt(grid_size)*self.row_id//(sqrt(grid_size))) + (self.column_id//int(sqrt(grid_size)))
        self._solution = solution
        self._potentials = [i+1 for i in range(grid_size)] if solution == None else [solution]

    @property
    def cell_id(self):
        return self._cell_id
    
    @cell_id.setter
    def cell_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Cell ID must be an integer")
        elif value < 0:
            raise ValueError("Cell ID should not be negative")
        else:
            self._cell_id = value
    
    @property
    def row_id(self):
        return self._row_id
    
    @property
    def column_id(self):
        return self._column_id
    
    @property
    def area_id(self):
        return self._area_id
    
    @property
    def solution(self):
        return self._solution
    
    @solution.setter
    def solution(self, solution: int):
        if solution == 0:
            self._solution = None
        else:
            self._solution = solution
    
    @property
    def potentials(self):
        return self._potentials

    @potentials.setter
    def potentials(self, potentials_list: list):
        self._potentials = potentials_list
    
    def reduce_potentials(self, number):
        try:
            self.potentials.remove(number)
        except ValueError:
            pass

    def solve(self):
        if len(self.potentials) == 1:
            self._solution = self.potentials[0]

