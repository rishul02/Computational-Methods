import numpy as np

def partial_pivot(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    for k in range(n - 1):
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

A = np.array([[0.0001, 2, 3],
              [1, 3, 4],
              [2, 1, 3]], dtype=float)
b = np.array([5, 14, 13], dtype=float)

x = partial_pivot(A.copy(), b.copy())
print("Partial Pivoting Solution:\n", x)
