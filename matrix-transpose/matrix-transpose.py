import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    Ap = np.array(A)
    n,m = Ap.shape
    B = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            B[j,i] = Ap[i,j]
    return B
            