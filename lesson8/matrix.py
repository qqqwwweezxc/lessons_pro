from typing import List

def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Multiplication of two matrices.

    The number of columns of the first matrix must be equal to the number of rows of the second matrix.

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[1, 2, 3]], [[4], [5], [6]])
    [[32]]

    >>> matrix_multiply([[2, 0], [1, 3]], [[1, 2], [3, 4]])
    [[2, 4], [10, 14]]

    >>> matrix_multiply([[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]])
    [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
    """

    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices cannot be multiplied")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)

    return result

def transpose_matrix(matrix):
    """
    Транспонує матрицю.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3]])
    [[1], [2], [3]]

    >>> transpose_matrix([[1], [2], [3]])
    [[1, 2, 3]]

    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return list(map(list, zip(*matrix)))
