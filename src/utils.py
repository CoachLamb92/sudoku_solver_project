from math import sqrt
from src.grid import Area, Column, Row, Cell

def isSquareNumber(number: int):
    return sqrt(number)==int(sqrt(number))

def reduce_potentials_by_solutions(grid):
    for i in range(grid.size):
        object_list =  [Row(grid, i), Column(grid, i), Area(grid, i)]
        for object in object_list:
            for cell in object:
                if cell.solution:
                    for j in range(grid.size):
                        object[j].reduce_potentials(cell.solution)

def one_number_left(grid):
    for i in range(grid.size):
        object_list =  [Row(grid, i), Column(grid, i), Area(grid, i)]
        for object in object_list:
            for j in range(1, grid.size + 1):   # J = 1
                if j in [cell.solution for cell in object]:
                    continue
                total = 0
                cell_id = -1
                for k in range(grid.size): # CELL
                    if not object[k].solution and j in object[k].potentials:
                        total += 1
                        cell_id = k
                        if total == 2:
                            break
                if total == 1:
                    object[cell_id].solution = j

