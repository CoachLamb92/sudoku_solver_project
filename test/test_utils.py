from src.utils import isSquareNumber, reduce_potentials_by_solutions
from src.example_grids import only_ones_four_by_four_grid as fxfgrid
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
    # def test_function_works_by_row(self):
    #     # Arrange
    #     dummy_grid = Grid(4)
    #     for i in range(len(fxfgrid)): dummy_grid[i].solution = fxfgrid[i]
    #     expected = [2, 3, 4]
    #     # Act
    #     reduce_potentials_by_solutions(dummy_grid)
    #     result = dummy_grid[1].potentials
    #     # Assert
    #     assert expected == result
