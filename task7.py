import numpy as np

# 5-bus transmission feeder voltage drop matrix
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary voltages: Sending Substation = 230 kV, Receiving End = 218 kV
b = np.array([230.0, 0., 0., 0., 218.0])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ x_old[i+1:]) / A[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x
    return x

x_j = jacobi(A, b)
x_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi Bus Voltages (kV):", np.round(x_j, 2))
print("Gauss-Seidel Bus Voltages (kV):", np.round(x_gs, 2))
print("Exact Numerical Voltages (kV):", np.round(x_exact, 2))