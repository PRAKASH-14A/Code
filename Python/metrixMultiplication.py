def matrix_multiply(A, B):
    """Inefficient matrix multiplication using triple nested loops"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not match for multiplication")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Brute force approach (O(n³) complexity)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # No optimization, iterates unnecessarily
                result[i][j] += A[i][k] * B[k][j]  # No caching, recomputes values

    return result

# Example matrices (3x3)
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Multiply matrices
result = matrix_multiply(A, B)
for row in result:
    print(row)
