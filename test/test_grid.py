from src.grid import Grid, Row, Column, Area, Cell
from src.example_grids import full_four_by_four_grid

class TestingGrids:
    def test_initialised_grid_has_get_size_property(self):
        # Arrange
        dummy_grid = Grid()
        expected = 'size'
        # Act
        result = dir(dummy_grid)
        # Assert
        assert expected in result

    def test_initialised_grid_get_size_property_returns_correctly(self):
        # Arrange
        dummy_grid = Grid()
        expected = 9
        # Act
        result = dummy_grid.size
        # Assert
        assert expected == result

        # Arrange
        dummy_grid = Grid(8)
        expected = 8
        # Act
        result = dummy_grid.size
        # Assert
        assert expected == result

    def test_initialised_grid_is_default_size(self):
        # Arrange
        dummy_grid = Grid()
        expected_length = 81
        expected_grid_type = list
        expected_grid_element_type = Cell
        # Act
        result_length = len(dummy_grid.data)
        result_grid_type = dummy_grid.data
        result_grid_element_type = dummy_grid.data[0]
        # Assert
        assert expected_length == result_length
        assert isinstance(result_grid_type, expected_grid_type)
        assert isinstance(result_grid_element_type, expected_grid_element_type)

    def test_initialised_grid_is_specified_size(self):
        # Arrange
        input_size = 3
        dummy_grid = Grid(input_size)
        expected_length = 9
        expected_grid_type = list
        expected_grid_element_type = Cell
        # Act
        result_length = len(dummy_grid.data)
        result_grid_type = dummy_grid.data
        result_grid_element_type = dummy_grid.data[0]
        # Assert
        assert expected_length == result_length
        assert isinstance(result_grid_type, expected_grid_type)
        assert isinstance(result_grid_element_type, expected_grid_element_type)

        # Arrange
        input_size = 17
        dummy_grid = Grid(input_size)
        expected_length = 289
        expected_grid_type = list
        expected_grid_element_type = Cell
        # Act
        result_length = len(dummy_grid.data)
        result_grid_type = dummy_grid.data
        result_grid_element_type = dummy_grid.data[0]
        # Assert
        assert expected_length == result_length
        assert isinstance(result_grid_type, expected_grid_type)
        assert isinstance(result_grid_element_type, expected_grid_element_type)

class TestingRows:
    def test_initialised_grid_has_get_size_property(self):
        # Arrange
        dummy_grid = Grid()
        dummy_row = Row(dummy_grid)
        expected = 'size'
        # Act
        result = dir(dummy_row)
        # Assert
        assert expected in result

    def test_initialised_row_get_size_property_returns_correctly(self):
        # Arrange
        dummy_grid = Grid()
        dummy_row = Row(dummy_grid)
        expected = 9
        # Act
        result = dummy_row.size
        # Assert
        assert expected == result

        # Arrange
        dummy_grid = Grid(3)
        dummy_row = Row(dummy_grid)
        expected = 3
        # Act
        result = dummy_row.size
        # Assert
        assert expected == result

    def test_initialised_row_has_default_correct_length(self):
        # Assert
        dummy_grid = Grid()
        dummy_row = Row(dummy_grid)
        expected_length = 9
        # Act
        result_length = dummy_row.size
        # Assert
        assert expected_length == result_length

    def test_initialised_row_has_specified_correct_length(self):
        # Assert
        input_size = 4
        dummy_grid = Grid(input_size)
        dummy_row = Row(dummy_grid)
        expected_length = 4
        # Act
        result_length = dummy_row.size
        # Assert
        assert expected_length == result_length

        # Assert
        input_size = 54
        dummy_grid = Grid(input_size)
        dummy_row = Row(dummy_grid)
        expected_length = 54
        # Act
        result_length = dummy_row.size
        # Assert
        assert expected_length == result_length

class TestingColumns:
    def test_initiated_grid_has_get_size_property(self):
        # Arrange
        dummy_grid = Grid()
        dummy_column = Column(dummy_grid)
        expected = 'size'
        # Act
        result = dir(dummy_column)
        # Assert
        assert expected in result

    def test_initiated_column_get_size_property_returns_correctly(self):
        # Arrange
        dummy_grid = Grid()
        dummy_column = Column(dummy_grid)
        expected = 9
        # Act
        result = dummy_column.size
        # Assert
        assert expected == result

        # Arrange
        dummy_grid = Grid(3)
        dummy_column = Column(dummy_grid)
        expected = 3
        # Act
        result = dummy_column.size
        # Assert
        assert expected == result

    def test_initiated_column_has_default_correct_length(self):
        # Assert
        dummy_grid = Grid()
        dummy_column = Column(dummy_grid)
        expected_length = 9
        # Act
        result_length = dummy_column.size
        # Assert
        assert expected_length == result_length

    def test_initiated_column_has_specified_correct_length(self):
        # Assert
        input_size = 4
        dummy_grid = Grid(input_size)
        dummy_column = Column(dummy_grid)
        expected_length = 4
        # Act
        result_length = dummy_column.size
        # Assert
        assert expected_length == result_length

        # Assert
        input_size = 54
        dummy_grid = Grid(input_size)
        dummy_column = Column(dummy_grid)
        expected_length = 54
        # Act
        result_length = dummy_column.size
        # Assert
        assert expected_length == result_length

class TestingAreas:
    def test_initialised_grid_has_get_size_property(self):
        # Arrange
        dummy_grid = Grid()
        dummy_area = Area(dummy_grid)
        expected = 'size'
        # Act
        result = dir(dummy_area)
        # Assert
        assert expected in result

    def test_initialised_area_get_size_property_returns_correctly(self):
        # Arrange
        dummy_grid = Grid()
        dummy_area = Area(dummy_grid)
        expected = 9
        # Act
        result = dummy_area.size
        # Assert
        assert expected == result

        # Arrange
        dummy_grid = Grid(3)
        dummy_area = Area(dummy_grid)
        expected = 3
        # Act
        result = dummy_area.size
        # Assert
        assert expected == result

    def test_initialised_area_has_default_correct_length(self):
        # Assert
        dummy_grid = Grid()
        dummy_area = Area(dummy_grid)
        expected_length = 9
        # Act
        result_length = dummy_area.size
        # Assert
        assert expected_length == result_length

    def test_initialised_area_has_specified_correct_length(self):
        # Assert
        input_size = 4
        dummy_grid = Grid(input_size)
        dummy_area = Area(dummy_grid)
        expected_length = 4
        # Act
        result_length = dummy_area.size
        # Assert
        assert expected_length == result_length

        # Assert
        input_size = 54
        dummy_grid = Grid(input_size)
        dummy_area = Area(dummy_grid)
        expected_length = 54
        # Act
        result_length = dummy_area.size
        # Assert
        assert expected_length == result_length

class TestingCells:
    def test_cell_initialises_correctly(self):
        # Arrange
        grid_index = 0
        grid_size = 1
        dummy_cell = Cell(grid_index, grid_size, None)
        expected_cell_id = 0
        expected_row_id = 0
        expected_column_id = 0
        expected_solution = None
        expected_potentials = [1]
        # Act
        result_cell_id = dummy_cell.cell_id
        result_row_id = dummy_cell.row_id
        result_column_id = dummy_cell.column_id
        result_solution = dummy_cell.solution
        result_potentials = dummy_cell.potentials
        # Assert
        assert expected_cell_id == result_cell_id
        assert expected_row_id == result_row_id
        assert expected_column_id == result_column_id
        assert expected_solution == result_solution
        assert expected_potentials == result_potentials

        # Arrange
        grid_index = 2
        grid_size = 2
        dummy_cell = Cell(grid_index, grid_size, None)
        expected_cell_id = 2
        expected_row_id = 1
        expected_column_id = 0
        expected_solution = None
        expected_potentials = [1, 2]
        # Act
        result_cell_id = dummy_cell.cell_id
        result_row_id = dummy_cell.row_id
        result_column_id = dummy_cell.column_id
        result_solution = dummy_cell.solution
        result_potentials = dummy_cell.potentials
        # Assert
        assert expected_cell_id == result_cell_id
        assert expected_row_id == result_row_id
        assert expected_column_id == result_column_id
        assert expected_solution == result_solution
        assert expected_potentials == result_potentials

    def test_cell_solution_options(self):
        # Arrange
        grid_index = 15
        grid_size = 9
        dummy_cell = Cell(grid_index, grid_size, '4')
        expected_cell_id = 15
        expected_row_id = 1
        expected_column_id = 6
        expected_solution = '4'
        expected_potentials = ['4']
        # Act
        result_cell_id = dummy_cell.cell_id
        result_row_id = dummy_cell.row_id
        result_column_id = dummy_cell.column_id
        result_solution = dummy_cell.solution
        result_potentials = dummy_cell.potentials
        # Assert
        assert expected_cell_id == result_cell_id
        assert expected_row_id == result_row_id
        assert expected_column_id == result_column_id
        assert expected_solution == result_solution
        assert expected_potentials == result_potentials

    def test_cell_solve_method_exists(self):
        # Arrange
        grid_index = 0
        grid_size = 9
        dummy_cell = Cell(grid_index, grid_size)
        expected = 'solve'
        # Act
        result = dir(dummy_cell)
        # Assert
        assert expected in result

    def test_cell_solve_method_works(self):
        # Arrange
        grid_index = 0
        grid_size = 9
        dummy_cell = Cell(grid_index, grid_size)
        expected_solution = '5'
        # Act
        dummy_cell.potentials = ['5']
        dummy_cell.solve()
        result_solution = dummy_cell.solution
        # Assert
        assert expected_solution == result_solution

    def test_cell_reduce_potentials_method(self):
        # Arrange
        dummy_cell = Cell(0, 4)
        expected = [2, 3, 4]
        # Act
        dummy_cell.reduce_potentials(1)
        result = dummy_cell.potentials
        # Assert
        assert expected == result

        # Arrange
        dummy_cell = Cell(0, 9)
        expected = [1, 2, 3, 4, 6, 7, 8, 9]
        # Act
        dummy_cell.reduce_potentials(5)
        result = dummy_cell.potentials
        # Assert
        assert expected == result

class TestingExampleGrids:
    def test_full_four_by_four_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(full_four_by_four_grid)): dummy_grid[i].solution = full_four_by_four_grid[i]
        expected_00_solution = 1
        expected_11_solution = 4
        expected_22_solution = 4
        expected_33_solution = 3
        # Act
        result_00_solution = dummy_grid[0].solution
        result_11_solution = dummy_grid[5].solution
        result_22_solution = dummy_grid[10].solution
        result_33_solution = dummy_grid[15].solution
        # Assert
        assert expected_00_solution == result_00_solution
        assert expected_11_solution == result_11_solution
        assert expected_22_solution == result_22_solution
        assert expected_33_solution == result_33_solution

    def test_row_class_on_completed_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(full_four_by_four_grid)): dummy_grid[i].solution = full_four_by_four_grid[i]
        expected_1 = [1, 2, 3, 4]
        expected_2 = [3, 4, 1, 2]
        expected_3 = [2, 3, 4, 1]
        expected_4 = [4, 1, 2, 3]
        # Act
        row_0 = Row(dummy_grid, 0)
        row_1 = Row(dummy_grid, 1)
        row_2 = Row(dummy_grid, 2)
        row_3 = Row(dummy_grid, 3)
        # Arrange
        for i in range(4):
            assert row_0.data[i].solution == expected_1[i]
            assert row_1.data[i].solution == expected_2[i]
            assert row_2.data[i].solution == expected_3[i]
            assert row_3.data[i].solution == expected_4[i]

    def test_column_class_on_completed_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(full_four_by_four_grid)): dummy_grid[i].solution = full_four_by_four_grid[i]
        expected_1 = [1, 3, 2, 4]
        expected_2 = [2, 4, 3, 1]
        expected_3 = [3, 1, 4, 2]
        expected_4 = [4, 2, 1, 3]
        # Act
        column_0 = Column(dummy_grid, 0)
        column_1 = Column(dummy_grid, 1)
        column_2 = Column(dummy_grid, 2)
        column_3 = Column(dummy_grid, 3)
        # Arrange
        for i in range(4):
            assert column_0.data[i].solution == expected_1[i]
            assert column_1.data[i].solution == expected_2[i]
            assert column_2.data[i].solution == expected_3[i]
            assert column_3.data[i].solution == expected_4[i]

    def test_area_class_on_completed_grid(self):
        # Arrange
        dummy_grid = Grid(4)
        for i in range(len(full_four_by_four_grid)): dummy_grid[i].solution = full_four_by_four_grid[i]
        expected_1 = [1, 2, 3, 4]
        expected_2 = [3, 4, 1, 2]
        expected_3 = [2, 3, 4, 1]
        expected_4 = [4, 1, 2, 3]
        # Act
        area_0 = Area(dummy_grid, 0)
        area_1 = Area(dummy_grid, 1)
        area_2 = Area(dummy_grid, 2)
        area_3 = Area(dummy_grid, 3)
        # Arrange
        for i in range(4):
            assert area_0.data[i].solution == expected_1[i]
            assert area_1.data[i].solution == expected_2[i]
            assert area_2.data[i].solution == expected_3[i]
            assert area_3.data[i].solution == expected_4[i]


