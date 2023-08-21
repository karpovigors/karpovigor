class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

# Пример использования:
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

if matrix1 == matrix2:
    print("Matrix 1 and Matrix 2 are equal.")
else:
    print("Matrix 1 and Matrix 2 are not equal.")

matrix3 = matrix1 + matrix2
print("Matrix 1 + Matrix 2:")
print(matrix3)

matrix4 = Matrix(2, 3)
matrix4.data = [[1, 2, 3], [4, 5, 6]]

matrix5 = Matrix(3, 2)
matrix5.data = [[7, 8], [9, 10], [11, 12]]

matrix6 = matrix4 * matrix5
print("Matrix 4 * Matrix 5:")
print(matrix6)
