from math import sqrt
from src.grid import Row

def isSquareNumber(number: int):
    return sqrt(number)==int(sqrt(number))

# def reduce_potentials_by_solutions(grid):
#     for i in range(grid.size):
#         this_row = Row(grid, i)
#         for cell in this_row:
#             if cell.solution:
#                 number_to_delete = cell.solution
#                 for j in range(grid.size):
#                     try:
#                         grid.data[i*grid.size+j].potentials = entials.remove(number_to_delete)
#                     except ValueError:
#                         pass
                


