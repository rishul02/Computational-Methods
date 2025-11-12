import numpy as np

def complete_pivot(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)
    col_index = np.arange(n) 

    for k in range(n - 1):
        sub = np.abs(A[k:, k:])
        i_max, j_max = np.unravel_index(np.argmax(sub), sub.shape)
        i_max += k
        j_max += k


        if i_max != k:
            A[[k, i_max]] = A[[i_max, k]]
            b[[k, i_max]] = b[[i_max, k]]

        if j_max != k:
            A[:, [k, j_max]] = A[:, [j_max, k]]
            col_index[[k, j_max]] = col_index[[j_max, k]]

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    x_final = np.zeros_like(x)
    for i in range(n):
        x_final[col_index[i]] = x[i]

    return x_final


x2 = complete_pivot(A.copy(), b.copy())
print("Complete Pivoting Solution:\n", x2)
