from src.utils import isSquareNumber, reduce_potentials_by_solutions
from src.example_grids import only_ones_four_by_four_grid as oofxfgrid
from src.example_grids import mixed_four_by_four_grid as mxfxfgrid
from src.example_grids import only_ones_nine_by_nine_grid as oonxngrid
from src.example_grids import mixed_nine_by_nine_grid as mxnxngrid
from src.grid import Grid, Row, Column, Area, Cell

class TestIsSquareNumberFunction:
    def test_utils_returns_true_correctly(self):
        # Arrange
        input_number = 9
        expected = True
        # Act
        result = isSquareNumber(input_number)
        # Assert
        assert expected == result

        # Arrange
        input_number = 4
        expected = True
        # Act
        result = isSquareNumber(input_number)
        # Assert
        assert expected == result

    def test_utils_returns_false_correctly(self):
        # Arrange
        input_number = 8
        expected = False
        # Act
        result = isSquareNumber(input_number)
        # Assert
        assert expected == result

        # Arrange
        input_number = 6
        expected = False
        # Act
        result = isSquareNumber(input_number)
        # Assert
        assert expected == result

class TestReducePotentialsBySolutions:
    def test_function_works_on_simple_four_by_four_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(oofxfgrid)): dummy_grid[i].solution = oofxfgrid[i]
        expected_potentials = [2, 3, 4]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for cell in dummy_grid: assert expected_potentials == cell.potentials

    def test_function_works_on_complex_four_by_four_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(mxfxfgrid)): dummy_grid[i].solution = mxfxfgrid[i]
        expected_grid_potentials = [[4], [4], [], [4],
                                    [4], [4], [], [2, 4],
                                    [], [], [], [],
                                    [4], [4], [], [3]]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for i in range(len(mxfxfgrid)):
            assert expected_grid_potentials[i] == dummy_grid[i].potentials

    def test_function_works_on_simple_nine_by_nine_grid(self):
        # Arrange
        dummy_grid = Grid(9)
        for i in range(len(oonxngrid)): dummy_grid[i].solution = oonxngrid[i]
        expected_potentials = [2, 3, 4, 5, 6, 7, 8, 9]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for cell in dummy_grid: assert expected_potentials == cell.potentials

    def test_function_works_on_complex_nine_by_nine_grid(self):
        # Arrange
        dummy_grid = Grid(9)
        for i in range(len(mxnxngrid)): dummy_grid[i].solution = mxnxngrid[i]
        expected_grid_potentials_row_0 = [[4, 5, 6, 9],
                                          [4, 5, 6, 7, 9],
                                          [4, 5, 7],
                                          [4, 5, 6, 7, 8, 9],
                                          [5, 7, 8],
                                          [4, 5, 6, 7, 8, 9],
                                          [4, 5, 6, 8, 9],
                                          [4, 7, 8, 9],
                                          [4, 5, 6, 7, 8, 9]]
        
        expected_grid_potentials_row_1 = [[4, 5, 6, 9],
                                          [4, 5, 6, 7, 9],
                                          [4, 5, 7],
                                          [3, 4, 5, 6, 7, 9],
                                          [3, 5, 7],
                                          [3, 4, 5, 6, 7, 9],
                                          [4, 5, 6, 9],
                                          [4, 7, 9],
                                          [4, 5, 6, 7, 9]]
        
        expected_grid_potentials_row_2 = [[2, 4, 5, 6, 9],
                                          [2, 4, 5, 6, 7, 9],
                                          [2, 4, 5, 7],
                                          [4, 5, 6, 7, 8, 9],
                                          [5, 7, 8],
                                          [4, 5, 6, 7, 8, 9],
                                          [4, 5, 6, 8, 9],
                                          [4, 7, 8, 9],
                                          [4, 5, 6, 7, 8, 9]]
        
        expected_grid_potentials_row_3 = [[4, 5, 6, 8, 9],
                                          [3, 4, 5, 6, 7, 9],
                                          [3, 4, 5, 7],
                                          [3, 4, 5, 7, 8, 9],
                                          [3, 5, 7, 8],
                                          [3, 4, 5, 7, 8, 9],
                                          [3, 4, 5, 6, 8, 9],
                                          [4, 8, 9],
                                          [3, 4, 5, 6, 8, 9]]
        
        expected_grid_potentials_row_4 = [[2, 4, 5, 8, 9],
                                          [2, 3, 4, 5, 7, 9],
                                          [2, 3, 4, 5, 7],
                                          [3, 4, 5, 7, 8, 9],
                                          [2, 3, 5, 7, 8],
                                          [2, 3, 4, 5, 7, 8, 9],
                                          [3, 4, 5, 8, 9],
                                          [4, 8, 9],
                                          [3, 4, 5, 8, 9]]
        
        expected_grid_potentials_row_5 = [[2, 4, 5, 6, 8, 9],
                                          [2, 3, 4, 5, 6, 9],
                                          [2, 3, 4, 5],
                                          [3, 4, 5, 8, 9],
                                          [2, 3, 5, 8],
                                          [2, 3, 4, 5, 8, 9],
                                          [3, 4, 5, 6, 8, 9],
                                          [4, 8, 9],
                                          [3, 4, 5, 6, 8, 9]]
        
        expected_grid_potentials_row_6 = [[4],
                                          [3, 4],
                                          [3, 4],
                                          [3, 6, 7, 8],
                                          [3, 7, 8],
                                          [3, 6, 7, 8],
                                          [3, 4, 8],
                                          [4, 7, 8],
                                          [3, 4, 7, 8]]
        
        expected_grid_potentials_row_7 = [[2, 5],
                                          [2, 3, 5],
                                          [2, 3, 5],
                                          [3, 5, 7],
                                          [2, 3, 5, 7],
                                          [2, 3, 5, 7],
                                          [3, 9],
                                          [7, 9],
                                          [3, 7, 9]]
        
        expected_grid_potentials_row_8 = [[2, 4, 5],
                                          [2, 3, 4, 5],
                                          [2, 3, 4, 5],
                                          [3, 5, 8],
                                          [2, 3, 5, 8],
                                          [2, 3, 5, 8],
                                          [3, 4, 8],
                                          [4, 8],
                                          [3, 4, 8]]
        
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for i in range(9): assert expected_grid_potentials_row_0[i] == dummy_grid[i].potentials
        for i in range(9, 18): assert expected_grid_potentials_row_1[i%9] == dummy_grid[i].potentials
        for i in range(18, 27): assert expected_grid_potentials_row_2[i%18] == dummy_grid[i].potentials
        for i in range(27, 36): assert expected_grid_potentials_row_3[i%27] == dummy_grid[i].potentials
        for i in range(36, 45): assert expected_grid_potentials_row_4[i%36] == dummy_grid[i].potentials
        for i in range(45, 54): assert expected_grid_potentials_row_5[i%45] == dummy_grid[i].potentials
        for i in range(54, 63): assert expected_grid_potentials_row_6[i%54] == dummy_grid[i].potentials
        for i in range(63, 72): assert expected_grid_potentials_row_7[i%63] == dummy_grid[i].potentials
        for i in range(72, 81): assert expected_grid_potentials_row_8[i%72] == dummy_grid[i].potentials


        
