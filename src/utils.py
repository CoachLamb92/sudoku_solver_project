from math import sqrt
from src.grid import Area, Column, Row, Cell

def isSquareNumber(number: int):
    return sqrt(number)==int(sqrt(number))

def reduce_potentials_by_solutions(grid):
    for i in range(grid.size):
        """, Area(grid, i)"""
        object_list =  [Row(grid, i), Column(grid, i)]
        for object in object_list:
            for cell in object:
                if cell.solution:
                    for j in range(grid.size):
                        object[j].reduce_potentials(cell.solution)




