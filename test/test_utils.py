from src.utils import isSquareNumber, reduce_potentials_by_solutions
from src.example_grids import only_ones_four_by_four_grid as oofxfgrid
from src.example_grids import mixed_four_by_four_grid as mxfxfgrid
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
        expected = [2, 3, 4]
        # Act
        reduce_potentials_by_solutions(dummy_grid)
        # Assert
        for cell in dummy_grid: assert expected == cell.potentials

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
        pass

    def test_function_works_on_complex_nine_by_nine_grid(self):
        pass

            

