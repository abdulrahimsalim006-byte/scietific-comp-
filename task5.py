import numpy as np

# System of Equations:
# 3x + 5y = 31  (Total daily energy target: 31 MWh)
# 4x + 2y = 18  (Grid inertia reserve target: 18 units)
#
# Solar Farm Block (x): generates 3 MWh, provides 4 inertia units
# Wind Farm Block (y): generates 5 MWh, provides 2 inertia units

A = np.array([
    [3.0, 5.0],
    [4.0, 2.0]
])

b = np.array([31.0, 18.0])

# Solve linear system Ax = b
solution = np.linalg.solve(A, b)

reconstructed_b = A @ solution
residual = b - reconstructed_b
residual_norm = np.linalg.norm(residual)

print(f"Dispatched Solar Farm Blocks (x): {solution[0]:.0f}")
print(f"Dispatched Wind Farm Blocks (y): {solution[1]:.0f}")
print("Verification (A @ solution):", reconstructed_b)
print(f"Residual Error Norm: {residual_norm:.2e}")