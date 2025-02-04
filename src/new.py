
"""
  BOX 0       BOX 1       BOX 2
 0  1  2     3  4  5     6  7  8
 9 10 11    12 13 14    15 16 17
18 19 20    21 22 23    24 25 26

  BOX 3       BOX 4       BOX 5
27 28 29    30 31 32    33 34 35
36 37 38    39 40 41    42 43 44
45 46 47    48 49 50    51 52 53

  BOX 6       BOX 7       BOX 8
54 55 56    57 58 59    60 61 62
63 64 65    66 67 68    69 70 71
72 73 74    75 76 77    78 79 80

top_left = ((area_id%int(sqrt(grid.size))) * int(sqrt(grid.size))) + ((area_id//int(sqrt(grid.size))) * grid.size * int(sqrt(grid.size)))

self._data = [grid.data[top_left+(0*self.size):top_left+int(sqrt(self.size))] for i in int(sqrt(grid.size))]

# self._data = [
# grid.data[  i+(0*self.size)  :  i+int(sqrt(self.size))] +    # 0, 1, 2
# grid.data[  i+(1*self.size)  :  i+int(sqrt(self.size))] +    # 9, 10, 12 
# grid.data[  i+(2*self.size)  :  i+int(sqrt(self.size))] +    # 18, 19, 20
# for i in range(len(grid.data)) if i == row_and_column_start
# ][0]

# def __init__(self, grid: Grid, area_id: int=0):
# self._size = 4
#         self._area_id = area_id                             0   1   2   3   
#         row = int(self.area_id // 2)                        0   0   1   1
#         column = int(self.area_id % 2)                      0   1   0   1
#         row_start = (2 * 4 * row)                           0   0   8   8
#         row_and_column_start = row_start + (4 * column)     0   4   8   12


# id                                      0   1   2   3

# id%int(sqrt(grid.size))                 0   1   2   0
# * int(sqrt(grid.size))                  0   3   6   0
# ((id%int(sqrt(grid.size))) * int(sqrt(grid.size)))

# id//int(sqrt(grid.size))                0   0   0   1
# * grid.size * int(sqrt(grid.size))      0   0   0   27
# ((id//int(sqrt(grid.size))) * grid.size * int(sqrt(grid.size)))
#                                         0   3   6   27

((i%int(sqrt(grid.size))) * int(sqrt(grid.size))) + ((i//int(sqrt(grid.size))) * grid.size * int(sqrt(grid.size)))

"""