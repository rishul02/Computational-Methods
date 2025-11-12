import numpy as np

def scaled_pivot(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    s = np.max(np.abs(A), axis=1)

    for k in range(n - 1):
        ratios = np.abs(A[k:, k]) / s[k:]
        pivot_row = np.argmax(ratios) + k

        if pivot_row != k:
            A[[k, pivot_row]] = A[[pivot_row, k]]
            b[[k, pivot_row]] = b[[pivot_row, k]]
            s[[k, pivot_row]] = s[[pivot_row, k]]

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


x3 = scaled_pivot(A.copy(), b.copy())
print("Scaled Pivoting Solution:\n", x3)
