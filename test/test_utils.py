from src.utils import isSquareNumber

class TestIsSquareNumberFunction():
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