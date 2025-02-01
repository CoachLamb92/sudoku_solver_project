from src.utils import isSquareNumber, reduce_potentials_by_solutions
from src.example_grids import only_ones_four_by_four_grid as fxfgrid
from src.example_grids import mixed_four_by_four_grid as mixed4grid
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
    def test_function_works_on_simple_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(fxfgrid)): dummy_grid[i].solution = fxfgrid[i]
        expected = [2, 3, 4]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for cell in dummy_grid: assert expected == cell.potentials

    def test_function_works_on_complex_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(mixed4grid)): dummy_grid[i].solution = mixed4grid[i]
        expected_0 = [4]
        expected_1 = [4]
        expected_2 = []
        expected_3 = [4]
        expected_4 = [4]
        expected_5 = [4]
        expected_6 = []
        expected_7 = [2, 4]
        expected_8 = []
        expected_9 = []
        expected_10 = []
        expected_11 = []
        expected_12 = [4]
        expected_13 = [4]
        expected_14 = []
        expected_15 = [3, 4]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        result_0 = dummy_grid[0].potentials
        result_1 = dummy_grid[1].potentials
        result_2 = dummy_grid[2].potentials
        result_3 = dummy_grid[3].potentials
        result_4 = dummy_grid[4].potentials
        result_5 = dummy_grid[5].potentials
        result_6 = dummy_grid[6].potentials
        result_7 = dummy_grid[7].potentials
        result_8 = dummy_grid[8].potentials
        result_9 = dummy_grid[9].potentials
        result_10 = dummy_grid[10].potentials
        result_11 = dummy_grid[11].potentials
        result_12 = dummy_grid[12].potentials
        result_13 = dummy_grid[13].potentials
        result_14 = dummy_grid[14].potentials
        result_15 = dummy_grid[15].potentials
        # Assert
        assert expected_0 == result_0
        assert expected_1 == result_1
        assert expected_2 == result_2
        assert expected_3 == result_3
        assert expected_4 == result_4
        assert expected_5 == result_5
        assert expected_6 == result_6
        assert expected_7 == result_7
        assert expected_8 == result_8
        assert expected_9 == result_9
        assert expected_10 == result_10
        assert expected_11 == result_11
        assert expected_12 == result_12
        assert expected_13 == result_13
        assert expected_14 == result_14
        assert expected_15 == result_15
