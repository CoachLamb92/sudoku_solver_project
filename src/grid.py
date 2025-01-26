class Grid:
    def __init__(self, grid_size: int=9):
        self.__size = grid_size
        self.data = [Cell(i, self.__size) for i in range(self.__size**2)]
    
    @property
    def get_size(self):
        return self.__size

class Row:
    def __init__(self, grid: Grid, row_id: int=0):
        self.__size = grid.get_size
        self.row_id = row_id
        self.data = [grid.data[i] for i in range(len(grid.data)) if i >= (row_id * self.__size) and i < (row_id+1)*(self.__size)]

    @property
    def get_size(self):
        return self.__size

class Column(Grid):
    def __init__(self, grid: Grid, column_id: int=0):
        self.__size = grid.get_size
        self.column_id = column_id
        self.data = [grid.data[i] for i in range(len(grid.data)) if i % self.get_size == self.column_id]

    @property
    def get_size(self):
        return self.__size

class Area(Grid):
    
    def __init__(self, grid: Grid, area_id: int=0):
        self.__size = grid.get_size
        self.area_id = area_id
        self.data = [grid.data[i] for i in range(len(grid.data)) if i % self.get_size == self.area_id]

    @property
    def get_size(self):
        return self.__size
    """
    constraint: grid_size must be a square number
    
    cell_id = 70
    row_id = cell_id // grid.size
    box_row = row_id % sqrt(grid.size)   
    col_id = cell_id % grid.size
    box_col = col_id % sqrt(grid.size)   
    
    area = (box_row * sqrt(grid.size)) + box_col


    """

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
    def get_cell_number(self):
        return self.__cell_id
    @property
    def get_row(self):
        return self.__row_id
    @property
    def get_column(self):
        return self.__column_id
    @property
    def get_area(self):
        return self.__area_id
    @property
    def get_solution(self):
        return self.__solution
    @property
    def get_potentials(self):
        return self.__potentials

    def set_potentials(self, potentials_list: list):
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
        if len(self.get_potentials) == 1:
            self.__solution = self.get_potentials[0]

