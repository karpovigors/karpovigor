import pytest
from matrix_operations import Matrix

@pytest.fixture
def matrices():
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    matrix4 = Matrix(2, 3)
    matrix4.data = [[1, 2, 3], [4, 5, 6]]

    matrix5 = Matrix(3, 2)
    matrix5.data = [[7, 8], [9, 10], [11, 12]]

    return matrix1, matrix2, matrix4, matrix5

def test_matrix_addition(matrices):
    matrix1, matrix2, _, _ = matrices

    result = matrix1 + matrix2
    expected_result = Matrix(2, 2)
    expected_result.data = [[6, 8], [10, 12]]

    assert result == expected_result

def test_matrix_multiplication(matrices):
    _, _, matrix4, matrix5 = matrices

    result = matrix4 * matrix5
    expected_result = Matrix(2, 2)
    expected_result.data = [[58, 64], [139, 154]]

    assert result == expected_result
